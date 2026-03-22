import pandas as pd

def transform_data(df):
    df['order_date'] = pd.to_datetime(df['order_date'],dayfirst = True,errors='coerce')
    df['revenue'] = df['price'] * df['quantity']
    df['month'] = df['order_date'].dt.month
    df['month_name'] = df['order_date'].dt.month_name()

    return df

