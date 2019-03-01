import what3words
import sys
import json
import cv2
import pytesseract

country = 'pl'
API_KEY = '4MTIK6RG' #klucz API zrub se swoj!!

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
    inputImage = cv2.imread("w3wText.png")

config = ('-l eng --oem 1 --psm 3')

text = pytesseract.image_to_string(inputImage, config=config)

print('read from image = ',text)

lng,lat=w3wReturnLngLat(text)

print("lng = ", lng)
print("lat = ", lat)