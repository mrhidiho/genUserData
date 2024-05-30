import json
import datetime
import random
import uuid

# Load the data template from data.json
with open('data.json', 'r') as f:
    data_template = json.load(f)
# Generate an empty TestUserData.json file
with open('TestUserData.json', 'w') as f:
    pass
att_set = ["att1", "att2", "att3", "att4", "att5", "att6"]
attA_set = ["attA", "attB", "attC", "attD", "attE", "attF"]

# Print the data template
#print(json.dumps(data_template, indent=4))
# Prompt the user to enter the number of person objects to generate
num_persons = int(input("Enter the number of person objects to generate: "))

# Create a list to store the person objects
persons = []

# Generate the specified number of person objects
for _ in range(num_persons):
    # Create a new person object
    person = {}
    # Set the object type and time
    person['userID'] = str(uuid.uuid4())  # Generate a random uuid
    person['type'] = data_template['objectUser']['type']
    person['time'] = datetime.datetime.now().timestamp()
    # Create a list of attributes
    attributes = []
    attributesA = []
    # Generate a random number of attributes (max 6)
    num_attributes = random.randint(1, 6)
    # Create attributes and add them to the list
    for i in range(num_attributes):
        attribute = {}
        attributeA = {}
        attribute['attID'] = str(uuid.uuid4()) 
        attribute['type'] = random.choice(att_set)
        attribute['value'] = random.randint(1, 100)
        attribute['time'] = datetime.datetime.now().timestamp()
        attribute['queryCount'] = random.randint(1, 20)
        attributeA['attID'] = str(uuid.uuid4()) 
        attributeA['type'] = random.choice(attA_set)
        attributeA['value'] = random.randint(1, 100)
        attributeA['time'] = datetime.datetime.now().timestamp()
        attributeA['queryCount'] = random.randint(1, 20)
        attribute['properties'] = attributesA
        attributes.append(attribute)
        attributesA.append(attributeA)
    # Add the attributes to the person object
    person['properties'] = attributes
    # Add the person object to the list
    persons.append(person)

# Write the list of person objects to a JSON file
with open('TestUserData.json', 'w') as f:
    json.dump(persons, f, indent=4)

