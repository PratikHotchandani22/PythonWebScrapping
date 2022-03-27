from bs4 import BeautifulSoup
import requests

print("For which word do you want to find synonyms?")
inputWord = input('>')
print(f'Finding synonyms for {inputWord}')

synonmsUrl = f'https://www.thesaurus.com/browse/{inputWord}'
html_text = requests.get(synonmsUrl).text
soup = BeautifulSoup(html_text, 'lxml')
synonms = soup.find('div', class_ = 'css-ixatld e15rdun50').ul
list = synonms.find_all('a',class_='css-1gyuw4i eh475bn0')
for item in list:
    print(item.text)