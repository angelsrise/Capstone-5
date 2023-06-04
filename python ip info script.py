import geocoder
from geopy.geocoders import Nominatim

def get_ip_info(ip_address):
    ip_geocoder = geocoder.ipinfo(ip_address)
    
    if 'private' not in ip_geocoder:
        g = ip_geocoder
        geolocator = Nominatim(user_agent="ip_info_script")
        location = geolocator.geocode(g.city)
        
        country = g.country
        city = g.city if g.city else "N/A"
        continent = location.address.split(",")[-1].strip() if location else "N/A"
        
        return country, city, continent
    
    return "N/A", "N/A", "N/A"

ip_address_list = ['192.168.0.1', '8.8.8.8', '127.0.0.1']

for ip in ip_address_list:
    country, city, continent = get_ip_info(ip)
    print("IP: {}".format(ip))
    print("Country: {}".format(country))
    print("City: {}".format(city))
    print("Continent: {}".format(continent))
    print("----------")
