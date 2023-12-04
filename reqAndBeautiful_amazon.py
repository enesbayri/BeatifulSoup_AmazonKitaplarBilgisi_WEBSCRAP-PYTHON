import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

siteUrl="https://www.amazon.com.tr/gp/bestsellers/books/"

sayfaCevap=requests.get(siteUrl,headers = headers)

"""
bu kısa yol
if sayfaCevap.status_code==200:
    htmlIcerik=sayfaCevap.content
    soup=BeautifulSoup(htmlIcerik,"html.parser")
    for kitapLi in soup.find_all("div",{"id":"gridItemRoot"}):
        for icerik in kitapLi.find_all("span"):
            if icerik.get("class")==['_cDEzb_p13n-sc-price_3mJ9Z']:
                continue
            print(icerik.text)
        print("---------------------------------------------")

else:
    print("Siteye erisilemiyor!")
"""

if sayfaCevap.status_code==200:
    htmlIcerik=sayfaCevap.content
    soup=BeautifulSoup(htmlIcerik,"html.parser")
    for kitapLi in soup.find_all("div",{"id":"gridItemRoot"}):
        sira=kitapLi.find("span",{"class":"zg-bdg-text"})
        print(sira.text)
        sayac=0
        for kitapAdi in kitapLi.find_all("div",{"class":"_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"}):
            if sayac==0:
                print("kitap adi: "+kitapAdi.text)
            else:
                print("kitap yazari: "+kitapAdi.text)
            sayac+=1
        kitapPuan=kitapLi.find("span",{"class":"a-icon-alt"})
        print("Puani: "+kitapPuan.text)
        kitapFiyat=kitapLi.find("span",{"class":"_cDEzb_p13n-sc-price_3mJ9Z"})
        print("Fiyati: "+kitapFiyat.text)

        print("\n---------------------------------------------\n")

else:
    print("Siteye erisilemiyor!")
