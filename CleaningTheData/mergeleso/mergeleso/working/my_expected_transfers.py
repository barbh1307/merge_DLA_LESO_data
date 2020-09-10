import pandas as pd
import re
import sys

# DEFAULTS and customizations
default_path_datafiles = 'gs://dla_leso_quarterly_data/OriginalData/'
default_leso_file = 'TESTB_AllStatesAndTerritories_03312020.xlsx'

# EXPECTED
# load expected state and territory names and abbreviations
# set up expected the data dictionary key: abbreviation value: name
# load postal codes from file name,abbreviation
path_supportfiles = 'gs://dla_leso_quarterly_data/OriginalData/'
postal_file = '20200712_StateAbbreviations.txt'
try:
    postalcodes_dict = pd.read_csv(
        path_supportfiles + postal_file, header=None, quotechar = "'").\
        set_index([1])[0].to_dict()
except FileNotFoundError:
    print("Error: postal file missing:",path_supportfiles + postal_file)
except:
    print("Unexpected error A:", sys.exc_info()[0])

# all expected values for DISP_AllStatesAndTerritories_mmddyyyy_mmddyyyy.xlsx

# use state/territory names in postal file for expected_allstates_sheets
#expected_sheets = [state_name for state_name in postalcodes_dict.values()]
expected_sheets = ['Washington','Florida','Georgia','West Virginia','Delaware']

expected_columns = ['State', 'Station Name (LEA)',
                    'NSN', 'Item Name', 'Quantity', 'UI', 'Acquisition Value',
                    'DEMIL Code', 'DEMIL IC', 'Ship Date','Station Type']

unique_file_columns = ['NSN', 'DEMIL Code', 'DEMIL IC', 'Ship Date', 'Station Type']
# based on previous values
expected_station_types = ['State']

# based on DOD 4160.28 DEMIL Program or DOD 4100.39M FLIS Manual and this website:
# https://www.dla.mil/HQ/LogisticsOperations/Services/FIC/DEMILCoding/DEMILCodes/
expected_demil_codes = ['G','P','F','D','C','E','B','Q','A']
# based on DOD 4160.28 DEMIL Program or DOD 4100.39M FLIS Manual and this website:
# https://www.dla.mil/HQ/LogisticsOperations/Services/FIC/DEMILCoding/DEMILCodes/
expected_demil_integritycodes = [0,1,2,3,4,5,6,7,8,9]


# FUNCTIONS
def get_unique_values(a_dict: dict, col: str) -> list:
    """Return a list of unique values from all columns in a dictionary of dataframes.
    TODO add doctest
    """
    return [val for key in a_dict for val in a_dict[key][col].unique()]


def check_expected(actual: list,expected: list) -> list:
    """Returns [{missing value},{unexpected values}].
    >>> check_expected([1,2,3],[1,2,3])
    [[], []]
    >>> check_expected([2,3],[1,2,3])
    [[1], []]
    >>> check_expected([1,2,3,4],[1,2,3])
    [[], [4]]
    >>> check_expected([2,3,4],[1,2,3])
    [[1], [4]]
    """
    missing = set(expected).difference(actual)
    unexpected = set(actual).difference(set(expected))
    return [list(missing),list(unexpected)]



def check_userinput(userstring: str, default_value: str) -> str:
    """Returns user input if it is of the appropriate input type.
    >>> check_userinput('', 'some/path/')
    'some/path/'
    >>> check_userinput('', 'file.xlsx')
    'file.xlsx'
    >>> check_userinput('', 'file.txt')
    'file.txt'
    >>> check_userinput('file:/a_path/', 'some/path/')
    'file:/a_path/'
    >>> check_userinput('aFile_n1me.xlsx', 'file.xlsx')
    'aFile_n1me.xlsx'
    >>> check_userinput('pWn8_en.txt', 'file.txt')
    'pWn8_en.txt'

    """
    if len(userstring) == 0:
        return default_value
    elif default_value[-1] == '/':
        return userstring if (
            bool(re.match(r'[a-zA-Z0-9._:\-/]+[/]$',userstring))) else "NEED PATH"
    elif default_value[-5:] == '.xlsx' or default_value[-4:] == '.txt':
        return userstring if (
            bool(re.match(r'[a-zA-Z0-9_\-]+\.xlsx$',userstring))
            or bool(re.match(r'[a-zA-Z0-9_\-]+\.txt$',userstring))) else "NEED FILE"
    else:
        return "MESSED UP"


# MAIN
userpath = input('Enter the path to directory where datafiles are located: ')
#userpostal = input('Enter the name of the file containing postal abbreviations: ')
userleso = input('Enter the DLA LESO file name to check: ')

