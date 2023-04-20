import requests
import json


def ValidateJsonStringsAttribute(self):
    #Api URL
    url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"                                                                                                                                                                                                                                    

    #Send get request
    response = requests.get(url)

    #parsing API response
    json_response: object = response.json()

    #formatting to json
    obj = json.dumps(json_response, indent=3)

    #function to check for JSON String validity
    def is_valid(json_string):
        print("JSON String:", json_string)
        try:
            json.loads(json_string)
            print("  Is valid Json?: True")
        except ValueError:
            print("  Is valid Json?: False")
            return None

    
    is_valid(obj) 


ValidateJsonStringsAttribute(self=str)
