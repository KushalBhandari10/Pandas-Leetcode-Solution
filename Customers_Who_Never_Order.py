import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    unique_frame = orders['customerId']
    result = customers[~(customers['id'].isin(unique_frame))][['name']]
    return result.rename(columns={'name': 'Customers'})