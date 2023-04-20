import requests


#validate status code
def ValidateStatusCode(self):
    #Api URL
    url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"
    
    #Send get request
    response = requests.get(url)

    #checking for status code in API response 
    assert response.status_code == 200
    print("Status code is 200")
    

ValidateStatusCode(self=str)





