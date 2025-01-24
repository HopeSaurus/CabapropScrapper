from bs4 import BeautifulSoup
from constants import *
from helpers import traverseTree

def scrapPage(html_content):
  page_data_list = []
  soup = BeautifulSoup(html_content, 'html.parser')
  results = soup.find_all(class_=CONTAINER_CLASS)
  for result in results:
    data = scrapSingleRow(result)
    page_data_list.append(data)
  return page_data_list

def scrapSingleRow(container):
  data = ["Nombre"]
  soup = BeautifulSoup(str(container), 'html.parser')
  traverseTree(soup, data)
  return data

