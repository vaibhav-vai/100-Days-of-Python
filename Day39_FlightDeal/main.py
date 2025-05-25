#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import time
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
#pprint(sheet_data)
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_code()


tomorrow = datetime.now()+ timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flight for {destination['city']}...")
    flights = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    cheapest_flights = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flights.price}")
    time.sleep(2)

    if cheapest_flights.price != "N/A" and cheapest_flights.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flights.price} to fly "
                         f"from {cheapest_flights.origin_airport} to {cheapest_flights.destination_airport}, "
                         f"on {cheapest_flights.out_date} until {cheapest_flights.return_date}."
        )
