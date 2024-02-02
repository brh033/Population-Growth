##########################################################################
# name: Blaine Hord
# date: 10/28/2023
# description: A program that calculates population growth over a given time
#########################################################################
# A function that prints out the introduction to the program. It doesn't
# take any arguments and does not return any results.
def intro():
  print("This program will compare the populations of two different countries over time")
# A function that prompts the user for the name of the country. It takes
# in a number that is used in the prompt as an argument. It then returns
# the name of the country.
def countries(country):
  country = input(f"Please enter the name of Country #{country}: ")
  return country
# A function that prompts the user for the current population of a
# country. It takes the name of the country as an argument, and then
# returns the resulting population. The function also carries out range
# checking to make sure the value inputed by the user is valid (i.e. not
# negative)
def population(country):
  country_population = int(input(f"What is the current population of {country}? "))
  if country_population < 0:
    print("That doesn't seem right. Please enter a positive number")
    country_population = int(input(f"What is the current population of {country}? "))
  return country_population
# A function that prompts the user for the population growth rate of a
# country. It takes in the name of the country as an argument and then
# returns a value growth rate. It also carries out range checking to
# make sure that the result is not an unrealistic growth rate i.e. rate
# should be between -5 and 10 inclusive.
def popGrowth(country):
  country_growth = float(input(f"What is the annual population growth rate of {country}? "))
  if country_growth < -5 or country_growth > 10:
    print("That doesn't seem right. Please enter a value in the range [-5,10]")
    country_growth = float(input(f"What is the annual population growth rate of {country}? "))
  return country_growth
# A function that prompts the user for the number of years to show in
# the resulting table. The function doesn't take any arguments but
# returns a result. It is also in charge of range checking to make sure
# that the number of years is not less than 1.
def years():
  numyears = int(input("How many years of comparison should the table show? "))
  if numyears < 1:
    print("That doesn't seem right. Please enter a value >= 1")
    numyears = int(input("How many years of comparison should the table show? "))
  return numyears
# A function that prompts the user for the duration of the interval in
# the table i.e. how many years between each successive row of the
# resulting table. It doesn't take any arguments and does range checking
# to make sure that the user doesn't enter a value less than 1.
def interval():
  interval = int(input("How many years should the intervals be? "))
  if interval < 1:
    print("That doesn't seem right. Please enter a value >= 1")
    interval = int(input("How many years should the intervals be? "))
  return interval
# A function that calculates the population given an intial population,
# a growth rate, and the time. It takes 3 arguments (population, growth
# rate and time) and returns the resulting population.
def population_calc(population, popGrowth, numyears):
  finalPop = population * ((1 + (popGrowth/100)) ** numyears)
  return finalPop
# A functiont to print out the header of the table. It takes two
# arguments i.e. the country names, and then prints out the formatting
# lines as well as the first row seen at the top of the table.
def header(country1, country2):
  print("--------------------------------------------------")
  print(f"Years          {country1}          {country2}")
  print("--------------------------------------------------")
# A function to print out the rest of the table row by row. It receives
# 6 arguments: both country populations, both country rates, the
# duration of the analysis and the interval between each row. It then
# relies on calculate population function to calculate the population
# values for each row and print them out in order.
def table(country1_population, country2_population, country1_growth, country2_growth, time, interval):
  counter = 0
  print(f"{counter}                 {country1_population:,}                {country2_population:,}")
  while counter < time:
    counter += interval
    print(f"{counter}                {int(population_calc(country1_population, country1_growth, counter)):,}                {int(population_calc(country2_population, country2_growth, counter)):,}")
############### MAIN ##################################
# print the introduction
intro()
# Get the country names
country_1 = countries(1)
country_2 = countries(2)
# Get the country initial populations
pop_1 = population(country_1)
pop_2 = population(country_2)
# get the country population growth rates
growth_1 = popGrowth(country_1)
growth_2 = popGrowth(country_2)
# get the analysis detais e.g. the duration and the interval
time = years()
interval_ = interval()
# Print out the table
header(country_1, country_2)
table(pop_1, pop_2, growth_1, growth_2, time, interval_)