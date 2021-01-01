import urllib.request
from bs4 import BeautifulSoup

url='https://www.jeonbuk.go.kr/index.jeonbuk?menuCd=DOM_000000110006000000'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

table=soup.find('table', {'class':'covid_table'})
trs = table.find_all('tr')
data = [] #[도시, 군구, 상점이름...배열]
for idx, tr in enumerate(trs):
    if (idx) > 0:
        tds=tr.find_all('td')
        city = tds[0].text.strip()
        county = tds[1].text.strip()
        store_name = tds[2].text.strip()
        address = tds[3].text.strip()
        date = tds[4].text.strip()
        sterilization_status = tds[5].text.strip()
        data.append([city, county, store_name, address, date, sterilization_status])

print(data)
        

