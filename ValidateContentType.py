import requests


#validate status code
def ValidateContentType(self):
    #Api URL
    url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"
    
    #Send get request
    response = requests.get(url)
    
    #checking for header content type
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    print("Response is in JSON format")


ValidateContentType(self=str)