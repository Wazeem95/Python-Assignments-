# coding=utf-8
# # Q:1 Use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary. Add a new key value pair about qualification then update the
# qualification value to high academic level then delete it.


person_details = {"First_Name": "WASEEM",
                  "Last_Name": "AHMED",
                  "Age": "23",
                  "City": "KARACHI",
                  }

for i in person_details.values():
    print(i)

person_details.update({"qualification": "Under Graduate"})

print(person_details["qualification"])

person_details["qualification"] = "Graduate"
print("After Update Qualification : ", person_details["qualification"])

del person_details["qualification"]

print(person_details)

# # Q:2 Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a
# dictionary of information about each city and include the country that the city is in, its approximate population,
# and one fact about that city. The keys for each city’s dictionary should be something like country, population,
# and fact. Print the name of each city and all of the information you have stored about it.

city = {
    "NEW YORK": {
        "Country": "UNITED STATES OF AMERICA",
        "Approximate_population": "19.49 Million Approx.",
        "Fact": "The New York Public Library has over 50 million books and other items and is the second largest "
                "library system in the nation after the Library of Congress. It is also the 3rd largest library in "
                "the world. "
    },
    "ISTANBUL": {
        "Country": "TURKEY",
        "Approximate_population": "14.6 Million Approx.",
        "Fact": "Istanbul is the only city in the world which is both in Europe and Asia geographically."
    },
    "BERLIN": {
        "Country": "GERMANY",
        "Approximate_population": "3.5 Million Approx.",
        "Fact": "Berlin is considered by many as Germany`s greenest city with over 44% of its area made of waterways, "
                "woods, rivers and green areas. "
    }
}

for i in city.keys():
    print("City Name : ", i)
    print("Country Name  : ", city[i]["Country"])
    print("Approximate population  : ", city[i]["Approximate_population"])
    print("Fact of the City  : ", city[i]["Fact"])
    print(
        "**************************************************************************************************************************************************************************************************************************************")

# # Q:3 A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of
# 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

print("Welcome To Movie Theater")
persons = int(input("Enter the no. of Person : "))

total_price = 0

for i in range(1, persons + 1):
    age = int(input("Enter The Age Of Person: "))
    if age <= 3:
        print("Your Ticket is Free! Enjoy Your Movie")
    elif age <= 12:
        print("Your Ticket price will be $10")
        total_price += 10
    else:
        print("Your Ticket price will be $15")
        total_price += 15

print("Total Amount = ", total_price, " $ Enjoy Your Movie")

# # Q:4 Write a function called favorite_book() that accepts one parameter, title. The function should print a
# message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book
# title as an argument in the function call.

def favorite_book(book_name):

    print("One of my favorite book is ", book_name)


title = input("Enter the Book title: ")

favorite_book(title)

# # Q:5 Guess the number game Write a program which randomly generate a number between 1 to 30 and ask the user in
# input field to guess the correct number. Give three chances to user guess the number and also give hint to user if
# hidden number is greater or smaller than the number he given to input field.

import random

random_number = random.randrange(1, 30)

flag = False

for i in range(1, 4):
    guess = int(input("Guess the number between 1 to 30 : "))
    if guess == random_number:
        flag = True
        break
    elif guess < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

if flag:
    print("Congratulation you Win!!")
else:
    print("You Loose")
    print("Correct Number is ", random_number)
