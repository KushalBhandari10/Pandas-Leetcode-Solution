import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.loc[lambda x : (x['referee_id'] != 2) | (x['referee_id'].isnull()),['name']]
    