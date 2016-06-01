#Kate Bennion
5/25/2016
#Homework 2
#LISTS
numbers = [ 22, 90, 0, -10, 3, 22, 48 ]
print(len(numbers))
print(numbers[3])
print(numbers[3] + numbers[1])
print(max(n for n in numbers if n!=max(numbers)))
print(numbers[-1])

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
print("The population of Brooklyn is", population['Brooklyn'])
print("The population of all five boroughs is", sum(population.values()))
print((population['Manhattan'])/(sum(population.values())) * 100, "percent of NYC's population lives in Manhattan")
