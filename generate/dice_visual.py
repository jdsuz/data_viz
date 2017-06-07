import pygal

from die import Die

# Create two D8 dice.
die_1 = Die(8)
die_2 = Die(8)

# Testing system limits with the number of rolls
rolls = int(raw_input("How many rolls (Enter an integer)? "))

# Make some rolls, and store results in a list.
# Ex.15-6 List Comprehension
results = [die_1.roll() + die_2.roll() for roll_num in range(rolls)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8s 1000 times."
hist.x_labels = [x for x in range(2, max_result+1)]         # Ex.15-6
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D'+ str(die_1.num_sides) + '+ D'+ str(die_2.num_sides), frequencies)
hist.render_to_file('dice_visual.svg')
