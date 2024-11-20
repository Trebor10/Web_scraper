from imports import *

def find_results(driver, search_prompt): #FUNKCIJA KOJA PRONALAZI CONTAINER S REZULTATIMA ZA UPIT NA STRANICI
    
    return driver.find_element(By.CSS_SELECTOR, f'[aria-label="Rezultati za upit {search_prompt}"]')

def find_maps_links_and_names(html_list, urls=[], names=[]): #FUNKCIJA KOJA ZA SVAKI REZUTLAT PRONALAZI IME I LINK

    for elem in html_list:
        match = re.search(r'aria-label="[^"]*"[^>]*?href="[^"]*"', elem)
        if match:
            match_text = match.group()
            if "Posjetite web-lokaciju mjesta" and "Oglas" not in match_text:
                web_link = match_text.split('"')[3]
                urls.append(web_link)
                match2 = re.search(r'aria-label=".*?"', elem)
                if match2:
                    names.append(match2.group().replace("&quot;", '\\"').replace("&amp;", "\\&").replace("&lt;", "\\<").replace("&gt;", "\\>")[12:-1])
    
    return names, urls