import requests

url = "https://diagnosis.p.rapidapi.com/api/DDxItems/GetTests"

querystring = {"AuthenticationID":"DEMO_AuthenticationID"}

headers = {
	"X-RapidAPI-Key": "1928b6c638mshc68e7bff3b73d4fp193dc8jsn5b814cec4657",
	"X-RapidAPI-Host": "diagnosis.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

procedure=input("Enter the procedure:")
print("LowRange Value:",lowRangeValue)
