

# make the request, get the response back
# take the html we get back, send it through bs
# navigate through the bs, extract the info we want
# and write it to a csv


import requests as r
from bs4 import BeautifulSoup as bs
from csv import writer


response = r.get('https://www.rithmschool.com/blog')
#print(response.text)



soup = bs(response.text, 'html.parser')
#print(soup)
#since all the info we're looking for is inside each of the article tags we can
#save all the articles in a list called articles

articles = soup.find_all('article')
print(articles)

#open the file to write you want to write
with open('blog_data.csv', 'w', newline = '') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(['title', 'link', 'date'])
    #for each article we can get the title
    for article in articles:
        a_tag = article.find('a')
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find('time')['datetime']
        csv_writer.writerow([title,url,date])

