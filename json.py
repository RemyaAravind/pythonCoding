import json

x={"name":"xyx","age":"35"} //json

z=json.loads(x)  #json to dictionary

print(z["name"])

print(z["age"])

###################################################################

#Dictionary to JSON format

x1={

"name":"xyz",

"age":35

}

Y=json.dumps(x)

print(Y) # json format