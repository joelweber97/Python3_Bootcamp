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

el = soup.select('.special')[0]  #saves the first instance of the class_ special to el
print(el)
print(el.get_text())  #this actually retrieves the text from inside it.
print(type(el.get_text()))


#can also run a for loop to get all the text from everything with class_  special
print('########## for loop to get_text ############')
for el in soup.select('.special'):
    print(el.get_text())

print('######## for loop to get tag names ##############')
for el in soup.select('.special'):
    print(el.name)

print('######### for loop to get attributes ###########')
for el in soup.select('.special'):
    print(el.attrs)



attr = soup.find('h3')['data-example']
print(attr)

attr = soup.find('div')['id']
print(attr)












