import pandas as pd
import numpy as np

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    # triangle['triangle'] = (
    #     (triangle['x'] + triangle['y'] > triangle['z']) &
    #     (triangle['y'] + triangle['z'] > triangle['x']) &
    #     (triangle['x'] + triangle['z'] > triangle['y'])
    # ).map({True: 'Yes', False: 'No'})
    cond = (
        (triangle['x'] + triangle['y'] > triangle['z']) &
        (triangle['y'] + triangle['z'] > triangle['x']) &
        (triangle['x'] + triangle['z'] > triangle['y'])
    )
    triangle['triangle'] = np.where(cond, 'Yes', 'No')
    return triangle