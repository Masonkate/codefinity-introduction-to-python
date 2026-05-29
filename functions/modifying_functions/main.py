def apply_discount(price, discount=0.05):
    price -= price*discount 
    return price 

def apply_tax(price, tax=0.07):
    price += price*tax
    return price

def calculate_total(price, discount=0.05, tax=0.07):
    add_tax = apply_tax(price, tax)
    total_price = apply_discount(add_tax, discount) 
    return total_price

total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, 0.1, 0.08)
print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")
#def test(value=120, variable1="Var1", variable2="Var2", variable3="Var3"):
    #variable1 = apply_discount(value)
    #variable2 = apply_tax(value)
    #variable3 = calculate_total(value)
    #return variable1, variable2, variable3

#print(f"{test()}")