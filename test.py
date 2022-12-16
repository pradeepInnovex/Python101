print("Please Enter Weather Status in today")

weather_Status = input()

message_01 = "Please dont go out today is rainy day"
message_02 = "You can go any where today is sunny day"

if weather_Status == "rainy":
    print(message_01)

else:
    print(message_02)

