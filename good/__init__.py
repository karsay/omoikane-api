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
        # Insert database
        cursor = cnx.cursor()
        # sql = f"insert into questions(choiceWord, words, userId, schoolYear, subject, field) VALUES ('{choiceWord}','{words}',{userId},{schoolYear},'{subject}','{field}');"
        # cursor.execute(sql)

        # Select databases
        cursor.execute("SELECT * FROM userData WHERE userId = '90032'")
        result_list = cursor.fetchall()

        # Build result response text
        # result_str_list = []
        # for row in result_list:
        #     row_str = ', '.join([str(v) for v in row])
        #     result_str_list.append(row_str)
        # result_str = '\n'.join(result_str_list)
        field = []
        cnt = 0
        for row in result_list:
            for v in row:
                field.append(v)

        params = {
            'JapaneseLanguage':field[0],
            'Arithmetic':field[1],
            'English':field[2],
            'Science':field[3],
            'SocialStudies':field[4],
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
