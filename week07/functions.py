# Self assessment 1 - I went one by one through the code to try and figure it out myself. Once I found everything I coud and there was still an error I put the code into AI and had it talked to me one line at a time but never give me the answer so I still had to find it out myself. This tells me there is still a bit of work I need to get done when it comes to my debuging skills.  
# Self assessment 2 - You input the price and the tier of discount into the function. It then takes the price matches it with the what tier it is and then applies the discount that matches both inputs.
# I had AI help walk me through the code. It gave me no answers though and I feel like by using it as soley a tool it helped to develope my understanding.
# Exercise 1 # 

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7% is ${tax1:.2f}")
print(f"Tax for $250 at 8% is ${tax2:.2f}")
print(f"Tax for $350 at 5% is ${calculate_tax(350, 0.05):.2f}")

# Exercise 2 #

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3 #

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200,0.07, 'gold'):.2f}")

# Exercise 4 #

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total}")

# Exercise 5 #
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = total + sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6 # 

x = 100

def double_it():
    x = 999
    return x * 2
print(x)
print(double_it())
print(x)