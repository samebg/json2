#Implemented JavaScript Object Notation
import json

#Creates a dataset, in which most are variables and one such as age is an integer. A string array is introduced for interests
data= {

    'name':'James Bond',
    'age': 30,
    'city':'Washington State, WA',
    'interests': ['Traveling','English Football','Basketball','Eating','Sleeping'],
    'is_student': True
}

#Creating a JSON and writting the python object contents to the JSon
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

#Visibly outputs the sentence below
print("You have successfully written a JSON file")


#########

with open('data.json','r') as json_file:

    #Create a python object called data, converting the json file to a loaded data
    loaded_data = json.load(json_file)

print("Sucessfully able to read data.json")
print(loaded_data)

#
loaded_data['age'] = 11
loaded_data['interests'].append('Swimming')
loaded_data['interests'].remove('Eating')

###########
with open('data.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

#Visibly outputs the sentence below
print("You have successfully written a JSON file")