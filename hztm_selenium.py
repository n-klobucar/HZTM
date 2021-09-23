from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##import pandas as pd

grupe={"a+":"measure one","a-":"measure two","0+":"measure three","0-":"measure four","b+":"measure five","b-":"measure six","ab+":"measure seven","ab-":"measure eight"}

unos=input("Upišite krvnu grupu: ").lower()
while(unos not in grupe):
    print("Niste unijeli valjanu krvnu grupu!")
    unos=input("Upišite krvnu grupu: ").lower()

opcije=webdriver.FirefoxOptions()
opcije.headless=True
driver=webdriver.Firefox(options=opcije)

driver.get("http://hztm.hr/hr/content/22/zalihe-krvi/831/zalihe-krvi")
kolicina=driver.find_element_by_xpath("//div[@class='{vrecica}']/div[@class='outer']/div[@class='inner']" .format(vrecica=grupe[unos])).get_attribute("data-percent")
driver.quit()
print("Količina krvi za krvnu grupu %s iznosi %s%s" %(unos, kolicina, "%"))
####A=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[4]/div")


##print(A.get_attribute("data-percent"))
##podaci=driver.find_element_by_id("supplies")
##print(podaci)
##grupe={}
##grupe["a+"]=driver.find_element_by_class_name("measure one").find_element_by_class_name("inner")
##grupe["a-"]=driver.find_element_by_class_name("measure two").find_element_by_class_name("inner")
##grupe["0+"]=driver.find_element_by_class_name("measure three").find_element_by_class_name("inner")
##grupe["0-"]=driver.find_element_by_class_name("measure four").find_element_by_class_name("inner")
##grupe["b+"]=driver.find_element_by_class_name("measure five").find_element_by_class_name("inner")
##grupe["b-"]=driver.find_element_by_class_name("measure six").find_element_by_class_name("inner")
##grupe["ab+"]=driver.find_element_by_class_name("measure seven").find_element_by_class_name("inner")
##grupe["ab-"]=driver.find_element_by_class_name("measure eight").find_element_by_class_name("inner")

##print(grupe)

