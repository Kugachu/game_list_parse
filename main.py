import requests
from bs4 import BeautifulSoup as bs

comps = []

def parse():
    HEADERS = {
        'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0' 
    }
    
    comps = []
    
    for index in range(1, 53):
        response = requests.get("https://psdeals.net/tr-store/discounts/" + str(index), headers=HEADERS)
        soup = bs(response.content, 'html.parser')
        items = soup.findAll('div', class_='game-collection-item col-md-2 col-sm-4 col-xs-6')
    
        for item in items:
            comps.append({
                'title': item.find('span', class_="game-collection-item-details-title").get_text(strip = True)
            })
        
    for comp in comps:
        print(comp['title'])
        with open('parse_games_list.txt', 'a') as file:
            file.write(comp['title'] + '\n')
    

parse()
    