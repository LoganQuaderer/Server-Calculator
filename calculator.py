total_sales = float(input("Enter total sales for tonight: $"))
# Hardcoded percentages
busser_percentage = 0.04  # 4% for bussers
bar_team_percentage = 0.025  # 2.5% for bar team

# Calculate tipouts
busser_tipout = total_sales * busser_percentage
bar_team_tipout = total_sales * bar_team_percentage

# Format and print the results
print(f"You owe the bussers ${busser_tipout:.2f}")
print(f"You owe the bar ${bar_team_tipout:.2f}")
