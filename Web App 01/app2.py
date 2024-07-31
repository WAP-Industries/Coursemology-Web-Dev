import sys; sys.dont_write_bytecode = 1
from flask import Flask, render_template, request
from db import *

app = Flask("limpeh")

@app.route("/")
def index():
    return render_template("app 2/index.html")

@app.route("/results/")
def results():
    return render_template(
        "app 2/results.html",
        records=QueryDB(
            f"""
            SELECT 
                Agent.AgentID,
                printf("%.2f", SUM(CASE WHEN SUBSTRING(Startdate, 5, 2) = '01' THEN BaseSalary+CommissionRate*ProtectedSum ELSE 0 END)),
                printf("%.2f", SUM(CASE WHEN SUBSTRING(Startdate, 5, 2) = '02' THEN BaseSalary+CommissionRate*ProtectedSum ELSE 0 END)),
                printf("%.2f", SUM(CASE WHEN SUBSTRING(Startdate, 5, 2) = '03' THEN BaseSalary+CommissionRate*ProtectedSum ELSE 0 END))
            FROM Agent
            INNER JOIN PolicyRecord ON Agent.AgentID = PolicyRecord.AgentID
            INNER JOIN Policy ON Policy.PolicyID = PolicyRecord.PolicyID
            WHERE TeamNo = {request.args["team"]} AND SUBSTRING(StartDate, 1, 4) = "2020" AND SUBSTRING(Startdate, 5, 2) IN ('01', '02', '03')
            GROUP BY Agent.AgentID;
            """
        )
    )

if __name__=="__main__":
    app.run(debug=1)