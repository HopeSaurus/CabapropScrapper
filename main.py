from constants import *
from scrappage import scrapPage
from crawler import SeleniumGetHTML
from helpers import listToJSON
from toexcel import toExcel
import os
from rebuild_dumps import retrieve_dumps

def main():
  data_list = []
  result_dict = {}
  for key in COMPANY_FIELDS:
      result_dict[key] = []

  option = input("Elige una opción:\n1.Quieres scrapear toda la web\n2.reconstruir los dumps:\n>")

  try:
    option = int(option)
  except:
    print("Solo escribe 1 o 2")
  if option == 1:
    for barrio in BARRIOS:
      index = 1
      barrio_encoded = barrio.replace(" ","%20")
      while(1):
        url = BASE_URL + f"?barrio={barrio_encoded}&pagina={index}"
        html_content = SeleniumGetHTML(url)
        if("No existen inmobiliarias con esas características" in html_content):
          print("Llegaste al final de los resultados, continuando con el siguiente barrio")
          break
        results = scrapPage(html_content)
        data_list.extend(results)
        dump_name = f"Dump-{barrio.replace("/","-")}-page{index}"
        os.makedirs("dumps", exist_ok=True)
        f = open("dumps/" + dump_name, "w")
        f.write(str(results))
        f.close()
        index += 1
  
    f = open("full-data-list.txt","w")
    f.write(str(data_list))
    f.close()

    f = open("full-dict.txt","w")
    f.write(str(result_dict))
    f.close()
    for lst in data_list:
      listToJSON(lst,result_dict)
    toExcel(result_dict)

  elif option == 2:
    data_list = retrieve_dumps("dumps")
    for lst in data_list:
      listToJSON(lst,result_dict)
    toExcel(result_dict)
  else:
    return
    
main()