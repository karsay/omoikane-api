import logging
# from nis import cat

import azure.functions as func
import mysql.connector
import requests
import json

def main(req: func.HttpRequest) -> func.HttpResponse:

    cnx = mysql.connector.connect(
        user="dododo",
        password='Hal12345',
        host="omoikane-db.mysql.database.azure.com",
        port=3306,
        database="omoikane_db",
    )

    #post
    sortWords = req.get_json().get('sortWords')
    notChoiceWord = req.get_json().get('notChoiceWord')
    userId = req.get_json().get('userId')
    schoolYear = req.get_json().get('schoolYear')
    subject = req.get_json().get('subject')
    field = req.get_json().get('field')
    divId = 3;

    #get
    words = ""

    try:
        # Insert database
        cursor = cnx.cursor()
        sql = f"insert into questions(choiceWord, notChoiceWord, words, userId, schoolYear, subject, field, divId) VALUES ('{sortWords}','{notChoiceWord}','{words}',{userId},{schoolYear},'{subject}','{field}','{divId}');"
        cursor.execute(sql)

        # Select databases
        cursor.execute("SELECT MAX(ID) FROM questions")
        result_list = cursor.fetchall()

        # Build result response text
        result_str_list = []
        for row in result_list:
            row_str = ', '.join([str(v) for v in row])
            result_str_list.append(row_str)
        result_str = '\n'.join(result_str_list)

        cnx.commit()
        cursor.close()
        cnx.close()

        return func.HttpResponse(
            json.dumps(
            {
                "status":"success",
                "id":result_str
            }),
            status_code=200
        )

    except:
        return func.HttpResponse(
        {
            "status":"error",
        },
        status_code=200
        )
