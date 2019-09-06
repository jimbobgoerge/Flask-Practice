from flask import Flask
app = Flask(__name__)

@app.route("/")
def view_list():
  """
  When users hit the main url displays the user's
  current shopping list.
  
  TODO: 
    * Add a greeting to the user with their name at the top of the page
    * Figure out how to make an HTML form to add a new item (let me know if you need guidence)
  """
    # an HTML representation of the user shopping list
    printed_list = html_list(user["shopping_list"]) 

    return printed_list
​
@app.route("/hello")
def hello():
  """ When someone goes to /hello the browser
  will just return hello"""
  return "Hello"
​
def list_to_html(shopping_list):
  """Takes in a python list and returns the list
  as a string of HTML content.

  Parameters
  ----------
  shopping_list(list): A python list of arbitrary items
  """
  html_list = "<ul>" # start with an open unordered list
  for item in shopping_list:
    html_list += f"<li>{item}</li>" # add the current item as a list item
  html_list += "</ul>" # end the unordered list
  return html_list


if __name__ == "__main__":
  user = {
      "name":"Kieran",
      "age":10,
      "shopping_list": ["eggs", "ham", "sausages"]
    }