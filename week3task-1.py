  # Shopping Discount

total_purchase = float(input("Enter the total purchase amount: "))

if total_purchase >= 500000:
    discount = 0.20 * total_purchase
elif total_purchase >= 250000:
    discount = 0.10 * total_purchase
else:
    discount = 0

final_amount = total_purchase - discount

print(f"Discount amount: {discount}")
print(f"Final amount to be paid: {final_amount}")