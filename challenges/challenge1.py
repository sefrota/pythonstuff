#Asks the user to input the number of miles
#Convert miles to Kilometers (1 mi = 1.60934 km)
#Print this for example 5 miles equals 8.0467 kilometers

miles = float(input("Input the number of miles: "))

kms = 1.60934 * miles

print("{} miles correspond to {} kilometers".format(miles, kms))
