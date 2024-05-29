#import class library of json.
import json

#Creating data dictionary.

data = {
    
    'name': 'John Doe',
    'age': 27,
    'city': 'Seattle, WA',
    'interests':['Reading','Dogs','Videogames','Drawing','Traveling'],
    'is_student': True

}


#Create a json file and writing the pyton object contents to json. 
with open('data.json','w') as json_file:
    
    json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

#With statement for reading
with open('data.json','r') as json_file:
    
    #Create a object called loaded_data. Load the json file into the argument parameter.
    loaded_data = json.load(json_file)

print("Succesfully able to read data.json")
print(loaded_data)

#Altering the JSON Object.
loaded_data['age'] = 30 #<-ints

loaded_data['interests'].append('Secret Hobby')

#rewrite changes to the json file
with open('data.json','w') as json_file:
    
    json.dump(loaded_data,json_file,indent=4)

print("Data has been re-written to data.json")
