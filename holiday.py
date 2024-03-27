"""
For this task I decided to store the information needed in a dictionary with a nested list of dictionaries,
to better access the information.
With the input "catalogue" I will display the info to the user with the print(), so they can select the destination
based on the various costs.
Then, I coded the three inputs requested by the task, which will be the argument of the relevant functions.
I defined three functions for the night cost, the car rental and for the total amount of the holidays. The function
plane_cost() will show the cost of the flight.
"""

# This is the catalogue that the user will see on the console once they press Enter when requested
cities = {'Rome': [{'flight': 400}, {'hotel': 150}, {'car': 50}],
          'Paris': [{'flight': 650}, {'hotel': 300}, {'car': 100}],
          'Barcelona': [{'flight': 500}, {'hotel': 250}, {'car': 70}],
          'London': [{'flight': 600}, {'hotel': 200}, {'car': 60}],
          'Tokyo': [{'flight': 1600}, {'hotel': 400}, {'car': 160}]
          }

catalogue = input('Please press enter to see our catalogue.')

# This loop will show all the destinations and the relevant information
for destination in cities.keys():
    flight_price = cities[destination][0]['flight']
    hotel_price = cities[destination][1]['hotel']
    car_price = cities[destination][2]['car']
    print(f"The flight to {destination} costs £{flight_price}. The cost of the hotel per night is £{hotel_price}, "
          f"and the car rental will cost you £{car_price} per day.")

# This is the function that will return the flight cost
city_flight = input('\nPlease select your destination: ').capitalize()


def plane_cost(city_flight):
    return cities[city_flight][0]['flight']


# This while loop will manage the incorrect answers of the user
while city_flight not in cities.keys():
    city_flight = input("Your destination is not in our catalogue.\n"
                        "Please select a destination from the catalogue: ").capitalize()
else:
    plane_cost(city_flight)

# This is the function that returns the cost of the hotel
num_nights = int(input('\nHow many nights do you want to stay in your destination? '))


def hotel_cost(num_nights):
    hotel_price = cities[city_flight][1]['hotel']
    return num_nights * hotel_price


# This is the function that returns the cost of the car rental
rental_days = int(input('\nHow many days of car rental do you need? '))


def car_rental(rental_days):
    car_price = cities[city_flight][2]['car']
    return car_price * rental_days


# This is the function that returns the total cost of the holiday
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
    return f'\nThe total cost of the holidays is {total_cost}.'


# This line will print out the total cost of the holidays, using the last function
print(holiday_cost(city_flight, num_nights, rental_days))
