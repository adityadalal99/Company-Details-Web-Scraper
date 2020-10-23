import requests
import _json
from bs4 import BeautifulSoup


def writeToFile():
    pass


def checkInFile():
    pass


def useGoogle(companyName):
    search_url = 'https://www.google.com/search'
    payload = {'q': companyName}
    search_parsed = BeautifulSoup(requests.get(search_url, payload).text,'lxml')
    list = search_parsed.find_all('h3')
    final_list  =[]
    for res in list:
        final_list.append(res.text)
    print(final_list)
    print(list)

def useCompaniesHous(companyName):
    searchURL = 'https://find-and-update.company-information.service.gov.uk/search/companies'
    payload = {'q': companyName}
    searchParsed = BeautifulSoup(requests.get(searchURL, payload).text, 'lxml')
    #print reultList
    #companiesTags = searchParsed.find('ul', class_ = 'results-list').find_all('li', limit=5, class_='type-company')
    companies = {}
    for companyTag in searchParsed.find('ul', class_ = 'results-list').find_all('li', limit=5, class_='type-company'):
        name = companyTag.h3.a.text
        link = companyTag.h3.a['href']
        companies.update({name: link.split('/').pop()})
    print(companies)
    companyPageURL = 'https://find-and-update.company-information.service.gov.uk/company/{company_no}/persons-with-significant-control'
    employee_info = {}
    for company_name, company_no in companies.items():
        company_page = BeautifulSoup(requests.get(companyPageURL.format(company_no = company_no)).text, 'lxml')
        employee_info.update({company_name:company_page.find('div', class_='appointments-list').find_all('div',class_='appointment-1')[0].h2.text})
    print(employee_info)

companyName = raw_input()
#useCompaniesHous(companyName)
useGoogle(companyName)

#PINNACLE FINANCIAL PLANNING LTD
#https://find-and-update.company-information.service.gov.uk/company/06754206/persons-with-significant-control