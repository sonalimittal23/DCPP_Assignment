import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

df_yt = pd.read_csv('C:/Users/HP/Documents/Python/Project/Finaldata.csv')


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.youtube.com")

#Function to query the recipe name in Youtube's search bar
def youtube_search_views(i):
    search=[]
    element=driver.find_element_by_xpath("//input[@id='search']")
    element.click()
    element.send_keys(Keys.CONTROL+"A") #For clearing the search bar after each iteration
    element.send_keys(Keys.DELETE)
    element.send_keys(i)
    element.send_keys(Keys.ENTER)
    time.sleep(8)
#Extracting the video url and views element from YT
    element=driver.find_element_by_xpath("//a[@id='video-title']")
    element.click()
    time.sleep(10)
    element=driver.find_element_by_xpath("//span[@class='view-count style-scope ytd-video-view-count-renderer']")
    url=driver.current_url
    search.append(url)
    count=element.text
    search.append(count)
    return search

for index, row in df_yt.iterrows(): #For iteration
    if (index<=5675): # Total number of recipies
        try:
            recipe_name = row['Recipe_Name']
            search_views=youtube_search_views(recipe_name)
            views=search_views[1]
            views_2=views.split(' ') # Replacing the 'views' keyword with space and removing commas from number
            views=views_2[0].replace(',','')
            final_url = search_views[0]
            df_yt.at[index,"Video_URL"]=final_url # Storing the Video_URL as an attribute in our dataset
            df_yt.at[index,"Views"]=int(views) #Storing the number of views as an attribute in our dataset
            print(index)
        except:
            df_yt.to_csv("temp_random.csv") # Exception Handling for saving whatever iterations have been performed

driver.close() #Closing the Chrome brower when the last recipe index is reached
print(df_yt.dtypes)
df_yt.to_csv("data_random.csv") # Final file