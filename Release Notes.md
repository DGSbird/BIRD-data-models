# Release Notes LDM 6.3
This document contains both the high-level release notes and - in the
annexes - the details of the of the changes from version 6.2 as
published in July 2023 to version 6.3. This describes the summary of
the changes made to the LDM since its previous release. It is based on
the issues in GitLab that were included in this release.


## Older Release Notes
Older release notes can be found in the [GitLab
repo](https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/tree/develop?ref_type=heads).

# Summary of Changes
The past half year, we updated 127 entity types, added 59 new entity
types, of which 13 are derived data entity types, and we removed 11
entity types. Of those many changes in the logical data model (LDM)
the following are the most impactful. These are mainly for FINREP, the
Fundamental Review of the Trading Book (FRTB), with a handful for
AnaCredit.

## Many Updates for the FINREP Alignment. 
1. More subtypes related to real estate to include both AnaCredit and
   FINREP requirements.
2. Non-negotiable security positions, either forborne or non-forborne.
3. Multiple additions both for performing and for forbearance
   information.
4. New Perpetual versus Non-perpetual debt securities distinction.
4. More connections between collateral and securities and loans.
5. Many derived attributes for aiding the generation of the reporting
   templates.

## AnaCredit Additions
For AnaCredit we added the long missing attributes `next interest rate
reset date` and `interest rate reset frequency`. We also did split
parts of the instrument role _Financial asset instrument_ into a new
role called _Serviced asset instrument_ for those instruments that are
still serviced by the financial institution but are not considered to
be a financial asset.

## Inclusion of Fundamental Review of the Trading Book
The FRTB is the first part of COREP that is intentionally included. It
includes the risk factors and risk measures for the standardised
approach with links to the various assets that can cause the risk.

# Detailed Changes Included in Version 6.3
The changes recorded in Gitlab that are listed below have had a direct
impact on the model. These changes are split into two types. The first
concerns those changes where the structure of the model has been
amended or changed in such a way that when data is reported via the
BIRD LDM, the reported data would change. The second type of changes
are those that updated the model without impacting the structure of
the reported data.

## Updates that do not impact the structure of the logical data model/input layer
- Names of relationship types were updated to include the names of
  the entity types they relate to.
- Names of entity types and attributes where harmonised towards the
  English spelling.
- Small additions and update to various definitions to fix typing mistakes 
  and provide more clarity. 

## Updates that changed the structure of the logical data model/input layer

- The final AnaCredit attributes - Next interest rate reset date, and
  Interest rate reset frequency - have been added.
- Included new entity types to support the COREP reporting of the
  Fundamental Review of the Trading Book (FRTB)
- Moved most attributes from the instrument role _Financial asset
  instrument_ to the new entity type _Serviced asset instrument_. This
  is because instruments that are assets, but are only serviced by the
  financial institution are considered not to be _Financial asset
  instruments_ but they are _Serviced asset instruments_.

## Changes to domain members

- Updates to many members related to FINREP. 
- Inclusion of domains with members for FRTB.

## Changes to the forward engineering

- Only updates to fix bugs and streamline the process.

## Changes to the documentation

- The introduction to the LDM document contains updated pictures and
  an update for forbearance measures, and includes the highlights of
  FRTB.
- For ease of creating new issues, we introduced 3 templates that help
  with the creation of issues in GitLab. This is not so much a
  documentation change as an update to the process of capturing
  issues.


###	Introduction to the BIRD LDM
1. The introductory pictures to each chapter have been updated to
better illustrate which part of the model is discussed.  
2. The pictures in this document are updated to include the relevant
LDM changes that are listed above.


# Annex 1:	List of closed GitLab issues
This list shows the overview of issues covered in the release of the
BIRD LDM and its documentation. The full list of issues can be found here:
https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/

| Issue  | Link to GitLab issue | Milestone in GitLab |
|--------|----------------------|---------------------|
| Interest rate reset frequency is missing                                                                                                                        | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/3   | AnaCredit requirements                                                       |
| Next interest rate reset date is missing                                                                                                                        | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/6   | AnaCredit requirements                                                       |
| AnaCredit.Protection received data.Type of protection missing values                                                                                            | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/11  | IReF requirements                                                            |
| Probability of default & Probability of default according to AnaCredit                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/36  | Implementation of suggestions from the subgroup on BIRD documentation review |
| Enhancement of the documentation (1) - Conceptual schema of entities and relationships                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/38  | Implementation of suggestions from the subgroup on BIRD documentation review |
| Enhancement of the documentation (2) - Overview of complete hierarchies                                                                                         | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/39  | Implementation of suggestions from the subgroup on BIRD documentation review |
| Descriptions/Names enhancements                                                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/49  | Implementation of suggestions from the subgroup on BIRD documentation review |
| Content - modelling suggestion - Classification of Debt securities Fair value                                                                                   | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/53  | Input from WS P regarding BIRD documentation review                          |
| Content - need for clarity - "BIRD LDM design principles - v1.0.0"                                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/54  | Input from WS P regarding BIRD documentation review                          |
| Content - need for clarity - "Introduction to the BIRD LDM - v1.0.1"                                                                                            | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/56  | Input from WS P regarding BIRD documentation review                          |
| Content - need for clarity - "BIRD 6.0.0 Overview of published files - v1"                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/57  | Input from WS P regarding BIRD documentation review                          |
| International organisation with and without International organisation code                                                                                     | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/68  | Amendments to the modelling approach                                         |
| Information, currently located in Financial asset instrument that is already required before the Instrument can act in the role of a Financial asset instrument | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/70  | AnaCredit requirements                                                       |
| Institutional unit replacing Institutional unit of foreign branches                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/71  | AnaCredit requirements                                                       |
| Review Instrument type definitions for possible overlaps / inconsistencies                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/72  | Amendments to the modelling approach                                         |
| Need for clarity - "Introduction to the BIRD LDM - v1.0.1" - instrument role why optional?                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/81  | Input from WS P regarding BIRD documentation review                          |
| Need for clarity - "Introduction to the BIRD LDM - v1.0.1" - definitions of collaterals                                                                         | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/88  | Input from WS P regarding BIRD documentation review                          |
| entity "default status" - questions on linkages                                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/93  | Input from WS P regarding BIRD documentation review                          |
| FE - Clarify what is normalization                                                                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/103 | Updates to the Forward Engineering documentation (WSP)                       |
| Collateral - Amend description (of Physical Collateral entity)                                                                                                  | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/105 | Updates to the LDM content (WSP)                                             |
| Intro to LDM - Clarify "Self-employed natural person" mandatory attributes                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/112 | Updates to the Introduction to LDM documentation (WSP)                       |
| FE - For consideration - Balance sheet total for legal/natural persons                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/114 | Updates to the Forward Engineering documentation (WSP)                       |
| FOR CLARIFICATION: Instrument types to fulfil AnaCredit requirements                                                                                            | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/117 | Request for clarification                                                    |
| Intro to LDM - Clarify abbreviation of classifications                                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/118 | Updates to the Introduction to LDM documentation (WSP)                       |
| FOR CLARIFICATION: Personal guarantees in the LDM                                                                                                               | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/124 | Request for clarification                                                    |
| Intro to LDM - Consider changing "Non-registered party" to "Organizational unit"                                                                                | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/125 | Updates to the Introduction to LDM documentation (WSP)                       |
| Intro to LDM - consistently report information about party role                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/126 | Updates to the Introduction to LDM documentation (WSP)                       |
| Need for clarity - "Introduction to the BIRD LDM - v1.0.1" - perpetuals as debt securities                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/127 | Input from WS P regarding BIRD documentation review                          |
| Attribute Accounting standard is missing from party data.                                                                                                       | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/133 | AnaCredit requirements                                                       |
| Rename attribute purpose to purpose type in financial asset instrument                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/137 | [LDM] Modelling debt                                                         |
| Roles of  OTC derivatives                                                                                                                                       | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/141 |                                                                              |
| [LDM] end date of interest-only period cannot be mandatory                                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/147 | [LDM] Modelling debt                                                         |
| Review and update the relationships in Non-financial asset and Non-financial liability                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/148 | [LDM] Modelling debt                                                         |
| Revisit "empty" generalisations in the LDM                                                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/154 | [LDM] Modelling debt                                                         |
| Names of entity types containing "issue based" must be hyphenated to "issue-based"                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/156 | [LDM] Modelling debt                                                         |
| Accounting measures in BIRD - no action to be taken for now                                                                                                     | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/158 | Implementation of suggestions from the subgroup on BIRD documentation review |
| NEXT INTEREST RATE RESET DATE                                                                                                                                   | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/165 | IReF requirements                                                            |
| Fair value option designation vs Fair value designation & Fair value changes                                                                                    | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/171 | Implementation of suggestions from the subgroup on BIRD documentation review |
| INSTTTNL_SCTR and INSTTTNL_SCTR_EBA_ITS - analysis and results                                                                                                  | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/176 | FINREP requirements                                                          |
| Finrep: requirements for collateral - Indicator for under construction/development                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/180 | FINREP requirements                                                          |
| Finrep: requirements for collateral - Indicator for with or without planning permission                                                                         | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/181 | FINREP requirements                                                          |
| Finrep: requirements for collateral - Type of real estate                                                                                                       | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/182 | FINREP requirements                                                          |
| Finrep: requirements for collateral - Commercial real estate corporation                                                                                        | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/183 | FINREP requirements                                                          |
| Finrep: Identification of main debtor of an instrument                                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/184 | FINREP requirements                                                          |
| Finrep: Litigation status                                                                                                                                       | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/185 | FINREP requirements                                                          |
| Finrep: Current Loan-to-value ratio                                                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/186 | FINREP requirements                                                          |
| [Asset Sec][FINREP] New derived attribute for loan: Performing status indicator                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/250 | FINREP requirements                                                          |
| Performing forborne exposure under probation reclassified from non-performing indicator                                                                         | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/276 | FINREP requirements                                                          |
| Inclusion of Fundamental Review of the Trading Book (FRTB)                                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/277 |                                                                              |
| Collateral received - uncapped amounts                                                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/278 | FINREP requirements                                                          |
| Date of past due on credit facility                                                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/338 | FINREP requirements                                                          |
| Investment on subsidiaries, joint ventures or associates                                                                                                        | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/339 | FINREP requirements                                                          |
| Loan commitments given and other commitments given                                                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/340 | FINREP requirements                                                          |
| Renegotiation status and forbearance measures                                                                                                                   | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/341 | FINREP requirements                                                          |
| Forbearance measure type                                                                                                                                        | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/342 | FINREP requirements                                                          |
| Instruments subject to forbearance measures at multiple points in time                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/343 | FINREP requirements                                                          |
| Instruments with forbearance measures granted during the period                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/344 | FINREP requirements                                                          |
| Non-performing prior to forbearance indicator                                                                                                                   | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/345 | FINREP requirements                                                          |
| Accumulated changes                                                                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/349 | FINREP requirements                                                          |
| Changes in fair value in the period                                                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/351 | FINREP requirements                                                          |
| Derived attribute â€“ Time Past due                                                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/352 | FINREP requirements                                                          |
| Fair value hierarchy                                                                                                                                            | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/353 | FINREP requirements                                                          |
| Impairment status - General allowances for GAAP                                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/354 | FINREP requirements                                                          |
| Specific allowances amount for national GAAP                                                                                                                    | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/355 | FINREP requirements                                                          |
| Add definition to attributes Measurement method                                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/360 | Amendments to the modelling approach                                         |
| Immediate parent undertaking in Organisation derived data is obsolete                                                                                           | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/361 | Amendments to the modelling approach                                         |
| Finrep: ACCNTNG_FRMWRK                                                                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/365 | FINREP requirements                                                          |
| Finrep: ENTTY_RIAD_CD_RPRTNG_AGNT                                                                                                                               | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/366 | FINREP requirements                                                          |
| Finrep: SUBA_CD                                                                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/367 | FINREP requirements                                                          |
| Finrep: Gross Carrying Amount (GRSS_CRRYNG_AMNT)                                                                                                                | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/371 | FINREP requirements                                                          |
| Finrep: Cost and Revaluation model                                                                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/373 | FINREP requirements                                                          |
| Finrep: Protection allocated value for Credit Facility                                                                                                          | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/374 | FINREP requirements                                                          |
| Finrep: Of which: Software assets                                                                                                                               | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/376 | FINREP requirements                                                          |
| Collateral assignment                                                                                                                                           | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/378 | FINREP requirements                                                          |
| Finrep: Accumulated coverage ratio                                                                                                                              | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/380 | FINREP requirements                                                          |
| Finrep: Application forbearance status date (APPLCTN_FRBRNC_STTS_DT)                                                                                            | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/381 | FINREP requirements                                                          |
| Accumulated write-offs â€“ Partial and Total                                                                                                                    | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/382 | FINREP requirements                                                          |
| Purchased or originated credit-impaired financial assets                                                                                                        | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/387 | FINREP requirements                                                          |
| Transfers between impairment stages                                                                                                                             | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/403 | FINREP requirements                                                          |
| derivation rule for ENTRPRS_SZ                                                                                                                                  | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/405 | FINREP requirements                                                          |
| Non-financial assets taken into possession                                                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/406 | FINREP requirements                                                          |
| New collateral obtained by taking possession during the period                                                                                                  | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/409 | FINREP requirements                                                          |
| Debt securities collateralised                                                                                                                                  | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/410 | FINREP requirements                                                          |
| Fair value                                                                                                                                                      | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/412 | FINREP requirements                                                          |
| Held for sale indicator                                                                                                                                         | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/413 | FINREP requirements                                                          |
| Entity types not showing up in logical diagram                                                                                                                  | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/415 |                                                                              |
| Add members to Accounting classification domain                                                                                                                 | https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/issues/419 | FINREP requirements                                                          |


