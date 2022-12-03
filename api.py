import http.client

conn = http.client.HTTPSConnection("diagnosis.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "1928b6c638mshc68e7bff3b73d4fp193dc8jsn5b814cec4657",
    'X-RapidAPI-Host': "diagnosis.p.rapidapi.com"
    }

conn.request("GET", "/api/DDxItems/GetTests?AuthenticationID=DEMO_AuthenticationID", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.)  