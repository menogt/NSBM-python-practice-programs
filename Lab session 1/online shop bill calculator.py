total = 0
for i in range(1,5):
    price = float(input("Enter the price of the product: "))
    total = float(total+price)

delivery_charges = float(input("Enter the amount of Delivery Charges: "))
discount = float(input("Enter the discount percentage: "))
product_total = total - (total*(discount/100))
final_bill = product_total + delivery_charges
print("Product total is", product_total)
print("Final Bill is ", final_bill)
