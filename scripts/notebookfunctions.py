"""Useful fuctions for analyzing discrepancies in transfers data."""

import pandas as pd


def get_unique_values(a_dict: dict, col: str) -> list:
    '''Given a dictionary of dataframes, returns a list of the unique values
       in the given column across all dataframes.'''
    unique_values_list = []
    for dict_key in a_dict:
        unique_values_list += list(a_dict[dict_key][col].unique())
    return unique_values_list


def get_unexpected_values(to_check: set, expect: set) -> set:
    '''Returns a set of unexpected values, empty if none found.'''
    return to_check.difference(expect)


def make_dataframe(a_thing, a_col: str) -> pd.DataFrame:
    """ Return dataframe with only transfers, shipments or cancellations.
        Requires a_col contain datetime data.
        Requires a_thing to have a column called 'State'
    """
    if isinstance(a_thing, dict):
        a_df = pd.concat([pd.concat([v], ignore_index=True)
                         for k, v in a_thing.items()], ignore_index=True)
    else:
        a_df = a_thing
    a_df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    col_types = {'State': 'category'}
    a_df = a_df.astype(col_types)
    a_df.index = a_df[a_col]
    a_df.index = a_df.index.normalize()
    a_df.index.name = 'Date'
    return a_df


def count_by_time(period: str, start_period: str, end_period: str,
                  *dfs) -> pd.DataFrame:
    """ Returns a dataframe with number of different agencies in a given
        time period. Requires column 'Station Name (LEA).'
    """
    df_list = []
    for a_df in dfs:
        df_list.append(a_df.loc[start_period:end_period]
                           .groupby(pd.Grouper(
                                       freq=period))['Station Name (LEA)']
                           .count().rename(a_df.name))
    return pd.concat(df_list, axis=1).fillna(0).astype(int)


def differences_by_time(period: str, start_period: str, end_period: str,
                        frame1: pd.DataFrame,
                        frame2: pd.DataFrame) -> pd.DataFrame:
    """ Returns a single dataframe with only rows where column counts between
        two dataframes are different. Requires column 'State.'
    """
    count_frame1 = frame1.loc[start_period:end_period]\
                         .groupby(pd.Grouper(freq=period))['State'].count()
    count_frame2 = frame2.loc[start_period:end_period]\
                         .groupby(pd.Grouper(freq=period))['State'].count()
    counts_df = pd.DataFrame({'count1': count_frame1,
                              'count2': count_frame2},
                             index=count_frame2.index).fillna(0).astype(int)
    return counts_df[(counts_df['count1'] != counts_df['count2'])]


def split_demilcodes(a_df: pd.DataFrame) -> [pd.DataFrame, pd.DataFrame]:
    """split the dataframe into controlled and noncontrolled records
       excluding code 'Q'
    """
    allQ = a_df[a_df['DEMIL Code'].isin(['Q'])]
    ncQ = allQ[allQ['DEMIL IC'] != 3]
    cQ = allQ[allQ['DEMIL IC'] == 3]
    noncontrolled = a_df[a_df['DEMIL Code'].isin(['A'])]
    controlled = a_df[a_df['DEMIL Code'].isin(['B', 'C', 'D', 'E', 'F', 'G'])]
    return [controlled.append(cQ), noncontrolled.append(ncQ)]
