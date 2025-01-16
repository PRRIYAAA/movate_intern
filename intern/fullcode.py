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