# Annex 2:  List of Updated or New Entity Types

<!-- To get the numbers and list below, run the python script listNewAndUpdatedEntityTypes.py -->

This is the list of entity types in the LDM where something has
changed. This can range from a definition change, or an attribute or
relationship type change, to a technical change in the internal file
structure of the file that represents the entity type. For these 201
changed entity types, 886 changes where recorded.

 - Abstract instrument role 
 - Advance Debtor assignment 
 - Assigned debtor 
 - Balance sheet recognised exchange tradable derivative asset position 
 - Balance sheet recognised exchange tradable derivative asset position derived data 
 - Balance sheet recognised exchange tradable derivative liability position 
 - Balance sheet recognised financial asset instrument 
 - Balance sheet recognised financial asset instrument according to International Financial Reporting Standard (IFRS) 
 - Balance sheet recognised financial asset instrument according to national general accepted accounting principles (nGAAP) 
 - Balance sheet recognised financial asset instrument derived data 
 - Balance sheet recognised financial liability instrument 
 - Branch 
 - Central bank and private sector company 
 - Collateral 
 - Commercial real estate and offices and commercial premises collateral 
 - Commercial real estate collateral 
 - Commercial real estate loan indicator 
 - Commodity risk factor for standardised approach 
 - Country 
 - Credit facility 
 - Credit facility Collateral received instrument assignment 
 - Credit facility risk data 
 - Credit facility risk data derived data 
 - Credit spread risk (CSR) non-securitisation risk factor for standardised approach 
 - Curvature 
 - Date / period of application of forbearance measure type 
 - Debt financing according to AnaCredit indicator 
 - Debt security 
 - Debt security Protection arrangement assignment 
 - Debt security derived data 
 - Debt security issued (by the reporting agent) 
 - Default financial asset instrument individually assessed 
 - Delta sensitivity 
 - Deposit 
 - Equity and fund security 
 - Equity risk factor for standardised approach 
 - Equity security 
 - European Union member country 
 - European Union member postal code 
 - Exchange tradable derivative position 
 - Fair value designation 
 - Fair value hierarchy 
 - Fair value option designation 
 - Fair valued balance sheet recognised financial asset instrument 
 - Fair-valued balance sheet recognised exchange tradable derivative asset position 
 - Fair-valued balance sheet recognised exchange tradable derivative liability position 
 - Fair-valued balance sheet recognised financial liability instrument 
 - Fair-valued debt security issued 
 - Financial asset instrument 
 - Financial asset instrument derived data 
 - Financial contract 
 - Financial corporation 
 - Financial guarantee instrument 
 - Forbearance measure granted during reference period indicator 
 - Forbearance measure type 
 - Forbearance status 
 - Forborne long non-negotiable security position 
 - Forborne long non-negotiable security position indicator 
 - Foreign exchange risk factor for standardised approach 
 - Fundamental review of the trading book standard approach risk measure 
 - Fundamental review of the trading book standard approach risk measure for ETD positions 
 - Fundamental review of the trading book standard approach risk measure for OTC positions 
 - Fundamental review of the trading book standard approach risk measure for security positions 
 - General interest rate risk (GIRR) factor for standardised approach 
 - Held for sale type 
 - Immaterial rights as collateral 
 - Impairment status 
 - Initial exposure class of the security 
 - Initial impairment status 
 - Institutional unit 
 - Instrument 
 - Instrument resulting directly from a Financial contract 
 - Interest rate reset frequency 
 - Internal group role 
 - International organisation 
 - International securities identification number (ISIN) security 
 - Investment property not taken into possession 
 - Investment property taken into possession 
 - Issue-based rating system 
 - Land excluding agriculture 
 - Land including agriculture 
 - Listed central bank and private sector company 
 - Listed indicator 
 - Litigation status 
 - Loan (excluding repurchase agreement) 
 - Loan (excluding repurchase agreement) and advance 
 - Loan (excluding repurchase agreement) and advance Collateral assignment 
 - Loan (excluding repurchase agreement) and advance Collateral assignment derived data 
 - Loan (excluding repurchase agreement) and advance derived data 
 - Loan (excluding repurchase agreement) derived data 
 - Long debt security position 
 - Long debt security position Prudential portfolio assignment 
 - Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment 
 - Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment according to International Financial Reporting Standard (IFRS) 
 - Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment according to national general accepted accounting principles (nGAAP) 
 - Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment derived data 
 - Long equity or fund security position Prudential portfolio assignment Accounting classification for assets assignment according to International Financial Reporting Standard (IFRS) 
 - Long negotiable security position 
 - Long non-negotiable security position 
 - Long security position 
 - Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment 
 - Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment derived data 
 - Long security position Prudential portfolio assignment 
 - Long security position derived data 
 - Measurement method 
 - Multilateral development bank indicator 
 - Multiple forbearance measures in place indicator 
 - Negotiable security indicator 
 - Non-International securities identification number (ISIN) security derived data 
 - Non-International securities identification number (Non-ISIN) security 
 - Non-fair valued balance sheet recognised financial asset instrument 
 - Non-fair-valued balance sheet recognised exchange tradable derivative asset position 
 - Non-fair-valued balance sheet recognised exchange tradable derivative liability position 
 - Non-fair-valued balance sheet recognised financial liability instrument 
 - Non-fair-valued debt security issued 
 - Non-forborne long non-negotiable security position 
 - Non-listed central bank and private sector company 
 - Non-performing debt security 
 - Non-performing exit criteria met indicator 
 - Non-performing financial asset instrument debtor assessed 
 - Non-performing non-default financial asset instrument individually assessed 
 - Non-performing non-retail exposure class financial asset instrument 
 - Non-performing prior to forbearance type 
 - Non-perpetual debt security 
 - Non-retail exposure financial asset instrument 
 - Off-balance sheet item given instrument 
 - Off-balance sheet item given instrument derived data 
 - Offices and commercial premises collateral 
 - Offices and commercial premises not related to land collateral 
 - Offices and commercial premises related to land collateral 
 - Organisation 
 - Organisation with legal proceeding 
 - Organisation without legal proceeding 
 - Other collateral received instrument 
 - Other commitment 
 - Other financial collateral 
 - Other intangible asset not taken into possession 
 - Other intangible asset taken into possession 
 - Other loan 
 - Other non-financial asset taken into possession 
 - Other party code 
 - Over the counter (OTC) Derivative as a hedge 
 - Over the counter (OTC) Derivative instrument 
 - Party code identifier 
 - Party derived data 
 - Party risk data 
 - Performing debt security 
 - Performing financial asset instrument debtor assessed 
 - Performing forborne exposure under probation reclassified from non-performing type 
 - Performing non-default financial asset instrument individually assessed 
 - Performing non-retail exposure class financial asset instrument 
 - Performing status 
 - Perpetual debt security 
 - Physical collateral 
 - Project finance loan indicator 
 - Property, plant and equipment not taken into possession 
 - Property, plant and equipment taken into possession 
 - Protection arrangement 
 - Prudential consolidation group 
 - Purpose type 
 - Rating agency 
 - Rating grade 
 - Rating grade for issue-based rating system 
 - Rating grade for issue-based rating system Debt security assignment 
 - Rating system 
 - Re-securitisation type 
 - Real estate collateral 
 - Registered collateral 
 - Registered postal code system party 
 - Renegotiated financial asset instrument with forbearance measure 
 - Renegotiated financial asset instrument with forbearance measure derived data 
 - Renegotiation status 
 - Reporting agent internal group role 
 - Residential real estate collateral 
 - Revocable type 
 - Risk factor for standardised approach 
 - Risk position (Kb) per bucket derived data 
 - Securitisation correlation trading portfolio (CTP) Risk Factor for standardised approach 
 - Securitisation non-correlation trading portfolio, (non-CTP) Risk Factor for standardised approach 
 - Securitisation tranche 
 - Security 
 - Security Issuer assignment 
 - Security derived data 
 - Security or exchange tradable derivative position 
 - Security position 
 - Serviced asset instrument 
 - Short security position 
 - Software assets indicator 
 - Subject to impairment indicator 
 - Subordinated debt indicator 
 - Time past due band 
 - Trade receivable 
 - Tranche in a synthetic securitisation 
 - Tranche in a synthetic securitisation with Securitisation Special Purpose Entity (SSPE) 
 - Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) 
 - Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a deposit 
 - Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a financial guarantee 
 - Transfer between impairment stages 
 - Type of interest rate 
 - Under construction or developement indicator 
 - Vega sensitivity 

# Annex 3:  List of Commits Relevant for the BIRD LDM

 This list shows the descriptions given to each change that is stored
 – or committed – in the version control system used for the BIRD LDM
 in GitLab, after the release 6.2 of the BIRD LDM. The full list
 can be found in the ECB SoFa environment for the BIRD logical data
 model
 (https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model/-/commits/main).
 
