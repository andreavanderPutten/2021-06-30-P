from database.DB_connect import DBConnect
from model.stato import Stato


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getLocalizzazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct c.Localization as localizzazione
         from genes_small.classification c"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row["localizzazione"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select c.Localization as loc1, c2.Localization as loc2,count(distinct i.`Type`) as peso  
        from genes_small.interactions i , genes_small.classification c, genes_small.classification c2 
        where c.Localization > c2.Localization and ((c.GeneID = i.GeneID1 and c2.GeneID  = i.GeneID2 ) or (c2.GeneID  = i.GeneID1 and c.GeneID = i.GeneID2 ))
        group by c.Localization , c2.Localization """

        cursor.execute(query, )

        for row in cursor:
            result.append([row["loc1"],row["loc2"],row["peso"]])

        cursor.close()
        conn.close()
        return result

