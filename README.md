# Exploring Defense Logistics Agency Law Enforcement Support Office Public Data

These notebooks merge and do simple explorations of the quarterly XLSX files published at the [DLA LESO site](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). The files can also be found [here](https://www.dla.mil/DispositionServices/FOIA/EFOIALibrary/).   

This repository does NOT include the XLSX files nor the merged dataset.   

# How to use the notebooks

### Step 1
 - git the repository   
### Step 2
 - Download the AllStatesAndTerritories and Shipments_Cancellations files from [DLA LESO site](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/). Place the XLSX files in the 'data' folder.   
### Step 3
 - Download the state names/abbreviations from [US Postal Service Publication 28](https://pe.usps.com/text/pub28/28apb.htm). Covert the file to a 'Comma Separated Values' file with the full state or territory name first followed by the state or territory abbreviation.   
### Step 4
 - Run the notebooks in the 'CheckOriginalFiles' first to see if the XLSX files are consistant with previous files.   
 - Run the notebook in the 'MergeOriginalFiles' to merge the AllStatesAndTerritories and Shipments_Cancellations XLSX files from the same quarter into TSV files. By default, the data is separated into TSV files by state which are placed in the data/merged directory.   
 - Explore the XLSX data with the notebooks in the 'ExploreOriginalData' folder. Before trying to analyze the merged data there are some important things to notice about the original data.

# More information
It is forked from OpenTwinCities [police-militarization-data-analysis](https://github.com/OpenTwinCities/police-militarization-data-analysis) repository.   

An interesting kaggle dataset that has its own version of this data is [here](https://www.kaggle.com/jpmiller/police-violence-in-the-us).   
