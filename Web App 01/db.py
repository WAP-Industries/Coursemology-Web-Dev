import sqlite3

# general purpose function to get results of database queries
def QueryDB(query):
    # connect to the database
    conn = sqlite3.connect("insurance.db")
    # execute the query and get all results
    results = conn.execute(query).fetchall()
    # close the connection
    conn.close()
    return results

# Task 1.3
def GetPerf(name, year):
    """
    join the policy record table and the agent tables
    then filter out results where the agent name and year matches
    to check the year we use substring() to get the first 4 characters in the date
    then just select the necessary columns
    """
    return QueryDB(
        f"""
        SELECT PolicyRecordNo, StartDate, Agent.AgentID, Name, PolicyID FROM Agent 
        INNER JOIN PolicyRecord ON Agent.AgentID = PolicyRecord.AgentID
        WHERE Agent.Name = "{name}" and SUBSTRING(StartDate, 1, 4) = "{year}"
        """
    )