import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return (
        orders.groupby('customer_number').size()
        .reset_index(name='order_count')
        .loc[lambda df: df['order_count'] == df['order_count'].max()]
    )[['customer_number']]