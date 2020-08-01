from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'C:\phantomJS\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url1 = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
url2 = 'https://www.imdb.com/title/tt0111161/mediaviewer/rm10105600'

driver.get(url1)


#print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'lxml')

table = soup.find('table', class_= 'chart')
for td in table.find_all('td', class_ = 'titleColumn'):
    full_title = td.text.strip().replace('\n','').replace('      ','')
    print(full_title)

    rank = full_title.split('.')[0]
    print(rank)

    title = full_title.split('.')[1].split('(')[0]
    print(title)

    year = full_title.split('(')[1][:-1]
    print(year)

    print('\n')


driver.quit()


