import requests
import time


#validate API response time
def ValidateAPIResponseTime(self):
    #Api URL
    url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"
    
    start = time.time() * 1000
    #Send get request
    response = requests.get(url)
    
    end = time.time() * 1000
    APIResponsetime = end - start
    
    if APIResponsetime < 1000 :
        print("Response time is less than 1000ms")
    else:
        print("Response time is more than 1000ms")


ValidateAPIResponseTime(self=str)





