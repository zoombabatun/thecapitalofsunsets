from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


months=['yanvarya','fevralya','marta','aprelya','maya','iunya','iulya','avgusta','sentyabrya','oktyabrya','noyabrya','dekabrya']
def getFilmsByDate(day, month):
    #open start page
    url = 'https://www.afisha.ru/nnovgorod/schedule_cinema/'+day+'-'+months[month-1]+'/'
    page = urlopen(url)
    html_ = page.read().decode('utf-8')
    soup = BeautifulSoup(html_, 'html.parser')
    strings = soup.find_all(class_="CjnHd y8A5E nbCNS yknrM")
    resultnames = []
    links = []
    descriptions = []
    descriptionstr = []
    #get film names and links for descriptions
    for name in strings:
        resultnames.append(re.search('>(.+?)<', str(name)).group(1))
        links.append(findHref(str(name)))
    #get descripnions
    i=resultnames.index('Мастер и Маргарита')
    links.pop(i)
    resultnames.pop(i)
    for link in links:
        url = 'https://www.afisha.ru'+link
        page = urlopen(url)
        html_ = page.read().decode('utf-8')
        soup = BeautifulSoup(html_, 'html.parser')
        string = soup.find_all(class_ ="aEVDY t1V2l")
        descriptions.append(string)
    # format descriptions
    for desc in descriptions:
        descriptionstr.append(str(desc))

    for i in range(len(descriptionstr)):

        while True:
            if(descriptionstr[i].find('<')==-1):
                descriptionstr[i]=descriptionstr[i][1:-1]
                break
            else:
                descriptionstr[i] = re.sub('<(.+?)>','',descriptionstr[i])






    return(resultnames, links,descriptionstr)

def findHref(str):
    start=str.find('href="')
    end=str.find('"', start+6)
    return(str[start+6:end])

films,links,descript=getFilmsByDate('11',3)

# print(links)
#for i in range(len(films)):
#    print(films[i]+'\n'+descript[i]+'\n------------------------------------------\n\n\n')

