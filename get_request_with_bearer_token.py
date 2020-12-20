import requests
url = 'https://atlas.mapmyindia.com/api/places/search/json?query=New BMC Office'
response = requests.get(url, headers = {"Authorization":"Bearer " + 'XXXXX'})
print(response)
print(response.json())

