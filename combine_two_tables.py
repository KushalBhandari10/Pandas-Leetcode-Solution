import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    #Used inner join to join two tables
    result = pd.merge(person, address, on='personId', how='left')
    #used boolean filtering to filter require columns
    result = result[['firstName', 'lastName', 'city', 'state']]
    return result
    