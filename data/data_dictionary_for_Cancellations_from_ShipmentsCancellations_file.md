   
| Field | Data Type | Description | Length | Expected Pattern | null? |   
| ----- | ---- | ---- | ---- | ---- |---- |   
| Cancelled By | string | apparently agency that cancelled request; needs further research | varies | varies | yes | 
| RTD Ref | string | apparently unique identifier; needs further research | 6 or 7 | [0-9]{7} | no |   
| State | string | two digit postal abbreviation for U.S. state or territory| 2 | \[A-Z\]\[A-Z\] | no |   
| Station Name (LEA) | string | descriptive name of requesting law enforcement agency | varies | varies | no |   
| FSC | string | [Federal Supply Number](https://en.wikipedia.org/wiki/NATO_Stock_Number#Federal_Supply_Classification_Group_(FSCG)) consisting of the Federal Supply Group and Federal Supply Classification | 4 | \[0-9\]{4} | no |   
| NIIN | string | [National Item Identification Number](https://en.wikipedia.org/wiki/NATO_Stock_Number#National_Item_Identification_Number_(NIIN)) a Country Code followed by a 7-digit item identifier string | 9 | \[0-9\]{9} | no |   
| Item Name | string | descriptive name of requested item | varies | varies | no |   
| UI | string | units of requested item known as unit increments | varies | varies | no |   
| Quantity | integer | number of units requested | varies | [0-9]+ | no |   
| Acquisition Value | float | U.S. dollar amount paid when the item was originally purchased by the government | varies | [0-9]+.[0-9]{2} | no |   
| Date Requested | datetime64 | date request made; needs further research | 29 | yyyy-mm-ddT00:00:00.000000000 | no |   
| Justification | string | descriptive text justifying request; needs further research | varies | varies | yes |   
| Reason Cancelled | string | capitalized code followed by description of why request is cancelled; needs further research | varies | varies | yes |   
