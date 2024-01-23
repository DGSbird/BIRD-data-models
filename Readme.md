# Welcome to the Banks' Integrated Reporting Dictionary (BIRD) repository!

## Repository content

This repository comprises the BIRD data models, specifically the BIRD Logical Data Model (BIRD LDM) and thereof forward engineered (relational) models like the BIRD Input Layer (BIRD IL) and the BIRD Enriched Input Layer (BIRD EIL). We use [SQL data modeler](https://www.oracle.com/database/technologies/appdev/datamodeler.html) to design these data models, hence the data models are stored using SQL data modeler storage format, i.e. a set of interconnected xml files organised in a specific folder structure and a .dmd file. 

## Forward engineering

The forward engineering scripts, used to extend the out-of-the-box forward engineering capabilities of SQL data modeler are also stored in this repository. They may be found under [BIRD Logical Data Model/BIRD data models/forward engineering](BIRD data models/forward engineering) accompanied by a txt file listing the order in which these scripts should be run. Forward engineering scripts can be imported into SQL data modeler using Tools --> Data Modeler --> Design Rules And Transformations --> Transformations --> Import --> selecting the file [fe_scripts.xml](BIRD data models/forward engineering/fe_scripts.xml). After the import of the forward engineering scripts they can be run using the transformation dialog window. Each script comes with a description that should be understandable by software engineers familiar with forward engineering proceedures.

## Git branching model

We try to follow [a successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/). The main branch comprises the latest published version of the BIRD data models, and will be tagged accordingly to indicate the version of the BIRD data models, e.g. version [1.0](https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/commit/d93a8bc5e9459cb5984af3c300c6bd30ff0f77aa). The develop branch comprises the latest features that have been discussed and agreed within the Work stream on data modelling (WS DM). Please note that these features are subject to approval from the BIRD Expert Group (EG) to be incorporated into the main branch. Other branches than the main and develop branch comprise features, bug- or hotfixes.

# How you can help
There are several ways in which to help. You could raise issues, or want to get more involved. You could also update the model itself. Simply clone the repo, create a new branch and add to the model.

## Raising / reporting issues

If you find / identify issues, please don't hesitate to create a new issue in this repository to inform us about it. The [wiki](wikipage) in this repo has a [specific page](feedbackwiki) that goes into detail.  

## Updating the model
To update the model, please first install SQL Developer and clone the repository. The wiki page on [SQL Data modeler and Git repositorys][usesqldeveloper] explains how.

Then please create a branch starting from the develop branch, either for an existing issue in Gitlab, or for your own additions. After you are ready to merge your changes, please get in contact with us. We will then discuss and review your additions together with the rest of the Work Stream on Data Modelling. After this, if all is fine, we will merge the branch back into the develop branch.

## Further questions, contact information & getting involved

Please let us know if something is unclear or if you have suggestions for improvement by sending an email to BIRD@ecb.europa.eu. If you want to get involved in the project, please also feel free to contact us.

More detailed documentation can be found in the [Wiki pages](wikipage) of this project.

[wikipage]: https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/wikis/home
[feedbackwiki]: https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/wikis/Providing-feedback-to-the-Logical-Data-Model-and/Provide-Feedback-to-the-LDM-or-the-Work-Stream-on-Data-Modelling
[usesqldeveloper]: https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/wikis/SQL-Data-Modeler-and-Git-repositories
