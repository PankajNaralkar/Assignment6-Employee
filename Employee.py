import json
Employees = [

{
    "Name-->": "Raviraj", "DOB-->": "10/12/1997", "Height ": "170.12Cm.", "City": "Patna", "State": "Goa",
    
   
},
    
{
    "Name-->": "Pankaj", "DOB-->": "18/11/1998", "Height ": "172.09Cm.", "City": "Mumbai", "State": "Maharashtra",
    
   
},
    
{
    "Name-->": "Divya", "DOB-->": "10/09/1999", "Height ": "160.12Cm.", "City": "Pune", "State": "Maharashtra",
    
   
},
    
{
    "Name-->": "Priyanka", "DOB-->": "14/12/2000", "Height ": "160.12Cm.", "City": "Kolhapur", "State": "Maharashtra",
    
   
},
    
{      
    "Name-->": "Rajesh", "DOB-->": "11/02/1987", "Height ": "165.12Cm.", "City": "panji", "State": "Goa",
    
}
       
            ]

 
with open("Employee.json", "w") as f:
    json.dump(Employees, f)
    S = open('Employee.json',)
data = json.load(S)
for n in range(len(Employees)):
        Employees[n] = Employees[n]
        print (Employees[n])
        f.close()