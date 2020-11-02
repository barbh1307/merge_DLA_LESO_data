__Dataset Title:__ military_equipment_distributions_to_law_enforcement_agencies_us.zip   
 __Type:__ compiled, growing   
 __Schedule:__ new files are appended at the end of each quarter \(March 31, June 30, September 30, December 31\)   
 __Timeframe:__ 2020-03-31 to present   
 __Description:__ This is a set of TSV files containing merged transfer, shipment/request and cancellation data for excess military supplies made available to law enforcement agencies in U.S. states and territories. The merged data is divided into files by U.S. state or territory postal abberviation. The data is published quarterly by Defense Logistics Agency (DLA) Law Enforcement Support Office (LESO) in two XLSX files.   

__Primary Data Sources:__   
*The XLSX files used to create the dataset are archived in GCP cloud storage.*
 - __DISP\_AllStatesAndTerritories\___*yyyymmdd*__.xlsx__   [LESO Property Transferred to Participating Agencies](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/)   
This is a cumulative file of transfers to law enforcement agencies in U.S. states and territories. However, the records are not consistent from quarterly data file to quarterly data file (see the analysis in [Inconsistancies_AllStatesAndTerritories.ipynb](notebooks/ExploreOriginalFiles/Inconsistancies_AllStatesAndTerritories.ipynb)).   
 - __DISP\_Shipments\_Cancellations\___*yyyymmdd*__\_to\___*yyyymmdd*__.xlsx__   [LESO Information for Shipments (Transfers) and Cancellations of Property](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/)   
This is a non-cumulative file of shipments (a.k.a requests) and cancellations made by law enforcement agencies to the program.   

__Supporting Data Sources:__   
 - Postal codes: [U.S. State and Territory Postal Codes](https://pe.usps.com/text/pub28/28apb.htm)   

__Processing Steps Using the Notebooks in this Repository:__   
 1. Place the original *LESO Property Transferred to Participating Agencies* and *LESO Information for Shipments (Transfers) and Cancellations of Property* files to be merged in the [merging_DLA_LESO_data/data/](./data/).   
 2. If the data is being added to an existing dataset, unzip the existing dataset to [merging_DLA_LESO_data/data/merged/](./data/merged/).   
 3. Check that the files to be merged are consistent with the previous file structure.   
    a. see the notebooks in [merging_DLA_LESO_data/notebooks/CheckOriginalFiles/](./notebooks/CheckOriginalFiles/)   
    b. after running these notebooks, use nbconvert to save them to [merging_DLA_LESO_data/data/merged/about/NotebooksHTMLs/](./data/merged/about/NotebooksHTMLs)   
 4. Merge the data from the original files.   
    a. see the notebook in [merging_DLA_LESO_data/notebooks/MergeOriginalFiles/](./notebooks/MergeOriginalFiles/)   
    b. after running this notebook, use nbconvert to save it to [merging_DLA_LESO_data/data/merged/about/NotebooksHTMLs/](./data/merged/about/NotebooksHTMLs)   
    c. run checksums on all the generated TSV files; save the output to [merging_DLA_LESO_data/data/merged/checksums_merged.txt](./data/merged/checksums_merged.txt)   
 5. Zip the contents of [merging_DLA_LESO_data/data/merged/](./data/merged/) into __military_equipment_distributions_to_law_enforcement_agencies_us.zip__.   
    a. check that following are all present and updated in [merging_DLA_LESO_data/data/merged/](./data/merged/)   
       -  state TSV files
       -  about/checksums_merged.txt (should have a list of checksums-filename for each state TSV file)   
       -  about/README.txt (should have appended filename-md5_checksums for each original file merged with the dataset)   
       -  about/NotebookHTMLs/ (should be one for each notebook run on the original data for this dataset)   
 6. Back up the original *LESO Property Transferred to Participating Agencies* and *LESO Information for Shipments (Transfers) and Cancellations of Property* along with accompanying checksums files to a long term cloud storage.   
