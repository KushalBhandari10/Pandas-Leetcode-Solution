import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    #Used Map filtering to find corresponding manager salary
    employee['manager_salary'] = employee['managerId'].map(employee.set_index('id')['salary'])
    #used boolean filtering to check salary is greater or not
    result = employee[employee['salary'] > employee['manager_salary']]
    return result[['name']].rename(columns={'name': 'Employee'})