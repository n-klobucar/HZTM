import urllib.request

web_stranica=urllib.request.urlopen(r"http://hztm.hr/hr/content/22/zalihe-krvi/831/zalihe-krvi").read().decode("utf8").split('"')
##print(web_stranica)
postotak=[]
pozicija=0
krvne_grupe=['a+','a-','0+','0-','b+','b-','ab+','ab-']
for el in web_stranica:
    if el == ' data-percent=':
        pozicija=web_stranica.index(el, pozicija)
        postotak.append(web_stranica[pozicija+1])
        pozicija+=1

##print(postotak)


unos=input("Upišite krvnu grupu: ").lower()
print("Količina krvi za krvnu grupu %s iznosi %s%s" % (unos, postotak[krvne_grupe.index(unos)], "%"))

'''
probaj pregledati s regularnim izrazima

koristi selenium
'''
