import logging

import azure.functions as func
import mysql.connector

def main(req: func.HttpRequest) -> func.HttpResponse:

    cnx = mysql.connector.connect(
        user="dododo",
        password='Hal12345',
        host="omoikane-db.mysql.database.azure.com",
        port=3306,
        database="omoikane_db",
    )

    #post
    choiceWord = req.get_json().get('choiceWord')
    words = req.get_json().get('words')
    userId = req.get_json().get('userId')
    schoolYear = req.get_json().get('schoolYear')
    subject = req.get_json().get('subject')
    field = req.get_json().get('field')

    #get
    #name = req.params.get('name')

    try:
        # Insert database
        cursor = cnx.cursor()
        sql = f"insert into questions(choiceWord, words, userId, schoolYear, subject, field) VALUES ('{choiceWord}','{words}',{userId},{schoolYear},'{subject}','{field}');"
        cursor.execute(sql)

        # Select databases
        cursor.execute("SELECT * FROM questions")
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
            # f"Hello, {choiceWord}/{words}/{userId}/{schoolYear}",
            result_str,
            status_code=200
        )

    except:
        return func.HttpResponse(
        "error",
        status_code=200
        )
