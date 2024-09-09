from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi(goal_fatti):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct a.PlayerID as idplayer,sum(a.Goals)/count(*) as rateo 
from premierleague.actions a
group by a.PlayerID
having sum(a.Goals)/count(*) > %s"""

        cursor.execute(query,(goal_fatti,) )

        for row in cursor:
            result.append(row["idplayer"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.PlayerID as id1, a2.PlayerID as id2,(sum(a.TimePlayed) - sum(a2.TimePlayed)) as peso 
from premierleague.actions a , premierleague.actions a2  
where a.PlayerID > a2.PlayerID 
and a2.Starts = 1 
and a.Starts = 1 
and a.MatchID = a2.MatchID 
group by a.PlayerID,a2.PlayerID
having (sum(a.TimePlayed) > sum(a2.TimePlayed))"""

        cursor.execute(query,)

        for row in cursor:
            result.append([row["id1"],row["id2"],row["peso"]])

        cursor.close()
        conn.close()
        return result
