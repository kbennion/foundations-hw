#graded 12/14
#Kate Bennion
5/31/2016
#Homework 3

#LISTS
countries = ["Cambodia", "France", "U.K.", "Mexico", "Hong Kong", "Israel", "Palestine"]

for countrie in countries:
    print(countrie)

print(countries.sort)
#TA-STEPHAN: Need to add () to the end of sort. Also don't need to print.
print("sorted", countries)
print(countries[0])
penultimate = len(countries)-1
#TA-STEPHAN: Need to subtract 2 not 1 (because we start at 0)
print("penultimate",countries[penultimate])
countries.remove("Mexico")
for countrie in countries:
    print(countrie)

#DICTIONARIES
tree = {'name': 'Sunland Baobab', 'species': 'Adansonia digitata', 'age': '1060', 'location_name': 'Limpopo Province, South Africa', 'latitude': -23.401295, 'longitude': 29.417932}

print(tree['name'], "is a", tree['age'], "year-old tree that is in", tree['location_name'])

if tree['latitude'] < 40.7128:
    print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC."),
else:
    print ("The tree", tree['name'], "in", tree['location_name'], "is north of NYC.")

age = input("How old are you?")
tree_older = 1060 - int(age)
age_older = int(age) - 1060
if int(age) >= 1060:
    print("You are", age_older, "years older than", tree['name'])
else:
    print(tree['name'], "was", tree_older, "years old when you were born.")

#LISTS OF DICTIONARIES
#Loop through the list, printing whether each city is north of south of your tree from the previous section.

places = ["Moscow", "Tehran", "Falkland Islands", "Seoul", "Santiago"]
place_info = [
    {'name': 'Moscow', 'latitude': 55.755826, 'longitude': 37.617300},
    {'name': 'Tehran', 'latitude': 35.689197, 'longitude': 51.388974},
    {'name': 'Falkland Islands', 'latitude': -51.796253, 'longitude': -59.523613},
    {'name': 'Seoul', 'latitude': 37.566535, 'longitude': 126.977969},
    {'name': 'Santiago', 'latitude': 42.878213, 'longitude': -8.544844},
    ]

for place in place_info:
    print(place['name'])
    if place['latitude'] > 0:
        print("above the equator"),
    else:
        print("below the equator")
    if place['name'] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

for place in place_info:
    if int(place['latitude']) > int(tree['latitude']):
        print(place['name'], "is north of", tree['name'])
    else:
        print(place['name'], "is south of", tree['name'])
