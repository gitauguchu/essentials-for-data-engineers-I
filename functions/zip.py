def combine_sales_data(products, sales):
    return list(zip(products, sales))

print(combine_sales_data(['Laptop', 'Mouse', 'Keyboard'], [150, 200, 300]))