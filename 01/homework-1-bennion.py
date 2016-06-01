#Kate Bennion
5/23/16
#Homework 1

year_of_birth = input("What year were you born in?")
if 2016 < int(year_of_birth):
    year_of_birth = input("Nice try, time travel is impossible. What year were you born in, really?")
age = 2016 - int(year_of_birth)
blue_whale = str(age * 3153600)
rabbit = str(age * 107748000)
venus = str(age/.615)
neptune = str(age/164.79)
age_diff = str(26 - age)
print("You are roughly", str(age), "years old.")
print("Your heart has beaten", str(age * 42000000), "times.")
print("A blue whales heart has beaten", blue_whale, "times.")
if int(rabbit) > 1000000000:
    print("A rabbit's heart has beaten", str(int(rabbit)/1000000000), "billion.")
else:
    print("A rabbit's heart has beaten", rabbit, "times.")
print("Your age in Venus years is", venus)
print("Your age in Neptune years is", neptune)
print("Our age difference is", age_diff)

if age == 26:
    print("You are the same age as me!")
elif age < 26:
    print("You are younger than me!")
elif age > 26:
    print("You are older than me!")

if (int(year_of_birth) % 2) == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

if age >= 7:
    print("The Steelers have won the Superbowl twice since you were born.")
elif 4 <= age < 7:
    print("The Steelers have won the Superbowl once since you were born.")
elif age < 4:
    print("The Steelers have not won the Superowl since you were born.")

if 1933 <= int(year_of_birth) < 1945:
    print("FDR was president when you were born!")
if 1945 <= int(year_of_birth) < 1953:
    print("Truman was president when you were born!")
if 1953 <= int(year_of_birth) < 1961:
    print("Eisenhower was president when you were born!")
if 1961 <= int(year_of_birth) < 1963:
    print("JFK was president when you were born!")
if 1963 <= int(year_of_birth) < 1969:
    print("LBJ was president when you were born!")
if 1969 <= int(year_of_birth) < 1974:
    print("Nixon was president when you were born!")
if 1974 <= int(year_of_birth) < 1977:
    print("Ford was president when you were born!")
if 1977 <= int(year_of_birth) < 1981:
    print("Carter was president when you were born!")
if 1981 <= int(year_of_birth) < 1989:
    print("Reagan was president when you were born!")
if 1989 <= int(year_of_birth) < 1993:
    print("Bush Sr. was president when you were born!")
if 1993 <= int(year_of_birth) < 2001:
    print("Clinton was president when you were born!")
if 2001 <= int(year_of_birth) < 2009:
    print("Dubya was president when you were born!")
if 2009 <= int(year_of_birth):
    print("Obama was president when you were born!")
