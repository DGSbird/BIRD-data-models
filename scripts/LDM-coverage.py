# %%
import pandas as pd
import openpyxl

from sddutilslib import import_utils, information_model

# %%
# Function returning a set of distinct variables in a framework.
# TODO: consider creating function returning a set of distinct members (ignore for now)
def distinct_variables_in_framework(framework: information_model.Framework) -> set:
    # get cubes associated with the framework
    cubes = framework.cubes
    # get the list of underlying cube structure items (we filter on
    # the desired cube types)
    cube_structure_items = [cube_structure_item \
        for cube in cubes \
            for cube_structure_item in cube.cube_structure_items\
                if cube.cube_type in CUBE_TYPES]
    # initialize empty set to populate with variables
    distinct_variables = set()
    # iterate over cube structure items and append variables
    for cube_structure_item in cube_structure_items:
        # we exclude attributes to remove operational metadata
        # (approximation)
        # TODO: consider adding variables underlying variable sets
        # (ignore for now)
        if cube_structure_item.role != "A":
            distinct_variables.add(cube_structure_item.variable)
    # return the set of distinct variables
    return distinct_variables

# %%
def shared_variables_in_framework(framework: information_model.Framework) -> list:
    # get cubes associated with the framework
    cubes = framework.cubes
    # get the list of underlying cube structure items (we filter on
    # the desired cube types)
    cube_structure_items = [cube_structure_item \
        for cube in cubes \
            for cube_structure_item in cube.cube_structure_items\
                if cube.cube_type in CUBE_TYPES]
    # initialize empty set to populate with variables
    shared_variables = list()
    # iterate over cube structure items and append variables
    for cube_structure_item in cube_structure_items:
        # we exclude attributes to remove operational metadata
        # (approximation)
        # TODO: consider adding variables underlying variable sets
        # (ignore for now)
        if cube_structure_item.role != "A":
            shared_variables.append(cube_structure_item.variable)
    # return the set of distinct variables
    return shared_variables

# %%
# Specify the file paths accordingly
working_dir = "../../../BIRD coverage"
VARIABLE_IDS_TO_INCLUDE_IN_THE_BIRD_EXCEL_FILE_PATH = working_dir + "/variable_ids_to_include_in_the_bird.xlsx"
MULTI_FRAMEWORK_EXPORT_FILE_PATH = working_dir + "/multi-framework-export-22_03_2024_09_10_48.xlsx"

# %%
# Specify desired collection cube types we want to filter on
CUBE_TYPES = ["C", "RC", "EIL", "ELDM", "IL", "LDM"]

# %%
# Import the variable ids to include in the BIRD and store them in a
# set
variable_ids_to_include_in_the_bird = set(pd.read_excel(VARIABLE_IDS_TO_INCLUDE_IN_THE_BIRD_EXCEL_FILE_PATH)['VARIABLE_ID'])

# %%
# Import the reference frameworks downloaded from the SDD (it will
# take some time)
import_service = import_utils.ImportService()
import_service.import_from_excel(MULTI_FRAMEWORK_EXPORT_FILE_PATH)
storage = import_service.storage

# %%
# Calculate the distinct variables in the BIRD framework and add
# variables to add in the BIRD
variables_to_include_in_the_bird = {storage[information_model.Variable][variable_id] for variable_id in variable_ids_to_include_in_the_bird}
bird_variables = distinct_variables_in_framework(storage[information_model.Framework]["BIRD"]).union(variables_to_include_in_the_bird)


# %%
# Load the Excel file with bird abbreviations of entity types,
# attributes, domain that are solved or named differently in the
# various frameworks in SDD. They count as a match but they are
# matched differently.
print("Importing BIRD specific variables...")
file_path = working_dir + "/BIRD attributes.xlsx"
workbook = openpyxl.load_workbook(file_path)

# Get the active sheet (assuming it's the first sheet)
sheet = workbook.active

# Iterate through the rows and extract the "Variable_ID" column
for row in sheet.iter_rows(min_row=1, values_only=True):
    variable_id = row[0]  # Assuming "Variable_ID" is the first column
    if variable_id:
        bird_variables.add(variable_id)

# %%
# prepare a list of reference framework to iterate over
reference_frameworks = [framework for framework in storage[information_model.Framework].values() \
                        if framework.maintenance_agency.code == "ECB" or framework.code == "BIRD"]

# %%
# instantiate bird coverage dictionary to populate
bird_coverage_df = pd.DataFrame(columns=['VARIABLE_ID', 'FRAMEWORK_NAME'])
# iterate over non reference frameworks and populate dictionary with
# info about variables covered in the BIRD
for framework in reference_frameworks:
    # get distinct variables in framework of interest
    framework_variables = distinct_variables_in_framework(framework)
    # get a set with the variables of this framework that are covered
    # in the BIRD (intersection)
    variables_intersection = framework_variables.intersection(bird_variables)
    # populate bird_coverage_df
    for variable in variables_intersection:
        temp_df = pd.DataFrame({'VARIABLE_ID': [variable.identifier], 'FRAMEWORK_NAME': [framework.name], "MATCH": [1]})
        bird_coverage_df = pd.concat ([bird_coverage_df, temp_df], ignore_index=True)
    for variable in framework_variables.difference(variables_intersection):
        temp_df = pd.DataFrame({'VARIABLE_ID': [variable.identifier], 'FRAMEWORK_NAME': [framework.name], "MATCH": [0]})
        bird_coverage_df = pd.concat([bird_coverage_df, temp_df], ignore_index=True)
    # print some summary statistics about the LDM coverage
    print(f"{framework.name} has {len(framework_variables)} variables and {len(variables_intersection)} are covered in the BIRD ({len(variables_intersection)/len(framework_variables)}).")

