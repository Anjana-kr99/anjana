import requests as req

res = req.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22").json()["list"]

while True:
  n = int(input("Enter 1 to get temperature, 2 to get wind speed, 3 to get pressure, and 0 to exit: "))
  if n == 0:
    print("Thanks for using the service")
    break
  if n not in {1,2,3}:
    print("Invalid input")
    continue 
  date = input("Enter a date. (data for 27, 28, 29, 30, and 31 are available only): ")
  if date not in {"27", "28", "29", "30", "31"}:
    print("Data for this date is not available")
    continue
  date = "2019-03-" + date
  for i in res:
    if i["dt_txt"][:10] == date:
      break
  if n == 1:
    print("The temperature for " + i["dt_txt"] + " is " + str(i["main"]["temp"]))
  if n == 2:
    print("The wind speed for " + i["dt_txt"] + " is " + str(i["wind"]["speed"]))
  if n == 3:
    print("The pressure for " + i["dt_txt"] + " is " + str(i["main"]["pressure"]))