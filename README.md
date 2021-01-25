## Exploring Defense Logistics Agency Law Enforcement Support Office Public Data

The goal of this repository is to create a dataset from DLA LESO public data that can be integrated with other policing practices datasets.   

LESO stands for Law Enforcement Support Office. It is a branch of the Defense Logistics Agency (a.k.a. DLA). The purpose of the office is to manage the transfer of excess military material to law enforcement agencies in U.S. states and territories for a program known as the '1033 Program.' It is codified in [10 U.S.C. &sect; 2576a](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section2576a&num=0&edition=prelim). More information on this program can be found in the [Overview of the Program](#overview-of-the-program) section of this document.   

The data source for this project is the [DLA LESO Public Information website](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). This repository uses two files published quarterly on that site.  __LESO Property Transferred to Participating Agencies__ (DISP_AllStatesAndTerritories_yyyymmdd.xlsx) is the inventory of all excess military material transfered to law enforcement agencies as of the most recent quarter. __LESO Information for Shipments (Transfers) and Cancellations of Property__ (DISP_Shipments_Cancellations_yyyymmdd_to_yyyymmdd.xlsx) contains all the requests/shipments and cancellations made during the most recent quarter. See [Notes on the Data](#notes-on-the-data) section of this document for important notes about the data.   

There are three kinds of Python notebooks in this repository. Notebooks in the CheckOriginalFiles folder perform checks to ensure the latest quarterly files match previous versions of the data files. Notebooks in MergeOriginalFiles folder merge the data files in such a way that the original data could be recreated. Notebooks in ExploreOriginalFiles folder do simple explorations of the original data.   

This repository contains a zipped file containing merged data:   
```
25 Jan 2021    10860780    military_equipment_distributions_to_law_enforcement_agencies_us.zip
               SHA256     E700458A51FF00475F28D2B5827F04D4BBAA4992C2B23A67AD9696009BAAAD46
```
Citation:      Hawes, B. (2020, November). Merged Data from DLA LESO Public Data. Retrieved [to be filled in] from [link to this repository]

#### How to use the notebooks

###### Step 1
 - git the repository   
###### Step 2
 - Download the DISP_AllStatesAndTerritories_yyyymmdd.xlsx and DISP_Shipments_Cancellations_yyyymmdd_to_yyyymmdd.xlsx files from [DLA LESO site](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). Place the XLSX files in the 'data' folder of your repository.   
###### Step 3
 - Download the state names/abbreviations from [US Postal Service Publication 28](https://pe.usps.com/text/pub28/28apb.htm). Covert the file to a comma-separated-values file named USPS_StateAbbreviations.csv with the full state or territory name first followed by the state or territory abbreviation. Place the CSV file in the data folder of your repository.  
###### Step 4
 - Run the notebooks in the 'CheckOriginalFiles' first to see if the XLSX files are consistant with previous files.   
 - Run the notebook in the 'MergeOriginalFiles' to merge the DISP_AllStatesAndTerritories_yyyymmdd.xlsx and DISP_Shipments_Cancellations_yyyymmdd_to_yyyymmdd.xlsx  files from the same quarter into TSV files. By default, the data is separated into TSV files by state which are placed in the data/merged directory. If you collect data from multiple quarters, you can append the new data to the existing TSV files.   
 - Explore the XLSX data with the notebooks in the 'ExploreOriginalData' folder.  These notebooks walk through some of the idiosyncracies of the data.

### Other Projects Using DLA LESO Public Data
This project is forked from OpenTwinCities [police-militarization-data-analysis](https://github.com/OpenTwinCities/police-militarization-data-analysis) repository.   

An interesting kaggle dataset that has its own version of this data is [JohnM's Police Violence & Racial Equity Part 2 of 3](https://www.kaggle.com/jpmiller/police-violence-racial-equity).   

### Overview of the Program
The following information is from [DLA LESO FAQ](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/ProgramFAQs.aspx) unless otherwise specified.

The Defense Logistics Agency (DLA) Law Enforcement Support Office (LESO) 1033 Program comes from the National Defense Authorization Act (NDAA). The 2016 version of this act, also known as FY16 NDAA, requires programs that transfer excess military supplies to law enforcement agencies to make certain data about those transfers public. '1033' referes to the section of FY97 NDAA where the modern version of these types of transfers originated. The exact wording for what data is to be made public is defined in [10 U.S.C. &sect; 2576a](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section2576a&num=0&edition=prelim). This is one way that law enforcement agencies in the U.S. and its territories can acquire military equipment, but there are others that are outside the scope of this repository.   

#### Public Data Requirements
[10 U.S.C. &sect; 2576a](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section2576a&num=0&edition=prelim) requires publishing of a current inventory of all items transferred through the 1033 Program. It appears that this inventory can be found under *LESO Property Transferred to Participating Agencies* section of the DLA LESO Public Information website. For data analysis, be aware that, though the file has records going back to 1980, materials appear and disappear from the file outside the previous quarter. This may be related to the way controlled and non-controlled materials are handled (see [Notes on the Data](#notes-on-the-data)).   

Another bit of data that is required to be made public are pending requests for transfers. The *LESO Information for Shipments (Transfers) and Cancellations of Property* section of the DLA LESO Public Information website has a file that contains quarterly information regarding requests, also known as shipments, and cancellations. This file has data only from the current quarter. Eventually this repository would like to build a dataset where requests, cancellations and transfers are connected or traceable.

There are other requirements for publishing data about this program, like all law enforcement agencies should make protocols for the appropriate use, supervision and evaluation of effectiveness of controlled property (including auditing and accountability policies) public, but that public data outside the current scope of this repository.

#### Notes on the Data
The DLA LESO 1033 Program distinguishes between 'controlled' and 'non-controlled' materials. [Controlled materials](https://www.dla.mil/Portals/104/Documents/DispositionServices/LESO/DISP_ControlledPropertyDefinition_062019.pdf) are defined as having 'DEMIL Codes' of {B,C,D,E,F,G,Q3} in the [DoD Manual 4160.21-M](https://www.dla.mil/HQ/InformationOperations/DLMS/elibrary/manuals/regulations/). This is more specific that the definition in [10 U.S.C. &sect; 2576a(f)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section2576a&num=0&edition=prelim).   

Controlled materials must be returned to the DLA when a law enforcement agency no longer has need of them. Non-controlled materials become the property of the law enforcement agency after one year from the date of transfer. These changes appear to be implicitly handled by additional or missing records from quarter to quarter in the LESO Property Transferred to Participating Agencies (DISP_AllStatesAndTerritiories_yyyymmdd.xlsx) file.   

The DLA LESO 1033 Program distributes excess military materials to agencies whose primary purpose is the enforcement of laws particularly those related to drugs, terrorism and border patrol. Goverment bodies at the federal, state and local level are included, as are agencies in U.S. territories. The [FAQ](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/ProgramFAQs.aspx) states:   

> Every law enforcement agency is now vetted through the National Crime Information Center database, ensuring the Originating Agency Identifier number is
> associated to the agency requesting enrollment into the program. An ORI number is distributed via the FBI Criminal Justice Information Services.   

The Originating Agency Identifier (ORI) information for participating agencies is not included on the DLA LESO Public Information website data. However, having the ORI associated with the participating agency would be valuable for transparency as well as be a definitive way to track policing agencies across crime reporting datasets. This repository will eventually incorporate the ORI into DLA LESO public data. A file called 'Agency Participation Data' from the [FBI Crime Explorer website](https://crime-data-explorer.fr.cloud.gov/) contains ORIs for agencies in the U.S. states and territories. More information about this number can be found at the [FBI Criminal Justice Information Services website](https://www.fbi.gov/services/cjis/fingerprints-and-other-biometrics/ordering-fingerprint-cards-and-training-aids).   

An alternate source for the XLSX files can be found at the [DLA's Reading Room](https://www.dla.mil/DispositionServices/FOIA/EFOIALibrary/).

#### Timeline of NDAA as related to the DLA LESO 1033 Program
The program for transferring excess military supplies to law enforcement agencies as we know it today originated in the FY90-91 NDAA. Some important highlights, as found on the [DLA LESO FAQ](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/ProgramFAQs.aspx) are listed here:   
 - 1990-91 authorizes the transfer of excess Department of Defense (DoD) material to federal, state and local enforcement agencies  
 - 1997 specifies that the DoD material must be used for 'bona fide law enforcement purposes - particularly those associated with counter-drug and counter-terrorism activities.' The program is referred to as the '1033 Program' because that is the section number of the NDAA where the wording occurs.    
 - 2015 every agency receiving material from this program is responsible for training personnel in use of material, maintaining and repairing material. Certified documentation of these procedures must be supplied annually.   
 - 2016 requirement that data related to 1033 Program be made public. It also added 'border patrol' as a bona fide law enforcement purpose.   
