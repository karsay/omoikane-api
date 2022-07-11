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
        cursor.execute("SELECT JapaneseLanguage,Arithmetic,English,Science,SocialStudies FROM userData WHERE userId = '"+ userId +"'")
        result_list = cursor.fetchall()

        threshold = 30
        genre = []
        score = []
        for row in result_list:
            for v in row:
                temp = []
                genretemp = []
                scoretemp = []
                temp.append(v.split(','))
                for i in temp:
                    for o in i:
                        sp = o.find(' ')
                        if int(o[sp+1:]) <= threshold:
                            genretemp.append(o[0:sp])
                            scoretemp.append(o[sp+1:])
                    genre.append(genretemp)
                    score.append(scoretemp)

        params = {
            'JapaneseLanguage':genre[0],
            'Arithmetic':genre[1],
            'English':genre[2],
            'Science':genre[3],
            'SocialStudies':genre[4],
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
