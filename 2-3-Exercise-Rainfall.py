'''

Exercise: Rainfall

    Define an empty dict, rainfall, in which we'll keep track of city names (keys) and mm rain that fell in each city (values).
    Repeatedly ask the user to enter the name of a city.
        If they enter an empty string, stop asking
    If we got the name of a city, then ask how many mm rain fell there.
    Store this information in the rainfall dict:
        If the city is new, assign that value
        If the city already exists in our dict, add the new rainfall to what was already there.
    At the end, print the rainfall dict.

Example:

City: Jerusalem
Rain: 5
City: 

'''




#mycode




'''
#SOLUTION


rainfall = {}

while True:
    city = input('City: ').strip()
    
    if not city:   #if it's an empty string, stop the loop
        break
        
    mm_rain = input('Rain: ').strip()
    mm_rain = int(mm_rain)
    
    if city in rainfall:
        rainfall[city] += mm_rain
    else:
        rainfall[city] = mm_rain
        
print(rainfall)        



'''
