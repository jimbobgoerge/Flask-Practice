import json

user = {
      "name":"Kieran",
      "age":10,
      "shopping_list": ["eggs", "ham", "sausages"]
  }

with open("user.json", "w") as user_file:
    json.dump(user, user_file)