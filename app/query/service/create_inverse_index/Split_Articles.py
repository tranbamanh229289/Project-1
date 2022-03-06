from app.query.service.constant import URL_LIST_ARTICLES, URL_BASE_ARTICLE, N_ARTICLE

try:
    file = open(URL_LIST_ARTICLES, mode='r', encoding='utf-8')
    a=file.readlines()
finally:
    file.close()
URL = "URL: http://www.nytimes.com/"
N_URL = len(URL)
j=2
for i in range(N_ARTICLE):
    namefile = URL_BASE_ARTICLE + str(i) + ".txt"

    f=open(namefile, mode='w', encoding='utf-8')
    while True:
        if (a[j][:N_URL] != URL and a[j+1] != "/n"):
            f.write(a[j])
            j=j+1
        else:
            j=j+2
            break

