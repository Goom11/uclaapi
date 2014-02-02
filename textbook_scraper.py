from bs4 import BeautifulSoup

def single():
    soup = BeautifulSoup(open("/Users/Lowell/Desktop/single_textbook.html"))
    
    title = str(soup.tbody.a.text).strip()
    
    bar = soup.findAll('div', id=lambda x: x and x.endswith('SKU'))
    SKU = str(bar[0].text).strip()[5:]
    
    textbook = {
        "title": title,
        "SKU": SKU
    }
    
    print textbook

def main():
    print "sane"

if __name__ == "__main__":
        main()
