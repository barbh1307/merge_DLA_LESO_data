import pandas as pd
import re
import sys, traceback

# DEFAULTS and customizations
default_path_datafiles = 'gs://dla_leso_quarterly_data/OriginalData/'
default_leso_file = 'TESTB_AllStatesAndTerritories_03312020.xlsx'
#PROD default_leso_file = 'DISP_AllStatesAndTerritories_03312020.xlsx'

# EXPECTED 
# load expected state and territory names and abbreviations
# set up expected the data dictionary key: abbreviation value: name
# load postal codes from file name,abbreviation
path_supportfiles = 'gs://dla_leso_quarterly_data/OriginalData/'
#PROD postal_file = '20200712_StateAbbreviations.txt'
 #try:
 #    postalcodes_dict = pd.read_csv(
 #        path_supportfiles + postal_file, header=None, quotechar = "'").\
 #        set_index([1])[0].to_dict()
 #except FileNotFoundError:
 #    print("Error: postal file missing:",path_supportfiles + postal_file)
 #except:
 #    print("Unexpected error A:", sys.exc_info()[0])

# ALL EXPECTED VALUES for DISP_AllStatesAndTerritories_mmddyyyy.xlsx

# use state/territory names in postal file for expected_allstates_sheets
#PROD expected_sheets = [state_name for state_name in postalcodes_dict.values()]
#TEST expected_sheets = set(['Washington','Florida','Georgia','West Virginia','Delaware'])

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
    'NEED FILE'
    >>> check_userinput('', 'file.txt')
    'NEED FILE'
    >>> check_userinput('file:/a_path/', 'some/path/')
    'file:/a_path/'
    >>> check_userinput('DISP_AllS_00000000.xlsx', 'file.xlsx')
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


def is_nonempty(a_list: list) -> int:
    """ Returns 1 if a_list is non-empty, 0 if it is empty.
    >>> is_nonempty([])
    0
    >>> is_nonempty([1])
    1
    """
    return 1 if a_list else 0


def is_disjoint(a_set: set, b_set: set) -> int:
    """ Given non-empty sets, returns 1 if a_set is disjoint from b_set.
    >>> is_disjoint({1},{1})
    0
    >>> is_disjoint({1},{2})
    1
    >>> is_disjoint({1,2},{1})
    0
    >>> is_disjoint({1},{1,2})
    0
    >>> is_disjoint({1,2},{2,3})
    0
    """
    return 1 if (a_set.isdisjoint(b_set)) else 0


def is_superset(a_set: set, b_set: set) -> int:
    """ Given non-empty sets, returns 1 if a_set is a proper superset of b_set.
    >>> is_superset({1},{1})
    0
    >>> is_superset({1},{2})
    0
    >>> is_superset({1,2},{1})
    1
    >>> is_superset({1},{1,2})
    0
    >>> is_superset({1,2},{2,3})
    0
    """
    return 1 if (a_set) > (b_set) else 0


def is_subset(a_set: set, b_set: set) -> int:
    """ Given non-empty sets, returns 1 if a_set is a proper subset of b_set.
    >>> is_subset({1},{1})
    0
    >>> is_subset({1},{2})
    0
    >>> is_subset({1,2},{1})
    0
    >>> is_subset({1},{1,2})
    1
    >>> is_subset({1,2},{2,3})
    0
    """
    return 1 if (a_set) < (b_set) else 0


def is_equal(a_set: set, b_set: set) -> int:
    """ Given non-empty sets, returns 1 if a_set is equal to b_set
    >>> is_equal({1},{1})
    1
    >>> is_equal({1},{2})
    0
    >>> is_equal({1,2},{1})
    0
    >>> is_equal({1},{1,2})
    0
    >>> is_equal({1,2},{2,3})
    0
    """
    return 1 if (a_set) == (b_set) else 0
        

