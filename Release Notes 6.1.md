# Release notes LDM 6.1
High-level release notes of the changes from version 6.0.0 as published in November 2021 to version 6.1. This describes the summary of the changes made to the LDM since its previous release. It is based on the issues in GitLab that were included in this release.

# Summary of changes
Of the many changes in the logical data model (LDM) the following are the most impactful. Collateral subtypes have been added to explicitly model the AnaCredit requirement regarding type of valuation, type of protection and type of valuation approach. Exchange tradable derivatives are now included in the LDM. All reference data sets used in the LDM are now entity types in the model. The roles of credit facility have been removed; there was no reporting requirement for them. The context of the data that is subject to the logical data model is now modelled in the LDM itself. This impacts almost every primary and foreign key.

# Changes included in version 6.1
The changes recorded in Gitlab that are listed below have had a direct impact on the model. These changes are split into two types. The first concerns those changes where the structure of the model has been amended or changed in such a way that when data is reported via the BIRD LDM, the reported data would change. The second type of changes are those that updated the model without impacting the structure of the reported data.

## Updates that do not impact the structure of the logical data model/input layer
1.	The definition of reporting agent identifier was mistakenly only partially completed. It is now fully completed.
2.	Introduced the domain Year to be able to restrict values to years. This is applied to the attribute “Year” in entity type Party previous period data.
3.	Currency as reference data is now correctly related to where currency is used.
4.	Reference entity type Forbearance measure is now renamed to Forbearance measure type.
5.	Updated the word boarders to borders in the definition of Real estate collateral.

## Updates that changed the structure of the logical data model/input layer
1.	Syndicated loan identifier added. This allows for the AnaCredit requirement to group together loans that are part of the same syndication at the ECB side.
2.	Move the attribute Type of product from Debt security to Debt security issued , because the FINREP reporting requirement is only for Type of product for issued debt securities.
3.	Collateral subtypes and their value made explicit according to AnaCredit. This replaced the previous attributive entity type used where the meaning of the value attribute was stored in the type of value attribute. The new model structure allows for explicit type of values, coupled with the valuation approach that is applicable to that type of value.
4.	All reference data sets that are relevant for entity types within the logical data model have been modelled explicitly as entity types in the LDM. This allows for better communication of what is the reference data, and who is responsible for it, and where the values can be found. Also, because of the explicit relationship types from the reference data entity types, it is now directly obvious if a reference data set is used in multiple entity types.
5.	Reference data has been removed from the input layer as it is input to the input layer, not input to the report derived from the input layer.
6.	The subtypes of reference data entity types that do not have their own attributes, have been removed. They did not provide extra clarity nor information for the LDM.
7.	On the suggestion of the subgroup LDM/IL   review, the party roles are now split into entity group roles and entity transaction roles. This extra classification helps structure the information in the model.
8.	Credit facility no longer is broken down into separate roles. The Work Stream on Data Modelling did not find a reporting requirement for the roles.  
9.	Exchange tradable derivatives have been added preliminary as there are still questions outstanding.
10.	Model context has been added as an entity type. It defines the context of the data within the scope of the LDM and it internalizes the scope within the model itself. To do this, all entity types that do not describe reference data are now dependent on the model context. This means that basically every entity type now has reporting agent identifier and reference date as part of its primary key.

## Changes to domain members
1.	The domain Party code type now has the domain members Legal Entity Identifier (LEI) and RIAD code  . The latter is to identify parties within the ECB Register of Institutions and Affiliates Database
2.	The members of the domain purpose, used in Financial asset instrument now allow for all purposes required for reporting AnaCredit.
3.	The members of the domain Balance sheet recognition status have been clarified and made mutually exclusive.
4.	The members of the domain Group role type have been aligned to the model structure. A mismatch had arisen here.

## Changes to the forward engineering
These include changes to the documentation of the forward engineering.
1.	The logging and documentation in the scripts has been updated and made clearer.
2.	In the documentation describing the forward engineering methods, there have been a few fixes of typing mistakes. For example, the term legal person has been replaced by natural person in the description
3.	It was clarified that the forward engineering does not include aggregations.
4.	It was clarified that both the LDM and the IL use domains for their attributes and columns.
5.	The usage of Null-explanatory values within validation rules was also made clearer.

## Changes to the documentation
Please note that the changes to the documentation regarding forward engineering have been noted in the previous paragraph.

