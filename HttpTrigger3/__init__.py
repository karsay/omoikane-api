import logging

import azure.functions as func
import mysql.connector

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    cnx = mysql.connector.connect(
        user="dododo",
        password='Hal12345',
        host="omoikane-db.mysql.database.azure.com",
        port=3306,
        database="omoikane_db",
    )

    try:
        # Insert database
        # cursor = cnx.cursor()
        # sql = f"select * from questions;"
        # cursor.execute(sql)
        # sql = f"create table questions (id int AUTO_INCREMENT PRIMARY KEY,choiceWord varchar(255) NOT NULL,notChoiceWord varchar(255) NOT NULL,words varchar(255) NOT NULL,userId int NOT NULL,schoolYear int NOT NULL,subject varchar(255) NOT NULL,field varchar(255) NOT NULL,divId int NOT NULL);"
        # cursor.execute(sql)

        # result_list = cursor.fetchall()

        # result_str_list = []
        # for row in result_list:
        #     row_str = ', '.join([str(v) for v in row])
        #     result_str_list.append(row_str)
        # result_str = '\n'.join(result_str_list)

        # cnx.commit()
        # cursor.close()
        # cnx.close()

        # return func.HttpResponse(f"{name},{result_str}")

        return func.HttpResponse(f"a")

    except:
        return func.HttpResponse(
        {
            "status":"error",
        },
        status_code=200
        )
