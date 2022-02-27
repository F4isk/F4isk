import pymysql.cursors

def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='A19922005a',
                                 db='support',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)


    return connection