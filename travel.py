destination=input("where is your destination?: ")
distance=int(input("what is the approximate distance? in Km: "))
speed=int(input("what is your average speed? in km/hr: "))
time=distance/speed
print(f"Destination: {destination}")
print(f"Distance: {distance}Km")
print(f" Average Speed: {speed} km/hr")
print(f"Estimated Travel Time in hour: {time} hours")
print(f" Estimated Travel Time in minute: {time*60} minutes")