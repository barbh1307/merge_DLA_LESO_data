import pandas as pd
import sys

# load expected state and territory names and abbreviations
# set up expected the data
# load postal codes from file
path_supportfiles = 'gs://dla_leso_quarterly_data/OriginalData/'
postal_file = '20200712_StateAbbreviations.txt'
try:
    expected_postalcodes_dict = pd.read_csv(
        path_supportfiles + postal_file, header=None, quotechar = "'").\
        set_index([1])[0].to_dict()
except FileNotFoundError:
    print("Error: postal file missing:",path_supportfiles + postal_file)
except:
    print("Unexpected error A:", sys.exc_info()[0])

# all expected values for DISP_shipments_cancellations_mmddyyyy.xlsx

expected_sheets = ['SHIPMENTS','CANCELLATIONS']

expected_shipments_columns = ['State', 'Station Name (LEA)', 'Requisition ID',
                              'FSC', 'NIIN', 'Item Name', 'UI', 'Quantity',
                              'Acquisition Value', 'Date Shipped', 'Justification']

expected_cancellations_columns = ['Cancelled By', 'RTD Ref', 'State', 'Station Name (LEA)',
                                  'FSC', 'NIIN', 'Item Name', 'UI', 'Quantity',
                                  'Acquisition Value', 'Date Requested', 'Justification',
                                  'Reason Cancelled']
unique_file_colummns = ['FSC', 'NIIN', 'Justification']
unique_shipments_columns = ['Requisition ID', 'Date Shipped']
unique_cancellations_columns = ['Cancelled By', 'Date Requested', 
                                'RTD Ref', 'Reason Cancelled']

def check_sheets(sheets: list) -> list:
    """Returns [{missing sheets},{unexpected sheets}].
    """
    missing = set(expected_shipcanc_sheets).difference(sheets)
    unexpected = set(sheets).difference(set(expected_shipcanc_sheets))
    return [missing, unexpected]

# main
# Q does this file have the expected sheets? if no, what unexpected sheets?
""" TESTS:
#unexpected_sheets = check_sheets(['SHIPMENTS','CANCELLATIONS']) #good
#unexpected_sheets = check_sheets(['SHIPMENT','CANCELLATIONS'])  #good
#unexpected_sheets = check_sheets([]) #BAD shouldn't say all okay
#unexpected_sheets = check_sheets(['SHIPMENTS','other']) #good
#unexpected_sheets = check_sheets() #traceback error needs sheets
#unexpected_sheets = check_sheets(['SHIPMENTS','CANCELLATIONS','OTHER']) #good
#unexpected_sheets = check_sheets(['CANCELLATIONS','OTHER','SHIPMENTS']) #good
#unexpected_sheets = check_sheets(['CANCELLATIONS','SHIPMENTS']) #good
"""
unexpected_sheets = check_sheets(['SHIPMENTS','other']) #good
if (len(unexpected_sheets[0]) != 0) & (len(unexpected_sheets[1]) != 0):
    print('Found the following unexpected sheets:\n',)
    print('   Missing sheets:',unexpected_sheets[0])
    print('   Unexpected sheets:',unexpected_sheets[1])
else:
    print('XLSX has only expected sheets.')

print('done executing')
