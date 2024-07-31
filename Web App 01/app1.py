import sys; sys.dont_write_bytecode = 1
from flask import Flask, render_template, request
from db import *

app = Flask("limpeh")

@app.route("/")
def index():
    return render_template("app 1/index.html")

@app.route("/results/")
def results():
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

@app.route("/policy/<string:id>")
def policy(id):
    return render_template(
        "app 1/policy.html",
        record=QueryDB(f"SELECT * from Policy WHERE PolicyID='{id}'")[0]
    )

if __name__=="__main__":
    app.run(debug=1)