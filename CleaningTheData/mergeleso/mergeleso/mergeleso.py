import pandas as pd
import re
import sys, traceback

import setstate

# DEFAULTS and customizations
default_path_datafiles = 'gs://dla_leso_quarterly_data/OriginalData/'
default_leso_file = 'DISP_AllStatesAndTerritories_03312020.xlsx'
state_dict = {0:'No values found in file.',
              100:'No expected or unique values.',
              110:'No expected values, but all are unique.',
              120:'No expected values, but some are unique.',
              101:'All expected values, but none are unique.',
              111:'All expected values, and all are unique.',
              121:'All expected values, and some are unique.',
              102:'Some missing values, and none are unique.',
              112:'Some missing values, and all are unique.',
              122:'Some missing values, and some are unique.',
              103:'Some missing & unexpected values, and none are unique.',
              113:'Some missing & unexpected values, and all are unique.',
              123:'Some missing & unexpected values, and some are unique.',
              104:'Some unexpected values, and none are unique.',
              114:'Some unexpected values, and all are unique.',
              124:'Some unexpected values, and some are unique.',
              -999:'Missing expected values.'}

# EXPECTED 
# load expected state and territory names and abbreviations
# set up expected the data dictionary key: abbreviation value: name
# load postal codes from file name,abbreviation
path_supportfiles = 'gs://dla_leso_quarterly_data/OriginalData/'
#postal_file = '20200712_StateAbbreviations.txt'
#try:
#    postalcodes_dict = pd.read_csv(
#        path_supportfiles + postal_file, header=None, quotechar = "'").\
#        set_index([1])[0].to_dict()
#except FileNotFoundError:
#    print("Error: postal file missing:",path_supportfiles + postal_file)
#except:
#    print("Unexpected error A:", sys.exc_info()[0])
postalcodes_dict = {'ZZ':'Zero State'}
# ALL EXPECTED VALUES for DISP_AllStatesAndTerritories_mmddyyyy.xlsx

# use state/territory names in postal file for expected_allstates_sheets
expected_sheets = [state_name for state_name in postalcodes_dict.values()]

expected_columns = set(['State', 'Station Name (LEA)',
                    'NSN', 'Item Name', 'Quantity', 'UI', 'Acquisition Value',
                    'DEMIL Code', 'DEMIL IC', 'Ship Date','Station Type'])

file_specific_columns = set(['NSN', 'DEMIL Code', 'DEMIL IC', 'Ship Date', 'Station Type'])
# based on previous values
expected_station_types = set(['State'])

# based on DOD 4160.28 DEMIL Program or DOD 4100.39M FLIS Manual and this website:
# https://www.dla.mil/HQ/LogisticsOperations/Services/FIC/DEMILCoding/DEMILCodes/
expected_demil_codes = set(['G','P','F','D','C','E','B','Q','A'])
# based on DOD 4160.28 DEMIL Program or DOD 4100.39M FLIS Manual and this website:
# https://www.dla.mil/HQ/LogisticsOperations/Services/FIC/DEMILCoding/DEMILCodes/
expected_demil_integritycodes = [0,1,2,3,4,5,6,7,8,9]


# FUNCTIONS
def check_userinput(userstring: str, default_value: str) -> str:
    """Returns user input if it is of the appropriate input type.
    >>> check_userinput('', 'some/path/')
    'some/path/'
    >>> check_userinput('', 'file.xlsx')
    'file.xlsx'
    >>> check_userinput('file:/a_path/', 'some/path/')
    'file:/a_path/'
    >>> check_userinput('DISP_ALLS_00000000.xlsx', 'file.xlsx')
    'DISP_ALLS_00000000.xlsx'
    >>> check_userinput('_en32-2.xlsx', 'file.xlsx')
    '_en32-2.xlsx'
    """
    if (len(userstring) == 0):
        return default_value
    elif (default_value[-1] == '/'):
        return userstring if (\
            bool(re.match(r'[a-zA-Z0-9._:\-/]+[/]$',userstring))) else "NEEDPATH"
    elif (default_value[-5:] == '.xlsx'):
        return userstring if (
            bool(re.match(r'[a-zA-Z0-9_\-]+\.xlsx$',userstring))) else "NEEDFILE"
    else:
        return "MESSED UP"

def get_realdata() -> dict:
    """ using input from user, get actual data from LESO AllStates file"""
    userpath = input('Enter the path to directory where datafiles are located: ')
    userleso = input('Enter the DLA LESO file name to check: ')

    path_datafiles = check_userinput(userpath, default_path_datafiles)
    leso_file = check_userinput(userleso, default_leso_file)
    try:
        data = pd.read_excel(path_datafiles + leso_file, sheet_name=None)
    except FileNotFoundError:
        print('File not found:',path_datafiles + leso_file)
        sys.exit(-1)
    except:
        traceback.print_exc()
        sys.exit(-9999)
    return data


def main():
    test_flag = input('Go live?')
    if test_flag == 'yes':
        transfer_dict = get_realdata()
    else:
        """
        user_list = list(input('Enter a list: '))
        user_set = set(list(input('Enter a set: ')))

        working_list = list(user_list)
        working_set = set(user_set)
        working_state = setstate.state_of_list(working_list,working_set)
        print(working_state)
        print(state_dict[working_state])
        """
        import testdata

        transfer_dict = testdata.get_data()
        postalcodes_dict = {'FL':'Florida','AL':'Alabama','DE':'Delaware'\
                           ,'WV':'West Virginia'}
        # SHEETS 
        # pass 111,112
        # flag, continue 113,114
        # all others fail
        actual_sheets = [sheet for sheet in transfer_dict]
        expected_sheets = set([state for state in postalcodes_dict.values()])
        sheets_state = setstate.state_of_list[actual_sheets,expected_sheets]
        if sheets_state in [112,111]:
            print('Sheets look good.')
        elif sheets_state in [113,114]:
            print('Some unexpected sheets found, but otherwise looks good.')
        else:
            print('Bad sheets, cannot continue.')
        print(sheets_state,state_dict[sheets_state])

        # COLUMNS
        # pass 111
        # all others fail
        actual_columns = [list(columns) for sheet in transfer_dict\
                                           for columns in transfer_dict[sheet].columns]
        






if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
