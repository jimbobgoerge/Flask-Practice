from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def view_list():
    """
    When users hit the main url displays the user's
    current shopping list.
​
    TODO: 
    * Add a greeting to the user with their name at the top of the page
    * Figure out how to make an HTML form to add a new item (let me know if you need guidence)
    """
    # an HTML representation of the user shopping list
    with open("user.json", "r") as user_file:
        user = json.load(user_file)
        """loads the user.json file"""

    if request.method == "POST":
      if isinstance(request.form.get("submit", type=int), int): #
        var1 = (request.form.get("submit", type=int))
        del user["shopping_list"][var1]
        #print(type())
        print("deleted number: %i" % var1)
        with open("user.json", "w") as user_file:
          json.dump(user, user_file)
      if (request.form["submit"] == "Submit"):
        id = (request.form["newitem"])
        """bringing the form for 'newitem' into callable python by being stored in a string
        as id request.form will call on the input from the user for in this case the textbox 
        with name='newitem'"""
        print(request.form["newitem"])
        user["shopping_list"].append(id)
        with open("user.json", "w") as user_file:
          json.dump(user, user_file)
          """creates a user.json file using the user shoppinglist from the user dictionary, 
          and appends and saves that list"""
    #printed_list = user["name"]
    #printed_list += '<form method="POST">'
    #printed_list += '<br>'
    #printed_list += 'New Item:<br>'
    #printed_list += '<input type="text" name="newitem">'
    #printed_list += '<br>'
    #printed_list += '<input type="submit" name="submit" value="Submit">'
    #printed_list += "</form>"
    """ HTML form for a simple text box with submit button"""
    #printed_list += list_to_html(user["shopping_list"])
    """ the += adds them all together"""
    #return printed_list
    return render_template("index.html", user=user, shopping_list=list_to_html(user["shopping_list"]))

@app.route("/hello")
def hello():
  """ When someone goes to /hello the browser
  will just return hello"""
  return "Hello"

def list_to_html(shopping_list):
  """Takes in a python list and returns the list
  as a string of HTML content.
​
  Parameters
  ----------
  shopping_list(list): A python list of arbitrary items
  """
  html_list = "" # start with an open unordered list
  for item in shopping_list:# <li>{item}</li> adds the current item as a list item
    html_list += f'\
    <li>{item}</li>\
    <form method="POST">\
    <button type="submit" name="submit" value=%i>X</button>\
    </form>\
    '% shopping_list.index(item) #passes position of the item in the
  return html_list

if __name__ == "__main__":
  user = {
      "name":"Kieran",
      "age":10,
      "shopping_list": ["eggs", "ham", "sausages"]
  }
  app.run(debug=True)