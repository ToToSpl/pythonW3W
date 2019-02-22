import what3words
import sys
import json
import cv2

"""kraj w ktrorym jest dany kwadrat.
W roznych krajach slowa sie powtarzaja,
jest to upewnienie ze nie lecimy do np. austrii"""

country = 'pl'
API_KEY = '4MTIK6RG' #klucz API zrub se swoj!!


#mozna podac nazwe zdjecia jak nie chcemy address.png

if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    inputImage = cv2.imread("address.png")


# Create a qrCodeDetector Object
qrDecoder = cv2.QRCodeDetector()
# Detect and decode the qrcode
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)

if len(data) > 0:
    print("on QR found text: " ,data)

    #lukasz mowil ze przed tym w3w ma byc /// wiec dodalem usuwanie tego
    data = data.split('///')[1]

    # what3words


    geocoder = what3words.Geocoder(API_KEY)

    #res = geocoder.autosuggest_ml('thinkers.online.alarm') #testowy slup przy polibudzie
    res = geocoder.autosuggest_ml(data)
    
    res = json.dumps(res)
    loadedRes = json.loads(res)

    #podawane koordynaty to juz te w srodku kwadratu. api to liczy za nas

    for x in loadedRes['suggestions']:
        if x['country'] == country:
            print("lng = ", x['geometry']['lng'])
            print("lat = ", x['geometry']['lat'])
            break

else:
    print("No QR code found")
 