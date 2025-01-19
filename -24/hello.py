print('Hello, world!')

a = 32
b = 44
if a < b:
    print("Es mayor")
fact = "The Moon has no atmosphere."
fact + "No sound can be heard on the Moon."
print(fact)
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print(planets)
print("There are", len(planets), "planets")


# # Create the variable for user input
# user_input = ''
# # Create the list to store the values
# inputs = []

# # The while loop
# while user_input.lower() != 'done':
#     # Check if there's a value in user_input
#     if user_input:
#         # Store the value in the list
#         inputs.append(user_input)
#     # Prompt for a new value
#     user_input = input('Enter a new value, or done when done')

# print(inputs)

new_planet = ''
list_planet = []

while len(list_planet) != 7:
    if new_planet:
        list_planet.append(new_planet)
    new_planet = input('Cual son los planetas 8M = ')
