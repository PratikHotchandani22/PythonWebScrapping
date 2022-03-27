from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
import requests
import xlwt
from xlwt import Workbook

print("For which word do you want to find synonyms?")
inputWord = input('>')
print(f'Finding synonyms for {inputWord}')

wb = Workbook();
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0,'Word')
sheet1.write(0,1,'Synonms')
sheet1.write(0,2,'Antonyms')
sheet1.write(1,0,f'{inputWord}')
wb.save('xlwt example.xls')

synonmsUrl = f'https://www.thesaurus.com/browse/{inputWord}'
html_text = requests.get(synonmsUrl).text
soup = BeautifulSoup(html_text, 'lxml')
synonms = soup.find('div', class_ = 'css-ixatld e15rdun50').ul
listSynonms = synonms.find_all('a',class_='css-1gyuw4i eh475bn0')
print('synonyms are: \n')
for index, itemSynonms in enumerate(listSynonms):
    print(itemSynonms.text)
    print(f"writing {itemSynonms.text} in index {index + 1}")   
    sheet1.write(index+1,1,f'{itemSynonms.text}')

print('antonyms are \n')
antonyms = soup.find('div', class_='css-1fsijta e1q3oo7j0').ul
listAntoynms = antonyms.find_all('a',class_='css-15bafsg eh475bn0')
for index, itemAntonym in enumerate(listAntoynms):
    print(itemAntonym.text)
    sheet1.write(index+1,2,f'{itemAntonym.text}')

wb.save('xlwt example.xls')

