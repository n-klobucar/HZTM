from selenium import webdriver
from selenium.webdriver.common.by import By

grupe={"a+":"aplus","a-":"aminus","0+":"zeroplus","0-":"zerominus","b+":"bplus","b-":"bminus","ab+":"abplus","ab-":"abminus"}

unos=input("Upišite krvnu grupu: ").lower()
while(unos not in grupe):
    print("Niste unijeli valjanu krvnu grupu!")
    unos=input("Upišite krvnu grupu: ").lower()

opcije=webdriver.FirefoxOptions()
opcije.headless=True
driver=webdriver.Firefox(options=opcije)

driver.get("https://hztm.hr/zalihe_krvi/")
'''
ako je više od 210px ne moraš ići dati krv

ako je ispod 70px moraš ići dati krv

0px-250px === 0%-100%
'''
kolicina=driver.find_element(By.ID, grupe[unos]).get_attribute("style").split()[1]
kolicina=float(kolicina[:-3])/2.5

driver.quit()
print("Količina krvi za krvnu grupu %s iznosi %.2f%s" %(unos, kolicina, "%"))
