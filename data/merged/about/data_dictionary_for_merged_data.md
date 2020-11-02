   
| Field | Data Type | Description | Original Column | Length | Expected Pattern | null? |   
| ----- | ---- | ---- | ---- | ---- |---- | ---- |   
||| __Constructed Fields__ |||||   
| File | string | file that populated this record | same as LESO filename | varies | see LESOfile variables | no |   
| Sheet | string | sheet that populated this record | same as sheet name in LESO file | varies | varies | no |   
| Item_FSG | string | supply category the item belongs to; see [Federal Supply Group Number](https://en.wikipedia.org/wiki/List_of_NATO_Supply_Classification_Groups#References) | file dependent, digits 1&2 of \['NSN','FSC'\]| 2 | \[0-9\]{2} | no |   
| Item_FSC | string | supply class the item belongs to; see [Federal Supply Group Number](https://en.wikipedia.org/wiki/List_of_NATO_Supply_Classification_Groups#References) | file dependent, digits 3&4 of \['NSN','FSC'\] | 2 | \[0-9\]{2} | no |   
| Item_CC | string | country code for where final assembly of item occurred (a.k.a. nation code; see [Federal Supply Group Number](https://en.wikipedia.org/wiki/National_Codification_Bureau) | file dependent, digits 5&6 of \['NSN'\] or digits 1&2 of \['NIIN'\]| 2 | \[0-9\]{2} | no |   
| Item_Code | string | supply class the item belongs to; see [Federal Supply Group Number](https://en.wikipedia.org/wiki/List_of_NATO_Supply_Classification_Groups#References) | file dependent, last 7 digits of \['NSN','NIIN'\] | 7 | \[0-9\]{7} | no |   
||| __Fields in All Files__ |||||   
| StateAbbreviation | string | two digit postal abbreviation for U.S. state or territory | State | 2 | \[A-Z\]\[A-Z\] | no |   
| RequestingAgency | string | descriptive name of requesting law enforcement agency | Station Name (LEA) | varies | varies | no |   
| ItemDescription | string | descriptive name of requested item | Item Name | varies | varies | no |   
| RecordDate | datetime64 | date | file dependent \['Ship Date','Date Shipped','Date Requested'\] | 29 | yyyy-mm-ddT00:00:00.000000000 | no |   
| AcquisitionValue | float | U.S. dollar amount paid when the item was originally purchased by the government | Acquisition Value | varies | [0-9]+.[0-9]{2} | no |   
| Quantity | integer | number of units requested | Quantity | varies | [0-9]+ | no |   
| UnitIncrement | string | units of requested item known as unit increments | UI | varies | varies | no |   
||| __Fields in AllStatesAndTerritories Only__ | __fill value 'not in file'__ ||||   
| NSN | string | [NATO Stock Number](https://en.wikipedia.org/wiki/NATO_Stock_Number) a government-assigned identifier for requested item | NSN | 9 | \[0-9\]{4}-\[0-9\]{2}-\[A-Z0-9\]{3}-\[A-Z0-9\]{4} | no |   
| DEMILCode | character | [demilitarization code](https://www.dla.mil/HQ/LogisticsOperations/Services/FIC/DEMILCoding/DEMILCodes/) for level of destruction required when the item leaves Department of Defense control | DEMIL Code | 1 | \[GPFDCEBQA\] | no |   
| DEMILIC | integer | [demilitarization itegrity code](https://www.dla.mil/HQ/LogisticsOperations/Services/FIC/DEMILCoding/DEMILCodes/) validity of DEMIL Code (a missing value means it has not yet been reviewed), see [FLIS manual](https://www.dla.mil/HQ/LogisticsOperations/TrainingandReference/FLISProcedures/) for more information | DEMIL IC | 1 | [0-9] or blank | yes |   
| StationType | string | level of government associated with requesting agency; needs further research | Station Type | 5 | 'State' | no |   
||| __Fields in Shipments_Cancellations Only__ | __fill value 'not in file'__ ||||   
| FSC | string | [Federal Supply Number](https://en.wikipedia.org/wiki/NATO_Stock_Number#Federal_Supply_Classification_Group_(FSCG)) consisting of the Federal Supply Group and Federal Supply Classification | FSC | 4 | \[0-9\]{4} | no |   
| NIIN | string | [National Item Identification Number](https://en.wikipedia.org/wiki/NATO_Stock_Number#National_Item_Identification_Number_(NIIN)) a Country Code followed by a 7-digit item identifier string | NIIN | 9 | \[0-9\]{9} | no |   
| Justification | string | descriptive text justifying request; needs further research | Justification | varies | varies | yes |   
||| __Fields in Shipments Only__ | __fill value 'not in file'__ ||||   
| RequisitionID | string | apparently unique identifier needs further research | Requisition ID | 14 | [A-z0-9]{14} | no |   
||| __Fields in Cancellations Only__ | __fill value 'not in file'__ ||||   
| CancelledBy | string | apparently agency that cancelled request; needs further research | Cancelled By | varies | varies | yes | 
| RTDRef | string | apparently unique identifier; needs further research | RTD Ref | 6 or 7 | [0-9]{7} | no |     
| ReasonCancelled | string | why request is cancelled; needs further research | Reason Cancelled | varies | varies | yes |   
