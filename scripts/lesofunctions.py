"""Useful fuctions for analyzing discrepancies in transfers data."""

import pandas as pd


def make_transfers_dataframe(a_dict: dict) -> pd.DataFrame:
    """ Return dataframe of all values in transfers dictionary."""
    a_df = pd.concat([pd.concat([v], ignore_index=True)
                      for k, v in a_dict.items()], ignore_index=True)\
             .apply(lambda x: x.str.strip() if x.dtype == 'object' else x)
    col_types = {'State': 'category'}
    a_df = a_df.astype(col_types)
    a_df.index = a_df['Ship Date']
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
