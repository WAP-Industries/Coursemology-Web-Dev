import sys;sys.dont_write_bytecode = 1 # prevent python from generating the __pycache__ bytecode
from flask import Flask, render_template, request, redirect, url_for
from db_handler import *

app = Flask(__name__)

# root endpoint
@app.route("/")
def index():
    return render_template("index.html")

# form endpoint
@app.route("/form/", methods=["GET", "POST"])
def form():
    # if post request was made, the user posted a new message, so we add it to our database and connect to the success endpoint
    if request.method=="POST":
        query_db(f"""INSERT INTO posting (username, email, message) VALUES {tuple(i.strip() for i in request.form.values())}""")
        return redirect(url_for("success"))
    
    # otherwise, just render the page
    else:
        return render_template("form.html")

# success endpoint
@app.route("/success/")
def success():
    # selects all entries in our database and renders it
    return render_template("success.html", records=query_db("SELECT * FROM posting"))

# update endpoint
@app.route("/update/", methods=["POST"])
def update():
    # get both the posting id and the message from the post request
    id, message = request.get_json().values()
    # use sql to get the message with the matching posting id and update it
    return query_db(f'UPDATE posting SET message="{message}" WHERE id={id}')

# delete endpoint
@app.route("/delete/", methods=["POST"])
def delete():
    # delete the entry with the matching posting id from our post request
    return query_db(f"DELETE FROM posting where id={request.get_json()['id']}")

if __name__=="__main__":
    app.run(debug=1)    