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

    # cnx = mysql.connector.connect(
    #     user="fukui",
    #     password='fukui',
    #     host="localhost",
    #     port=3306,
    #     database="omoikane_db",
    #)

    #post
    id = req.get_json().get('subject_ID')


    try:
        # Insert database
        cursor = cnx.cursor()

        # Select databases
        cursor.execute("SELECT * FROM questions WHERE id = '"+ id +"'")
        result_list = cursor.fetchall()

        list = []

        for row in result_list:
            for v in row:
                list.append(v)
            
        params = {
            "question_ID":list[0],
            "question_creator":list[4],
            "subject":list[6],
            #"question_title":list[2],
            "question_text":list[2],
            "question_answer":list[1],
            "question_fakeanswer":list[3],
            "question_fieldID":list[7],
            #"question_fieldname":"歴史１",
            #"question_type":"1",
            #"question_answerrate":"78.3",
            #"question_respons":"193"
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
