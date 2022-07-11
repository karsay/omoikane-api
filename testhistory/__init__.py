from ast import Param
import logging
import azure.functions as func
import mysql.connector
import json

def main(req: func.HttpRequest) -> func.HttpResponse:

    # cnx = mysql.connector.connect(
    #     user="dododo",
    #     password='Hal12345',
    #     host="omoikane-db.mysql.database.azure.com",
    #     port=3306,
    #     database="omoikane_db",
    # )

    cnx = mysql.connector.connect(
        user="fukui",
        password='fukui',
        host="localhost",
        port=3306,
        database="omoikane_db",
    )

    #get
    #name = req.params.get('name')
    userId = req.route_params.get('userId')

    try:
        # Insert database
        cursor = cnx.cursor()

        # Select databases
        cursor.execute("SELECT subject,field,score,testDay FROM userData WHERE userId = '"+ userId +"'")
        result_list = cursor.fetchall()

        list = []
        
        for row in result_list:
            for v in row:
                listTemp = []
                for i in v.split(','):
                    listTemp.append(i)
                list.append(listTemp)

        params = {
            'subject':list[0],
            'field':list[1],
            'score':list[2],
            'testday':list[3],
        }
        
        json_str = json.dumps(params, ensure_ascii=False, indent=2)

        # cnx.commit()
        cursor.close()
        cnx.close()

        return func.HttpResponse(
            json_str,
            status_code=200
        )

    except:
        return func.HttpResponse(
        "error",
        status_code=200
        )
