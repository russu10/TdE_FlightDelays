from database.DB_connect import DBConnect
from model.airport import Airport
from model.archi import Arco


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result


    def getAllCompagnie():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result

    def getNumCompagnie(airportId):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT COUNT(DISTINCT f.AIRLINE_ID) AS cTot
            FROM flights f
            WHERE f.ORIGIN_AIRPORT_ID = %s OR f.DESTINATION_AIRPORT_ID = %s
        """

        cursor.execute(query, (airportId, airportId))  # Passaggio corretto dei parametri

        row = cursor.fetchone()  # Ottieni una sola riga
        cTot = row["cTot"] if row else 0  # Gestione caso vuoto

        cursor.close()
        conn.close()

        return cTot

    def getAllArchi(a1,a2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT COUNT(*) AS peso
                        FROM flights f
                        WHERE (f.ORIGIN_AIRPORT_ID = %s AND f.DESTINATION_AIRPORT_ID = %s)
                           OR (f.ORIGIN_AIRPORT_ID = %s AND f.DESTINATION_AIRPORT_ID = %s)"""

        cursor.execute(query,(a1,a2,a2,a1))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row and row["peso"] > 0:
            return Arco(a1, a2, row["peso"])
        else:
            return None