import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium


# find county

num = "+237651345022"
myNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(myNum, "en")
print(localisation)

# Now try to find mobile operator

operator = phonenumbers.parse(num)
print(carrier.name_for_number(operator, "en"))

# find latitude and longitude

key = "8296238b32484bae924ab2b68523b86e"
coord = OpenCageGeocode(key)
request = str(localisation)
answer = coord.geocode(request)
lat = answer[0]['geometry']['lat']
lon = answer[0]['geometry']['lng']
print(lat, lon)

# create map

myMap = folium.Map(location=[lat, lon], zoom_start=12)
folium.Marker([lat, lon], popup=localisation).add_to(myMap)
myMap.save("map.html")