def split_uniqueness(a_list: list):
    """ Splits a_list into a set, a set of non-duplicates and a set of duplicates
    >>> split_uniqueness([1])
    ({1}, {1}, set())
    >>> split_uniqueness([1,1])
    ({1}, set(), {1})
    >>> split_uniqueness([1,1,2])
    ({1, 2}, {2}, {1})
    """
    set_alist = set(a_list)
    #NOTE: this could be done with pandas Series  a_series[a_series.duplicated()]
    track_duplicates = a_list.copy()
    for val in set_alist:
        track_duplicates.remove(val)
    set_duplicates = set(track_duplicates)
    set_noduplicates = set_alist.difference(set_duplicates)
    return set_alist, set_noduplicates, set_duplicates


def state_unique(noduplicates: set, duplicates: set) -> int:
    """ Returns 0 if all are duplicates, 1 if no duplicates, 2 if some duplicates
    >>> state_unique({1},{2})
    2
    >>> state_unique({1},{})
    1
    >>> state_unique({},{1})
    0
    """
    if (is_nonempty(noduplicates) == 1):
        state = (is_nonempty(duplicates) + 1)
    else:
        state = 0
    return state


def state_expected(actual: set,expected: set) -> int:
    """ Returns int for whether set has missing or unexpected values
    >>> state_expected({2},{1})
    0
    >>> state_expected({1},{1})
    1
    >>> state_expected({1},{1,2})
    2
    >>> state_expected({2,3},{1,2})
    3
    >>> state_expected({1,2},{1})
    4
    """
    if (is_equal(actual,expected) == 1):
        state = 1
    elif (is_subset(actual,expected) == 1):
        state = 1 + 1
    elif (is_disjoint(actual,expected) == 0):
        state = (is_subset(expected,actual) + 3)
    else:
        state = 1 - 1
    return state


# MAIN

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
              124:'Some unexpected values, and some are unique.'}

userpath = input('Enter the path to directory where datafiles are located: ')
userleso = input('Enter the DLA LESO file name to check: ')

path_datafiles = check_userinput(userpath, default_path_datafiles)
leso_file = check_userinput(userleso, default_leso_file)
try:
    transfer_dict = pd.read_excel(path_datafiles + leso_file, sheet_name=None)
except FileNotFoundError:
    print('File not found:',path_datafiles + leso_file)
    sys.exit(-1)
except:
    traceback.print_exc()
    sys.exit(-9999)

print('CHECKING',leso_file,'FOR EXPECTED VALUES')

# SHEETS
print('Sheets:')
#TEST actual_list = [[],[1],[2],[1,2],[2,3],[1,1],[1,1,2],[1,2,2],[2,2,3],[2,3,3]]
#TEST expected_list = [set([1]),set([1,2])]
for expected_sheets in expected_list:
    for actual_sheets in actual_list:
        sheets_unique, sheets_noduplicates, sheets_duplicates = set(),set(),set()
        #PROD actual_sheets = [sheet for sheet in transfer_dict]
        
        # Q1 are there sheets in the file? yes continue, no fall out
        state_of_sheets = is_nonempty(actual_sheets) * 100
        if state_of_sheets > 0:
            #actual_sheets = [sheet for sheet in transfer_dict]
            sheets_unique, sheets_noduplicates, sheets_duplicates = split_uniqueness(actual_sheets)
            # Q2 are the sheet names unique?
            state_of_sheets = state_of_sheets + (state_unique(sheets_noduplicates,sheets_duplicates) * 10)

            # Q3 ignoring duplicates, are there any unexpected sheets/state names?
            state_of_sheets = state_of_sheets + (state_expected(sheets_unique,expected_sheets) * 1)
        
        print('Sheets have a state',state_of_sheets,'\n',state_dict[state_of_sheets])
        print(expected_sheets,actual_sheets\
              ,'\t',sheets_unique,sheets_noduplicates,sheets_duplicates)

# COLUMNS

#STOP


# 6 set machine, all sets optional
print('done')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
