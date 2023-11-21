                                                                                #
import json
import requests
import time

JsonFileTaksOne = open("test_data_one.json")
jsonFileTaskFive = open("test_data_five.json")
dataTaksOnePythonList = json.load(JsonFileTaksOne)                              # Load the JSON data into a Python dictionary
dataTaksFivePythonList = json.load(jsonFileTaskFive)                            # Load the JSON data into a Python dictionary

wait = 0.01

url = "http://localhost:3002/people"

headers = {"Content-Type": "application/json"}

#Task 1: Create a file in your directory containing valid JSON data for your server, import it, and send it to the API using a POST request.
                                                                                #
if type(dataTaksOnePythonList) is dict:                                         # check if file contains a single entrie or a list of entries
    responseTaskOne = requests.post(url, json=dataTaksOnePythonList, headers=headers)
    print("#Task 1 post request response code:", responseTaskOne)
elif type(dataTaksOnePythonList) is list:                                       # and act accordingly
    for i in range(len(dataTaksOnePythonList)):
        responseTaskOne = requests.post(url, json=dataTaksOnePythonList[i], headers=headers)
        print("#Task 1 post request response code:", responseTaskOne)
else:
    print("#Task 1 - json file not valid!!!!!")

#Task 2: Send a get request to your API and filter the data until you find the data you posted
                                                                                #
resultTaskTwo = []                                                              # declare list variable to hold results' "id"

responseTaskTwo = requests.get(url)                                             # request all server data as a json file
responseJsonTaskTwo = responseTaskTwo.json()                                    # load the JSON data into a Python dictionary

if type(dataTaksOnePythonList) is dict:                                         # check if file contains a single entrie or a list of entries
    postedEmail = dataTaksOnePythonList["email"]                                # take "emial" from test_data_one.json and fearch for it in the server response json
    print (postedEmail)
    for i in range(len(responseJsonTaskTwo)):                                   # once entrie found with matching "email", store the corresponding "id" in resultTaskTwo
        if responseJsonTaskTwo[i]["email"] == postedEmail:
            resultTaskTwo.append(responseJsonTaskTwo[i]["id"])
elif type(dataTaksOnePythonList) is list:                                       # this one is similar to the one above
    for i in range(len(dataTaksOnePythonList)):
        postedEmail = dataTaksOnePythonList[i]["email"]
        print (postedEmail)
        for i in range(len(responseJsonTaskTwo)):
            if responseJsonTaskTwo[i]["email"] == postedEmail:
                resultTaskTwo.append(responseJsonTaskTwo[i]["id"])
else:
    print("#Task 1 - json file not valid!!!!!")

print("Found person:", resultTaskTwo)

#Task 3: Update the data using a PATCH and PUT request

for i in range(len(resultTaskTwo)):
    time.sleep(wait)
    temporaryUrl = url + "/" + resultTaskTwo[i]
    taskThreeResponse = requests.patch(temporaryUrl, data ={"dob":"01/01/1970"})
    print("#Task 3 patch request response code", taskThreeResponse)
    print("#Task 3 patch request response", taskThreeResponse.content)
    time.sleep(wait)

#Task 4: Remove the data using a DELETE request

for i in range(len(resultTaskTwo)):
    time.sleep(wait)
    temporaryUrl = url + "/" + resultTaskTwo[i]
    responseTaskFour = requests.delete(temporaryUrl, timeout=1)
    print("#Task 4 delete request response code", responseTaskFour)
    time.sleep(wait)

#Task 5: Create a json file with various example of people data, within the data create several duplicates,

for i in range(len(dataTaksFivePythonList)):
    time.sleep(wait)
    temporaryDataAmphora = dataTaksFivePythonList[i]
    responseTaskFive = requests.post(url, json=temporaryDataAmphora, headers=headers)
    print("#Task 5 post request response code:", responseTaskFive)
    time.sleep(wait)

# import this data, remove duplicates and POST to the API

responseTaskFive = requests.get(url)
responseJsonTaskFive = responseTaskFive.json()
noDuplicatesEmailList = []
duplicateIdList = []

for i in range(len(responseJsonTaskFive)):
    idTemporaryStorage = responseJsonTaskFive[i]["id"]
    if responseJsonTaskFive[i]["email"] not in noDuplicatesEmailList:
        noDuplicatesEmailList.append(responseJsonTaskFive[i]["email"])
        print(responseJsonTaskFive[i])
    else:
        duplicateIdList.append(idTemporaryStorage)

for i in range(len(duplicateIdList)):
    time.sleep(wait)
    temporaryUrl = url + "/" + duplicateIdList[i]
    responseTaskFive = requests.delete(temporaryUrl, timeout=1)
    print("#Task 5 delete request response code", responseTaskFour)
    time.sleep(wait)

#Task 6: When importing the data, add some validation to ensure the data is structured how you would expect. Correct data types, etc.

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