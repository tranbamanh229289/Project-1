try:
    f = open('../data/nytimes_news_articles.txt', mode='r', encoding='utf-8');
    a=f.readlines()
finally:
    f.close()
URL = "URL: http://www.nytimes.com/"
N_URL = len(URL)
j=2
for i in range(1001):
    namefile = '../data/articles/nytimes' + str(i) + ".txt"
    try:
        f=open(namefile, mode='w', encoding='utf-8')
        while True:
            if (a[j][:N_URL] != URL and a[j+1] != "/n"):
                f.write(a[j])
                j=j+1
            else:
                j=j+2
                break
    finally:
        f.close()

