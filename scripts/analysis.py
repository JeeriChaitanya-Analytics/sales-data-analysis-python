import matplotlib.pyplot as plt

def get_top_customers(df):
    return df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False).head(5)


def get_top_products(df):
    return df.groupby('product_name')['revenue'].sum().sort_values(ascending=False).head(5)


def get_top_cities(df):
    return df.groupby('city')['revenue'].sum().sort_values(ascending=False).head(5)


def get_monthly_revenue(df):
    return df.groupby('month_name')['revenue'].sum().sort_values(ascending=False)

def plot_monthly_revenue(df):
    revenue = df.groupby(['month', 'month_name'])['revenue'].sum().sort_index()
    
    revenue = revenue.reset_index()

    plt.bar(revenue['month_name'], revenue['revenue'])
    
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    
    plt.show()