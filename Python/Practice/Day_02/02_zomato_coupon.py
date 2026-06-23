# Need to write python code to categorize users and send coupon based on order history

# Step 1 - Get order history
user_name = input("Enter your name: ")
total_orders = int(input("Enter total number of orders: "))

# Step 2 - Categorize user based on order history
if total_orders < 0:
    category = "Invalid"
    coupon = "No Coupon"
elif total_orders == 0:
    category = "New User"
    coupon = "WELCOME10"
elif total_orders <= 29:
    category = "Silver"
    coupon = "SILVER5"
elif total_orders <= 59:
    category = "Gold"
    coupon = "GOLD10"
else:
    category = "Platinum"
    coupon = "PLATINUM15"
    
# Step 3 - Send coupon based on category
print("\nCoupon sent successfully!")

# Step 4 - Display coupon code
print("Username: ",user_name,"|| User Category:",category,"|| Coupon Code:",coupon)