import requests
import json
import jsonschema
from jsonschema import validate

def ValidateAPIScheme(self):
    #Api URL
    url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"                                                                                                                                                                                                                                    

    #Send get request
    response = requests.get(url)

    #parsing API response
    json_response: object = response.json()

    #Function to get json schema for validation
    def get_schema():
        with open('\EA_CodingTest\EA_APIValidation\JsonSchema.json', 'r') as file:
            schema = json.load(file)
        return schema

    #Function to validate json schema
    def ValidateJsondata(json_response):
        execute_api_schema = get_schema()

        try:
            validate(instance=json_response, schema=execute_api_schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Is Invalid Json schema"
            return False, err

        message = "Is Valid Json schema"
        return True, message

    finalmessage = ValidateJsondata(json_response)
    print(finalmessage)


ValidateAPIScheme(self=str)