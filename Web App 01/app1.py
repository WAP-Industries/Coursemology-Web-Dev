import sys; sys.dont_write_bytecode = 1 # prevent python from generating the __pycache__ bytecode
from flask import Flask, render_template, request
from db import *

# create our app
app = Flask("limpeh")

# root endpoint
@app.route("/")
def index():
    return render_template("app 1/index.html")

# results endpoint
@app.route("/results/")
def results():
    """
    join the policy record and customer tables
    then filter out all entries where the customer name matches (we use request.args to access the user's search)
    then select all necessary columns

    also pass in the results under the records keyword argument, so that jinja can access it later
    """
    return render_template(
        "app 1/results.html", 
        records=QueryDB(
            f"""
            SELECT PolicyRecordNo, AgentID, Customer.CustomerID, PolicyID, StartDate FROM Customer
            INNER JOIN PolicyRecord ON Customer.CustomerID = PolicyRecord.CustomerID
            WHERE Customer.Name="{request.args["customer"]}"
            """
        )
    )

# policy endpoint, <string:id> is a parameter that will take in the policy name
@app.route("/policy/<string:id>")
def policy(id):
    # select all entries where the policy id matches
    return render_template(
        "app 1/policy.html",
        record=QueryDB(f"SELECT * from Policy WHERE PolicyID='{id}'")[0]
    )

if __name__=="__main__":
    app.run(debug=1)