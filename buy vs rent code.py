import pandas as pd

p = 7000000  # Principal amount
r = 10.25 / 1200  # Monthly interest rate
t = 240  # Total number of months (loan tenure)
emil = []  # List to store EMIs
intl = []  # List to store interests

for i in range(1, t + 1):
    emi = (p * r * (1 + r) ** t) / ((1 + r) ** t - 1)  # Calculation of EMI
    emil.append(emi)
    interest = p * r  # Calculation of interest for each month
    intl.append(interest)
    if i % 3 == 0:
        r = r + 0.049 / 1200  # Incrementing interest rate every three months

# Creating a DataFrame to store EMIs and interests
df = pd.DataFrame({'emi': emil, 'interest': intl})

# Printing the total sum of EMIs
total_sum_of_emis = df['emi'].sum()
print("Total sum of EMIs:", total_sum_of_emis)

# Additional logic to determine whether to buy or rent
property_price = 7000000  # Example property price
rental_rate = 35000  # Example monthly rental rate
years_to_compare = 5  # Number of years to compare buying vs. renting

# Calculate total cost of buying
down_payment_percentage = 0.2  # Example down payment percentage
mortgage_interest_rate = 0.05  # Example mortgage interest rate
loan_tenure_years = 20  # Example loan tenure in years

down_payment = property_price * down_payment_percentage
loan_amount = property_price - down_payment
monthly_interest_rate = mortgage_interest_rate / 12
total_payments = loan_tenure_years * 12
monthly_mortgage_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_payments)
total_cost_of_buying = down_payment + (monthly_mortgage_payment * total_payments)

# Calculate total cost of renting
total_cost_of_renting = rental_rate * 12 * years_to_compare

# Determine whether it's more beneficial to buy or rent
decision = 'buy' if total_cost_of_buying < total_cost_of_renting else 'rent'

# Print the decision and total costs
print(f"\nIt is more financially beneficial to {decision}.\n")
print(f"Total cost of buying over {years_to_compare} years: ${total_cost_of_buying:,.2f}")
print(f"Total cost of renting over {years_to_compare} years: ${total_cost_of_renting:,.2f}")
