from imports import *

#DOHVAĆANJE LINKOVA NA SOCIJALNE MREŽE SA WEB-LINKA MJESSTA
def get_social_media_from_web(web_link, selectors):

    if selectors[0] or selectors[1] or selectors[2]:
        social_media = []
        try:
            web_content = requests.get(url=web_link)
            soup = BeautifulSoup(web_content.content, 'html.parser')
            web_content_html = soup.prettify()

            if selectors[0]:
                instagram_link = re.search(r'www\.instagram[^"]*"', web_content_html)
                if instagram_link:
                    social_media.append(instagram_link.group()[:-1])
                else:
                    social_media.append("Nema dostupnog instagrma")
            else:
                social_media.append("")
            
            if selectors[1]:
                facebook_link = re.search(r'www\.facebook[^"]*"', web_content_html)
                if facebook_link:
                    social_media.append(facebook_link.group()[:-1])
                else:
                    social_media.append("Nema dostupnog facebooka")
            else:
                social_media.append("")

            if selectors[2]:
                linkedin_link = re.search(r'www\.linkedin[^"]*"', web_content_html)
                if linkedin_link:
                    social_media.append(linkedin_link.group()[:-1])
                else:
                    social_media.append("Nema dostupnog linkedina")
            else:
                social_media.append("")

            return social_media
            
        except requests.exceptions.Timeout:
            return ["Nema dostupnog instagrma","Nema dostupnog facebooka","Nema dostupnog linkedina"]
        except requests.exceptions.ConnectionError:
            return ["Nema dostupnog instagrma","Nema dostupnog facebooka","Nema dostupnog linkedina"]
        except requests.exceptions.HTTPError:
            return ["Nema dostupnog instagrma","Nema dostupnog facebooka","Nema dostupnog linkedina"]
        except requests.exceptions.RequestException:
            return ["Nema dostupnog instagrma","Nema dostupnog facebooka","Nema dostupnog linkedina"]
    return ["", "", ""]

def get_results_html(driver, results): #FUNKCIJA KOJA VADI HTML U KOJEM SE NALAZE IMENA I LINKOVI SVAKOG POJEDINOG REZULTATA PRETRAŽIVANJA
    
    all_as = results.find_elements(By.TAG_NAME, 'a')
    return [driver.execute_script("return arguments[0].outerHTML;", elem) for elem in all_as]

def get_adress(adress_selector, info_html): #DOHVAĆANJE ADRESE IZ HTMLA INFORMACIJA
    
    if adress_selector:
        adress_regex = re.search(r'aria-label="adresu:[^"]*"', info_html)
        if adress_regex:
            return adress_regex.group()[19:-1]
    return ""

def get_working_hours(working_hours_selector, info_html): #DOHVAĆANJE RADNOG VREMENA IZ HTMLA INFORMACIJA
    
    if working_hours_selector:
        working_hours_regex = re.search(r'aria-label="[^"]*Sakrij radno vrijeme u tjednu"', info_html)
        if working_hours_regex:
            return working_hours_regex.group()[12:-30]
        return "Nema dostupnog radnog vremena"
    return ""

def get_web_link(web_link_selector, info_html): #DOHVAĆANJE WEB LINKA IZ HTMLA INFORMACIJA
    if web_link_selector:
        web_link_regex1 = re.search(r'aria-label="web-lokaciju:[^>]*>', info_html)
        if web_link_regex1:
            web_link_regex2 = re.search(r'href="[^"]*"', web_link_regex1.group())
            return web_link_regex2.group()[6:-1]
        else:
            return "Nema dostupnog linka"
    return ""

def get_phone_number(phone_number_selector, info_html): #DOHVAĆANJE BROJA TELEFONA IZ HTMLA INFORMACIJA

    if phone_number_selector:
        phone_number_regex = re.search(r'aria-label="telefon:.*?"', info_html)
        if phone_number_regex:
            return phone_number_regex.group()[20:-2]
        else:
            return "Nema dostupnog broja telefona"
    return ""

def get_information_from_urls(driver, urls, names, selectors, final_info=[]): #PROLAZAK KROZ LISTU URLOVA I DOHVAĆANJE INFORMACIJE O OBJEKTU
    for i in range(len(urls)):
        driver.get(urls[i])
        time.sleep(5) #TRENUTNO NAJBOLJI BALANS IZMEĐU BRZINE I IZBJEGAVANJA GOOGLOVE DODATNE PORVJERE (POTREBNO JOŠ TESTIRANJA)
        info = driver.find_element(By.CSS_SELECTOR, f'[aria-label="{names[i]}"]')
        info_html = driver.execute_script("return arguments[0].outerHTML;", info)
        current_info = []

        #DOHVAĆANJE SVAKE POJEDINE INFORMACIJE O OBJEKTU
        #RASPORED: [IME, ADRESA, RANDNO_VRIJEME, WEB_LINK, BROJ_TELEFONA, INSTAGRAM, FACEBOOK, LINKEDIN]
        current_info.append(names[i])
        current_info.append(get_adress(selectors[0], info_html))
        current_info.append(get_working_hours(selectors[1], info_html))
        current_info.append(get_web_link(selectors[2], info_html))
        current_info.append(get_phone_number(selectors[3], info_html))
        social_media_links = get_social_media_from_web(current_info[3], selectors[4:])
        current_info += social_media_links

        final_info.append(current_info)
    
    return final_info
                