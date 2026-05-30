# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


def calculate_revenue(price_list, quantity_sold_list):
    revenue = [0] * len(price_list)
    for i in range(len(price_list)):
        revenue[i] = price_list[i] * quantity_sold_list[i]
    return revenue

def formatted_output(revenue_list):
    revenue_per_product = list(zip(products, revenue_list))
    revenue_per_product.sort()
    return revenue_per_product



# Example of expected output line (do not remove):
revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = formatted_output(revenues)
print(revenue_per_product)  
for name, rev in revenue_per_product:
    print(f"{name} has total revenue of ${rev}")
