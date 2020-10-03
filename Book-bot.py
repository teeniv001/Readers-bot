import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
      
global details
details = {}
 
 # using selenium to automate the process
def getDownloadLink(url):
    driver = webdriver.Chrome('C:/Users/vineet/Downloads/chromedriver.exe')
    driver.get(url)
    download = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/a[1]')
    download.click()

def readOnline(url):
    driver = webdriver.Chrome('C:/Users/vineet/Downloads/chromedriver.exe')
    driver.get(url)
    online = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/a[3]')
    online.click()
    
global l # len    
def user_input(details,href,url):
    user=input('Enter your book selection no.: '+'\n')
    l=len(details)
    for key in range(0,l):
        if user==key:
            new_url='https://b-ok.cc' + '+'.join(map(str,href[key].split()))
            #print new_url
    #new_page=requests.get(new_url)
    #soups = BeautifulSoup(new_page.text,'lxml')

    same_user=input('1->download_book\n2->Read book_online\nEnter ur selection: ')
    if same_user==1:
        getDownloadLink(new_url)
    else:
        readOnline(new_url)
            
def download_book(url):
    global details
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')


    #book name
    i=0
    for name in soup.find_all("a", class_="tdn"):
        details[i] = [name.text]
        i+=1

    #author name
    i=0
    for name in soup.find_all("a", title="Find all the author's book"):
        try:
            details[i].append(name.text)
        except:
            pass
        i+=1


    #book link
    href=[]
    for link in soup.find_all("a",class_="tdn"):
            href.append(link.attrs['href'])
    

    #details
    for key, value in details.iteritems():
        print key,
        for val in value:
            print '--> ', val,
        print

    user_input(details,href,url)

    
def home_pg(book_name):
    url= 'https://b-ok.cc/s/?q=' + '+'.join(map(str, book_name.split()))
    #print url
    download_book(url)

    

print "Enter the book name"
book_name=raw_input()
home_pg(book_name)