###	Introduction to the BIRD LDM
In the document Introduction to the BIRD LDM, the updated all the figures where the addition of reporting agent identifier and reference date to the primary key or foreign key was visible.
1.	Clarified that currently only one address is required for a party.
2.	It is clarified how the various reporting frameworks are prioritised
3.	Updated the section on master data. It now is the section on reference data. This better covers the meaning of the type of data.
4.	Many smaller suggestions to improve readability have been incorporated into the introduction document.

### BIRD LDM design principles
1.	Design principle 9 has been scrapped by the WS DM. It is clarified now in the document that it is indeed correct that it is missing.
2.	Many smaller suggestions to improve readability have been incorporated into the design principles document.


# Annex 1:	List of closed GitLab issues  
This list shows the overview of issues covered in the release of the BIRD LDM and its documentation. The full list can be found here: https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/ 

| Title of the issue | Link to the issue on the GitLab environment |
| ---- | ---- |
 | Review of forward engineering scripts | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/1  | 
 | Model design for syndicated loans | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/4 | 
  | Specify necessary allowed values for the Attribute Party code type in Other party code | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/8 | 
 | AnaCredit requirement: distinction between commercial and residential real estate collateral and offices and commercial premises | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/10 | 
 | Specific vs. generic representation of numeric values | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/20 | 
 | Explicit representation of reference data | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/24 | 
 | Update logging and documentation in forward engineering Javascript scripts | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/29 | 
 | Balance sheet recognition status | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/46 | 
 | Editorial changes to accompanying documentation to BIRD 6.0.0 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/51 | 
 | Wording changes to "Forward engineering methods in the context of BIRD - v1.0.0" | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/52 | 
 | Wording changes to "Introduction to the BIRD LDM - v1.0.1" | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/58 | 
 | Content - modelling suggestion - Master Data consideration | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/64 | 
 | to be corrected  - description of "...Reporting agent identifier" | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/74 | 
 | Party previous period data - attribute Year | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/75 | 
 | Reporting agent internal group role - clarification | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/76 | 
 | Need for clarification - Master/Reference data - Currency entity isolated | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/90 | 
 | Move the attribute Type of product from Debt security to Debt security issued | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/91 | 
 | Entity Forbearance measure - rename? | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/94 | 
 | FE - Clarify that FE does not include aggregation | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/98 | 
 | FE - Clarify that both LDM and IL use Domains | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/100 | 
 | FE - Clarify validation rules and the use of NEVs | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/102 | 
 | Collateral - Correct typo (in Real Estate Entities) | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/104 | 
  | Intro to LDM - Clarify how frameworks are prioritised | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/107 | 
  | FE - correct sentence -  "legal" to "natural" | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/108 | 
  | Intro to LDM - renaming of a section | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/109 | 
  | Party Role re-modelling proposal | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/116 | 
  | Design principles - Editorial changes | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/121 | 
  | Intro to LDM - Editorial changes | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/122 | 
  | Design principles - Wording changes | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/130 | 
  | Entity Forbearance measure - rename | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/132 | 
  | [LDM] remove role subtypes from Credit facility | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/144 | 
  | [LDM] Remove unused reference data subtypes | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/146 | 
  
 # Annex 2:  List of commits relevant for the BIRD LDM   
 This list shows the descriptions given to each change that is stored – or committed – in the version control system used for the BIRD LDM in GitLab, after the release 6.0.0 of the BIRD LDM.. The full list can be found in the ECB SoFa environment for the BIRD logical data model (https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/commits/main). 
 
 | Date | Change | 
 | --- | --- |
 | 16/12/2022 |     made both value attributes of entity type 'Real estate collateral' optional because only one of them is needed. | 
 | 16/12/2022 |     >fix: made the word 'fair value' lower case in the name of the attribute 'Type of proection valuation approach for fair value' of entity type 'Aircraft collateral'. | 
 | 16/12/2022 |     >doc: updated the subviwew on collateral usage as an instrument and updated the definition of collateral itself. | 
 | 16/12/2022 |     >fix: removed unassigned domain | 
 | 16/12/2022 |     >fix: IL with adding columns Protection value date and Type of hedge | 
 | 16/12/2022 |     >fix: added Protection value date | 
 | 16/12/2022 |     >fix: renamed interest only to interest-only in the entity type name and the attribute name and the definitions. | 
 | 15/12/2022 |     >fix: added attribute Type of hedge to Over the counter (OTC) Derivative as a hedge | 
 | 15/12/2022 |     >fix: foreign key fixes in IL | 
 | 15/12/2022 |     updated the version number of the LDM from 6.0.0 to 6.1.0 | 
 | 15/12/2022 |     >chore: Update the name of self employed natural person to Self-employed natural person. Likewise for Non-self-employed natural person. | 
 | 14/12/2022 |     >fix: fixes to domains of IL | 
 | 14/12/2022 |     >chore: names of unassigned domains | 
 | 13/12/2022 |     >fix: Rename relationship type Forbearance measure is applied to Renegotiated financial asset instrument with forbearance measure | 
 | 13/12/2022 |     >fix: allowed values of domain Party code type | 
 | 13/12/2022 |     >fix: attribute Type of product to Debt securities issued | 
 | 13/12/2022 |     >fix: domain of attribute Year | 
 | 13/12/2022 |     >chore: update the lay-out of the logical diagram of the LDM. | 
 | 12/12/2022 |     >fix: changed layout of reference data | 
 | 12/12/2022 |     >fix: changed layout of the LDM | 
 | 12/12/2022 |     >feat: removed protection value entity since explicit representation of numeric values was implemented in collateral | 
 | 12/12/2022 |     Merge of changes regarding syndicated loans, ETDs, collateral and EU parties distinction | 
 | 12/12/2022 |     >doc: added description of Financial contracts | 
 | 12/12/2022 |     >doc: added description of Trade receivable collateral | 
 | 12/12/2022 |     >doc: added description of Life insurance policy pledged collateral | 
 | 12/12/2022 |     >doc: added description of Entity group and transaction role | 
 | 12/12/2022 |     >fix: assigned domains to attributes with Unknown domain | 
 | 12/12/2022 |     >feat: added domains for address party discriminators | 
 | 12/12/2022 |     >feat: added Abstract instrument role domain | 
 | 12/12/2022 |     >doc: updated descriptions in Exchange tradable derivative position role subtypes | 
 | 12/12/2022 |     >fix: updated attributes in Exchange tradable derivative position role subtypes | 
 | 08/12/2022 |     >feat: added relationship Postal code of SSM member country is a location of Real estate located in member state | 
 | 08/12/2022 |     >feat: restructured entities Address, Pstal code, country to allow for distinction between EU and non EU parties | 
 | 05/12/2022 |     >fix: added Fair values to collateral hierarchy explicitly | 
 | 05/12/2022 |     >fix: removed attribute 'security status' from entity type 'Security' and renamed foreign key attribute 'security status1' to 'Security status'. This got rid of the double attribute. | 
 | 05/12/2022 |     >fix updates to the names of the newly created attributes for specific collateral values. | 
 | 22/11/2022 |     >feat: added renamed Type of protection value and Type of protection valuation approach to be more specific in collateral | 
 | 22/11/2022 |     >feat: added Type of protection value and Type of protection valuation approach to Security and Other financial collateral | 
 | 22/11/2022 |     >feat: added Life insurace and Trade receivable to collateral | 
 | 22/11/2022 |     >feat: added Type of protection value and Type of protection valuation approach to Financial collateral | 
 | 22/11/2022 |     >feat: added Type of protection value and Type of protection valuation approach to Other commodity collateral | 
 | 22/11/2022 |     >feat: added Type of protection value and Type of protection valuation approach to Other non-registered collateral | 
 | 22/11/2022 |     >feat: added Type of protection valuation approach for registered collateral | 
 | 22/11/2022 |     >feat: added Type of protection value to Registered collateral | 
 | 10/11/2022 |     >feat: populated entity Fair valued exchange tradable derivative liability position | 
 | 08/11/2022 |     >fix: removed credit facility role | 
 | 07/11/2022 |     >fix: Removed the word "of". "one of the of several" --> "one of the several". | 
 | 07/11/2022 |     >feat: added subtyping layer to party roles | 
 | 07/11/2022 |     >feat: added Fair value attributes to ETD positions | 
 | 04/11/2022 |     >feat: added Carrying amount and Accounting classification to ETD | 
 | 04/11/2022 |     >feat: removed subtypes from reference entities | 
 | 03/11/2022 |     >fix: lay-out changes | 
 | 03/11/2022 |     >feat: removed credit facility roles | 
 | 03/11/2022 |     >doc: added description to atribute Syndicated financial contract identifier | 
 | 03/11/2022 |     >feat: added Syndicated contract entity | 
 | 03/11/2022 |     >feat: added Syndicated contract member entity | 
 | 03/11/2022 |     >feat: added entity Single financial contract | 
 | 03/11/2022 |     >fix: Fixed a typo - Reverse repurchase agreemnts --> Reverse repurchase agreements | 
 | 03/11/2022 |     Merge branch 'feature/explicit_reference_data' into 'develop' | 
 | 02/11/2022 |     >doc: rearranging the model | 
 | 02/11/2022 |     >fix: Fixed a typo in the definition of Asset pool Loon (excluding repurchase agreement) assignment: an Loan --> a Loan | 
 | 31/10/2022 |     >fix: update to the lay-out of the logical data model. | 
 | 31/10/2022 |     >fix: updated the lay-out of the logical model. | 
 | 27/10/2022 |     >Fix: Added AnaCredit regulation as a document. Updated the definition of attribute 'probability of default in AnaCredit' to match the definition in the AnaCrdit regulation. | 
 | 27/10/2022 |     Added AnaCredit regulation as a document. updated the definition of probability of default in AnaCredit to match the definition in AnaCredit regulation. | 
 | 21/10/2022 |     >fix: renamed entity type 'securities financial transaction' to 'Securities financing transaction'. It now fits with both the name used in the definition and with the text found on the internet. Also rephrased the definition from plural to singular. | 
 | 20/10/2022 |     >fix: renamed entity Forbearance measure into Forbearance measure type | 
 | 20/10/2022 |     Removed relationship and foreign key Accounting classification for assets is applied to Balance sheet recognised financial asset(s) because it was 1) duplicated and 2) pointed to financial liabilities instead of financial assets. | 
 | 13/10/2022 |     Both the grid and the page grid are not shown anymore in the Logical view. | 
 | 13/09/2022 |     >fix: description of Real estate collateral | 
 | 13/09/2022 |     >fix: fixed domain Group role type | 
 | 13/09/2022 |     >fix: fixed values of domain Balance shet recognition of the financial asset | 
 | 13/09/2022 |     >feat: amended description of Collateral | 
 | 22/08/2022 |     >feat: added constraint creation to fe procedure | 
 | 04/08/2022 |     >feat: added Security status as reference entity | 
 | 04/08/2022 |     >feat: added Institutional sector as reference entity | 
 | 04/08/2022 |     >feat: added Treatment of securitised / transfered assets in balance sheet as reference entity | 
 | 04/08/2022 |     >feat: added Structured note indicator as reference entity | 
 | 04/08/2022 |     >feat: added Simple, transparent and standardised (STS) securitisation indicator as reference entity | 
 | 04/08/2022 |     >feat: added Significant risk transfer type as reference entity | 
 | 04/08/2022 |     >feat: added Short term credit assessment indicator as reference entity | 
 | 04/08/2022 |     >feat: added Security level as reference entity | 
 | 04/08/2022 |     >feat: added Security guarantee level as reference entity | 
 | 04/08/2022 |     >feat: added Retail exposure according to CRR, Article 123 (b) indicator as reference entity | 
 | 04/08/2022 |     >feat: added Re-securitisation indicator as reference entity | 
 | 04/08/2022 |     >feat: added Repayment rights as reference entity | 
 | 04/08/2022 |     >feat: added Renegotiation status as reference entity | 
 | 04/08/2022 |     >feat: added Reference rate as reference entity | 
 | 04/08/2022 |     >feat: added Purpose as reference entity | 
 | 04/08/2022 |     >feat: added Pulling effect indicator as reference entity | 
 | 04/08/2022 |     >feat: added Protection value reported in AnaCredit indicator as reference entity | 
 | 04/08/2022 |     >feat: added Project finance loan indicator as reference entity | 
 | 04/08/2022 |     >feat: added Truncated primary asset classification as reference entity | 
 | 04/08/2022 |     >feat: added Payment frequency as reference entity | 
 | 04/08/2022 |     >feat: added Original maturity as reference entity | 
 | 04/08/2022 |     >feat: added Main debtor indicator as reference entity | 
 | 04/08/2022 |     >feat: added Legal proceeding status as reference entity | 
 | 04/08/2022 |     >feat: added Legal form as reference entity | 
 | 04/08/2022 |     >feat: added Initial exposure class of the security as reference entity | 
 | 04/08/2022 |     >feat: added Immediate parent undertaking as reference entity | 
 | 04/08/2022 |     >feat: added Immediate parent according to AnaCredit indicator as reference entity | 
 | 04/08/2022 |     >feat: added High liquidity and credit quality (HQLA) indicator as reference entity | 
 | 04/08/2022 |     >feat: added Forbearance status as reference entity | 
 | 04/08/2022 |     >feat: added Fair value hierarchy as reference entity | 
 | 04/08/2022 |     >fix: description of Reporting agent identifier | 
 | 28/07/2022 |     >feat: added Fair value designation as a reference entity | 
 | 28/07/2022 |     >feat: added ECAI/ECA as a reference entity | 
 | 28/07/2022 |     >feat: added Enterprise size (calculated) as a reference entity | 
 | 28/07/2022 |     >feat: added Enterprise size as a reference entity | 
 | 28/07/2022 |     >feat: added Enterprise indicator as a reference entity | 
 | 28/07/2022 |     >feat: added Eligible for central bank funding indicator as a reference entity | 
 | 28/07/2022 |     >feat: added Early redemptions included indicator as a reference entity | 
 | 28/07/2022 |     >feat: added Balance sheet recognition status as a reference entity | 
 | 28/07/2022 |     >feat: added Assessment aproach for credit quality status as a reference entity | 
 | 28/07/2022 |     >feat: added Area where the entity is located as a reference entity | 
 | 28/07/2022 |     >feat: added Approach for prudential purposes as a reference entity | 
 | 28/07/2022 |     >feat: added Accrued interests for market values indicator as a reference entity | 
 | 28/07/2022 |     >feat: added Accounting treatment (IFRS Group) as a reference entity | 
 | 28/07/2022 |     >feat: added Accounting treatment (CRR Group) as a reference entity | 
 | 18/07/2022 |     >feat: added reference entity Accounting hedge indicator | 
 | 30/06/2022 |     >fix: fix members of domain Subordinated debt indicator | 
 | 30/06/2022 |     >feat: added Significant asset class entity as a reference entity | 
 | 29/06/2022 |     >fix: removed duplicated relationship | 
 | 29/06/2022 |     >feat: added Subject to operating lease type entity as a reference entity | 
 | 29/06/2022 |     >feat: added Source of encumbrance entity as a reference entity | 
 | 29/06/2022 |     >feat: added Revolving loan type entity as a reference entity | 
 | 29/06/2022 |     >feat: added Revocable type entity as a reference entity | 
 | 28/06/2022 |     >feat: added Purchased credit-impaired type entity as a reference entity | 
 | 28/06/2022 |     >feat: added Performing forborne exposure under probation reclassified from non-performing type entity as a reference entity | 
 | 28/06/2022 |     >feat: added Non-performing prior to forbearance type entity as a reference entity | 
 | 28/06/2022 |     >feat: added Measurement method entity as a reference entity | 
 | 28/06/2022 |     >feat: added LOCOM type entity as a reference entity | 
 | 28/06/2022 |     >feat: added Impairment status type entity as reference entity | 
 | 28/06/2022 |     >fix: removed duplicated relationship between Accounting classification and Balance sheet recognised financial asset instrument | 
 | 27/06/2022 |     >feat: added Impairment assessment method entity as a reference entity | 
 | 27/06/2022 |     >feat: added Held for sale type as a reference entity | 
 | 27/06/2022 |     >feat: added Fiduciary instrument type as a reference entity | 
 | 27/06/2022 |     >feat: created relationships with Currency | 
 | 13/04/2022 |     >fix: removed domains that are not used | 
 | 11/04/2022 |     >fix: cascaded reationship on Protection Protection provider assignment | 
 | 11/04/2022 |     >feat: added overlapping attributes on Instrument Protection arrangement assignment, Securitisation | 
 | 11/04/2022 |     >fix: made Deposit protects Tranch in a synthetic securitisation without SSPE being a deposit into an identifying relationship | 
 | 06/04/2022 |     >fix: replaced attributes Subordinated debt indicator in Debt security and Financial asset instrument with reference to Subordinated debt type | 
 | 06/04/2022 |     >feat: added CRR & BSI regulation and liked them to relevant entities | 
 | 06/04/2022 |     >feat: created Subordinated debt type as Reference data | 
 | 07/03/2022 |     >fix: fixed relationship between Accounting classification and Balance sheet recognised financial asset instrument (was related to Accounting classification for liabilities) | 
 | 07/02/2022 |     >feat: added overlapping attributes to folded overlapping attributes | 
 | 07/02/2022 |     >feat: renamed foreign keys in Security related assignments | 
 | 07/02/2022 |     >feat: renamed foreign keys in Entity role assignments | 
 | 07/02/2022 |     >feat: renamed foreign keys in Instrument Party related | 
 | 07/02/2022 |     >feat: renamed foreign keys in Securitisation related assignments | 
 | 07/02/2022 |     >feat: renamed foreign keys in Instrument Protection related | 
 | 07/02/2022 |     >feat: renamed foreign keys in Instrument assignments | 
 | 07/02/2022 |     >feat: renamed foreign keys with Model Context in Securitisation related | 
 | 07/02/2022 |     >feat: renamed foreign keys with Modex Context in Security related | 
 | 07/02/2022 |     >feat: renamed foreign keys with Model Context in Credit facility related | 
 | 07/02/2022 |     >feat: renamed foreign keys with Model Context in Instrument related | 
 | 07/02/2022 |     >feat: rename relationships with Model Context | 
 | 04/02/2022 |     >feat: renamed foreign keys in Contract related | 
 | 04/02/2022 |     >feat: renamed foreign keys in Group related | 
 | 04/02/2022 |     >feat: renamed foreign keys in Balance sheet related | 
 | 04/02/2022 |     >feat: sort attributes in Rating system related | 
 | 04/02/2022 |     >feat: renamed foreign keys in Immediate parent | 
 | 04/02/2022 |     >feat: renamed foreign keys of Party role, Orgnasation role, Legal person role | 
 | 04/02/2022 |     >feat: rename foreign keys in Organisation risk data and Organisation derived data | 
 | 04/02/2022 |     >feat: added Model Context Entity with Attributes Refernce date and Reporting agent identifier | 
 | 20/01/2022 |     >fix: renamed Purchased credit impaired attribute to Purchased credit impaired indicator, assigning a different SQL Domain | 
 | 17/12/2021 |     >fix: updated sql domain of Postal code Attribute | 
 | 17/12/2021 |     >fix: added Protection allocated value to Instrument Collateral received instrument assignment | 
 | 16/12/2021 |     >fix: moved Attribute Arrears for the instrument from Balance sheet recognised financial asset instrument to Financial asset instrument because it is an AnaCredit reporting requirement | 
 | 16/12/2021 |     >fix: removed Attributes Payment frequency and Type of amortisation from Balance sheet recognised financial asset instrument | 
 | 08/12/2021 |     >feat: integration of Reference date | 
 | 02/12/2021 |     >feat: added missing Entity Rating grade for issue based rating system Debt security assignment to link Debt securities with their ratings | 
 | 01/12/2021 |     >fix: typo in definition of Rating agency | 
 | 01/12/2021 |     >fix: specify data type for remaining Attributes (mainly SHS or FINREP related) | 
 | 01/12/2021 |     >fix: specify correct domains for Attributes used in AnaCredit, e.g. Carrying amount | 
 | 30/11/2021 |     >fix: updated definition of Entity Default status | 
 | 30/11/2021 |     >fix: removed Relationship between Debt security Debtor assignment and Loan debtor Party role | 
 | 30/11/2021 |     >fix: description of Attribute Central bank eligible | 
 | 29/11/2021 |     >fix: removed relationship between Accounting classification for assets and Balance sheet recognised financial liability instrument | 
 | 29/11/2021 |     >fix: fixed relationship between Accounting classification and Balance sheet recognised financial liability instrument (was related to Accounting classification for assets) | 
 | 29/11/2021 |     >fix: renamed Purchased credit impaired to Purchased credit impaired indicator | 
 | 29/11/2021 |     fix: replaced Attribute Prudential portfolio with reference to Entity Prudential portfolio for Balance sheet recognised financial asset instrument | 
 | 29/11/2021 |     >fix: removed Impairment assessment method because it is reflected in the subtyping by retail exposure | 
 | 26/11/2021 |     >feat: set default value for party role attribute in assignment Entities | 
 | 25/11/2021 |     >fix: amended description of Loan debtor Party role type Attribute from "The party identifier of the involved debtor" to "The loan debtor role" | 
 | 25/11/2021 |     >fix: replaced Attribute Accounting classification by reference to Entity Accounting classification for assets / liabilities | 
 
