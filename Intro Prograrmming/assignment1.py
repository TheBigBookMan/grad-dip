
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

# serving_size = float(input("What is the serving size in grams? "))
# grams_fat = float(input("How many grams of fat in a serving? "))
# grams_carbs = float(input("How many grams of carbohydrates in a serving? "))
# grams_protein = float(input("How many grams of protein in a serving? "))

# FATS_CALS_PER_GRAM = 9
# CARBS_CALS_PER_GRAM = 4
# PROTEINS_CALS_PER_GRAM = 4

# total_fat = grams_fat * FATS_CALS_PER_GRAM
# total_carbs = grams_carbs * CARBS_CALS_PER_GRAM
# total_protein = grams_protein * PROTEINS_CALS_PER_GRAM

# total_cals = total_fat + total_carbs + total_protein
# cals_per_100_grams = (total_cals / serving_size) * 100
# print(cals_per_100_grams)


# Task 4
# initial_deposit = float(input("What is the initial deposit amount? "))
# interest_rate = float(input("What is the interest rate? "))
# term_length = int(input("What is the term length in years? "))

# final_amount = 0

# if term_length == 0:
#     final_amount = initial_deposit
# else:
#     compound_price = initial_deposit
#     for i in range(term_length):
#         compound_price = compound_price + (compound_price * (interest_rate / 100))

#     final_amount = compound_price

# print(f"Deposit amount ($): {initial_deposit}")
# print(f"Interest rate (%): {interest_rate}")
# print(f"Years invested: {term_length}")
# print(f"Balance after {term_length} years: ${final_amount}")


# Task 5
# Part A

# device_total_battery_capacity = 0

# while True:
#     device_capacity = float(input("What is the device capacity? "))
#     device_total_battery_capacity = device_total_battery_capacity + device_capacity

#     more_devices = input("Do you have more devices? ")

#     if more_devices == "n":
#         break

# SMALL_MAH = 3000
# MEDIUM_MAH = 10000
# LARGE_MAH = 20000

# powerbank_recommend = ''

# if device_total_battery_capacity <= SMALL_MAH:
#     powerbank_recommend = "Small MAH"
# elif device_total_battery_capacity <= MEDIUM_MAH:
#     powerbank_recommend = "Medium MAH"
# else:
#     powerbank_recommend = "Large MAH"

# print(f"Total requirement: {device_total_battery_capacity} mAH")
# print(f"Recommended powerbank: {powerbank_recommend}")