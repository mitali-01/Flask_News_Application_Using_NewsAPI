from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__, static_folder='static')
newsapi = NewsApiClient(api_key='043511dec98a475990018061d1c369fb')

@app.route('/')
def news():
   sources = 'bbc-news,cnn,the-washington-post,the-new-york-times,al-jazeera-english,reuters,the-guardian,time,usa-today,fox-news'
   top_headlines = newsapi.get_top_headlines(sources=sources)
   top_headlines = top_headlines['articles']
   desc = []
   news = []
   img = []
   link = []
   for i in range(len(top_headlines)):
      myarticles = top_headlines[i]
      news.append(myarticles['title'])
      desc.append(myarticles['description'])
      img.append(myarticles['urlToImage'])
      link.append(myarticles['url'])
        
   mylist = zip(news, desc, img, link)
   return render_template('news.html', context=mylist)

if __name__ == '__main__':
   app.run()