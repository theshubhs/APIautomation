import requests


def ValidateEmptyStringAttribute(self):
    #Api URL
    url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"                                                                                                                                                                                                                                    

    #Send get request
    response = requests.get(url)

    #parsing API response
    json_response: object = response.json()
    
    #function to flatten json object
    def flatten_json(y):
        out = {}
        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x

        flatten(y)
        return out
    
    flat = flatten_json(json_response)
    print(flat)

    #Search empty string value keys
    keys = [k for k, v in flat.items() if v == '']
    print("Found an empty string key value pair:",keys)


ValidateEmptyStringAttribute(self=str)
