from ast import Param
import logging
import azure.functions as func
import mysql.connector
import json

def main(req: func.HttpRequest) -> func.HttpResponse:

    cnx = mysql.connector.connect(
        user="dododo",
        password='Hal12345',
        host="omoikane-db.mysql.database.azure.com",
        port=3306,
        database="omoikane_db",
    )

    #get
    name = req.params.get('name')

    try:
        cursor = cnx.cursor()
        # Select databases
        cursor.execute("SELECT JapaneseLanguage,Arithmetic,English,Science,SocialStudies FROM userData WHERE userId = '"+ name +"'")
        result_list = cursor.fetchall()

        # Build result response text
        field = []
        for row in result_list:
            for v in row:
                temp = []
                value = []
                temp.append(v.split(','))
                for i in temp:
                    for o in i:
                        sp = o.find(' ')
                        value.append(o[0:sp])
                    field.append(value)

        params = {
            'ProblemID':name,
        }
        
        json_str = json.dumps(params, ensure_ascii=False, indent=2)

        # cnx.commit()
        cursor.close()
        cnx.close()

        return func.HttpResponse(
            # f"Hello, {choiceWord}/{words}/{userId}/{schoolYear}",
            json_str,
            status_code=200
        )

    except:
        return func.HttpResponse(
        "error",
        status_code=200
        )