# %%
bird_coverage_df_wide = bird_coverage_df.pivot(index='VARIABLE_ID', columns='FRAMEWORK_NAME', values='MATCH')

# %%
# Group by 'Category' column and calculate the mean of 'Value'
summary_df = bird_coverage_df.groupby('FRAMEWORK_NAME')['MATCH'].mean()

# %%
summary_df

# %%

# Create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter('../../../BIRD coverage/bird_coverage.xlsx', engine='xlsxwriter')
# Write the dataframe to the Excel file for the summary
summary_df.to_excel(writer, sheet_name='Summary', index=True, header=True)
# Write the dataframe to the Excel file for the granular overview
bird_coverage_df_wide.to_excel(writer, sheet_name='Granular Overview', index=True, header=True)
# Get the workbook and worksheet objects
workbook = writer.book
worksheet = writer.sheets['Granular Overview']
# Freeze the top row
worksheet.freeze_panes(1, 0)

# Save the workbook
# writer.save()
writer.close()

# %%
type(reference_frameworks[0])

# %%
# Calculate the KPIs but this time counting duplicate attributes
# (within framework)
for framework in reference_frameworks:
    # get shared variables in framework of interest
    shared_framework_variables = shared_variables_in_framework(framework)
    # get shared framework variables covered
    shared_framework_variables_covered = list()
    for shared_framework_variable in shared_framework_variables:
        if shared_framework_variable in bird_variables:
            shared_framework_variables_covered.append(shared_framework_variable)
    # print some summary statistics about the LDM coverage
    print(f"{framework.name} has {len(shared_framework_variables)} shared variables and {len(shared_framework_variables_covered)} are covered in the BIRD ({len(shared_framework_variables_covered)/len(shared_framework_variables)}).")

# %%
# Calculate the KPIs but this time counting duplicate attributes
# (within and across frameworks)
def coverage_with_redundancies_within_and_across_frameworks(frameworks_list: list) -> None:
    shared_variables = list()
    for framework in frameworks_list:
        shared_framework_variables = shared_variables_in_framework(framework)
        shared_variables = shared_variables + shared_framework_variables

    shared_variables_covered = list()
    for shared_variable in shared_variables:
        if shared_variable in bird_variables:
            shared_variables_covered.append(shared_variable)
    
    print(f"{frameworks_list} has/have {len(shared_variables)} shared variables and {len(shared_variables_covered)} are covered in the BIRD ({len(shared_variables_covered)/len(shared_variables)}).")

# %%
# Calculate the KPIs but this time considering distinctive attributes
# (within and across frameworks)
def coverage_within_and_across_frameworks(framework_list: list) -> None:
    distinct_variables = set()
    for framework in framework_list:
        distinct_framework_variables = distinct_variables_in_framework(framework)
        distinct_variables = distinct_variables.union(distinct_framework_variables)
    
    covered_variables = distinct_variables.intersection(bird_variables)

    print(f"Out of a total of {len(distinct_variables)} {len(covered_variables)} are covered in the BIRD ({len(covered_variables)/len(distinct_variables)})")

# %%
# total coverage distinct variables
coverage_within_and_across_frameworks(
    [
        storage[information_model.Framework]["FINREP_REF"],
        storage[information_model.Framework]["ANCRDT"],
        storage[information_model.Framework]["SHS_REF"]
    ]
)

# %%
# total coverage distinct variables
coverage_within_and_across_frameworks(
    [
        storage[information_model.Framework]["FINREP_REF"],
        storage[information_model.Framework]["ANCRDT"],
        storage[information_model.Framework]["SHS_REF"],

        storage[information_model.Framework]["RES_REF"],
        storage[information_model.Framework]["AE_REF"],
        storage[information_model.Framework]["BSI_REF"],
        storage[information_model.Framework]["MIR_REF"]
    ]
)

# %%
# total coverage counting duplicates
coverage_with_redundancies_within_and_across_frameworks(
    [
        storage[information_model.Framework]["FINREP_REF"],
        storage[information_model.Framework]["ANCRDT"],
        storage[information_model.Framework]["SHS_REF"]
    ]
)

# %%
coverage_with_redundancies_within_and_across_frameworks(
    [
        storage[information_model.Framework]["FINREP_REF"],
        storage[information_model.Framework]["ANCRDT"],
        storage[information_model.Framework]["SHS_REF"],

        storage[information_model.Framework]["RES_REF"],
        storage[information_model.Framework]["AE_REF"],
        storage[information_model.Framework]["BSI_REF"],
        storage[information_model.Framework]["MIR_REF"]
    ]
)


