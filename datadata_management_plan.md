__Dataset Title:__ military_equipment_distributions_to_law_enforcement_agencies_us.zip   
 __Type:__ compiled, growing   
 __Schedule:__ new files are available at the end of each quarter \(March 31, June 30, September 30, December 31\)   
 __Timeframe:__ 2020-03-31 to present   
 __Description:__ This is a set of TSV files containing merged transfer, shipment/request and cancellation data for excess military supplies made available to law enforcement agencies in U.S. states and territories. The merged data is divided into files by U.S. state or territory postal abberviation. The data is published quarterly by Defense Logistics Agency (DLA) Law Enforcement Support Office (LESO) in two XLSX files.   

__Primary Data Sources:__   
 - __DISP\_AllStatesAndTerritories\___*yyyymmdd*__.xlsx__   [LESO Property Transferred to Participating Agencies](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/)   
This is a cumulative file of transfers to law enforcement agencies in U.S. states and territories. However, the records are not consistent from quarterly data file to quarterly data file (i.e. DISP_AllStatesAndTerritories_20200331.xlsx has more records for 2002 than DISP_AllStatesAndTerritories_202000630.xlsx).   
 - __DISP\_Shipments\_Cancellations\___*yyyymmdd*__\_to\___*yyyymmdd*__.xlsx__   [LESO Information for Shipments (Transfers) and Cancellations of Property](https://www.dla.mil/DispositionServices/Offers/Reutilization/LawEnforcement/PublicInformation/)   
This is a non-cumulative file of shipments (a.k.a requests) and cancellations made by law enforcement agencies to the program.   

__Supporting Data Sources:__   
 - Postal codes: [U.S. State and Territory Postal Codes](https://pe.usps.com/text/pub28/28apb.htm)   
 - ORI lists: TODO create this file from [agencies.zip](http://s3-us-gov-west-1.amazonaws.com/cg-d4b776d0-d898-4153-90c8-8336f86bdfec/agencies.zip) downloaded 2020-09-29   
 An explanation of ORI can be found [here](https://omnixx.dps.ms.gov/OMNIXX5/DOCUMENTS/NCIC.OP/ORI.htm).   

Processing Steps:   
 1. Download files (April 15, June 15, October 15, January 15)   
 2. Check the files are consistant with previous versions   
 3. Append the files to existing TSV files   
    a. merge records   
    b. add ori codes   
