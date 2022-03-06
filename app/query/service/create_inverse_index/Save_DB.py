import pymysql.cursors
from app.query.service.constant import URL_BASE_ARTICLE, N_ARTICLE

try:
    conn = pymysql.connect(host='localhost',
                           user='root',
                           db='project1',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor )
except:
    print ("connect fail")
val=[]
for i in range(0, N_ARTICLE):
    with open(URL_BASE_ARTICLE+ f'{i}' + '.txt', 'r', encoding='utf-8') as f:
        str = f.read()
        header=""
        j=0
        while str[j] != "." or j<70:
            header += str[j]
            j=j+1
    val.append((i, header, str))

try:
    cursor = conn.cursor()
    sql = "INSERT INTO " + "query_article" + " (id_article, title, content) VALUES (%s, %s, %s)"
    cursor.executemany(sql, val)
    conn.commit()
finally:
    conn.close()





