import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby('num').size().reset_index(name='count')
    df = df[df['count'] == 1]
    if df.empty:
        return pd.DataFrame({'num': [pd.NA]})
    max = df['num'].max()
    return pd.DataFrame({'num': [max]})