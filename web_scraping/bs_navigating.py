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
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
print(soup)
print('##### navigating using tags ######')
print('##### ascending down into contents #####')
print('########## soup.body.contents ###########')
data = soup.body.contents #selects the entire body and everything inside it.
print(data)
print('####### soup.body.contents[1] #############')
data = soup.body.contents[1]
print(data)
print('########## soup.body.contents[1].contents ############')
data = soup.body.contents[1].contents
print(data)

print('###### navigating across siblings #########')
data = soup.body.contents[1].next_sibling.next_sibling  #the first next_sibling takes you to the '/n' new line so we need to access 2 next siblings
print(data)

print('####### going up a level using .parent #####')
data = soup.find(class_ = 'special').parent
print(data)
print('##### going up 2 levels using .parent.parent ######')
data = soup.find(class_ = 'special').parent.parent
print(data)

print('###### next sibling using find_next_sibling() ######')
data = soup.find(id = 'first').find_next_sibling()  
#only need find_next_sibling() once, unlike .next_sibling because
#find_next_sibling skips the first '/n' character while .next_sibling does not skip it.
#skips the newline character until it finds an actual instance of an element
print(data)
print('##### chaining find_next_siblings() together ######')
data = soup.find(id = 'first').find_next_sibling().find_next_sibling()
print(data)
print('##### previous siblings #####')
data = soup.select('[data-example]')[1].find_previous_sibling()
print(data)

print('###### selecting next sibling based on a class name of the sibling ########')
data = soup.find(class_ = 'super-special').find_next_sibling(class_ = 'special')
print(data)

print('#### finding a parent ######')
data = soup.find('h3').find_parent()
print(data)
print('##### find parent with a given tag .find_parent("html") #####')
data = soup.find('h3').find_parent('html')
print(data)