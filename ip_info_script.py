import geocoder
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_location_geocoder(query):
    geolocator = Nominatim(user_agent="ip_info_script")
    try:
        return geolocator.geocode(query)
    except GeocoderTimedOut:
        return get_location_geocoder(query)

def get_ip_info(ip_address):
    ip_geocoder = geocoder.ipinfo(ip_address)
    
    if 'private' not in ip_geocoder:
        g = ip_geocoder
        
        if g.city:
            location = get_location_geocoder(g.city)
        else:
            location = None
        
        country = g.country
        city = g.city if g.city else "N/A"
        continent = location.address.split(",")[-1].strip() if location else "N/A"
        
        return country, city, continent
    
    return "N/A", "N/A", "N/A"

ip_address_list = ['192.168.0.1', '8.8.8.8', '127.0.0.1', '185.86.151.11', '103.86.96.100', '74.125.24.100', '210.79.249.66', '45.79.156.10', '212.58.246.91', '13.107.4.50']

for ip in ip_address_list:
    country, city, continent = get_ip_info(ip)
    print("IP: {}".format(ip))
    print("Country: {}".format(country))
    print("City: {}".format(city))
    print("Continent: {}".format(continent))
    print("----------")