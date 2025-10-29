import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema.loc[(cinema['id'] % 2 != 0) & ~(cinema['description'].str.startswith('b'))].sort_values(by='rating', ascending= False)
    