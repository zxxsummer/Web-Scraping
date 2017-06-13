import requests
from bs4 import BeautifulSoup as bs

contact_name=list()
company_name=list()
company_add=list()
company_web=list()
company_ali=list()
response_time=list()
response_rate=list()
business_type=list()
location=list()
main_products=list()
total_employees=list()
total_annual_revenue=list()
year_established=list()
top_3_markets=list()
certification=list()
product_certification=list()
market=list()
export=list()
trade_employees=list()

for i in range(1,6):
    r=requests.get(url='http://????'+str(i))
    soup=bs(r.text,'lxml')
    
    for item in soup.find_all('div',class_='sup-til-right'):
        company_name.append(item.find('a').get_text())  
    for item in soup.find_all('a',class_='phone'):
        link=item.get('href')
        cont=bs(requests.get(link).text,'lxml')
        for det in cont.find_all('div',class_='contact-info'):
            contact_name.append(det.find('h1',class_='name').get_text().strip())
        for det in cont.find_all('div',class_='public-info'):
            company_add.append(det.find('dl',class_='dl-horizontal').text.strip('\n').replace('\n',' '))
    for item in soup.find_all('a',class_='phone'):
        link=item.get('href')
        cont=bs(requests.get(link).text,'lxml')
        count=0
        for td in cont.find('table',class_='company-info-data table').find_all('td'):
            count += 1
            if count%8==0:
                company_ali.append(td.text.strip('\n'))
            if count%6==0:
                company_web.append(td.text.strip('\n').replace('\n',' '))
        try:
            response_time.append(cont.find('table', class_="card-table performance-table").find_all('td')[0].text.strip().replace('\n',''))
        except:
            response_time.append('NA')
        try:
            response_rate.append(cont.find('table', class_="card-table performance-table").find_all('td')[1].text.strip().replace('\n',''))
        except:
            response_rate.append('NA')
    for item in soup.find_all('div',class_='sup-til-right'):
        link=item.find('a').get('href')
        newpage=bs(requests.get(link).content,'lxml')
        for table in newpage.find_all('table',class_='content-table'):
            try:
                business_type.append(table.find_all('td',class_='col-value')[0].text.strip())
                location.append(table.find_all('td',class_='col-value')[1].text.strip())
                main_products.append(table.find_all('td',class_='col-value')[2].text.strip())
                total_employees.append(table.find_all('td',class_='col-value')[3].text.strip())
            except:
                total_employees.append("NA")
            try:
                total_annual_revenue.append(table.find_all('td',class_='col-value')[4].text.strip())
            except:
                total_annual_revenue.append("NA")
            try:
                year_established.append(table.find_all('td',class_='col-value')[5].text.strip())
            except:
                year_established.append("NA")
            try:
                top_3_markets.append(table.find_all('td',class_='col-value')[6].text.strip().replace('\n',' '))
            except:
                top_3_markets.append("NA")
            try:
                certification.append(table.find_all('td',class_='col-value')[7].text.strip().replace('\n',' '))
            except:
                certification.append('NA')
            try:
                product_certification.append(table.find_all('td',class_='col-value')[8].text.strip().replace('\n',' '))
            except:
                product_certification.append('NA')
        try:
            mkt=newpage.find('div',class_='trade-market-table').find_all('td')
            for i in range(0,len(mkt)):
                mkt[i]=mkt[i].text
            market.append(mkt)
        except:
            market.append('NA')
        try:
            exp=newpage.find('div',class_='trade-content').find_all('td',class_='col-center')[0].text
            export.append(exp)
        except:
            export.append('NA')
        try:
            tra=newpage.find('div',class_='trade-content').find_all('td',class_='col-center')[1].text
            trade_employees.append(tra)
        except:
            trade_employees.append('NA')