from bs4 import BeautifulSoup 
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
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

soup = BeautifulSoup(html, "html.parser")
# print(soup)
# print(soup.body)
# print(soup.body.div)
# print(soup.find("div"))
# print(soup.find_all("div"))
# print(soup.find_all("li"))

# Selecting by id
# print(soup.find(id="first"))

# Selecting by class 
# print(soup.find_all(class_="special"))

# Selecting by attribute 
# print(soup.find_all(attrs={"data-example": "yes"}))

# Selecting by css selectors
# d = soup.select("#first")[0]
# print(d)

# d = soup.select(".special")
# print(d)

# d = soup.select("div")
# print(d)

# d = soup.select("[data-example]")
# print(d)

# Accessing data in elements 

#get_text()
# for el in soup.select(".special"):
#   print(el.get_text())

#name
# for el in soup.select(".special"):
#   print(el.name)

#attrs
# for el in soup.select(".special"):
#   print(el.attrs["class"])

# attr = soup.find("h3")["data-example"]
# attr = soup.find("div")["id"]
# print(attr)

# Navigating with beautiful soup 

# data = soup.body.contents[1].contents
# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_="super-special").parent.parent
# data = soup.find(id="first").find_next_sibling()
# data = soup.find(id="first").next_sibling
# data = soup.find(id="first").find_next_sibling().find_next_sibling()
# data = soup.select("[data-example]")[1].find_previous_sibling()

# data = soup.find("h3").find_parent()
data = soup.find("h3").find_parent("html")

print(data)
# print(type(soup))