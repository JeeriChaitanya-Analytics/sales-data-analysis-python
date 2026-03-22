from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.analysis import get_top_customers, get_top_products, get_top_cities, get_monthly_revenue
from scripts.analysis import plot_monthly_revenue

def main():
    # Extract
    df = extract_data("data/data_analytics_orders_2000_rows.csv")
    
    # Transform
    df = transform_data(df)
    
    # Analysis
    print("Top Customers:\n", get_top_customers(df))
    print("\nTop Products:\n", get_top_products(df))
    print("\nTop Cities:\n", get_top_cities(df))
    print("\nMonthly Revenue:\n", get_monthly_revenue(df))

    plot_monthly_revenue(df)


if __name__ == "__main__":
    main()