
def poverty_ratio(household_income, num_in_hh):
    poverty_ratio = household_income / 8340 + (num_in_hh * 4540)
    return poverty_ratio
household_income = float(input(“Enter the total income: “))
num_in_hh = float(input(“Enter the number of people in the household: “))
try:
    poverty_ratio = poverty_ratio(household_income, num_in_hh)
    print(f”The poverty ratio is {poverty_ratio}“)
except Exception as e:
    print(e.message)


def to_int(input):
    return int(input, 10)

age = input("Enter age: ")
age_value = to_int(age)
print(f"The integer value is: {age_value}")

weight = input("Enter weight in pounds: ")
weight_value = to_int(weight)
print(f"The integer value is: {weight_value})