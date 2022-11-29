import pymysql as MySql
def ConnectionPooling():
    DB=MySql.Connect(host='localhost',port=3306,user='root',password='Abhishek@2912',database='medassist_com',cursorclass=MySql.cursors.DictCursor)
    CMD = DB.cursor()
    return DB,CMD