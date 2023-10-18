import requests
from datetime import datetime
import smtplib
import time

MY_LAT = "ENTER LAT HERE, remove parenthesis"  # Your latitude
MY_LONG = "ENTER LONG HERE, remove parenthesis"  # Your longitude
MY_EMAIL = "EMAIL HERE"
PASSWORD = "PASSWORD HERE" # Generate app password


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


# Try to refrain from using == when comparing variables that are floats because it will be incredibly rare for each to equal exactly
# A better use of comparing these types of variables, especially instead of using range(), for example, is to use <=
# Put the variable you're comparing on either side of the variable it's being compared to, like below, and use math to create margins/a range

on = True
while on:
    time.sleep(60)
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        if MY_LONG - 5 <= iss_latitude <= MY_LONG + 5:
            if time_now < sunset:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=MY_EMAIL,
                                        to_addrs="EMAIL TO SEND TO HERE",
                                        msg="Subject:Look up!\n\nThe ISS is overhead. And it should be dark enough to see it.")





