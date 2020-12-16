from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
print('test')
print(soup)
print(type(soup))
print(soup.body)
print(soup.title)
print('##########find all#####')
d = soup.find_all('div')
print(d)
print(d[1])
print('########## id selector using find ##############')
print(soup.find(id='first'))
print('########### class_ selector using find ###########')
print(soup.find_all(class_ = 'special'))
print('########### attribute selector ##########')
print(soup.find_all(attrs = {'data-example': 'yes'}))
print('########### css style selector using select ##############')
print(soup.select('#first')[0])
print(soup.select('.special'))
print(soup.select('div'))
print(soup.select('[data-example]'))