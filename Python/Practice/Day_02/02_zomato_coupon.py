# Need to write python code to categorize users and send coupon based on order history

# Step 1 - Get order history
total_orders = int(input("Enter total number of orders: "))

# Step 2 - Categorize user based on order history
if total_orders >= 20:
    category = "Gold"
    coupon = "GOLD20"
elif total_orders >= 10:
    category = "Silver"
    coupon = "SILVER10"
else:
    category = "Bronze"
    coupon = "BRONZE5"

# Step 3 - Send coupon based on category
print("\nCoupon sent successfully!")

# Step 4 - Display coupon code
print("User Category:", category)
print("Coupon Code:", coupon)