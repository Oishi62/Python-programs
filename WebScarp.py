import requests
from bs4 import BeautifulSoup
import pandas
scraped_info_list=[]
oyo_url="https://www.oyorooms.com/hotels-in-bangalore/"
req=requests.get(oyo_url)
content=req.content
soup=BeautifulSoup(content,"html.parser")
all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
    hotel_dict["address"]=hotel.find("span",{"itemprop":"StreetAdress"}).text
    hotel_dict["price"]=hotel.find("span",{"class":"listingPrice_finalPrice"}).text
    scraped_info_list.append(hotel_dict)
dataFrame=pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv")
    


    

