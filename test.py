
import json
import requests
import time

JsonFileTaksOne = open("test_data_one.json")
jsonFileTaskFive = open("test_data_five.json")
dataTaksOnePythonList = json.load(JsonFileTaksOne)                              # Load the JSON data into a Python dictionary
dataTaksFivePythonList = json.load(jsonFileTaskFive)                            # Load the JSON data into a Python dictionary

url = "http://localhost:3002/people"

headers = {"Content-Type": "application/json"}

#Task 6: When importing the data, add some validation to ensure the data is structured how you would expect. Correct data types, etc.

# !!!!!create an error list, that would hold all errors to list at the end, or to say finished wit no erros

def validate_data_function(jsonFile):
    dataToValidatePythonList = json.load(open(jsonFile))                              # Load the JSON data into a Python dictionary
    validateKeysList = ["fullName", "email", "job", "dob"]
    if type(dataToValidatePythonList) is dict:                                        # check if file contains a single entrie or a list of entries
        for i in range (len(validateKeysList)):
            if validateKeysList[i] in dataToValidatePythonList:
                if not isinstance(dataToValidatePythonList[validateKeysList[i]], str):
                    print(validateKeysList[i], " is a key, but the value is not a string.")
            else: print(validateKeysList[i], "is not a key in the dictionary.")
    elif type(dataToValidatePythonList) is list:
        for i in range(len(dataToValidatePythonList)):
                if type(dataToValidatePythonList[i]) is dict:                         # check if file contains a single entrie or a list of entries
                    for j in range (len(validateKeysList)):
                        if validateKeysList[j] in dataTaksFivePythonList[i]:
                            if not isinstance(dataToValidatePythonList[i][validateKeysList[j]], str):
                                print(validateKeysList[j], "is a key, but the value is not a string.")
                        else: print(validateKeysList[j], "is not a key in dictionary:", dataToValidatePythonList[i])
                else:
                    print("entrie is not a 'dict' - formating error")
    else:
        print("entrie is not a 'dict' or a 'list' - formating error")

validate_data_function("test_data_one.json")
validate_data_function("test_data_five.json")


# load json
# convert it to python list
# check if it's a dict or a list.
# if dict, check if it has keys "fullName", "email", "job"
  # check if these are all string
# if list, check if list items are dict
  # is so, check if they have keys "fullName", "email", "job"
  # check if they are string



#Task 1: Create a file in your directory containing valid JSON data for your server, import it, and send it to the API using a POST request.

# print(type(dataTaksOnePythonList))
# print(type(dataTaksFivePythonList))

# if type(dataTaksOnePythonList) is dict:
#     print("it works")
#     responseTaskOne = requests.post(url, json=dataTaksOnePythonList, headers=headers)
#     print("#Task 1 post request response code:", responseTaskOne)