path_datafiles = check_userinput(userpath, default_path_datafiles)
#postal_file = check_userinput(userpostal, default_postal_file)
leso_file = check_userinput(userleso, default_leso_file)

transfer_dict = pd.read_excel(path_datafiles + leso_file, sheet_name=None)

print('CHECKING',leso_file,'FOR EXPECTED VALUES')
# Q does this file have the expected sheets? if no, what unexpected sheets?
print('\n\nChecking for expected sheets.')
transfer_sheets = [sheet for sheet in transfer_dict]
unexpected_sheets = check_expected(transfer_sheets,expected_sheets) 
if (len(unexpected_sheets[0]) > 0):
    print('Found',len(unexpected_sheets[0]),'missing sheets.')
    print('\tMissing sheets:',\
          [unexpected_sheets[0] if (len(unexpected_sheets[0]) > 0)\
                                else 'none found'])
if (len(unexpected_sheets[1]) > 0):
    print('Found',len(unexpected_sheets[1]),'new sheets.')
    print('\tNew sheets:',\
          [unexpected_sheets[1] if (len(unexpected_sheets[1]) > 0)\
                                else 'none found'])
    #of unexpected sheets which have valid abbreviations
    for new_state in unexpected_sheets[1]:
        new_state_abbreviations = transfer_dict[new_state]['State'].unique()
        print('\tNew state name',new_state,'might be corrected to:')
        for abbrev in new_state_abbreviations:
            try:
                corrected_state = postalcodes_dict[abbrev]
                print('\t\t',corrected_state)
            except:
                continue
else:
    print('XLSX has only expected sheets.')

# Q Do all sheets have the expected columns?
print('\n\nChecking for expected columns in each sheet.')
irregularities_columns = []
print('Expected columns are:',expected_columns)
for sheet in transfer_dict:
    unexpected_columns = check_expected(list(transfer_dict[sheet].columns),\
                                        expected_columns)
    if (len(unexpected_columns[0]) > 0) | (len(unexpected_columns[1]) > 0):
        irregularities_columns.append(
                (sheet,unexpected_columns[0],unexpected_columns[1]))
if (len(irregularities_columns) > 0):
    print('Unexpected columns found in the following sheets:')
    for irregular_value in irregularities_columns:
        print('\t',irregular_value[0],\
              '\n\t\tMissing columns:',irregular_value[1],\
              '\n\t\tUnexpected columns:',irregular_value[2])
else:
    print('Only expected columns found in each sheet of XLSX.')

#import pdb; pdb.set_trace() #DEBUGGING
actual_postalcodes = [{sheet:transfer_dict[sheet]['State'].unique()}\
                      for sheet in transfer_dict]
# Q Does each sheet have exactly one value for 'State'?
print('\n\nChecking that \'State\' has exactly one value per sheet.')
more_values_list = [state for a_dict in actual_postalcodes\
                      for state,abbr_list in a_dict.items()\
                      if len(abbr_list) > 1]
if (len(more_values_list) > 0):
    print('These sheets have more than one postal abbreviation:')
    print('\t',more_values_list)
else:
    print('All sheets have exactly one value for \'State.\'')

# Q Are all the values of 'State' valid U.S. postal abbreviations?
print('\n\nChecking that \'State\' values are all actual postal abbreviations.')
invalid_abbrev_list = [[state,abbr]\
                        for a_dict in actual_postalcodes\
                        for state,abbr_list in a_dict.items()\
                        for abbr in abbr_list\
                        if abbr not in\
                        [post_abbr for post_abbr in postalcodes_dict]]
if (len(invalid_abbrev_list) > 0):
    print('These sheets have invalid postal abbreviations:')
    for invalid_abbrev in invalid_abbrev_list:
        print('\t',invalid_abbrev[0],':  ',invalid_abbrev[1])
else:
    print('All sheets have valid postal codes.')

#actual_station_types = [{sheet:transfer_dict[sheet]['Station Type'].unique()}\
#                         for sheet in transfer_dict]
actual_station_types = {'Washington':['State']}

# Q Are the values of 'Station Type' as expected?
unexpected_station_types = check_expected(set(get_unique_values(transfer_dict,'Station Type'))\
                                         ,set(expected_station_types))
if (len(unexpected_station_types > 0)):
    unexpected_list = [[state,stationtype]\
                        for a_dict in actual_station_types\
                        for state,stationtype_list in a_dict.items()\
                        for stationtype in stationtype_list\
                        if stationtype not in expected_station_types]
    print('These sheets have unexpected station types:')
    for stationtype in unexpected_list:
        print('\t',unexpected_list[0],':  ',unexpected_list[1])
else:
    print('Only expected station types found.')

# Q Are the values of 'DEMIL Code' as expected?
# Q Are the values of 'DEMIL IC' as expected?

# Q Which columns have null/NaN values?

print('done executing')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
