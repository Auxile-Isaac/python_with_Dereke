# ask the investment
investment = eval(input("Enter your investment: "))
# ask the expected interest
interest = eval(input("Enter your expected interest: "))

# calcurate and print investment + interest after 10 years
for i in range(10):
    investment = investment + (investment * interest / 100)

print(f"investment after 10 years: {investment :.2f}")
