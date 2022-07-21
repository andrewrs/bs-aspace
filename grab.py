# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
  
  
# function to extract html document from given url
def getHTMLdocument(url):
      
    # request for HTML document of given url
    response = requests.get(url)
      
    # response will be provided in JSON format
    return response.text
  



i = 1
while i < 18:
  print(i)

  # assign required credentials
  # assign URL

  urlbegin = "https://aspace.gmu.edu/repositories/resources?page="

  url_to_scrape = urlbegin + str(i) 
  
  # create document
  html_document = getHTMLdocument(url_to_scrape)
  
  # create soap object
  soup = BeautifulSoup(html_document, 'html.parser')
  
  
  # find all the anchor tags with "href" 
  # attribute starting with "https://"
  for link in soup.find_all('a', 
                          attrs={'href': re.compile("^/resources")}):
    # display the actual urls
    print(link)  


  i += 1




    
