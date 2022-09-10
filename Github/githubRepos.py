from bs4 import BeautifulSoup
import requests
import csv

# Provide the  url input here
urls=list(map(str,input('Please enter the url separated by a comma : \n ').split(',')))
with open('Github/repos.csv','w',newline='') as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Owner','Name','Link','Privacy','Language','Last Updated'])
    for url in urls: 
        print(url)
        owner=url.split('/')[3].split('?')[0]

        doc_tmplt=requests.get(url=url).content

        soup=BeautifulSoup(doc_tmplt,'html.parser')

        repos=soup.find('div',id='user-repositories-list')
        for repo in repos.find_all('li'):
            name=repo.h3.a.text.strip()
            link=f'https://github.com/{repo.h3.a["href"]}'
            privacy=repo.h3.find_all('span')[1].text
            pl=repo.find('span',{'itemprop':'programmingLanguage'})
            language=pl.text if pl else 'Text File'
            lastUpdated=repo.find('relative-time').text
            csv_writer.writerow([owner,name,link,privacy,language,lastUpdated])





