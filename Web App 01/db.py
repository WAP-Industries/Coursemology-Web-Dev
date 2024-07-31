import sqlite3

def QueryDB(query):
    conn = sqlite3.connect("insurance.db")
    results = conn.execute(query).fetchall()
    conn.close()
    return results

# Task 1.3
def GetPerf(name, year):
    return QueryDB(
        f"""
        SELECT PolicyRecordNo, StartDate, Agent.AgentID, Name, PolicyID FROM Agent 
        INNER JOIN PolicyRecord ON Agent.AgentID = PolicyRecord.AgentID
        WHERE Agent.Name = "{name}" and SUBSTRING(StartDate, 1, 4) = "{year}"
        """
    )