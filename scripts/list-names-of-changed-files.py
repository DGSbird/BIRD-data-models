####
## List the names and the types of the data model objects that have
## been updated, added or deleted.
##
## To Do:
## Print whether it is added, updated or deleted.
#### 

# import modules
import os
import sys
import git
import linecache

is_debug    = True
is_debug    = False
total_plus  = 0
total_minus = 0

def get_name_from_line(line):
    line_splits = line.split('name="', 1)
    if len(line_splits) > 1:
        right_part = line_splits[1]
        line_splits = right_part.split('"', 1)
        name = line_splits[0]
    else:
        name = "(no name available)"
    # end if len(line_splits)
    return name

def get_description_from_line(line):
    line_splits = line.split('description="', 1)
    description = ""
    if len(line_splits) > 1:
        right_part = line_splits[1]
        line_splits = right_part.split('"', 1)
        description = line_splits[0]
    # end if len(line_splits)
    
    return description

def get_valuecode_from_line(line):
    line_splits = line.split('value="', 1)
    value = ""
    if len(line_splits) > 1:
        right_part = line_splits[1]
        line_splits = right_part.split('"', 1)
        value = line_splits[0]
    # end if len(line_splits)

    return value
    
    return description
def get_name_from_xml_file(file):
    # parse the xml file
    second_line = linecache.getline(file, 2)
    name = ""
    if second_line:
        # print(f"second line  {second_line}")
        name = get_name_from_line(second_line)
    # end if second_line
    return name

def get_model_type_from_xml_file(file):
    # parse the xml file
    model_type = ''
    line_splits = file.split('/')
    if len(line_splits) >= 3:
        if line_splits[1] == "domains":
            model_type = "domain or member"
        elif line_splits[1] == "logical":
            model_type = line_splits[2]
            if model_type == 'entity':
                model_type = 'entity type'
            elif model_type == 'relation':
                model_type = 'relationship type'
            elif model_type == 'subviews':
                model_type = 'subview'
            # end if model_type
        else:
            model_type = line_splits[1]
        # end if
    # end if >=3
    return model_type    

def get_oid_from_line(line, model_type):
    if is_debug:
        print(f"model_type {model_type}")
        print(f"split_remainder line: {line}")
    if model_type == 'arc':
        split_remainder = line.split('id=', 1)
    else:
        split_remainder = line.split('oid=', 1)

    if is_debug:
        print(f"split_remainder: {split_remainder}")
    oid_attribute = split_remainder[1]
    oid = oid_attribute[0:38]
    return oid

def get_object_type_from_line(line):
    object_type = ''
    split_line = line.split(' ')
    for s in split_line:
        if s.startswith('otype'):
            object_type = s[7:]
            line_splits = s.split('"', 1)
            object_type = line_splits[0]
            # object_type = object_type[:-1]
            break
    return object_type

def get_commit_type_for_model_type(model_type):
    if model_type == "subview":
        commit_type = ">chore:"
    else:
        commit_type = ">feat:"
    return commit_type

def get_tag_from_line(line):
    tag = ""
    tag = line.split(' ')[0]
    if '>' in tag:
        tag = tag.split('>')[0]

    return tag

