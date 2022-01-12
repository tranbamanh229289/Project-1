import pymysql.cursors
try:
    file = open('../data/nytimes_news_articles.txt', mode='r', encoding='utf-8')
    articles=file.readlines()
finally:
    file.close()

try:
    conn = pymysql.connect(host='localhost',
                           user='root',
                           db='project1',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor )
except:
    print ("connect fail")

def insert(data, table):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO " + table + " (content) VALUES (%s)"
        val=[]
        for item in data:
            val.append((item['header'], item['content']))
        cursor.executemany(sql, val)
        conn.commit()
    finally:
        conn.close()

# insert(trending,'trending')
insert(, 'articles')
# insert(editors,'editors')
