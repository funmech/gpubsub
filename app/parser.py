import googlemaps
from datetime import datetime

def print_address_components(ac):
    print('Address components')
    for com in ac:
        for k, v in com.items():
            print(k, v)
    print()
gmaps = googlemaps.Client(key='yourkey')

# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result)
# print()
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((-36.9270919, 168.596691))
# print(reverse_geocode_result)

i = 0
for d in reverse_geocode_result:
    i += 1
    print(i)
    for k, v in d.items():
        if k == 'address_components':
            print_address_components(v)
        else:
            print(k, v)
# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
