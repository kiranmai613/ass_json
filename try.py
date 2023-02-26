import json

emp = [
	{
		"Name": input("Enter the name of Employee1: "),
		"dob": input("Enter the DOB of Employee1: "),
		"height": input("Enter the Height of Employee1: "),
		"City": input("Enter the City of Employee1: "),
		"State": input("Enter the State of Employee1: ")
	},    
	{
		"Name": input("Enter the name of Employee2: "),
		"dob": input("Enter the DOB of Employee2: "),
		"height": input("Enter the Height of Employee2: "),
		"City": input("Enter the City of Employee2: "),
		"State": input("Enter the State of Employee2: ")
	},    
	{
		"Name": input("Enter the name of Employee3: "),
		"dob": input("Enter the DOB of Employee3: "),
		"height": input("Enter the Height of Employee3: "),
		"City": input("Enter the City of Employee3: "),
		"State": input("Enter the State of Employee3: ")
	},  
	{
		"Name": input("Enter the name of Employee4: "),
		"dob": input("Enter the DOB of Employee4: "),
		"height": input("Enter the Height of Employee4: "),
		"City": input("Enter the City of Employee4: "),
		"State": input("Enter the State of Employee4: ")
	},    
	{
		"Name": input("Enter the name of Employee5: "),
		"dob": input("Enter the DOB of Employee5: "),
		"height": input("Enter the Height of Employee5: "),
		"City": input("Enter the City of Employee5: "),
		"State": input("Enter the State of Employee5: ")
	}
]

json_object = json.dumps(emp, indent=4)

print(type(emp))
with open("Employee.json", "w") as outfile:
    outfile.write(json_object)

emp1 = open("Employee.json")

employee = json.load(emp1)
print(type(employee))
employee1 = list(employee)
print(employee1)
emp1.close()
