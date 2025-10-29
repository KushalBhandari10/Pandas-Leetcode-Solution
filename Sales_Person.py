import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # red_ids = company.query('name == "RED"')['com_id']
    # red_sales = orders.query('com_id in @red_ids')['sales_id']
    # return sales_person.query('sales_id not in @red_sales')[['name']]
    red_ids = company.loc[company['name'] == 'RED', 'com_id']
    red_sales = orders.loc[orders['com_id'].isin(red_ids), 'sales_id'].unique()
    return sales_person.loc[~sales_person['sales_id'].isin(red_sales), ['name']]