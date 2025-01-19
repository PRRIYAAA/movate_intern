""" import pandas as pd 
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import time


driver = webdriver.Chrome()

driver.get(url = 'https://www.flipkart.com/apple-iphone-13-midnight-128-gb/product-reviews/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&aid=overall&certifiedBuyer=false&sortOrder=NEGATIVE_FIRST&page=1')

html_data = BeautifulSoup(driver.page_source, 'html.parser')
url = 'https://www.flipkart.com/apple-iphone-13-midnight-128-gb/product-reviews/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&aid=overall&certifiedBuyer=false&sortOrder=NEGATIVE_FIRST&page=1'

i = 0

ratings = []
reviews_text = []
while url !=None or len(ratings) < 1000:
    i = i + 1
    url = 'https://www.flipkart.com/apple-iphone-13-midnight-128-gb/product-reviews/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&aid=overall&certifiedBuyer=false&sortOrder=NEGATIVE_FIRST&page='+str(i+1)
    driver.get(url)
    time.sleep(5)
    html_data = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = html_data.find_all('div',{'class':'EKFha-'})
    for review in reviews:
        rating = review.find('div',{'class':'Ga3i8K'}).text
        ratings.append(rating)
        review_text = review.find('div',{'class':'ZmyHeo'}).text
        reviews_text.append(review_text)


data = pd.DataFrame({'ratings':ratings, 'review':reviews_text})
data.to_csv('reviews_and_comments_negative.csv')

"""


#https://www.flipkart.com/apple-iphone-13-midnight-128-gb/product-reviews/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&aid=overall&certifiedBuyer=false&sortOrder=MOST_HELPFUL&page=1


'https://www.flipkart.com/flipkart-smartbuy-army-keychain-torch-screwdriver-knife-bottle-opener-key-chain/product-reviews/itm9d4dbcd2cd4b6?pid=KECFZYXGHKHBVBK8&lid=LSTKECFZYXGHKHBVBK8PCUPSM&marketplace=FLIPKART&q=keychain&store=dgv%2Ftkw%2Famn&srno=s_1_5&otracker=search&fm=organic&iid=bb785e12-a439-44b3-8b13-23371ae5b76f.KECFZYXGHKHBVBK8.SEARCH&ppt=hp&ppn=homepage&ssid=cvdh45cclc0000001737122874770&qH=857823c186f036a6'

'https://www.flipkart.com/flipkart-smartbuy-army-keychain-torch-screwdriver-knife-bottle-opener-key-chain/product-reviews/itm9d4dbcd2cd4b6?pid=KECFZYXGHKHBVBK8&lid=LSTKECFZYXGHKHBVBK8PCUPSM&aid=overall&certifiedBuyer=false&sortOrder=MOST_HELPFUL'
'https://www.flipkart.com/flipkart-smartbuy-army-keychain-torch-screwdriver-knife-bottle-opener-key-chain/product-reviews/itm9d4dbcd2cd4b6?pid=KECFZYXGHKHBVBK8&lid=LSTKECFZYXGHKHBVBK8PCUPSM&aid=overall&certifiedBuyer=false&sortOrder=MOST_RECENT'
'https://www.flipkart.com/flipkart-smartbuy-army-keychain-torch-screwdriver-knife-bottle-opener-key-chain/product-reviews/itm9d4dbcd2cd4b6?pid=KECFZYXGHKHBVBK8&lid=LSTKECFZYXGHKHBVBK8PCUPSM&aid=overall&certifiedBuyer=false&sortOrder=POSITIVE_FIRST'
'https://www.flipkart.com/flipkart-smartbuy-army-keychain-torch-screwdriver-knife-bottle-opener-key-chain/product-reviews/itm9d4dbcd2cd4b6?pid=KECFZYXGHKHBVBK8&lid=LSTKECFZYXGHKHBVBK8PCUPSM&aid=overall&certifiedBuyer=false&sortOrder=NEGATIVE_FIRST'





