from bs4 import BeautifulSoup
import requests

response = requests.get("http://www.gabrielfreire.com.br")
html = response.text

# with open("scrapped.html", "w") as f:
    # f.write(html)

soup = BeautifulSoup(html, 'html.parser')
ass = soup.find_all('section')[3]

# get images
imgs = soup.find_all('section')[3].select('.img-responsive')
srcs = []

# get attribute src from images
for img in imgs:
    srcs.append(img['src'])

# displays
print(srcs)


# by_id = soup.find(id="some_id")
# by_class = soup.find(class_="some_class")
# by_attr = soup.find(attrs={"data-hello": "hi"}) { attrName: value }
# by_css_selector = soup.select("#section-1") # out list
# by_css_selector = soup.select("#section-1")[0] # out one
# by_css_selector = soup.select(".some_class")[0] # out one
# by_css_selector_get_text = soup.select(".some_class").get_text() # out the text