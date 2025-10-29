import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[['name', 'population', 'area']].query('area >= 3000000 or population >= 25000000')