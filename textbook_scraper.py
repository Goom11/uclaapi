from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/Users/Lowell/Desktop/textbooks.html"))

title = str(soup.tbody.a.text).strip()
# print "{%r}" % title 

bar = soup.findAll('div', id=lambda x: x and x.endswith('SKU'))
SKU = str(bar[0].text).strip()[5:]
# print "{%r}" % SKU

textbook = {
    "title": title,
    "SKU": SKU
}

print textbook
