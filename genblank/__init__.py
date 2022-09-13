import logging
# from nis import cat

import azure.functions as func
import mysql.connector
import requests
import json
import requests
from bs4 import BeautifulSoup
import re

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
    notChoiceWord = req.get_json().get('notChoiceWord')
    userId = req.get_json().get('userId')
    schoolYear = req.get_json().get('schoolYear')
    subject = req.get_json().get('subject')
    field = req.get_json().get('field')
    divId = 2;

    #get
    url = "https://renso-ruigo.com/word/" + choiceWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    elems = soup.find_all(href=re.compile("renso-ruigo.com/word/"))
    words = choiceWord + ","
    i = 0
    cnt = 0
    while True:
        if cnt == 3:
            break
        if elems[i].contents[0] != choiceWord:
            words += elems[i].contents[0] + ","
            cnt = cnt+1
        i = i+1

    try:
        # Insert database
        cursor = cnx.cursor()
        sql = f"insert into questions(choiceWord, notChoiceWord, words, userId, schoolYear, subject, field, divId) VALUES ('{choiceWord}','{notChoiceWord}','{words}',{userId},{schoolYear},'{subject}','{field}','{divId}');"
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
