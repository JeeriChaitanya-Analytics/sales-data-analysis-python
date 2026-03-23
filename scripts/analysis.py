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

def plot_top_products(df):
    top_products = df.groupby('product_name')['revenue'].sum().sort_values(ascending=False).head(5)
    
    top_products.plot(kind='bar')
    plt.title("Top 5 Products by Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.show()


def plot_top_customers(df):
    top_customers = df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False).head(5)
    
    top_customers.plot(kind='bar')
    plt.title("Top 5 Customers by Revenue")
    plt.xlabel("Customer")
    plt.ylabel("Revenue")
    plt.show()


def plot_city_revenue(df):
    city_revenue = df.groupby('city')['revenue'].sum().sort_values(ascending=False).head(5)
    
    city_revenue.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Revenue Distribution by City")
    plt.ylabel('')
    plt.show()    