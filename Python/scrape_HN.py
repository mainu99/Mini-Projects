import requests
from bs4 import BeautifulSoup
import pprint       #to get prettier terminal op

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)
def get_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()      #links[idx].getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote) > 0:
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
pprint.pprint(get_custom_hn(links, subtext))
print('\n-----------------------------------\n')

morelink = soup.select('.morelink')
href2 = morelink[0].get('href', None)
res2 = requests.get('https://news.ycombinator.com/news'+href2)
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')
s2 = get_custom_hn(links2, subtext2)
pprint.pprint(s2)