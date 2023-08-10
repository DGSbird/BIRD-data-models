# Welcome to the Banks' Integrated Reporting Dictionary (BIRD) repository!

## Repository content

This repository comprises the BIRD data models, specifically the BIRD Logical Data Model (BIRD LDM) and thereof forward engineered (relational) models like the BIRD Input Layer (BIRD IL) and the BIRD Enriched Input Layer (BIRD EIL). We use [SQL data modeler](https://www.oracle.com/database/technologies/appdev/datamodeler.html) to design these data models, hence the data models are stored using SQL data modeler storage format, i.e. a set of interconnected xml files organised in a specific folder structure and a .dmd file. 

## Forward engineering

The forward engineering scripts, used to extend the out-of-the-box forward engineering capabilities of SQL data modeler are also stored in this repository. They may be found under "BIRD Logical Data Model/BIRD data models/forward engineering" accompanied by a txt file listing the order in which these scripts should be run. Forward engineering scripts can be imported into SQL data modeler using Tools --> Data Modeler --> Design Rules And Transformations --> Transformations --> Import --> selecting the file "BIRD data models/forward engineering/fe_scripts.xml". After the import of the forward engineering scripts they can be run using the transformation dialog window. Each script comes with a description that should be understandable by software engineers familiar with forward engineering proceedures.

# How you can help
There are several ways in which to help. You could raise issues, or want to get more involved. Please look at the bird website (https://bird.ecb.europa.eu) for contect information

## Updating the model
To update the model, please first install SQL Developer and clone the repository. 

## Further questions, contact information & getting involved

Please let us know if something is unclear or if you have suggestions for improvement by sending an email to BIRD@ecb.europa.eu. If you want to get involved in the project, please also feel free to contact us.
