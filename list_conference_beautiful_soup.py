import requests
from bs4 import BeautifulSoup

def scrape_bangla_nlp_papers():
    url = 'https://scholar.google.com/scholar?q=Bangla+NLP'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    papers = []
    results = soup.find_all('div', class_='gs_r gs_or gs_scl')
    
    for result in results:
        title = result.find('h3', class_='gs_rt').text
        journal_elem = result.find('div', class_='gs_a')
        if journal_elem:
            journal = journal_elem.text.split(' - ')[0]
        else:
            journal = "Unknown"
        year_elem = result.find('span', class_='gs_oph')
        if year_elem:
            year = year_elem.text.split()[-1]
        else:
            year = "Unknown"
        conf_elem = result.find('div', class_='gs_a')
        if conf_elem:
            conf_info = conf_elem.text.split(' - ')[1:]
            conference = ''.join(conf_info)
        else:
            conference = "Unknown"
        papers.append({'title': title, 'journal': journal, 'year': year, 'conference': conference})
    
    return papers

def main():
    papers = scrape_bangla_nlp_papers()
    print("List of Bangla NLP Papers:")
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Journal: {paper['journal']}")
        print(f"Conference: {paper['conference']}")
        print(f"Year: {paper['year']}")
        print()

if __name__ == "__main__":
    main()

