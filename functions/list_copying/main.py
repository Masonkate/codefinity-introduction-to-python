# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices


def apply_discount(prices):
    prices_copy = product_prices.copy()
    for item in range(len(prices_copy)):
        if prices_copy[item] > 2.00:
            prices_copy[item] -= prices_copy[item]*0.1
            
    return prices_copy

updated_prices = apply_discount(product_prices)

print(f"Updated product prices: ${updated_prices}")