import pandas as pd
def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # df = pd.merge(project, employee, on='employee_id', how='left')
    # df = df.groupby('project_id').agg({
    #     'employee_id' : 'size',
    #     'experience_years' : 'sum'
    # }).reset_index()
    # df['average_years'] = (df['experience_years']/df['employee_id']).round(2)
    # return df[['project_id', 'average_years']]
    return (
        project.merge(employee, on='employee_id', how='left')
        .groupby('project_id', as_index=False)['experience_years']
        .mean() #or use .agg
        .round({'experience_years': 2})
        .rename(columns={'experience_years': 'average_years'})
    )