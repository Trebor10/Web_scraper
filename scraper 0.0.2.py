from imports import *
from init import *
from config import *
from misc import *
from find import *
from get import *

#KORISNIK UNOSI SEARCH PROMPT I INCIJALIZACIJA SELEKTORA
search_prompt = str(input("Search prompt: "))
selectors = initialize_selectors()

#INICIJALIZACIJA DRIVERA
driver = webdriver.Chrome()
driver.get('https://www.google.com/maps')

#PRIHVAĆANJE UVJETA
accept_conditions(driver)

#PRETRAŽIVANJE GOOGLE MAPA
enter_search_prompt(driver, search_prompt)

#PRONALZAK REZULTATA I SKROLANJE PO NJIMA KAKO BI SE UČITALI SVI ELEMENTI
results = find_results(driver, search_prompt) 
scroll_results(driver, results, search_time)

#DOHVAĆANJE HTML SVIH REZULTAT I EKSTRAKCIJE IMENA I LINKA NA SVAKI REZULTAT
results_htmls = get_results_html(driver, results)
names, urls = find_maps_links_and_names(results_htmls)

#ODLAZAK NA LINK SVAKOG MJESTA I DOHVAĆANJE POTREBNIH INFORMACIJA
final_info = get_information_from_urls(driver, urls, names, selectors)

#ISPIS INFORMACIJA (RASPORED: [IME, ADRESA, RADNO_VRIJEME, WEB_LINK, BROJ_TELEFONA, INSTAGRAM, FACEBOOK, LINKEDIN])
print(final_info)
  
