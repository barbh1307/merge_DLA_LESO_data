import pandas as pd

df_DE = pd.DataFrame(
  {'State':['DE','DE','DE','DE','DE']\
  ,'Station Name (LEA)':['North Anton Pol Dep','Cityview Sheriff'\
                        ,'Center Cty Sheriff','Bluffpoint Public Safety'\
                        ,'Center Cty Sheriff']\
  ,'NSN':['4352-00-093-2344','4232-00-DIS-OBJT','2222-00-645-0909'\
         ,'5937-00-729-1122','5225-01-323-9743']\
  ,'Item Name':['rifle','maps','bullets','hats','coats']\
  ,'Quantity':[40,12,300,2,86]\
  ,'UI':['feet','boxes','each','piece','feet']\
  ,'Acquisition Value':[204.3,24,759,65.24,9024.00]\
  ,'DEMIL Code':['P','F','P','G','A']\
  ,'DEMIL IC':[2,3,2,5,3]\
  ,'Ship Date':['03-01-2020','03-01-2020','03-01-2020','03-01-2020','03-01-2020',]\
  ,'Station Type':['State','State','State','State','State']})

df_FL = pd.DataFrame(
  {'State':['FL','FL','FL','FL']\
  ,'Station Name (LEA)':['North Pol Dep','Citybay Police','Pointel Patrol','Weston PD']\
  ,'NSN':['4452-00-094-AALE','4232-00-DIS-OBJT','5327-00-721-1662','6365-01-333-9003']\
  ,'Item Name':['rifle','gloves','hats','winch']\
  ,'Quantity':[23,4,2,13]\
  ,'UI':['feet','each','piece','feet']\
  ,'Acquisition Value':[20.3,294,759,651.24,]\
  ,'DEMIL Code':['P','F','G','A']\
  ,'DEMIL IC':[2,3,5,3]\
  ,'Ship Date':['03-10-2020','03-12-2020','03-02-2020','03-11-2020',]\
  ,'Station Type':['State','State','State','State']})

df_WV = pd.DataFrame(
  {'State':['WV','WV','WV','','WV','WV','WV','WV']\
  ,'Station Name (LEA)':['Blue Police','Blue Police','Blue Police','Cay Sher Off'\
                        ,'Gery Patrol','Pointel Patrol','Pointel Patrol','Weston PD']\
  ,'NSN':['4451-01-094-2678','4223-00-578-8888','2121-01-LST-RMES','3527-00-211-1052'\
         ,'6365-01-322-9330','4232-00-DIS-OBJT','2112-00-425-0919','5327-00-721-1662']\
  ,'Item Name':['hats','chair','table','boots','winch','table','boots','rings']\
  ,'Quantity':[3,1,90,34,1,2,4,2]\
  ,'UI':['feet','boxes','each','piece','feet','each','piece','feet']\
  ,'Acquisition Value':[201.3,2.94,758,64.1,94.5,10,11,12.5]\
  ,'DEMIL Code':['P','F','P','G','A','P','G','A']\
  ,'DEMIL IC':[2,3,2,5,3,2,5,3]\
  ,'Ship Date':['04-10-2020','04-10-2020','04-10-2020','03-10-2020','04-21-2020'\
               ,'03-12-2020','03-12-2020','03-11-2020',]\
  ,'Station Type':['State','State','State','State','State','State','State','State']})

def get_data() -> dict:
    """ Return a dictionary from test data here. """
    return {'Deleware':df_DE, 'Florida':df_FL, 'West Virginia':df_WV}
