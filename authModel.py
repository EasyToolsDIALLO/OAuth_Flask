from authPayload import authPayload
from authResponse import authResponse
import jwt
import os
import json

# pip install psycopg2
import psycopg2

# pip install -U python-dotenv
from dotenv import load_dotenv
datas = load_dotenv()


def create(clientId, clientSecret, isAdmin):

    conn = None
    print("{},{},{}".format(clientId, clientSecret, isAdmin))
    try:
        # conn = None
        query = "insert into clients (\"ClientId\", \"ClientSecret\", \"IsAdmin\") values(%s,%s,%s)"
        """conn = psycopg2.connect("dbname=data_jwt" + os.environ.get("DBNAME") +
                                " user=" + os.environ.get("DBUSER") + " password=" + os.environ.get("DBPASSWORD"))"""""
        conn = psycopg2.connect(
<<<<<<< HEAD
            "postgresql://ousmane:bHvnpmqJmhXb9nhEeXa8l5fGewde83iJ@dpg-ci4q6jh8g3ne0dmma9hg-a.oregon-postgres.render.com/data_jwt")
=======
            "postgresql://ousmane:bHvnpmqJmhXb9nhEeXa8l5fGewde83iJ@dpg-ci4q6jh8g3ne0dmma9hg-a/data_jwt")
>>>>>>> 08c35aa6765303c695e2b4fd60b31e10c9513e2d
        cur = conn.cursor()
        cur.execute(query, (clientId, clientSecret, isAdmin))
        conn.commit()
        print("{},{},{}".format(clientId, clientSecret, isAdmin))
        print("CONNECTED")
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            cur.close()
            conn.close()
        print("GET A PROBLEM")
        print("{},{}".format(clientId,
              clientId, clientId))
        return False
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("CONNECTION CLOSED")


<<<<<<< HEAD
def delete_one(clientId):
    conn = None
    try:
        # conn = None
        query = "select * from clients where \"ClientId\"='{}'".format(
            clientId)
        """conn = psycopg2.connect("dbname=data_jwt" + os.environ.get("DBNAME") +
                                " user=" + os.environ.get("DBUSER") + " password=" + os.environ.get("DBPASSWORD"))"""""
        conn = psycopg2.connect(
            "postgresql://ousmane:bHvnpmqJmhXb9nhEeXa8l5fGewde83iJ@dpg-ci4q6jh8g3ne0dmma9hg-a.oregon-postgres.render.com/data_jwt")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("CONNECTED")
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            cur.close()
            conn.close()
        print("GET A PROBLEM")
        return False
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("CONNECTION CLOSED")


def delete_all():
    conn = None
    try:
        # conn = None
        query = "select * from clients where"
        """conn = psycopg2.connect("dbname=data_jwt" + os.environ.get("DBNAME") +
                                " user=" + os.environ.get("DBUSER") + " password=" + os.environ.get("DBPASSWORD"))"""""
        conn = psycopg2.connect(
            "postgresql://ousmane:bHvnpmqJmhXb9nhEeXa8l5fGewde83iJ@dpg-ci4q6jh8g3ne0dmma9hg-a.oregon-postgres.render.com/data_jwt")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("CONNECTED")
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            cur.close()
            conn.close()
        print("GET A PROBLEM")
        return False
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("CONNECTION CLOSED")


def update(clientId, clientSecret):
    pass


=======
>>>>>>> 08c35aa6765303c695e2b4fd60b31e10c9513e2d
def authenticate(clientId, clientSecret):

    conn = None
    query = "select * from clients where \"ClientId\"='{}' and \"ClientSecret\"='{}'".format(
        clientId, clientSecret)

    try:
        conn = psycopg2.connect(
<<<<<<< HEAD
            "postgresql://ousmane:bHvnpmqJmhXb9nhEeXa8l5fGewde83iJ@dpg-ci4q6jh8g3ne0dmma9hg-a.oregon-postgres.render.com/data_jwt")
=======
            "postgresql://ousmane:bHvnpmqJmhXb9nhEeXa8l5fGewde83iJ@dpg-ci4q6jh8g3ne0dmma9hg-a/data_jwt")
>>>>>>> 08c35aa6765303c695e2b4fd60b31e10c9513e2d
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchone()

        payload = authPayload(rows[0], rows[1], rows[3])
        encoded_jwt = jwt.encode(
            payload.__dict__, os.environ.get("AUTHSECRET"), algorithm='HS256')
        response = authResponse(
            encoded_jwt, os.environ.get("EXPIRESSECONDS"), rows[3])
        '''for row in rows:
            isAdmin = row[3]
            payload = authPayload(row[0], row[1], isAdmin)
            break

        
        response = authResponse(
            encoded_jwt, os.environ.get("EXPIRESSECONDS"), isAdmin)'''
        # print("SUCCESS AUTHENTICATION, Data: ", response.__dict__)
        # return payload.__dict__
        return response.__dict__

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        if conn is not None:
            cur.close()
            conn.close()
        print("ERROR AUTHENTICATION")
        return False
    finally:
        if conn is not None:
            cur.close()
            conn.close()


