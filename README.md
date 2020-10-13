## Exploring Defense Logistics Agency Law Enforcement Support Office Public Data

The goal of this repository is to create a dataset from DLA LESO public data that can be integrated with other policing practices datasets.

These notebooks merge and do simple explorations of the quarterly XLSX files published at the [DLA LESO Public Information website](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). The files can also be found [here](https://www.dla.mil/DispositionServices/FOIA/EFOIALibrary/).   

This repository does NOT include the XLSX files nor the merged dataset.   

#### How to use the notebooks

###### Step 1
 - git the repository   
###### Step 2
 - Download the AllStatesAndTerritories and Shipments_Cancellations files from [DLA LESO site](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). Place the XLSX files in the 'data' folder.   
###### Step 3
 - Download the state names/abbreviations from [US Postal Service Publication 28](https://pe.usps.com/text/pub28/28apb.htm). Covert the file to a 'Comma Separated Values' file with the full state or territory name first followed by the state or territory abbreviation.   
###### Step 4
 - Run the notebooks in the 'CheckOriginalFiles' first to see if the XLSX files are consistant with previous files.   
 - Run the notebook in the 'MergeOriginalFiles' to merge the AllStatesAndTerritories and Shipments_Cancellations XLSX files from the same quarter into TSV files. By default, the data is separated into TSV files by state which are placed in the data/merged directory.   
 - Explore the XLSX data with the notebooks in the 'ExploreOriginalData' folder. Before trying to analyze the merged data there are some important things to notice about the original data.

### Other Projects
It is forked from OpenTwinCities [police-militarization-data-analysis](https://github.com/OpenTwinCities/police-militarization-data-analysis) repository.   

An interesting kaggle dataset that has its own version of this data is [here](https://www.kaggle.com/jpmiller/police-violence-in-the-us).   

### Overview of DLA LESO 1033 Program   
The following information is from [DLA LESO FAQ](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/ProgramFAQs.aspx) unless otherwise specified.

The Defense Logistics Agency (DLA) Law Enforcement Support Office (LESO) 1033 Program comes from the National Defense Authorization Act (NDAA). The 2016 version of this act, also known as FY16 NDAA, requires programs that transfer excess military supplies to law enforcement agencies to make certain data about those transfers public. '1033' referes to the section where the requirement was specified. The exact wording for what data is to be made public is defined in U.S. Code [10 U.S.C. &sect; 2576a](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section2576a&num=0&edition=prelim). This is one way that law enforcement agencies in the U.S. and its territories can acquire military equipment, but there are others that are outside the scope of this repository.   

The DLA LESO 1033 Program distinguishes between 'controlled' and 'non-controlled' materials. Controlled materials are defined as having 'DEMIL Codes' of {B,C,D,E,G,Q} in the [DoD Manual 4160.21-M](https://www.dla.mil/HQ/InformationOperations/DLMS/elibrary/manuals/regulations/).Controlled materials must be returned to the DLA when a law enforcement agency no longer has need of them. Non-controlled materials become the property of the law enforcement agency after one year of receipt. These changes appear to be implicitly handled by additional or missing records in the inventory of transfers discussed in the next section.   

The DLA LESO 1033 Program supplies agencies whose primary purpose is the enforcement of laws. Goverment bodies at the federal, state and local level are included, as are agencies in U.S. territories. The FAQ states:   

> Every law enforcement agency is now vetted through the National Crime Information Center database, ensuring the Originating Agency Identifier number is
> associated to the agency requesting enrollment into the program. An ORI number is distributed via the FBI Criminal Justice Information Services.   

The ORI information for participating agencies is not included on the DLA LESO Public Information website data. However, having the ORI associated with the participating agency would be valuable for transparency as well as be a definitive way to track policing agencies across crime reporting datasets. This repository will eventually incorporate the ORI into DLA LESO public data. A file called 'Agency Participation Data' from the [FBI Crime Explorer website](https://crime-data-explorer.fr.cloud.gov/) contains ORIs for agencies in the U.S. states and territories. More information about this number can be found at the [FBI Criminal Justice Information Services website](https://www.fbi.gov/services/cjis/fingerprints-and-other-biometrics/ordering-fingerprint-cards-and-training-aids).

#### Public Data Requirements
[10 U.S.C. &sect; 2576a](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title10-section2576a&num=0&edition=prelim) requires publishing of a current inventory of all items transferred through the 1033 Program. It appears that this inventory can be found under __LESO Property Transferred to Participating Agencies__ section of the DLA LESO Public Information website. For data analysis, be aware that, though the file is cumulative with records going back to 1980, materials disappear from the file from quarter to quarter. This may be related to the way controlled and non-controlled materials are handled (see previous paragraph).   

Another bit of data that is required to be made public are pending requests for transfers. The __LESO Information for Shipments (Transfers) and Cancellations of Property__ section of the DLA LESO Public Information website has a file that contains quarterly information regarding requests, also known as shipments, and cancellations. This file is non-cumulative. An exploration of how to map the requests to the transfers to cancellations is part of this repository.

There are other requirements for publishing data about this program, like all law enforcement agencies should make protocols for the appropriate use, supervision and evaluation of effectiveness of controlled property (including auditing and accountability policies) public, but it is outside the current scope of this repository.

#### History of DLA LESO 1033 Program
The program for transferring excess military supplies to law enforcement agencies as we know it today originated in the FY90-91 NDAA. Some important highlights, as found on the [DLA LESO FAQ](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/ProgramFAQs.aspx) are listed here:   
 - 1990-91 authorizes the transfer of excess Department of Defense (DoD) material to federal, state and local enforcement agencies  
 - 1997 specifies that the DoD material must be used for 'bona fide law enforcement purposes - particularly those associated with counter-drug and counter-terrorism activities.' The program is referred to as the '1033 Program' because numbered section of the NDAA where the wording occurs.    
 - 2015 every agency receiving material from this program is responsible for training personnel in use of material, maintaining and repairing material. Certified documentation of these procedures must be supplied annually.   
 - 2016 requirement that data related to 1033 Program be made public. It also added 'border patrol' as a bona fide law enforcement purpose.   


