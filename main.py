import requests
import bs4 
res = requests.get('https://www.who.int/news-room/releases')
soup = bs4.BeautifulSoup(res.text,'html.parser')
headlines = soup.findAll('div', {'class': 'list-view--item vertical-list-item'})
i = 0
for line in headlines:
    headline =soup.findAll('p', {'class': 'heading text-underline'})[i].text
    print(headline)
    timeStamp = soup.findAll('span', {'class': 'timestamp'})[i].text
    print(timeStamp)
    i=i+1
    print("\n")

with open('list.txt','r+') as textfile:
    headlines = soup.findAll('div', {'class': 'list-view--item vertical-list-item'})
    i = 0
    textfile.write("\t\tWHO \n")
    for line in headlines:
        headline =soup.findAll('p', {'class': 'heading text-underline'})[i].text
        print(headline)
        timeStamp = soup.findAll('span', {'class': 'timestamp'})[i].text
        print(timeStamp)
        i=i+1
        pageline = "{num}.\nheadline: {head}\nPublished on: {Date}\n".format (
            num=i,
            head=headline,
            Date=timeStamp
        )
        textfile.write(pageline)