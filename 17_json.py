import json
x = '{"name": "rishabh", "age": 19, "city": "india"}'
y = json.loads(x)
print(y["name"])
