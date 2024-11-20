from imports import *

def accept_conditions(driver): #FUNKCIJA KOJA AUTOMATSKI KLIKA NA PRIHVAĆANJE UVJETA KOJE JE NUŽNU PRIJE PRISTUPA GOOGLE MAPAMA

    buttons = driver.find_elements(By.TAG_NAME, "button")
    button = buttons[3]
    button.click()

def enter_search_prompt(driver, search_prompt): #FUNKCIJA KOJA PRONALAZI PROSTOR ZA PRETRAŽIVANJE NA STRANICI I U NJEGA UNOSI POTREBAN TEKST

    searchbox = driver.find_element(By.ID, "searchboxinput")
    searchbox.send_keys(search_prompt)
    time.sleep(1)
    searchbox.send_keys(Keys.RETURN)
    time.sleep(5)

def scroll_results(driver, results, scroll_time): #FUNKCIJA KOJA SKROLA PO REZULTATIMA KAKO BI SE SVI UČITALI
    
    actions = ActionChains(driver)
    actions.move_to_element(results).perform()
    for i in range(scroll_time):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 1000", results)
        time.sleep(2)


