from ast import Param
import logging
from posixpath import split
from re import A
import azure.functions as func
import mysql.connector
import json
import random

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
    subject = req.get_json().get('subject_ID')

    try:
        # Insert database
        cursor = cnx.cursor()
        sql = "SELECT * FROM questions WHERE subject LIKE '"+ subject +"%'"
        # Select databases
        # cursor.execute("SELECT * FROM questions WHERE id = '5'")
        cursor.execute(sql)
        result_list = cursor.fetchall()

        """"
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
        """

        list = []
        list2 = []
        dict = {}

        for row in result_list:

            for v in row:
                # print("v:", v)
                list.append(v)

                # 回答群シャッフル
                if "list[3]" in locals():
                    list[3] = list[3].split(",")

                    def rand():
                        rand = random.randint(0,3)
                        return rand

                    for i in range(10):
                        num1 = rand()
                        num2 = rand()
                        str1 = list[3][num1]
                        str2 = list[3][num2]
                        list[3][num1] = str2
                        list[3][num2] = str1

            if "v" in locals():
                dict["question_ID"] = list[0]
                dict["question_answer"] = list[1]
                dict["question_text"] = list[2]
                dict["question_fakeanswer"] = list[3]
                dict["question_creator"] = list[4]
                dict["subject"] = list[5]
                dict["question_fieldID"] = list[6]

                # print("dict:",dict)
                list2.append(dict)

                dict = {}
                list.clear()
                # print("list:", list)

        json_str = json.dumps(list2, ensure_ascii=False, indent=2)
        # print("list2:" ,list2)

        # cnx.commit()
        cursor.close()
        cnx.close()

        return func.HttpResponse(
            json_str,
            status_code=200
        )

    except:
        return func.HttpResponse(
        json.dumps(
            {
                "status":"error"
            }),
            status_code=400
        )
