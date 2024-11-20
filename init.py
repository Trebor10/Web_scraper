#INCIJALIZACIJA SELEKTORA
def initialize_selectors():

    print("Unesite 1 ukoliko želite dohvbatiti navedeni podatak, 0 inače. \n")
    adress_selector = int(input("Adresa: "))
    working_hours_selector = int(input("Radno vrijeme: "))
    web_link_selector = int(input("Web: "))
    phone_number_selector = int(input("Broj telefona: "))
    instagram_selector = int(input("Instagram: "))
    facebook_selector = int(input("Facebook: "))
    linkedin_selector = int(input("Linkedin: "))
    if not web_link_selector:
        instagram_selector = facebook_selector = linkedin_selector = 0

    return [adress_selector, working_hours_selector, web_link_selector, phone_number_selector, instagram_selector, facebook_selector, linkedin_selector]