<!-- create the basics of the list below with the following command: -->
<!-- git log --date=format:'%Y.%m.%d' --pretty=format:'%ad %B' > gitlog.txt -->

 
 | Date | Change | 
 | --- | --- |
 | 2023.12.12 |  >feat: added Accounting framework domain and assigned it to Accounting standard for statistical reporting, Accounting standard for solo reporting, Accounting standard for consolidated reporting | 
 |  |  | 
 | 2023.12.12 |  >feat: added description to Loan (excluding repurchase agreement) and advance Collateral assignment derived data | 
 |  |  | 
 | 2023.12.12 |  >feat: moved attributes Allocated collateral value uncapped pre haircuts and Allocated unused collateral value from Loan (excluding repurchase agreement) and advance Collateral assignment to Loan (excluding repurchase agreement) and advance Collateral assignment derived data | 
 |  |  | 
 | 2023.12.12 |  >feat: created Loan (excluding repurchase agreement) and advance Collateral assignment derived data entity | 
 |  |  | 
 | 2023.12.12 |  >fix: renamed attribute Type of securitisation tranche to Securitisation tranche type and created the domain | 
 |  |  | 
 | 2023.12.12 |  >feat: created domain for Long negotiable security position | 
 |  |  | 
 | 2023.12.12 |  >feat: created domain for Transfer between impairment stages | 
 |  |  | 
 | 2023.12.12 |  >feat: created domain for Initial imapirment status | 
 |  |  | 
 | 2023.12.12 |  >fix: renamed attribute from Accounting standard for folo reporting to Accounting standard for solo reporting | 
 |  |  | 
 | 2023.12.11 |  >feat: created domain for Subject to impairment indicator | 
 |  |  | 
 | 2023.12.11 |  >feat: added Subject to impairment indicator to Financial asset instrument | 
 |  |  | 
 | 2023.12.11 |  >feat: added Subject to impairment indicator to Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment | 
 |  |  | 
 | 2023.12.11 |  >feat: created Subject to impairment indicator reference entity | 
 |  |  | 
 | 2023.12.07 |  >fix: updated the name of associative entity type 'Other Instrument Collateral received instrument assignment' to 'Instrument Collateral received instrument assignment' to indicate that the assignment is possible for all instruments. | 
 | | >fix: updated the name of the relationship type 'Collateral protects Loan(s) (excluding repurchase agreement) via Loan (excluding Repurchase agreement) Collateral assignment' to 'Collateral protects Loan(s) (excluding repurchase agreement) and advance via Loan (excluding Repurchase agreement) and advance Collateral assignment'. | 
 | | >fix: updated the name of the relationship type 'Loan (excluding repurchase agreement) and advance is protected by Protection item(s) via Loan (excluding repurchase agreement) Collateral assignment' to 'Loan (excluding repurchase agreement) and advance is protected by Protection item(s) via Loan (excluding repurchase agreement) and advance Collateral assignment' | 
 | | >fix: updated the name of associative entity type 'Loan (excluding repurchase agreement) Collateral assignment' to 'Loan (excluding repurchase agreement) and advance Collateral assignment' | 
 | | >fix: Updated the name of the relationship type 'Collateral received instrument protects Financial asset instrument(s) via Other Instrument Collateral received instrument assignment' to 'Collateral received instrument protects Financial asset instrument(s) via Instrument Collateral received instrument assignment'. | 
 | | >fix: updated the name of the relationship type 'Instrument is protected by Collateral received instrument(s) via Other Instrument Collateral received instrument assignment' to 'Instrument is protected by Collateral received instrument(s) via Instrument Collateral received instrument assignment'. | 
 |  |  | 
 | 2023.12.07 |  >feat: replaced attribute Change in fair value for the period into Fair value change | 
 |  |  | 
 | 2023.12.07 |  >feat: amended the description of attribute Fair value change to Fair value changes in the period and before taxes. | 
 |  |  | 
 | 2023.12.06 |  >feat: removed attribute Held for sale indicator from Short security position | 
 |  |  | 
 | 2023.12.04 |  >feat: updated the position of the foreign key attributes from entity type 'Institutional unit' in entity type 'Organisation'. | 
 | 2023.12.04 |  >feat: renamed entity type 'Debt security issued Protection arrangement assignment' to 'Debt security Protection arrangement assignment'. | 
 |  |  | 
 | 2023.12.04 |  >feat: created entity Balance sheet recognised exchange tradable derivative asset position derived data, added attribute Gross carrying amount | 
 |  |  | 
 | 2023.12.01 |  >feat: added Gross carrying amount to Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment derived data | 
 |  |  | 
 | 2023.12.01 |  >feat: added Gross carrying amount to Financial asset instrument derived data | 
 |  |  | 
 | 2023.11.29 |  >feat: Updated the relationship type 'Institutional unit comprises Financial Corporation' and changed its target from 'Financial corporation' to 'Organisation'. | 
 | | >feat: Renamed relationship type 'Institutional unit comprises Financial Corporation' to 'Institutional unit comprises organisation'. | 
 | | >feat: Added foreign key attributes 'Institutional unit Group identifier', Institutional unig Group Reference date', and 'Institutional unit Group Reporting agent identifier' to entity type 'Organisation'. | 
 | | >feat: Removed foreign key attributes 'Institutional unit Group identifier', Institutional unig Group Reference date', and 'Institutional unit Group Reporting agent identifier' from entity type 'Financial corporation'. | 
 |  |  | 
 | 2023.11.28 |  >fix: updated the source of relationship type 'Type of interest rate classifies Serviced asset instrument' from entity type 'Security' to entity type 'Serviced asset instrument'. | 
 | | >fix: removed attribute 'Type of interest rate' from entity type 'Security'. | 
 | | >fix: updated the definition of attribute 'Type of interest rate' of entity type 'Type of interest rate' to conform to the legal definition.> | 
 | | fix: Updated the name of relationship type 'Asset backed security has Securitisation non-correlation trading portfolio' to include the correct spelling of the name of entity type 'Securitisation non-correlation trading portfolio, (non-CTP) Risk Factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Currency is main currency for General interest rate risk (GIRR) factor' to include the correct spelling of the name of entity type 'General interest rate risk (GIRR) factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Date / period of application of forbearance measure classifies Long security position derived data' to include the correct spelling of the name of entity type 'Date / period of application of forbearance measure type'. | 
 | | >fix: Updated the name of relationship type 'Deposit protects Tranche in a synthetic securitisation without SSPE being a deposit via Tranche in a synthetic securitisation without SSPE being a deposit' to include the correct spelling of the name of entity type 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a deposit'. | 
 | | >fix: Updated the name of relationship type 'Equity security has equity risk factor' to include the correct spelling of the name of entity type 'Equity risk factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Exchange tradable derivative position specifies Fundamental review of the trading book standard approach risk measure for ETD' to include the correct spelling of the name of entity type 'Fundamental review of the trading book standard approach risk measure for ETD positions'. | 
 | | >fix: Updated the name of relationship type 'Fair value hierarchy classifies Fair-valued exchange tradable derivative liability position' to include the correct spelling of the name of entity type 'Fair-valued balance sheet recognised exchange tradable derivative liability position'. | 
 | | >fix: Updated the name of relationship type 'Fair value is applied to Fair-valued balance sheet recognised financial asset instrument(s)' to include the correct spelling of the name of entity type 'Fair value hierarchy'. | 
 | | >fix: Updated the name of relationship type 'Fair value is applied to Fair-valued balance sheet recognised financial asset instrument(s)' to include the correct spelling of the name of entity type 'Fair valued balance sheet recognised financial asset instrument'. | 
 | | >fix: Updated the name of relationship type 'Financial guarantee instrument guarantees Tranche in a synthetic securitisation without SSPE being a financial guarantee' to include the correct spelling of the name of entity type 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a financial guarantee'. | 
 | | >fix: Updated the name of relationship type 'Forborne long non-negotiable security position indicator classifies Non-negotiable security' to include the correct spelling of the name of entity type 'Forbearance measure type'. | 
 | | >fix: Updated the name of relationship type 'Forborne long non-negotiable security position indicator classifies Non-negotiable security' to include the correct spelling of the name of entity type 'Long security position'. | 
 | | >fix: Updated the name of relationship type 'Forborne non-negotiable security indicator classifies Non-negotiable security' to include the correct spelling of the name of entity type 'Forborne long non-negotiable security position indicator'. | 
 | | >fix: Updated the name of relationship type 'Forborne non-negotiable security indicator classifies Non-negotiable security' to include the correct spelling of the name of entity type 'Long non-negotiable security position'. | 
 | | >fix: Updated the name of relationship type 'Issuer has Credit spread risk (CSR) non-securitisation risk factor' to include the correct spelling of the name of entity type 'Credit spread risk (CSR) non-securitisation risk factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Litigation status is applied to Loan(s) and Advance(s)' to include the correct spelling of the name of entity type 'Loan (excluding repurchase agreement) and advance'. | 
 | | >fix: Updated the name of relationship type 'Loan (excluding repurchase agreement) and advance is protected by Protection item(s) via Loan (excluding Repurchase agreement) Collateral assignment' to include the correct spelling of the name of entity type 'Loan (excluding repurchase agreement) Collateral assignment'. | 
 | | >fix: Updated the name of relationship type 'Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment may have Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment derive data' to include the correct spelling of the name of entity type 'Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment derived data'. | 
 | | >fix: Updated the name of relationship type 'Negotiabel security indicator classifies International securities identification number (ISIN) security' to include the correct spelling of the name of entity type 'Negotiable security indicator'. | 
 | | >fix: Updated the name of relationship type 'Non-International securities identification number (ISIN) security has Non-International securities identification number (ISIN) security derived data' to include the correct spelling of the name of entity type 'Non-International securities identification number (Non-ISIN) security'. | 
 | | >fix: Updated the name of relationship type 'Non-performing prior to forbearance is applied to Credit facility' to include the correct spelling of the name of entity type 'Non-performing prior to forbearance type'. | 
 | | >fix: Updated the name of relationship type 'Relation_394' to include the correct spelling of the name of entity type 'Long security position derived data'. | 
 | | >fix: Updated the name of relationship type 'Risk factor for standardised approach has risk measure' to include the correct spelling of the name of entity type 'Fundamental review of the trading book standard approach risk measure'. | 
 | | >fix: Updated the name of relationship type 'Software assets indicator specifies Other intangible asset not taken into possessionv2' to include the correct spelling of the name of entity type 'Other intangible asset taken into possession'. | 
 | | >fix: removed primary key definition 'Long security position PK' from entity type 'Long security position', because it is a subtype of 'Security position' and inherits its primary key. | 
 |  |  | 
 | | >fix: Updated the name of relationship type 'Equity risk factor determines risk of Equity and fund security' to include the correct spelling of the name of entity type 'Equity risk factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Forborne long non-negotiable security indicator classifies Long non-negotiable security position' to include the correct spelling of the name of entity type 'Forborne long non-negotiable security position indicator'. | 
 | | >fix: Updated the name of relationship type 'Currency is second currency of General interest rate risk (GIRR) factor' to include the correct spelling of the name of entity type 'General interest rate risk (GIRR) factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Collateral protects Loan(s) (excluding repurchase agreement) via Loan (excluding Repurchase agreement) Collateral assignment' to include the correct spelling of the name of entity type 'Loan (excluding repurchase agreement) Collateral assignment'. | 
 | | >fix: Updated the name of relationship type 'Non-performing prior to forbearance indicator classifies Credit facility risk data' to include the correct spelling of the name of entity type 'Non-performing prior to forbearance type'. | 
 | | >fix: Updated the name of relationship type 'Software assets indicator specifies Other intangible asset not taken into possessionv2' to include the correct spelling of the name of entity type 'Other intangible asset taken into possession'. | 
 | | >fix: Updated the name of relationship type 'Fundamental review of the trading book standard approach risk measure has risk measure' to include the correct spelling of the name of entity type 'Risk factor for standardised approach'. | 
 | | >fix: Updated the name of relationship type 'Synthetic securitisation without involvement of an SSPE comprises Tranche in a synthetic securitisation without SSPE being a deposit' to include the correct spelling of the name of entity type 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a deposit'. | 
 | | >fix: Updated the name of relationship type 'Non-performing prior to forbearance indicator classifies Debt security issued (by the reporting agent)' to include the correct spelling of the name of entity type 'Non-performing prior to forbearance type'. | 
 | | >fix: Updated the name of relationship type 'Non-performing prior to forbearance indicator classifies Long security position Prudential portfolio assignment' to include the correct spelling of the name of entity type 'Non-performing prior to forbearance type'. | 
 |  |  | 
 | 2023.11.28 |  >feat: renamed associative entity type name from 'Debt security issued (by the reporting agent) Protection arrangement assignment' to 'Debt security Protection arrangement assignment'. | 
 | 2023.11.28 |  >feat: renamed relationship type 'Debt security issued (by the reporting agent) is secured via Debt security issued (by the reporting agent) Protection arrangement assignment' to 'Debt security is secured via Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: updated the source of the relationship type 'Debt security is secured via Debt security issued (by the reporting agent) Protection arrangement assignment' from 'Debt security issued (by the reporting agent)' to 'Debt security'. | 
 | 2023.11.28 |  >chore: updated the name of the creator of the logical design diagram from 'BIRD Work stream on data modelling' to 'BIRD Work Stream on Data Modelling'. | 
 |  |  | 
 | 2023.11.23 |  >feat: made attribute 'Taken into possession date' of entity type 'Other intangible asset taken into possession'. | 
 | | >feat: made attribute 'Taken into possession date' of entity type 'Property, plant and equipment taken into possession'. | 
 | | >feat: made attribute 'Taken into possession date' of entity type 'Investment property taken into possession'. | 
 | | >feat: made attribute 'Taken into possession date' of entity type 'Other non-financial asset taken into possession'. | 
 | 2023.11.23 |  >feat: removed entity type 'Other intangible asset taken into possession during the period'. | 
 | | >feat: removed entity type 'Other intangible asset taken into possession before the period' | 
 | | >feat: removed arc 'Other intangible asset taken into possession type'. | 
 | | >feat: removed discriminator attribute 'Other intangible asset taken into possession type' of entity type 'Other intangible asset taken into possession'. | 
 | | >feat: removed domain 'Other intangible asset taken into possession type'. | 
 | | >feat: removed entity type 'Property, plant and equipment taken into possession during the period'. | 
 | | >feat: removed entity type 'Property, plant and equipment taken into possession before the period' | 
 | | >feat: removed arc 'Property, plant and equipment taken into possession type'. | 
 | | >feat: removed discriminator attribute 'Property, plant and equipment taken into possession type' of entity type 'Property, plant and equipment taken into possession'. | 
 | | >feat: removed domain 'Property, plant and equipment taken into possession type'. | 
 | | >feat: removed entity type 'Investment property taken into possession during the period'. | 
 | | >feat: removed entity type 'Investment property taken into possession before the period' | 
 | | >feat: removed arc 'Investment property taken into possession type'. | 
 | | >feat: removed discriminator attribute 'Investment property taken into possession type' of entity type 'Investment property taken into possession'. | 
 | | >feat: removed domain 'Investment property taken into possession type'. | 
 | | >feat: removed entity type 'Other non-financial asset taken into possession during the period'. | 
 | | >feat: removed entity type 'Other non-financial asset taken into possession before the period' | 
 | | >feat: removed arc 'Other non-financial asset taken into possession type'. | 
 | | >feat: removed discriminator attribute 'Other non-financial asset taken into possession type' of entity type 'Other non-financial asset taken into possession'. | 
 | | >feat: removed domain 'Other non-financial asset taken into possession type'. | 
 | | >feat: added attribute 'Taken into possession date' to entity type 'Other intangible asset taken into possession'. | 
 | | >feat: added attribute 'Taken into possession date' to entity type 'Property, plant and equipment taken into possession'. | 
 | | >feat: added attribute 'Taken into possession date' to entity type 'Investment property taken into possession'. | 
 | | >feat: added attribute 'Taken into possession date' to entity type 'Other non-financial asset taken into possession'. | 
 |  |  | 
 | 2023.11.20 |  >feat: added Protection allocated value to Credit facility Collateral received instrument assignment | 
 |  |  | 
 | 2023.11.20 |  >feat: updated the name of the attribute 'accumulated write-offs - Total' to 'Accumulated total write-offs' for both 'Financial asset insturment derived data' and 'Long debt security position Prudential portolio Accounting classification for Financial Assets assignment'. | 
 | | >feat: updated the name of the attribute 'accumulated write-offs - Partial' to 'Accumulated Partial write-offs' for both 'Financial asset insturment derived data' and 'Long debt security position Prudential portolio Accounting classification for Financial Assets assignment'. | 
 | 2023.11.20 |  >fix: minor ammendment in the comment section of the entity 'software asset indicator' | 
 |  |  | 
 | 2023.11.20 |  >feat: Changed the location of the 'Software asset indicator' entity in the LDM | 
 |  |  | 
 | 2023.11.20 |  >feat: Created the Reference entity 'Software assets indicator' and added the attribute 'Software assets indicator' to it. Both have the following description: 'Software asset indicator indicates whether the reported asset is a software asset or not.'. Added the attribute 'Software assets indicator' to the balance sheet related entities: Other intangible asset not taken into possession; Other intangible asset taken into possession; Property, plant and equipment not taken into possession; Property, plant and equipment taken into possession. Created 4 one to many relationships between the entity 'Software assets indicator' and the entities mentioned above where the attribute 'Software assets indicator' was added. | 
 |  |  | 
 | 2023.11.20 |  >feat: added Held for sale indicator to Short security position | 
 |  |  | 
 | 2023.11.20 |  >feat: added Held for sale indicator to Debt security issued (by the reporting agent) | 
 |  |  | 
 | 2023.11.20 |  >feat: Created the Entity Financial asset instrument derived data and the entity Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment derived data. In both entities were created two mandatory attributes with the respective description: Accumulated write-offs - Total: According to FinRep Annex 5: 'the accumulated total amount as at the reference date of principal and accrued past due interest and fees of any debt instrument that has been de-recognised to date  because the institution has no reasonable expectations of recovering the contractual cash flows.'; and Accumulated write-offs - Partial: According to FinRep Annex 5: 'the accumulated partial amount as at the reference date of principal and accrued past due interest and fees of any debt instrument that has been de-recognised to date because the institution has no reasonable expectations of recovering the contractual cash flows.'. Added more two '1 to 1' relationships: Between 'Financial asset instrument derived data' and 'Financial asset instrument'; between 'Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment derived data' and 'Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment '. | 
 |  |  | 
 | 2023.11.17 |  >feat: moved new attribute 'Current loan-to-value ratio' with domain 'Real numbers with to decimals' from entity type 'Financial asset instrument derived data' to entity type 'Loan (excluding repurchase agreement) derive data'. | 
 |  |  | 
 | 2023.11.17 |  >feat: Made the attributes 'Allocated collateral value uncapped pre haircuts' and 'Allocated unused collateral value' of entityh type 'Loan (excluding repurchase agreement) Collateral assignment' optional. | 
 |  |  | 
 | 2023.11.16 |  >feat: added new relationship type 'Measurement method classifies Property, plant and equipment not taken into possession'. | 
 | | >feat: added new foreign key attribute 'Measurement method' to entity type 'Property, plant and equipment not taken into possession'. | 
 | | >feat: added new relationship type 'Measurement method classifies Property, plant and equipment taken into possession'. | 
 | | >feat: added new foreign key attribute 'Measurement method' to entity type 'Property, plant and equipment taken into possession'. | 
 | 2023.11.16 |  >feat: update the domain "Cost and revaluation model". Renamed it to "Cost and Fair value / Revaluation model". | 
 | | >feat: renamed the member "Cost model: IAS 17.49 IAS 16.30 73(a)(d)" to "Cost model". | 
 | | >feat: renamed the member "Revaluation model: IAS 17.49 IAS 16.31 73(a)(d)" to "Fair value/Revaluation model". | 
 |  |  | 
 | 2023.11.16 |  >chore: added change request 360 Add definition to attributes Measurement method to the measurement attributes. | 
 | 2023.11.16 |  >feat: Added new classification type of entity types to proper colour the associatives between contract and security called 'Security Contract'. | 
 | | >feat: Added new associative entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment' with classification type 'Security Contract'. | 
 | | >feat: Added new identifying relationship type 'Debt security issued (by the reporting agent) is secured via Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new foreign key attribute 'Debt Security identifier' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new foreign key attribute 'Debt Security Reference date' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new foreign key attribute 'Debt Security Reporting agent identifier' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new identifying relationship type 'Protection arrangement secures debt security issued via Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new foreign key attribute 'Protection arrangement identifier' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new foreign key attribute 'Protection arrangement Reference date' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new foreign key attribute 'Protection arrangement Reporting agent identifier' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 | | >feat: Added new attribute 'Protection allocated value' to entity type 'Debt security issued (by the reporting agent) Protection arrangement assignment'. | 
 |  |  | 
 | 2023.11.16 |  >feat: updated the name of entity type 'Institutional unit of foreign branches' to 'Institutional unit' and updated the definition to match the name change. | 
 | | >feat: updated the target of relationship type 'Institutional unit of foreign branches comprises Branch(es)' from 'Branch' to 'Financial corporation'. | 
 | | >feat: updated the name of relationship type 'Institutional unit of foreign branches comprises Branch(es)' to 'Institutional unit comprises Financial Corporation'. | 
 | | >feat: removed foreign key attribute 'Institutional unit of foreign branches Group identifier' from entity type 'Branch'. | 
 | | >feat: removed foreign key attribute 'Group Reference date' from entity type 'Branch'. | 
 | | >feat: removed foreign key attribute 'Group Reporting agent identifier' from entity type 'Branch'. | 
 | | >feat: added foreign key attribute 'Institutional unit Group identifier' to entity type 'Financial corporation'. | 
 | | >feat: added foreign key attribute 'Institutional unit Group Reference date' to entity type 'Financial corporation'. | 
 | | >feat: added foreign key attribute 'Institutional unit Group Reporting agent identifier' to entity type 'Financial corporation'. | 
 |  |  | 
 | 2023.11.14 |  >feat: The attribute end date of interest-only period has been moved to entity type Interest-only financial asset instrument. They are be removed from both Deposit and Other loan and Trade receivable. | 
 | 2023.11.14 |  >feat: updated the cardinality of relationship type 'Instrument acts in Instrument role(s)' to make it mandatory for every instrument to always act in at least one instrument role. | 
 |  |  | 
 | 2023.11.14 |  >feat: Made attribute 'International organisation code' of entity type 'International organisation' optional to be able to deal with International organisations that do not have an International organisation code. | 
 |  |  | 
 | 2023.11.13 |  >fix: removed the trailing space of the name of the attribute 'Allocated collateral value uncapped pre haircuts'. | 
 |  |  | 
 | 2023.11.13 |  >fix: Updated the names of the entity types Credis spread risk (CSR) non-securitisation risk factor, Genral interest rate risk (GIRR) factor, Equity risk factor, Securitisation correlation trading portfolio (CTP) Risk Factor, Securitisation non-correlation trading portfolio (non-CTP) Risk factor by appending the words "ffor standardised approach" to them ,to make their reach and scope clear. | 
 | | >fix: Gave the as yet unnamed relationship type between the entity type Model Context and the entity type Risk factor for standardised approach the name 'Model Context provides context for Risk factor for standardised approach'. | 
 |  |  | 
 | 2023.11.10 |  >fix: removed spurious entity type 'Negotiable security', 'Non-negotiable security', 'Litigation Statusv2'. And moved the relationship types from 'Litigation statusv2' to 'Litigation status'. | 
 |  |  | 
 | 2023.11.10 |  >feat: Updated the name of the new attribute 'Unused collateral value' to 'Allocated unused collateral value'. | 
 |  |  | 
 | 2023.11.10 |  >feat:  renamed entity type 'Loan (excluding Repurchase agreement) collateral assignment' to  'Loan (excluding repurchase agreement) collateral assignment', made the R of repurchase lower case. | 
 | | >feat: added attribute 'Allocated collateral value uncapped pre haicuts' to entity type 'Loan (excluding repurchase agreement) collateral assignment'. | 
 | | >feat: added attribute 'Allocated unused collateral value' to entity type 'Loan (excluding repurchase agreement) collateral assignment'. | 
 |  |  | 
 | 2023.11.10 |  >fix: updated the order of the attributes in entity type 'Fundamental review of the trading book standard approach risk measure' so the model context foreign key attributes are first. | 
 |  |  | 
 | 2023.11.09 |  >feat: Updated the name of entity type 'Non-International securities identification number (ISIN) security' to 'Non-International securities identification number (Non-ISIN) security' to make it more clear that it is a non-ISIN security.' | 
 | | >feat: Updated the name of the member 'Non-International securities identification number (ISIN) security' of domain 'Security type by identifier' to 'Non-International securities identification number (Non-ISIN) security'. | 
 |  |  | 
 | 2023.11.09 |  >feat: updated the currency of record attribute in curvature, Vega sensitivity, Delta sensitivity to be the foreign key of Currency, instead of "Currency of Record." | 
 | | >feat: removed the reference entity type "Currency of record". | 
 |  |  | 
 | 2023.11.09 |  Added prime, mid-prime and sub-prime as members to Type of assets provided as security | 
 |  |  | 
 | 2023.11.09 |  >fix: Hyphenated all instances of the words 'Fair-valued' where applicable. | 
 |  |  | 
 | 2023.11.09 |  >feat: Added the members 'To lend or to provide acceptance facilities at a below-market interest rate' and 'To lend or to provide acceptance facilities under pre-specified terms and conditions other than those at a below-market interest rate' to the domain 'type of credit facility'. | 
 |  |  | 
 | 2023.11.08 |  >feat: added Change in fair value for the period to Fair valued balance sheet recognised exchange tradable derivative asset position | 
 |  |  | 
 | 2023.11.08 |  >feat: added Change in fair value for the period to Fair valued balance sheet recognised exchange tradable derivative liability position | 
 |  |  | 
 | 2023.11.08 |  >feat: added Change in fair value for the period to Long security position | 
 |  |  | 
 | 2023.11.08 |  >feat: added Change in fair value for the period to Balance sheet recognised financial asset instrument | 
 |  |  | 
 | 2023.11.08 |  >feat: renamed attribute Accumulated changes in fair value in the period into Change in fair value for the period | 
 |  |  | 
 | 2023.11.08 |  >fix: made the derived data entity types optional for Financial asset instrument, Credit facility risk data, and Debt security. | 
 |  |  | 
 | 2023.11.08 |  >feat: added Transfer between impairment stages to Off-balance sheet item given instrument derived data | 
 |  |  | 
 | 2023.11.08 |  >feat: created entity Off-balance sheet item given instrument derived data | 
 |  |  | 
 | 2023.11.08 |  >feat: added Transfer between impairment stages to Balance sheet recognised financial asset instrument derived data | 
 |  |  | 
 | 2023.11.08 |  >feat: created entity Balance sheet recognised financial asset instrument derived data | 
 |  |  | 
 | 2023.11.08 |  >feat: added Transfer between impairment stages to Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment derived data | 
 |  |  | 
 | 2023.11.08 |  >feat: added Long debt security position Prudential portfolio assignment entity to a subview | 
 |  |  | 
 | 2023.11.08 |  >fix: re-created the structure from issue 181. Added the entity types that had disappeared, removed two entity types that were superfluous (perhaps that was the problem?) and recreated the supertype relationship types and their arcs. | 
 |  |  | 
 | 2023.11.07 |  >feat: added new attribute 'Current loan-to-value ratio' with domain 'Real numbers with to decimals' to entity type 'Financial asset instrument derived data'. | 
 |  |  | 
 | 2023.11.07 |  >feat: added new entity type 'Real estate collateral derived data'. | 
 | | >feat: added new attribute 'Current loan-to-value ratio' with domain "Real numbers with 2 decimals" to entity type 'Real estate collateral derived data'. | 
 |  |  | 
 | 2023.11.07 |  >fix: updated the logical data model view. added the missing entity ytpe "Long negotiable security position". | 
 |  |  | 
 | 2023.11.06 |  >feat: included the forborne long non-negotiabl security positions et al into the layout of the LDM. | 
 |  |  | 
 | 2023.11.04 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.11.03 |  >feat: created reference entity Transfer between impairment stages | 
 |  |  | 
 | 2023.11.03 |  >feat: added Initial impairment status to Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment | 
 |  |  | 
 | 2023.11.03 |  >feat: added Initial impairment status to Balance sheet recognised financial asset instrument | 
 |  |  | 
 | 2023.11.03 |  >feat: created reference entity for Initial impairment status | 
 |  |  | 
 | 2023.11.03 |  >feat: removed attribute 'Purchased credit-impaired indicator' from entity type 'Balance sheet recognised financial asset instrument according to national general accepted accounting principles (nGAAP)'. | 
 | | >feat: removed attribute 'Purchased credit-impaired indicator' from entity type 'Long debt security position Prudential portfolio assignment Accounting classification for financial assets assignment according to national general accepted accounting principles (nGAAP)'. | 
 | | >feat: removed domain 'Purchased credit-impaired'. | 
 | | >feat: removed reference entity type 'Purchased credit-impaired type'. | 
 | 2023.11.03 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.11.02 |  >feat: updated the definition of entity type 'Commercial real estate collateral' to indicate the creditworthiness of the debtor plays a role. | 
 | | >feat: updated the definition of entity type 'Offices and commercial premises collateral' to indicate the creditworthiness of the debtor plays a role. | 
 | | >feat: removed the new disciminator attribute 'Commercial real estate collateral indicator'. | 
 | | >feat: renamed the new domain 'Commercial real estate collateral indicator' to 'Offices and commercial premises collateral indicator'. | 
 | | >feat: renamed the members of the domain 'Offices and commercial premises collateral indicator' to 'Offices and commercial premises related to land collateral' and 'Offices and commercial premises not related to land collateral'. | 
 | | >feat: renamed entity type 'Commercial real estate collateral related to land' to 'Offices and commercial premises related to land collateral'. | 
 | | >feat: renamed entity type 'Commercial real estate collateral not related to land' to 'Offices and commercial premises not related to land collateral'. | 
 | | >feat: updated the supertype of 'Offices and commercial premises related to land collateral' from 'Commercial real estate collateral' to 'Offices and commercial premies collateral' and updated the definition to match the new supertype and name. | 
 | | >feat: updated the supertype of 'Offices and commercial premises not related to land collateral' from 'Commercial real estate collateral' to 'Offices and commercial premies collateral' and updated the definition to match the new supertype and name. | 
 |  |  | 
 | 2023.11.02 |  >chore: finalisation of the merge / rebase of develop into 344. | 
 |  |  | 
 | 2023.11.02 |  Merge branch '344-instruments-with-forbearance-measures-granted-during-the-period' of https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model into 344-instruments-with-forbearance-measures-granted-during-the-period | 
 |  |  | 
 | 2023.11.02 |  Revert ">chore: removed an empty note from the subview 344" | 
 |  |  | 
 | | This reverts commit c25a1b7e4671a6a3ae2d955a9922ea113f535511. | 
 |  |  | 
 | 2023.11.02 |  >feat: added new domain 'Date / period of application of forbearance measure type' with values "Any date" and "Current reference period / date". | 
 | | >feat: added new reference entity type 'Date / period of application of forbearance measure type'. | 
 | | >feat: added new attribute 'Date / period of application of forbearance measure type' as primary key to entity type 'Date / period of application of forbearance measure type'. | 
 | | >feat: added new derived entity type 'Renegotiated financial asset instrument with forbearance measure derived data'. | 
 | | >feat: added new relationship type 'Date / period of application of forbearance measure type classifies Renegotiated financial asset instrument with forbearance measure derived data'. | 
 | | >feat: added new relationship type 'Date / period of application of forbearance measure classifies Long security position derived data'. | 
 |  |  | 
 | 2023.10.10 |  >fix: reapplied previous commited changes. | 
 |  |  | 
 | 2023.11.02 |  >fix: added definition to entity type 'Fair value hierarchy' | 
 | 2023.11.02 |  Merge branch '176-instttnl_sctr-and-instttnl_sctr_eba_its-analysis-and-results' into 'develop' | 
 |  |  | 
 | | >fix: INSTTTNL_SCTR and INSTTTNL_SCTR_EBA_ITS | 
 |  |  | 
 | | See merge request sdd-bird-team/bird-logical-data-model!21 | 
 | 2023.11.02 |  >fix: deleted entity Long debt security deried data and created Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment derived data | 
 |  |  | 
 | 2023.11.02 |  >feat: updated subviews | 
 |  |  | 
 | 2023.11.02 |  >fix: changed name of entity Fair valued exchange tradable derivative liability position to Fair valued balance sheet recognised exchange tradable derivative liability position | 
 |  |  | 
 | 2023.11.02 |  >fix: moved Fair value and Fair value change from Balance sheet recognised exchange tradable derivative liability position to Fair valued exchange tradable derivative liability position | 
 |  |  | 
 | 2023.11.02 |  >feat: added Fair value, Fair value change and Fair value hierarchy to Fair valued balance sheet recognised exchange tradable derivative asset position | 
 |  |  | 
 | 2023.11.02 |  >feat: created subtypes Fair valued balance sheet recognised exchange tradable derivative asset position and Non-fair valued balance sheet recognised exchange tradable derivative asset position to entity Balance sheet recognised exchange tradable derivative asset position | 
 |  |  | 
 | 2023.11.02 |  >fix: moved Fair value and Fair value hierarchy from Long debt security position to Long security position | 
 |  |  | 
 | 2023.11.01 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.31 |  >doc: added entity Long security position Prudential Portfolio assignment Accounting classification for financial assets assignment to the subview | 
 |  |  | 
 | 2023.10.31 |  >feat: added Accumulated coverage ration to entities Loan (excluding repurchase agreement) and advance derived data and Long debt security position derived data | 
 |  |  | 
 | 2023.10.31 |  >feat: created entity Long debt security derived data | 
 |  |  | 
 | 2023.10.31 |  >feat: created entity Loan (excluding repurchase agreement) and advance derived data | 
 |  |  | 
 | 2023.10.31 |  >feat: added more entities to the subview | 
 |  |  | 
 | 2023.10.31 |  >feat: added Fair value to Long debt security position | 
 |  |  | 
 | 2023.10.31 |  >fix: moved Fair value hierarchy from Balance sheet recognised financial asset instrument according to International Financial Reporting Standard (IFRS) to Fair valued balance sheet recognised financial asset instrument | 
 |  |  | 
 | 2023.10.31 |  >feat: added Fair valued balance sheet recognised financial asset instrument and Non-Fair valued balance sheet recognised financial asset instrument subtypes under Balance sheet recognised financial asset instrument as disjoint subtypes | 
 |  |  | 
 | 2023.10.31 |  >feat: added Fair value hierarchy to Long Debt security position | 
 |  |  | 
 | 2023.10.31 |  >feat: added Fair value hierarchy to Balance sheet recognised financial asset instrument according to International Financial Reporting Standard (IFRS) | 
 |  |  | 
 | 2023.10.31 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.30 |  >chore: updated the lay-out of the LDM for some instrument roles. | 
 |  |  | 
 | 2023.10.30 |  >chore: Repositioning of two entities | 
 |  |  | 
 | 2023.10.30 |  Merge branch '183-finrep-requirements-for-collateral-commercial-real-estate-corporation' into develop | 
 |  |  | 
 | 2023.10.30 |  >fix: updated the definition of Commercial real estate and offices and commercial premises collateral | 
 |  |  | 
 | 2023.10.30 |  >feat: Updated the name of the entity type 'Tranche in a synthetic securitisation without SSPE' to 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE). Matched the new name in the definition. | 
 | | >feat: Updated the name of attribute 'Tranche in a synthetic securitisation without SSPE type' of entity type 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE)' to 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) type'. Matched the new name in the definition. | 
 | | >feat: Updated the name of entity type 'Tranche in a synthetic securitisation without SSPE being a financial guarantee' to 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a financial guarantee'. Matched the new name in the definition. | 
 | | >feat: Updated the name of entity type 'Tranche in a synthetic securitisation without SSPE being a deposit' to 'Tranche in a synthetic securitisation without securitisation special purpose entity (SSPE) being a deposit'. Matched the new name in the definition. | 
 |  |  | 
 | 2023.10.30 |  >chore: update to the lay-out of the LDM. | 
 |  |  | 
 | 2023.10.30 |  >doc: Updated the subview 'Introduction to the LDM - Collateral hierarchy' to include the new collateral subtypes. | 
 |  |  | 
 | 2023.10.27 |  >fix: added the arc for Debt security by perfoming status type | 
 |  |  | 
 | 2023.10.27 |  >fix: moved Multiple forbearance measures in place indicator from Non-performing debt secuerity to Debt security | 
 |  |  | 
 | 2023.10.27 |  >fix: removed additional domain file and move the new domains to birdDomains | 
 |  |  | 
 | 2023.10.27 |  >fix: changed domain Real to Real numbers with 2 decimals | 
 |  |  | 
 | 2023.10.27 |  >doc: fixed typos in descriptions of the sensitivities | 
 |  |  | 
 | 2023.10.27 |  >fix: Currency of record is a foreign key to reference entity | 
 |  |  | 
 | 2023.10.27 |  >doc: added description to Delta, Vega sensitivity and Curvature | 
 |  |  | 
 | 2023.10.27 |  >feat: added arc Tranche in a synthetic securitisation type | 
 |  |  | 
 | 2023.10.27 |  >feat: created entity Tranche in a synthetic securitisation with SSPE | 
 |  |  | 
 | 2023.10.27 |  >feat: added Tranche in a synthetic securitisation type to Tranche in a synthetic securitisation | 
 |  |  | 
 | 2023.10.27 |  >feat: moved Currency of record to be a reference entity | 
 |  |  | 
 | 2023.10.27 |  >fix: moved Rating grade credit quality from Central bank and private sector company to Rating grade | 
 |  |  | 
 | 2023.10.27 |  >fix: removed pk from Fundamental review of the trading book standard approach risk measure | 
 |  |  | 
 | 2023.10.27 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.26 |  Merge branch '127-need-for-clarity-introduction-to-the-bird-ldm-v1-0-1-perpetuals-as-debt-securities' into 'develop' | 
 |  |  | 
 | | Resolve "Need for clarity - "Introduction to the BIRD LDM - v1.0.1" - perpetuals as debt securities" | 
 |  |  | 
 | | See merge request sdd-bird-team/bird-logical-data-model!24 | 
 | 2023.10.26 |  >chore: finish merg | 
 |  |  | 
 | 2023.10.26 |  >chore: added the change request to all of the added or changed elements. | 
 |  |  | 
 | 2023.10.26 |  >feat: made discriminator attribute 'Perpetual debt security indicator' of entity type 'Debt security' mandatory. | 
 |  |  | 
 | 2023.10.13 |  >fix: updated the layout of the subview for issue 127. | 
 |  |  | 
 | 2023.10.13 |  >feat: Added new subtype 'Perpetual debt security' to entity type 'Debt security'. | 
 | | >feat: Added new subtype 'Non-perpetual debt security' to entity type 'Debt security'. | 
 | | >feat: Moved attribute 'Legal final maturity date' from entity type 'Debt security' to entity type 'Non-perpetual debt security' because perpetual debt securities cannot have a maturity date. | 
 | | >feat: added domain 'Perpetual debt security indicator' with values 'Perpetual debt security' and 'Non-perpetual debt security'. | 
 | | >feat: added attribute 'Perpetual debt security indicator' to entity type 'Debt security' as discriminator for the two new subtypes. | 
 | | >feat: added new arc to 'Perpetual debt security indicator' to indicate that the subtypes 'Perpetual debt security' and 'Non-perpetual debt security' are disjoint subytpes. | 
 |  |  | 
 | 2023.10.26 |  >chore: added the change request to all of the added or changed elements. | 
 |  |  | 
 | 2023.10.26 |  >feat: made discriminator attribute 'Perpetual debt security indicator' of entity type 'Debt security' mandatory. | 
 |  |  | 
 | 2023.10.26 |  >feat: moved Performing forborne exposure under probation reclassified from non-performing indicator from Debt security to Performing debt security | 
 |  |  | 
 | 2023.10.26 |  >chore: updated the lay-out of the LDM and placed immaterial rights as collateral correctly. | 
 |  |  | 
 | 2023.10.26 |  Merge branch '105-collateral-amend-description-of-physical-collateral-entity' into 'develop' | 
 |  |  | 
 | | Resolve "Collateral - Amend description (of Physical Collateral entity)" | 
 |  |  | 
 | | See merge request sdd-bird-team/bird-logical-data-model!25 | 
 | 2023.10.26 |  Merge branch '276-performing-forborne-exposure-under-probation-reclassified-from-non-performing-indicator' of https://gitlab.sofa.dev/sdd-bird-team/bird-logical-data-model into 276-performing-forborne-exposure-under-probation-reclassified-from-non-performing-indicator | 
 |  |  | 
 | 2023.10.20 |  >fix: removed members Not forborne or renegotiated and Renegotiated instrument without forbearance measures from domain Forbearance status. | 
 |  |  | 
 | 2023.10.20 |  >fix: fixed domain of (Credit facility risk data) Renegotiation status to Renegotiated instrument without forbearance measures and Renegotiated instrument with forbearance measures | 
 |  |  | 
 | 2023.10.20 |  >doc: added a note with remaining questions on the topic | 
 |  |  | 
 | 2023.10.20 |  >feat: added Performing forborne exposure under probation reclassified from non-performing indicator to Debt security | 
 | | rebased branch to add subtyping of Debt security | 
 |  |  | 
 | 2023.10.20 |  >fix: removed attribute Performing forborne exposure under probation reclassified from non-performing indicator from entity Non-retail exposure financial asset instrument | 
 |  |  | 
 | 2023.10.20 |  >fix: changed the domain of attribute Performing forborne exposure under probation reclassified from non-performing indicator | 
 |  |  | 
 | 2023.10.20 |  >fix: removed attribute Performing forborne exposure under probation reclassified from non-performing indicator from Other commitment | 
 |  |  | 
 | 2023.10.26 |  >chore: added subview to model issue 406 | 
 |  |  | 
 | 2023.10.26 |  >feat: Added the member 'Investments in subsidiaries, joint ventures and associates' to the domain 'Accounting classification for assets'. | 
 |  |  | 
 | 2023.10.26 |  >chore: update to the lay-out of the LDM. | 
 |  |  | 
 | 2023.10.26 |  Merge branch '133-Attribute-Accounting-standard-is-missing-from-party-data' into develop | 
 |  |  | 
 | 2023.10.26 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.25 |  >doc: added subview for issue 182 and multilateral development bank indicator | 
 |  |  | 
 | 2023.10.25 |  >feat: added Multiple forbearance measures in place indicator and Non-performing exit criteria met indicator to Non-performing debt security | 
 |  |  | 
 | 2023.10.25 |  >feat: added Non-performing exit criteria met indicator attribute to Non-performing and default financial asset instruments | 
 |  |  | 
 | 2023.10.25 |  >fix: moved attributes Forbearance measure count and Multiple forbearance measure in place indicator from Serviced asset instrument to Renegotiated financial asset instrument with forbearance measure | 
 |  |  | 
 | 2023.10.25 |  >feat: added Forbearance measure count to Serviced asset instrument | 
 |  |  | 
 | 2023.10.25 |  >feat: added disjoint subtyping to Debt security (Non-performing and Performing) | 
 |  |  | 
 | 2023.10.25 |  >doc: added notes to the frtb subview | 
 |  |  | 
 | 2023.10.25 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.24 |  >chore: removed an empty note from the subview 344 | 
 |  |  | 
 | 2023.10.24 |  >feat: added new domain 'Forbearance measure granted during reference period'. | 
 | | >feat: added new domain 'Negotiable security position indicator'. | 
 | | >feat: added new domain 'Forborne non-negotiable security indicator' | 
 | | >feat: added new entity type 'Negotiable security position indicator'. | 
 | | >feat: added new attribute 'Negotiable security position indicator' with domain 'Negotiable security position indicator' as primary key to entity type 'Negotiable security position indicator'. | 
 | | >feat: added new relationship type 'Negotiable security position indicator classifies Long security position' | 
 | | >feat: added new foreign key attribute 'Negotiable security position indicator' to entity type 'Long security position' as discriminator. | 
 | | >feat: added new subtype 'Long negotiable security position' to entity type 'Long security position'. | 
 | | >feat: added new subtype 'Long non-negotiable security position' to entity type 'Long security position'. | 
 | | >feat: added new arc 'Negotiable security position indicator' to denote disjoint subtyping of the 'Long security position'. | 
 | | >feat: added new relationship type 'Forbearance measure type classifies Forborne non-negotiable security' to capture the forbearance measures at the long security position. | 
 | | >feat: added new entity type 'Forborne long non-negotiable security position indicator'. | 
 | | >feat: added new attribute 'Forborne non-negotiable security indicator' with domain 'Forborne non-negotiable security indicator' as primary key to entity type 'Forborne non-negotiable security indicator'. | 
 | | >feat: added new relationship type 'Forborne long non-negotiable security position indicator classifies Non-negotiable security'. | 
 | | >feat: added new foreign key attribute 'Forborne non-negotiable security indicator' to entity type 'Long non-negotiable security position' as discriminator. | 
 | | >feat: added new subtype 'Forborne long non-negotiable security position' to entity type 'Long non-negotiable security position'. | 
 | | >feat: added new subtype 'Non-forborne long non-negotiable security position' to entity type 'Long non-negotiable security position'. | 
 | | >feat: added new arc 'Forborne long non-negotiable security position indicator' to denote disjoint subtyping of the 'Long non-negotiable security position'. | 
 | | >feat: added new attribute 'Date of forbearance status' with domain 'All possible dates' to entity type 'Forborne long non-negotiable security position'. | 
 | | >feat: added new entity type 'Forbearance measure granted during reference period indicator' | 
 | | >feat: added new attribute 'Forbearance measure granted during reference period indicator' with domain 'Forbearance measure granted during reference period' to entity type 'Forbearance measure granted during reference period indicator'. | 
 | | >feat: added new derived entity type 'Long security position derived data'. | 
 | | >feat: added new relationship type 'Forbearance measure granted during reference period indicator classifies Long security position derived data'. | 
 | | >feat: added new derived attribute 'Forbearance measure granted during reference period indicator' to entity type 'Long security position derived data'. | 
 | 2023.10.24 |  >chore: updated the lay-out of the ldm. | 
 |  |  | 
 | 2023.10.24 |  >doc: added a note | 
 |  |  | 
 | 2023.10.24 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.23 |  >feat: added domain for Rating grade credit quality and set the attribute to mandatory | 
 |  |  | 
 | 2023.10.23 |  >feat: set Risk measure type attribute to mandatory | 
 |  |  | 
 | 2023.10.23 |  >feat: added names to relationships with Fundamental review of the trading book standard approach risk measure subtypes | 
 |  |  | 
 | 2023.10.21 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.20 |  >fix: removed members Not forborne or renegotiated and Renegotiated instrument without forbearance measures from domain Forbearance status. | 
 |  |  | 
 | 2023.10.20 |  >fix: fixed domain of (Credit facility risk data) Renegotiation status to Renegotiated instrument without forbearance measures and Renegotiated instrument with forbearance measures | 
 |  |  | 
 | 2023.10.20 |  >doc: added a note with remaining questions on the topic | 
 |  |  | 
 | 2023.10.20 |  >feat: added Performing forborne exposure under probation reclassified from non-performing indicator to Debt security | 
 |  |  | 
 | 2023.10.20 |  >fix: removed attribute Performing forborne exposure under probation reclassified from non-performing indicator from entity Non-retail exposure financial asset instrument | 
 |  |  | 
 | 2023.10.20 |  >fix: changed the domain of attribute Performing forborne exposure under probation reclassified from non-performing indicator | 
 |  |  | 
 | 2023.10.20 |  >fix: removed attribute Performing forborne exposure under probation reclassified from non-performing indicator from Other commitment | 
 |  |  | 
 | 2023.10.20 |  >feat: created reference entities for Multiple forbearance measures in place indicator and failed to meet the non-performing exit criteria indicator | 
 |  |  | 
 | 2023.10.20 |  >feat: added Multiple forbearance measures in place indicator to Debt security and Loan and advance | 
 |  |  | 
 | 2023.10.20 |  >feat: added attribute number of times an exposure has been under forbearance measures to Loan and advance and Debt security | 
 |  |  | 
 | 2023.10.20 |  >doc: added change request objects to the LDM from open issues from gitlab (pipeline) | 
 |  |  | 
 | 2023.10.19 |  >chore: removed subview for issue 250 | 
 | 2023.10.19 |  >chore: updated the lay-out of the logical data model. placed the reference data entity type 'performing status'. | 
 | 2023.10.19 |  Merge branch '250-asset-sec-finrep-new-derived-attribute-for-loan-performing-status-indicator' into 'develop' | 
 |  |  | 
 | | Resolve "[Asset Sec][FINREP] New derived attribute for loan: Performing status indicator" | 
 |  |  | 
 | | See merge request sdd-bird-team/bird-logical-data-model!27 | 
 | 2023.10.19 |  >feat: Created new reference data entity type 'Performing status' | 
 | | >feat: Replaced the attribute 'performing status' of the entity types 'Party risk data', 'Credit facility risk data' and 'Debt security' with a foreign key to the new entity type 'Performing status'. | 
 | | >feat: added new attribute 'Performing status' to entity type 'Financial asset instrument derived data' as a foreign key to 'Performing status'. This is a derived attribute from the subtyping structure of 'Financial asset instrument'. | 
 | | >feat: added new relationship type 'Performing status classifies Party risk data' from entity type 'Performing status' to entity type 'Party risk data'. | 
 | | >feat: added new relationship type 'Performing status classifies Credit facility risk data' from entity type 'Performing status' to entity type 'Credit facility risk data'. | 
 | | >feat: added new relationship type 'Performing status classifies Debt security' from entity type 'Performing status' to entity type 'Debt security'. | 
 | | >feat: added new relationship type 'Performing status classifies Financial asset instrument derived data' from entity type 'Performing status' to entity type 'Financial asset instrument derived data'. | 
 |  |  | 
 |  |  | 
 | 2023.10.19 |  >feat: added new attribute 'Commercial real estate collateral land indicator' to entity type 'Commercial real estate collateral' with domain 'Commercial real estate collateral land indicator' as discriminator for the new subtypes 'Commercial real estate collateral related to land' and 'Commercial real estate collateral not related to land'. | 
 | | >feat: added new arc 'Commercial real estate collateral indicator' to denote disjoint subtyping for the subtype 'Commercial real estate collateral related to land' and 'Commercial real estate collateral not related to land'. | 
 | | >feat: added new subtype 'Commercial real estate collateral related to land' to entity type 'Commmercial real estate collateral'. | 
 | | >feat: added new subtype 'Commercial real estaet collateral not related to land' to entity type 'Commercial real estate collateral'. | 
 | | >feat: added new attribute 'Agriculture land indicator' to entity type 'Commercial real estate collateral related to land' with domain 'Agriculture land indicator' as discriminator for the new subtypes 'Land excluding agriculture' and 'Land including agriculture'. | 
 | | >feat: added new arc 'Agriculture land indicator' to denote disjoint subtyping for the subtype 'Land excluding agriculture' and 'Land including agriculture'. | 
 | | >feat: added new subtype 'Land excluding agriculture' to entity type 'Commercial real estate collateral related to land'. | 
 | | >feat: added new subtype 'Land excluding agriculture' to entity type 'Commercial real estate collateral related to land'. | 
 | | >feat: added new attribute 'Planning permission for development indicator' to entity type 'Land excluding agriculture' with domain 'Planning permission for development indicator' to satisfy the Finrep requirements for collaterals on planning permission. | 
 |  |  | 
 | 2023.10.18 |  >fix: added new domains commercial real estate land indicator, agriculture land indicator, and planning permissions for development indicator to satisfy finrep requirements for commercial real estate collateral before subtype amendment. | 
 |  |  | 
 | 2023.10.18 |  >feat: Ammended the name of some attributes of the following entities: 'Credit facility risk data derived data', 'Debt security derived data' and 'Financial asset instrument derived data'. | 
 |  |  | 
 | 2023.10.18 |  >feat: Added the entity 'Loan (excluding repurchase agreement) derived data' and added a one to one relationship between the entitiy 'Loan (excluding repurchase agreement)' and 'Loan (excluding repurchase agreement) derived data'. Added the entity 'Commercial real estate loan indicator' and added a mandatory attribute to it: 'Commercial real estate loan indicator'. Added more three '1 to *' relationships: Between 'Commercial real estate loan indicator' and 'Loan (excluding repurchase agreement) derived data'. Added the domain 'Commercial real estate indicator' with two values: 'Commercial real estate' and 'Not Commercial real estate'. | 
 |  |  | 
 | 2023.10.18 |  >fix: updated the name of domain 'AnaCredit collection Impairment status' to 'Impairment status' because it is not only used in AnaCredit, but also for FINREP. | 
 |  |  | 
 | 2023.10.17 |  >fix: added reference entity type Multilateral development bank indicator with a 1:N relationship type to International organisation and the attribute Multilateral development bank indicator of entity type International organisation is the foreign key. | 
 |  |  | 
 | 2023.10.17 |  >fix: updated the abbreviation of the member value POCI to Purchased or originated credit-impaired instruments (POCI) for domain Impairment status. | 
 |  |  | 
 | 2023.10.16 |   >feat: Deleted the subview 361-Immediate parent undertaking in Organisation derived data is obsolete | 
 |  |  | 
 | 2023.10.13 |  >feat: Updated the definition of entity type 'Physical collateral' to indicate that this deals with material collateral. | 
 | | >feat: Added new entity type 'Immaterial rights as collateral' as subtype to entity type 'Collateral' that deals with things like intellectual property rights. | 
 | | >feat: Updated the domain 'Collateral type' to include the member 'Immaterial rights as collateral'. | 
 |  |  | 
 | 2023.10.13 |  >feat: Added new subtype 'Perpetual debt security' to entity type 'Debt security'. | 
 | | >feat: Added new subtype 'Non-perpetual debt security' to entity type 'Debt security'. | 
 | | >feat: Moved attribute 'Legal final maturity date' from entity type 'Debt security' to entity type 'Non-perpetual debt security' because perpetual debt securities cannot have a maturity date. | 
 | | >feat: added domain 'Perpetual debt security indicator' with values 'Perpetual debt security' and 'Non-perpetual debt security'. | 
 | | >feat: added attribute 'Perpetual debt security indicator' to entity type 'Debt security' as discriminator for the two new subtypes. | 
 | | >feat: added new arc to 'Perpetual debt security indicator' to indicate that the subtypes 'Perpetual debt security' and 'Non-perpetual debt security' are disjoint subytpes. | 
 |  |  | 
 | 2023.10.11 |  >feat: updated the members to the domain 'Forbearance measure type'. Removed the aggregated members that are made up of the individual forbearance measures. | 
 |  |  | 
 | 2023.10.10 |  >Feat: Updated the definition of entity type 'Other collateral received instrument' to align with the discussion in issue #138. | 
 |  |  | 
 | 2023.10.10 |  >feat: Added extra members to the domain 'Forbearance measure type' as described in issue #342 | 
 |  |  | 
 | 2023.10.10 |  >feat: added attribute 'Risk measure type' to entity type 'Fundamental review of the trading book standard approach risk measure' as discriminator. | 
 | | >feat: named the disjoint subtyping arc 'Risk measure type by position' for subtypes of Risk measure type by position 'Fundamental review of the trading book standard approach risk measure'. | 
 |  |  | 
 | 2023.10.10 |  >feat: Added the arc Negotiable security indicator | 
 |  |  | 
 | 2023.10.10 |  >feat: Moved the attribute 'Negotiable security indicator' from entity type 'International securities identification number (ISIN) security' to its supertype 'Security'. | 
 | | >feat: added the correct definition to attribute 'Negotiable security indicator' of entity type 'Security'. | 
 | | >feat: added subtype 'Negotiable security' to entity type 'Security'. | 
 | | >feat: added subtype 'Non-negotiable security' to entity type 'Security'. | 
 | | >feat: added disjoint subtyping arc to the 'Negotiable security' and 'Non-negotiable security' called 'Negotiable security indicator'. | 
 | | >feat: added reference data entity type 'Forborne non-negotiable security indicator' | 
 | | >feat: added domain 'Forborne non-negotiable security indicator' with values 'Forborne non-negotiable security' and 'Non-forborne non-negotiable security'. | 
 | | >feat: added primary key attribute 'Forborne non-negotiable security indicator' based on domain 'Forborne non-negotiable security indicator' to entity type 'Forborne non-negotiable security indicator'. | 
 | | >feat: added new relationship type 'Forborne non-negotiable security indicator classifies Non-negotiable security'. | 
 | | >feat: added new discriminator attribute 'Forborne non-negotiable security indicator' to entity type 'Non-negotiable security' as foreign key to reference entity type 'Forborne non-negotiable security indicator'. | 
 | | >feat: added new entity type 'Forborne non-negotiable security' as subtype to entity type 'Non-negotiable security'. | 
 | | >feat: added new entity type 'Non-forborne non-negotiable security' as subtype to entity type 'Non-negotiable security'. | 
 | | >feat: added disjoing subtyping arc to the 'Forborne non-negotiable security' and 'Non-forborne non-negotiable security' subtypes of 'Non-negotiable security' called 'Forborne non-negotiable security indicator'. | 
 | | >feat: added new attribute 'Date of forbearence measure' to entity type 'Forborne non-negotiable security' | 
 | | >feat: added new relationship type 'Forbearance measure type classifies Forborne non-negotiable security' | 
 | | >feat: added new foreign key attribute 'Forbearance measure' to entity type 'Forborne non-negotiable security'. | 
 |  |  | 
 | 2023.10.10 |  >feat: updated the business key by including the relationship type from model context as part of the primary key to the Risk factor for standardised approach. This primary key is then inherited to the Fundamental review of the trading bookd standard approach risk measure. | 
 | 2023.10.10 |  >chore: preparing the release notes for the next release. | 
 |  |  | 
 | 2023.10.09 |  >feat: added arc to the new subtyping for FRTB Risk measure. | 
 |  |  | 
 | 2023.10.05 |  >fix: Updated the placement of the reference entity type sources of encumbrance in the logical data model. | 
 |  |  | 
 | 2023.10.04 |  >fix: updated the lay-out of some of the non-financial assets subtypes. | 
 | 2023.10.04 |  >feat: real estate collateral now has the attribute 'Under construction or development indicator', so where the original change started. | 
 |  |  | 
 | 2023.10.04 |  >fix: revert to the solution where the real estate collateral has the indicator under construction or development. | 
 |  |  | 
 | 2023.10.04 |  Revert ">fix: named the unnamed subview to the name of the issue 180 under construction indicator." | 
 | | because the modelled solution that all registered collateral can have | 
 | | the under construction indicator was rejected. | 
 |  |  | 
 | 2023.10.04 |  >fix: added change request to the attribute 'Multilateral development bank indicator' of entity type 'International organisation'. | 
 |  |  | 
 | 2023.10.04 |  >fix: added missing member S.14 to domain institutional sector. | 
 | | >feat: added definition to attribute 'Non-performing prior to forbearance... | 
 |  |  | 
 | 2023.10.04 |  >feat: renamed the entity type 'Risk measure' to 'Fundamental review of the trading book standard approach risk measure. | 
 |  |  | 
 | 2023.10.04 |  >feat: added member S125_W Other financial corporations excluding financial vehicle corporations to the domain Institutional sector. | 
 | | >feat: added new domain 'Multilateral development bank indicator' | 
 | | >feat: added new attribute 'Multilateral development bank indicator' to entity type 'International organisation' with domain 'Multilateral development bank indicator'. | 
 | | >feat: updated the definition of attribute 'Multilateral development bank indicator' of entity type 'International organisation'.  | 
 | | >feat: updated the constraint of attribute 'Institutional sector according to EBA ITS' of entity type 'Party derived data' to have the description of member S.14 made empty and to have the description "Other financial corporations excluding financial vehicle corporations" changed to "Other financial corporations". | 
 |  |  | 
 | 2023.09.29 |  >fix: INSTTTNL_SCTR and INSTTTNL_SCTR_EBA_ITS | 
 |  |  | 
 | 2023.09.28 |  >fix: Added the change request for the litigation status to the relationship type between litigation status and loan | 
 |  |  | 
 | 2023.09.28 |  >fix: updated the definition of litigation status to make it appear where applicable. | 
 |  |  | 
 | 2023.09.28 |  >feat: renamed attribute 'Real estate collateral type' of entity type 'Real estate collateral' to 'Real estate collateral location type' to indicate that it discriminates into the location of the real estate. | 
 | | >feat: updated the definition of attribute 'Real estate collateral location type' of entity type 'Real estate collateral'. | 
 | | >feat: renamed domain 'Real estate collateral type' to 'Real estate collateral location type' to match the change in attribute name. | 
 | | >feat: renamed arc 'Real estate collateral type' to 'Real estate collateral location type' to match the change in name of the discriminator attribute 'Real estate collateral location type'. | 
 | | >feat: added new subtype 'Residential real estate collateral' to entity type 'Real estate collateral'. | 
 | | >feat: added new subtype 'Commercial real estate and offices and commercial premises collateral' to entity type 'Real estate collateral'. | 
 | | >feat: added new domain 'Real estate collateral type' with values 'Residential real estate collateral' and 'Commercial real estate and offices and commercial premises collateral'. | 
 | | >feat: added new attribute 'Real estate collateral type' of entity type 'Real esate collateral' with domain 'Real estate collateral type' as discriminator for the new subtypes 'Residential real estate collateral' and 'Commercial real estate collateral'. | 
 | | >feat: added new arc 'Real estate collateral type' to denote disjoint subtyping for the subtype 'Residential real estate collateral' and 'Commercial real estate collateral'  | 
 | | >feat: added new subtype 'Commercial real estate collateral' to entity type 'Commercial real estate and offices and commercial premises collateral'. | 
 | | >feat: added new subtype 'Offices and commercial premisis collateral' to entity type 'Commercial real estate and offices and commercial premises collateral'. | 
 | | >feat: added new arc 'Commercial real estate and offices and commercial premises collateral type' to denote the mutually exclusivity of the subtyping. | 
 | | >feat: added new domain 'Commercial real estate and offices and commercial premises collateral type' with values 'Commercial real estate collateral' and 'Offices and commercial permises collateral'. | 
 |  |  | 
 | 2023.09.28 |  >feat: Updated relationship type 'Under construction or development indicator classifies Real estate collateral' to point to 'Registered collateral' instead of Real estate collateral' because it is applicable to all registered collateral. | 
 | | >feat: Moved foreign key attribute 'Under construnction or development indicator' from entity type 'Real estate collateral' to 'Registered collateral'. | 
 |  |  | 
 | 2023.09.28 |  >feat: added definition to attribute 'Non-performing prior to forbearance indicator' of entity type 'Non-performing prior to forbearance type'. | 
 | | >feat: added definition to attribute 'Non-performing prior to forbearance indicator' of entity type 'Credit facility risk data'. | 
 | | >feat: added definition to attribute 'Non-performing prior to forbearance indicator' of entity type 'Non-performing prior to forbearance type' | 
 | | >feat: moved the relationship type 'Non-performing prior to forbearance indicator is applied to Debt security' from 'Debt security' to 'Debt security issued (by the reporting agent)'. This also moved the foreign key attribute 'Non-performing prior to forbearance indicator' from 'Debt security' to 'Debt security issued (by the reporting agent)'. | 
 | | >feat: renamed relationship type 'Non-performing prior to forbearance indicator is applied to Debt security' to 'Non-performing prior to forbearance indicator classifies Debt security issued (by the reporting agent)' | 
 | | >feat: renamed new relationship type 'Non-performing prior to forbearance indicator is applied to Credit facility risk data' to 'Non-performing prior to forbearance indicator classifies Credit facility risk data' | 
 | | >feat: added relationship type 'Non-performing prior to forbearance indicator classifies Long security position Prudential portfolio assignment' which resulted in adding foreign key 'Non-performing prior to forbearance indicator' to entity type 'Long security position Prudential portfolio assignment'. | 
 |  |  | 
 | 2023.09.27 |  >fix: added the definition to attribute 'Revocable indicator' of entity type 'Revocable type' from the SDD. | 
 | | >fix: added the definition to attribute 'Revocable indicator' of entity type 'Other commitment' from the SDD. | 
 |  |  | 
 | 2023.09.22 |  >feat: Added reference entity type 'Under construction or developement indicator' | 
 | | >feat: Added relationship type 'Under construction or developement indicator classifies Real estate collateral' to make attribute 'Under construction or developement indicator' of entity type 'Real estate collateral' a foreign key. | 
 |  |  | 
 | 2023.09.22 |  >feat: Added reference entity type 'Under construction or developement indicator' | 
 | | >feat: Added relationship type 'Under construction or developement indicator classifies Real estate collateral' to make attribute 'Under construction or developement indicator' of entity type 'Real estate collateral' a foreign key.  | 
 |  |  | 
 | 2023.09.21 |  >feat: Updated the definition of the new attribute 'Under construction or development indicator' to include the name of the attribute at the start of the definition. | 
 |  |  | 
 | 2023.09.20 |  >fix: Updated the layout of the entity types around 'Balance sheet recognised financial asset instrument according to International Financial Reporting Standard (IFRS)'. | 
 |  |  | 
 | 2023.09.14 |  >feat: Deleted the Entities: Immediate parent undertaking and Organization derived data, their respective attributes. Deleted the attributes:  Immediate parent undertaking from the entity Immediate parent undertaking; Organization Party identifier, Organization Party Reference date, Organization Party Reporting agent identifier, immediate parent undertaking from the entity Organization derived data. Deleted the relationships between the entities Immediate parent undertaking and Organization derived data and the relationship between the entities Organization and Organization derived data. Deleted the domain: immediate parent undertaking and the respective members Immediate parent undertaking and Not immediate parent undertaking. | 
 |  |  | 
 | 2023.09.14 |  >Fix: Updated the definition of the attribute 'purpose type' of entity type 'Serviced asset instrument' to make it more clear. | 
 | 2023.09.14 |  >feat: Changed the name 'Purpose' to 'Purpose type' in: name of the domain; name of the reference entity; name of the attribute of the reference entity; name of the relationship between purpose type entity and the entity serviced asset instrument; Primary key of the entity 'Purpose type'. Moreover, I changed the following descriptions: attribute 'Purpose type' of the entity 'Purpose type' to: 'Purpose type is the classification of instruments according to their purpose.'; entity 'Purpose type' to : 'Purpose type encompasses the aims for which the instrument has been given.'; attribute 'Purpose type' of the Entity serviced asset instrument to: 'Purpose type is the classification of instruments according to their purpose at a serviced asset instrument.'. | 
 |  |  | 
 | 2023.09.14 |  >fix: Updated the name of relationship type 'Project finance loan type classifies Financial asset instrument' to include the correct spelling of the name of entity type 'Project finance loan indicator' and of 'Serviced asset instrument'. | 
 | | >fix: Updated the name of relationship type 'Payment frequency is assigned to Financial asset instrument' to include the correct spelling of the name of entity type 'Serviced asset instrument'. | 
 | | >fix: Updated the name of relationship type 'Subordinated debt type classifies Debt security' to include the correct spelling of the name of entity type 'Subordinated debt indicator'. | 
 | | >fix: Updated the name of relationship type 'Exposure with recourse type classifies Financial asset instrument(s)' to include the correct spelling of the name of entity type 'Serviced asset instrument'. | 
 | | >fix: Updated the name of relationship type 'Debt financing according to AnaCredit indicator classifies Financial asset instrument' to include the correct spelling of the name of entity type 'Serviced asset instrument'. | 
 | | >fix: Updated the name of relationship type 'Purpose is assigned to Financial asset instrument' to include the correct spelling of the name of entity type 'Serviced asset instrument'. | 
 | 2023.09.13 |  >feat: added new domain 'Accounting framework' to classify which framework is used for the accounting classification. | 
 | | >feat: added new attributes to entity type 'Reporting agent internal group role' to indicate which Accounting standard is used by the reporting agent for reporting. These attributes are | 
 | |        - 'Accounting standard for statistical reporting' | 
 | |        - 'Accounting standard for solo reporting' | 
 | |        - 'Accounting standard for consolidated reporting' | 
 |  |  | 
 | 2023.09.13 |  >fix: updated the lay-out placement of reference data entity type 'Fiduciary instrument type'. | 
 |  |  | 
 | 2023.09.13 |  >fix: update the lay-out of the entity types 'factoring cash reserve', 'transferable deposit', and 'Deposit with agreed maturity' to show the full definition in the logical model diagram. | 
 |  |  | 
 | 2023.09.12 |  >fix: Fixed a missing " in the text "Private sector company other than corporation". | 
 |  |  | 
 | 2023.09.08 |  >fix: removed Loan and advance type by litigation status | 
 |  |  | 
 | 2023.09.08 |  >fix: moved Litigation status to Loan and Advance entity | 
 |  |  | 
 | 2023.09.07 |  >fix: Added the relevant change request to the changes for the attributes 'next interest rate reset date' and 'interest rate reset frequency' in entity type 'Serviced asset instrument'. | 
 |  |  | 
 | 2023.09.06 |  >feat: Fixed the usage of 'issue based' where it should be hyphenated to 'issue-based by changing the name of the following elements: | 
 | |       - relationship type 'Debt security is rated by Rating grade for issue-based rating system via Rating grade for issue-based rating system Debt security assignment' | 
 | |       - relationship type 'Issue-based rating system has Rating grade for issue-based rating system' | 
 | |       - relationship type 'Rating grade for issue-based rating system is applied to Debt security via Rating grade for issue-based rating system Debt security assignment' | 
 | |       - entity type 'Issue-based rating system' | 
 | |       - entity type 'Rating grade for issue-based rating system' | 
 | |       - entity type 'Rating grade for issue-based rating system Debt security assignment' | 
 | |       - subview 'Introduction to the LDM - Issue-based rating system applied to Debt security' | 
 | | >feat: Update the description by fixing the usage of 'issue based' to 'issue-based' in the following elements: | 
 | |       - attribute 'Rating system.'Rating system type by target (Issue vs. Issuer based)' | 
 |  |  | 
 | 2023.09.05 |  >feat: added Under construction or development indicator to Real estate collateral | 
 |  |  | 
 | 2023.09.04 |  >fix: Renamed the member "Covered bond programme" from "Covered bond program" of domain 'Securitisation and other credit transfer type' | 
 |  |  | 
 | | >fix: Renamed the member "Credit transfer other than securitisation and covered bond programme" from "Credit transfer other than securitisation and covered bond program " of domain 'Securitisation and other credit transfer type' | 
 | | >fix: Renamed the member "Asset pool (subject to a Covered bond program)" to "Asset pool (subject to a Covered bond programme)" of domain 'Asset pool (subject to securitisation and other credit transfer) type'. | 
 | | >fix: Renamed the member "Asset pool (subject to a credit transfer other than securitisation and covered bond program)" to "Asset pool (subject to a credit transfer other than securitisation and covered bond programme)" of domain 'Asset pool (subject to securitisation and other credit transfer) type'. | 
 |  |  | 
 | 2023.08.28 |  >fix: Added the domain 'Time past due band' to the primary key of 'time past due band'. | 
 |  |  | 
 | 2023.08.28 |  >feat: Added the members 'general allowances for credit risk' and 'general allowances for banking risk' to the Domain 'AnaCredit collection Impairment status'. Removed the member 'General allowances (GAAP): To be used if the instrument is subject to impairment in accordance with an applied accounting standard other than IFRS 9 and no specific loss allowances are raised against the instrument (unimpaired).' from the same domain. | 
 |  |  | 
 | 2023.08.28 |  >fix: set all attributes in risk measure sensitivity to mandatory | 
 |  |  | 
 | 2023.08.28 |  >fix: typos in a domain of asset class of a cover pool and updated notes | 
 |  |  | 
 | 2023.08.28 |  >feat: added classification type 'Risk related' to the new FRTB entity types. | 
 | | >feat: added the feature request of FRTB to most of the changed elements. | 
 | 2023.08.28 |  >feat: Added the classificastion type Risk related to color things red in the LDM. | 
 |  |  | 
 | 2023.08.25 |  >feat: Added the entity 'Financial asset instrument derived data' and added a one to one relationship between the entitiy 'Financial asset instrument' and 'Finantial asset instrument derived data'. | 
 | | >feat: Added the entity 'Credit facility risk data derived data' and added a one to one relationship between the entitiy 'Credit facility risk data' and 'Credit facility risk data derived data'.  | 
 | | >feat: Added the entity 'Debt security derived data' and added a one to one relationship between the entitiy 'Debt security' and 'Debt security derived data'.   | 
 | | >feat: Added the entity 'Time past due band' and added a mandatory attribute to it: 'Time past due band'. | 
 | | >feat: Added more three '1 to *' relationships: Between 'Time past due band' and 'Finantial asset instrument derived data'; Between 'Time past due band' and 'Credit facility risk data derived data'; Between 'Time past due band' and 'Debt security derived data'. | 
 |  |  | 
 | 2023.08.25 |  >feat: Update the definition of the attribute 'time past due band' in the entity types 'Financial asset instrument derived data', 'Credit facility risk data derived data', 'Debt security derived data'. Also updated the definition of the entity type 'Time past due band'. | 
 | 2023.08.25 |  >chore: added more notes to the FRTB as review comments. | 
 |  |  | 
 | 2023.08.25 |  >fix: updated the name of attribute 'Date of initiation of legal proceding' of entity type 'Organisation with legal proceeding' to 'Date of initiation of legal proceeding' to fix a typo in the word proceeding. | 
 | | >fix: updated the definition of entity type 'Organisation with legal proceeding' to fix a typo in the word proceeding. | 
 | | >fix: updated the definition of entity type 'Organisation without legal proceeding' to fix a typo in the word proceeding. | 
 | | >fix: updated the name of domain 'Organisation type by legal proceding status' to fix a typo in the word proceeding. | 
 | | >fix: updated the name of domain 'Organisation type by legal proceding status (Input Layer)' to fix a typo in the word proceeding. | 
 |  |  | 
 | 2023.08.25 |  >fix: Updated the name of the arc describing the subtype of the securitisation tranche to 'Type of securitistation tranche'. | 
 | 2023.08.25 |  >fix: added subtype 'Tranche in a synthetic securitisation' to the arc of its supertype discriminator | 
 | 2023.08.25 |  >chore: updated the lay-out of the diagrams | 
 | 2023.08.25 |  >feat: Updated the name of entity type 'Tranche in synthetic securitisation' to 'Tranche in a synthetic securitisation'. | 
 | | >feat: Added a definition to entity type 'Tranche in a synthetic securitisation'. | 
 |  |  | 
 | 2023.08.24 |  >feat: Added the entity 'Financial asset instrument derived data' and added a one to one relationship between the entitiy 'Financial asset instrument' and 'Finantial asset instrument derived data'. | 
 |  |  | 
 | 2023.08.24 |  >feat: Updated the definition of the entity type 'Measurement method' to indicate what it classifies. | 
 | | >feat: Updated the attribute 'Measurement method' of entity type 'Investment property not taken into possession' with a definition.  | 
 | | >feat: Updated the attribute 'Measurement method' of entity type 'Investment property taken into possession' with a definition.  | 
 | | >feat: Updated the attribute 'Measurement method' of entity type 'Measurement method' with a definition.  | 
 | | >feat: Updated the attribute 'Measurement method' of entity type 'Other intangible asset not taken into possession' with a definition.  | 
 | | >feat: Updated the attribute 'Measurement method' of entity type 'Other intangible asset taken into possession' with a definition.  | 
 |  |  | 
 | 2023.08.22 |  fix a typo in the defenition of rating agency | 
 |  |  | 
 | 2023.08.18 |  >feat: added Non-performing prior to forbearance to Credit facility risk data and Debt security | 
 |  |  | 
 | 2023.08.17 |  >fix: Added a definition to attribute 'European Union member country type' of entity type 'European Union member country'. | 
 | | >fix: Added a definition to attribute 'European Union member postal code type' of entity type 'European Union member postal code'. | 
 | | >fix: Fixed two typos in the definition of 'Assigned debtor'; our ==> or; withour ==> without | 
 |  |  | 
 | 2023.08.16 |  >Fix: Added a hyphen to the name of attribute 'End date of interest-only period' of entity type 'Deposit'. | 
 | | >Fix: Added a hyphen to the definition of attribute 'Financial asset instrument type by interest rate only' of entity type 'Financial asset instrument. | 
 | | >Fix: Added a hyphen to the name of attribute 'End date of interest-only period' of entity type 'Other loan'. | 
 | 2023.08.16 |  >fix: fixed a typo in the definition of attribute 'Debt financing according to AnaCredit indicator' of entity type 'Financial asset instrument' and of entity type 'Debt financing according to AnaCredit indicator'. Changed Wheather to Whether. | 
 |  |  | 
 | 2023.08.16 |  >fix: added definition to attribute 'country type' of entity type 'country'. | 
 |  |  | 
 | 2023.08.16 |  >fix: Added a definition to accounting hedge indicator | 
 |  |  | 
 | 2023.08.15 |  >feat: added domain Risk class, added entity CSR securitisation | 
 |  |  | 
 | 2023.08.14 |  >feat: added arc to Financial contract | 
 |  |  | 
 | 2023.08.14 |  >feat: added arcs to Entity role hierarchy | 
 |  |  | 
 | 2023.08.14 |  >feat: added arc to Collateral received instrument | 
 |  |  | 
 | 2023.08.14 |  >feat: added arcs to hierarchy Exchange tradable derivative position role | 
 |  |  | 
 | 2023.08.14 |  >fix: added arc to Abstract instrument role | 
 |  |  | 
 | 2023.08.14 |  >feat: updated model for the FRTB framework | 
 |  |  | 
 | 2023.08.10 |  >fix: Updated the name of relationship type 'Financial contract gives rise to IInstrument resulting directly from a Financial contract' to 'Financial contract gives rise to Instrument resulting directly from a Financial contract | 
 |  |  | 
 | 2023.08.09 |  >fix: Updated the preferred abbreviation of entity type 'Re-securitisation type' from RSCRTSTN_AMN to RSCRTSTN_INDCTR. It now matches the abbreviation of the corresponding variable in the BIRD SDD navigator. | 
 | 2023.08.09 |  >feat: Added issue #171 Fair value option designation vs Fair value designation & Fair value changes to the changed data model elements for this issue. | 
 |  |  | 
 | 2023.08.09 |  >Feat: Added new member "Management on a fair value basis" to domain 'Fair value designation' to be able to use it in attribute 'Fair value option designation' of entity type 'Balance sheet recognised financial asset instrument according to International Financial Reporting Standard (IFRS)'. | 
 |  |  | 
 | 2023.08.03 |  Replaced the non-definitions of attribute Protection value date with the definition from the AnaCredit regulation for Date of protection value. | 
 |  |  | 
 | 2023.08.03 |  fix: Fixed definitions of entity type 'Other financial collateral' to include all other siblings, and updated definition of attribute 'Protection value date' of entity type 'Collateral' to match the definition of the AnaCredit regulation. | 
