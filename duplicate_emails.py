import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    #used pandas duplicated() method to find all duplicate emails
    person = person[person['email'].duplicated()]
    #used drop_duplicates() method to keep 1duplicate amoung the duplicate
    duplicated_drop = person[['email']].drop_duplicates()
    #renaming the email to Email
    change_name = duplicated_drop[['email']].rename(columns={'email': 'Email'})
    return change_name
    