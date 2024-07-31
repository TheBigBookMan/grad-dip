
# Task1
# user_weight = float(input("What is your weight in kg? "))
# other_planet = input("What is the name of the other planet? ")

# EARTH_GRAVITY = 9.81
# planets_gravity = 0

# if other_planet == 'Sun':
#     planets_gravity = 274.13
# elif other_planet == 'Mercury':
#     planets_gravity = 3.59
# elif other_planet == "Earth's Moon":
#     planets_gravity = 1.62
# elif other_planet == "Mars":
#     planets_gravity = 3.77
# elif other_planet == "Pluto":
#     planets_gravity = 0.42

# weight_of_object = (user_weight / EARTH_GRAVITY) * planets_gravity

# print(f"Your weight on Earth (kg): {user_weight}")
# print(f"Other planets gravity (m/s^2): {planets_gravity}")
# print(f"On the other planet, you would weigh: {weight_of_object} kg")


# Task2
# user_height = float(input("How tall are you in metres? "))
# user_weight = float(input("What is your weight in kg? "))
# avg_hours_exercising = float(input("What's the average number of hours you exercise per week? "))

# bmi = user_weight / (user_height ** 2)

# print(f"Height (m): {user_height}")
# print(f"Weight (kg): {user_weight}")
# print(f"Average weekly activity (hours): {avg_hours_exercising}")

# if (bmi >= 25 and avg_hours_exercising < 3) or (bmi >= 30):
#     print("High diabetes risk")
# else:
#     print("Normal diabetes risk")


# Task 3
# TODO test on real food??? i dunno
# !!! need to test though
# serving_size = float(input("What is the serving size in grams? "))
# grams_fat = float(input("How many grams of fat in a serving? "))
# grams_carbs = float(input("How many grams of carbohydrates in a serving? "))
# grams_protein = float(input("How many grams of protein in a serving? "))

# FATS_CALS_PER_GRAM = 9
# CARBS_CALS_PER_GRAM = 4
# PROTEINS_CALS_PER_GRAM = 4

# total_fat = ((serving_size * grams_fat) / 100) * FATS_CALS_PER_GRAM
# total_carbs = ((serving_size * grams_carbs) / 100) * CARBS_CALS_PER_GRAM
# total_protein = ((serving_size * grams_protein) / 100) * PROTEINS_CALS_PER_GRAM

# total_cals = total_fat + total_carbs + total_protein
# print(total_cals)


# Task 4
# !!! NEED TO ADD IN PROPER PRINT STATEMENT
initial_deposit = float(input("What is the initial deposit amount? "))
interest_rate = float(input("What is the interest rate? "))
term_length = int(input("What is the term length in years? "))

# For loop iterating the compounding interest
if term_length == 0:
    print(initial_deposit)
else:
    for i in range(term_length):
        initial_deposit = initial_deposit + (initial_deposit * (interest_rate / 100))
        print(initial_deposit)

