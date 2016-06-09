#Kate Bennion
#Grade: 11/15
5/25/2016
#Homework 2
#LISTS
numbers = [ 22, 90, 0, -10, 3, 22, 48 ]
print(len(numbers))
print(numbers[3])
print(numbers[3] + numbers[1])
print(max(n for n in numbers if n!=max(numbers)))
#TA-STEPHAN: Nice way to get the second max number!
print(numbers[-1])

#TA-STEPHAN: 3 numbers produced the wrong results. Instead of using multiple
#elifs that make up for every possible combination, you can use multiple if
#statements. I'll include one way to run through the loop. Please email me with
# any questions.
print("____________")
for number in numbers:
    if number < 10 and number % 2 != 0:
        print((number * 30) - 1)
    elif number < 10 and number % 2 ==0 and number != -10:
        print((number * 30) + 6 - 1)
    elif number < 10 and number % 2 ==0 and number == -10:
        print((number * 30) + 6)
    elif number > 50 and number % 2 ==0:
        print((number - 10 + 6)-1)
    elif number < 50 and number % 2 ==0 and number != -10:
        print((number + 6)-1)
    else:
        print(number - 1)
print("____________")

#TA-STEPHAN: Here's an example of a for loop you can run to get the correct answers.
#for number in numbers:
#    original = number
#    if original > 50:
#        number = number - 10
#    if original < 10:
#        number = number * 30
#        if original % 2 == 0:
#            number = number + 6
#    if original > -10:
#        number = number - 1
#    print(number)


print((sum(numbers))/2)

#DICTIONARIES
movie = {'title': 'Star Wars', 'year': '1977', 'director': 'George Lucas', 'budget': 180, 'revenue': 1000000}
print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
profit = (movie['revenue']) - (movie['budget'])
print(profit)
if (movie['revenue']) < (movie['budget']):
    print("It was a flop.")
if (movie['revenue']) >= (movie['budget'] * 5):
    print("That was a good investment.")


population = {'Manhattan': 1600000, 'Brooklyn': 2600000, 'Bronx': 1400000, 'Queens': 2300000, 'Staten Island': 47000}
#TA-STEPHAN: Be careful with your zeros - you put Staten Island has a population of 47,000, not 470,000.
#This made your last two answers incorrect.
print("The population of Brooklyn is", population['Brooklyn'])
print("The population of all five boroughs is", sum(population.values()))
print((population['Manhattan'])/(sum(population.values())) * 100, "percent of NYC's population lives in Manhattan")
