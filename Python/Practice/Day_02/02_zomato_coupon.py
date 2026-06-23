# Need to write python code to categorize users and send coupon based on order history

# Step 1 - Get order history
user_name = input("Enter your name: ")
total_orders = int(input("Enter total number of orders: "))

# Step 2 - Categorize user based on order history
if total_orders >= 10:
    category = "Gold"
    coupon = "GOLD10"
elif total_orders >= 5:
    category = "Silver"
    coupon = "SILVER5"
else:
    category = "New User"
    coupon = "WELCOME10"

# Step 3 - Send coupon based on category
print("\nCoupon sent successfully!")

# Step 4 - Display coupon code
print("Username: ",user_name,"|| User Category:",category,"|| Coupon Code:",coupon)