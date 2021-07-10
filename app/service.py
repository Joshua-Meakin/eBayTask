import json
import urllib.request
from geopy.distance import geodesic

def dis_calculate(pickup_postcode, delivery_postcode, vehicle):
    vehicle_choice = {
        "Bicycle": 1.1,
        "Motorbike": 1.15,
        "Parcel car": 1.2,
        "Small van": 1.3,
        "Large van": 1.4
    }
    res1 = urllib.request.urlopen("http://api.postcodes.io/postcodes/{}/validate".format(pickup_postcode)).read()
    res2 = urllib.request.urlopen("http://api.postcodes.io/postcodes/{}/validate".format(delivery_postcode)).read()
    data1 = json.loads(res1)
    data2 = json.loads(res2)
    if data1['result'] == False or data2['result'] == False:
        return {
            "error": "The postcode is invalid",
        }
    res1 = urllib.request.urlopen("http://api.postcodes.io/postcodes/{}".format(pickup_postcode)).read()
    res2 = urllib.request.urlopen("http://api.postcodes.io/postcodes/{}".format(delivery_postcode)).read()
    data1 = json.loads(res1)
    data2 = json.loads(res2)
    lon1, lat1 = data1["result"]["longitude"], data1["result"]["latitude"] 
    lon2, lat2 = data2["result"]["longitude"], data2["result"]["latitude"]
    price = float(geodesic((lon1, lat1), (lon2, lat2)).km)
    price = int(round(price*vehicle_choice[vehicle]))
    return {
        "Pickup Postcode": pickup_postcode,
        "Delivery Postcode": delivery_postcode,
        "Vehicle": vehicle,
        "Price": price
    }