import what3words
import sys
import json
import cv2

country = 'pl'
API_KEY = '4MTIK6RG'

def w3wReturnLngLat(w3wText):
    geocoder = what3words.Geocoder(API_KEY)
    res = geocoder.autosuggest_ml(w3wText)
    res = json.dumps(res)
    loadedRes = json.loads(res)
    for x in loadedRes['suggestions']:
        if x['country'] == country:
            return x['geometry']['lng'],x['geometry']['lat']

if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    inputImage = cv2.imread("address.png")


qrDecoder = cv2.QRCodeDetector()
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)

if len(data) > 0:
    print("on QR found text: " ,data)

    lng,lat = w3wReturnLngLat(data)

    print("lng = ", lng)
    print("lat = ", lat)

else:
    print("No QR code found")
 