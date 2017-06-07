# Ex.15-8 Three D6 Die
import pygal

from die import Die

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Testing system limits with the number of rolls
rolls = int(raw_input("How many rolls (Enter an integer)? "))

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(rolls)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6s" + str(rolls) + "times."
hist.x_labels = [x for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_die.svg')
