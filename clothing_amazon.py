from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
import pandas as pd
'''/////                      options                     /////'''

options=webdriver.ChromeOptions()
options.add_argument('start-maximized')
#options.add_argument()
i=0

'''/////                     setting web driver and giving options                   /////'''

driver=Chrome(options=options)
driver.get('https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A1040658&ref=nav_em_0_2_23_2__nav_desktop_sa_intl_clothing')
sleep(10)
'''/////                function getting scraped data                     /////'''
prices=[]
texts=[]
rating=[]
best_sellers=[]


def scrape():

    '''css selector of single product block'''

    brand_contents=driver.find_elements_by_css_selector('div.a-section.a-spacing-medium')
    print(len(brand_contents))
    t=0
    p=0
    for brand_content in brand_contents:
      try:
        if True:

         '''product title'''

         text=brand_content.find_element_by_css_selector('span.a-size-base-plus.a-color-base.a-text-normal').get_attribute('innerText')
         t=t+1

         '''price of product'''

         price=brand_content.find_element_by_css_selector('span.a-price-whole').get_attribute('innerText')
         p=p+1
         '''ratings of product'''
         ratings=brand_content.find_element_by_css_selector('span.a-icon-alt').get_attribute('innerText')
         '''best seller'''
         best_seller=brand_content.find_element_by_css_selector('div.a-section.a-spacing-micro.s-grid-status-badge-container').get_attribute('innerText')

         '''print(best_seller)
         print(text)
         print(price)
         print(ratings)'''
         texts.append(text)
         prices.append(price)
         rating.append(ratings)
         best_sellers.append(best_seller)

        else:
         break
      except:
          pass
while (i<1):
    '''calling scraping function'''
    scrape()
    '''clicking the next page'''
    driver.find_element_by_css_selector('li.a-last').click()
    sleep(10)
    i=i+1
dict={'text':texts,'price':prices,'ratings':rating,'best_seller':best_sellers}
df=pd.DataFrame(dict)
df.to_csv('ama_data.xlsx',header=False,index=False)
print(df)
#print(t)
#print(p)
driver.close()