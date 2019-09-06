from flask import Flask
app = Flask(__name__)
@app.route("/")
def view_list():

    shopping_list = ["eggs", "ham", "Sausage"]
    printed_list = "<ul>" # start with an open unordered list
    for item in shopping_list:
      printed_list += f"<li>{item}</li>" # add the current item as a list item
    printed_list += "</ul>" # end the unordered list
    return printed_list
        
if __name__ == "__main__":
    app.run(debug=True)
    