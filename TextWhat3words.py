import what3words
import sys
import json
import cv2
import pytesseract

country = 'pl'
API_KEY = '4MTIK6RG' #klucz API zrub se swoj!!

def w3wReturnLngLat(w3wText):
    if w3wText.find('///') is not -1:
        geocoder = what3words.Geocoder(API_KEY)
        res = geocoder.autosuggest_ml(w3wText)
        res = json.dumps(res)
        loadedRes = json.loads(res)
        for x in loadedRes['suggestions']:
            if x['country'] == country:
                return 1,x['geometry']['lng'],x['geometry']['lat']
    else:
        return 0,0,0


if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    inputImage = cv2.imread("w3wText.png")

config = ('-l eng --oem 1 --psm 3')

text = pytesseract.image_to_string(inputImage, config=config)

print('read from image = ',text)

test,lng,lat = w3wReturnLngLat(text)
if test:
    print("lng = ", lng)
    print("lat = ", lat)
else:
    print("wrong text found")