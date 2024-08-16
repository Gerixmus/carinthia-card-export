from destination import Destination
from soup import return_soup
from timing import timeit

def update_info(destination):
    dest_soup = return_soup(destination.url)
    p = dest_soup.find('div', 'content-txt').find('p')
    destination.description = p.text
    
    h4 = dest_soup.find('div', 'kontakt-box').findAll('a')
    destination.contact_info = [i.text for i in h4]
    
url = "https://www.kaerntencard.at/sommer/en/ausflugsziele-uebersicht/"
soup = return_soup(url)

#TO-DO rewrite to use multithreading
@timeit
def fetch_destinations():
    excursion_destinations = []
    for div in soup.find_all('div', class_='col-lg-6 col-11 align-self-center'):
        destination = Destination()
        h3 = div.find('div', class_='txt-box').find('h3')
        if(h3 == None):
            continue   
        destination.name = h3.text
        
        destination.url = div.find('a', class_='btn-std')['href']
        update_info(destination)
        excursion_destinations.append(destination)
    
    return excursion_destinations

excursion_destinations = fetch_destinations()