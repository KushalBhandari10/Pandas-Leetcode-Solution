import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (
        courses.pipe(lambda df : df.value_counts('class'))
        .loc[lambda d: d >= 5]
        .reset_index()[['class']]
    )