import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Convert to datetime
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    
    # Sort by date
    
    weather = weather.sort_values('recordDate')
    
    # Compute previous temperature
    weather['prev_temp'] = weather['temperature'].shift(1)
    #Previous day
    weather['prev_day'] = weather['recordDate'].shift(1)
    weather['diff_day'] = (weather['recordDate'] - weather['prev_day']).dt.days
    
    # Select rows where temperature rises
    rising = weather[(weather['diff_day'] == 1) & (weather['temperature'] > weather['prev_temp'])]
    
    # Keep only Id column
    return rising.rename(columns={'id':'Id'})[['Id']]