def print_information_from_diff_of_file(file, model_type):
    # if the line starts with - say it is removed
    # if the line starts with + say it is added
    #
    # Working assumptions:
    # What is added is the tag that starts at position 2.
    # Single tags start with a Capital letter
    # collection of tags start with a lower case letter.
    #
    # Only print opening tags.
    
    no_change = True
    n_minus   = 0
    n_plus    = 0
    diff      = repo.git.diff(repo.head.commit.tree, file)

    for line_in_diff in diff.splitlines():
        print_tag = False
        if len(line_in_diff) >=4 :
            first_char = line_in_diff[0:1]
            remainder_of_line = line_in_diff[1:]
            if remainder_of_line[0:1] == '<':
                update_type = ''
                if first_char == '-' :
                    if is_debug:
                        print(f"removed: {remainder_of_line}")
                    update_type = "removed"
                    n_minus += 1
                # end if first_char = '-'
                if first_char == '+' :
                    if is_debug:
                        print(f"added: {remainder_of_line}")
                    update_type = "added"
                    n_plus += 1
                # end if first_char = '+'
                if update_type != "":
                    remainder_of_line = remainder_of_line[1:]
                    if remainder_of_line[0:1].isupper():
                        # It is a single tag. We need to print its content
                        print_tag = True
                    # end if remainder_of_line[0:1].isupper():

                    remainder_text = ''
                    object_type = ''
                    changed_tag = get_tag_from_line(remainder_of_line)
                    if is_debug:
                        print(f"changed_tag: {changed_tag}" )
                    if changed_tag == "Arc":
                        if model_type == "arc":
                            remainder_text = 'name="' + get_name_from_xml_file(remainder_of_line) + '"'
                        else:
                            remainder_text = 'oid=' + get_oid_from_line(remainder_of_line, model_type)
                        # end if model_type = "arc":

                    elif changed_tag == "Attribute":
                        name = get_name_from_line(remainder_of_line)
                        remainder_text = "'" + name + "'"
                    elif changed_tag == "CM":
                        print_tag = False
                    elif changed_tag == "commentInRDBMS":
                        remainder_text = "definition"
                        print_tag = True
                    elif changed_tag == "Connector":
                        print_tag = False
                    elif changed_tag == "Diagram":
                        name = get_name_from_line(remainder_of_line)
                        remainder_text = "'" + name + "'"
                    elif changed_tag == "Domain":
                        name = get_name_from_line(remainder_of_line)
                        remainder_text = "'" + name + "'"
                    elif changed_tag == "Entity":
                        name = get_name_from_line(remainder_of_line)
                        remainder_text = "'" + name + "'"
                    elif changed_tag == "Mg":
                        print_tag = False
                    elif changed_tag == "OView":
                        object_type = get_object_type_from_line(remainder_of_line)
                        oid_attribute = get_oid_from_line(remainder_of_line, model_type)
                        to_or_from = ' to' if update_type == "added" else ' from'
                        remainder_text = "for " + object_type + ' ' + oid_attribute + to_or_from + " the subview."
                    elif changed_tag == "Relation":
                        name = get_name_from_line(remainder_of_line)
                        remainder_text = "'" + name + "'"
                    elif changed_tag == "valueDef":
                        val = get_valuecode_from_line(remainder_of_line)
                        desc = get_description_from_line(remainder_of_line)
                        remainder_text = '"' + val + '"=' + '"' + desc + '"'
                        print_tag = True

                    else: # if remainder_of_line[0:1].isupper(): 
                        changed_tag = remainder_of_line.split(' ')[0]
                        if changed_tag == "item":
                            print_tag = False
                        else:
                            no_change = False

                        if no_change:
                            pass
                        else:
                            pass
                            # print("things changed")
                    # end if changed_tag == "Arc":

                    if print_tag:
                        print("       " + update_type + " " + changed_tag + " " + remainder_text)

                #end if update_type <> "":
            # end if remainder_of_line[0:1] == '<':
        # end if len(line_in_diff)
        # n += 1
    # next line_in_diff
    print(f"changes: {n_plus + n_minus} total (+{n_plus}/-{n_minus}).")
    global total_plus
    total_plus += n_plus
    global total_minus
    total_minus += n_minus
  

##########
# main routine
##########
# create a git repository object
repo = git.Repo(os.getcwd())

# get the list of untracked or changed xml files
# to do: add the files that are already staged for commit.
untracked_xml_files = []
updated_xml_files   = []
deleted_xml_files   = []
for file in repo.untracked_files:
   if file.endswith(".xml"):
        untracked_xml_files.append(file)
for item in repo.index.diff("HEAD"):
   if item.a_path.endswith(".xml"):
        updated_xml_files.append(item.a_path)
for item in repo.index.diff(None):
    if item.a_path.endswith(".xml"):
        updated_xml_files.append(item.a_path)
for item in repo.index.diff(None).iter_change_type('D'):
    if item.a_path.endswith(".xml"):
        deleted_xml_files.append(item.a_path)
        if item.a_path in updated_xml_files:
            updated_xml_files.remove(item.a_path)
        # end if item in updated_xml_files
    # end if
# next item

if is_debug:
    print(untracked_xml_files)
    print(updated_xml_files)
    print(deleted_xml_files)
# end if is_debug

# loop through the xml files and get the value of the name attribute
for file in updated_xml_files:
    name = get_name_from_xml_file(file)
    model_type = get_model_type_from_xml_file(file)
    commit_type = get_commit_type_for_model_type(model_type)
    print(f"{commit_type} updated {model_type} '{name}'.")
    print_information_from_diff_of_file(file, model_type)
# next file

for file in untracked_xml_files:
    name = get_name_from_xml_file(file)
    model_type = get_model_type_from_xml_file(file)
    commit_type = get_commit_type_for_model_type(model_type)
    print(f"{commit_type} added {model_type} '{name}'.")
# next file

for file in deleted_xml_files:
    name = get_name_from_xml_file(file)
    model_type = get_model_type_from_xml_file(file)
    # if is_debug:
    #  print(f"Deleted file name: {file}")
    commit_type = get_commit_type_for_model_type(model_type)
    print(f"{commit_type} deleted {model_type} '{name}'.")
    # print_information_from_diff_of_file(file)

# next file

total_files = len(updated_xml_files) + len(untracked_xml_files) + len(deleted_xml_files)
if total_files == 1:
    print("1 change to commit.")
else:
    print(f"{total_files} files to commit.")
    
print(f"changes: {total_plus + total_minus} total (+{total_plus}/-{total_minus}).")

