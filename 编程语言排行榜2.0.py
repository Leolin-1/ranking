import requests
from bs4 import BeautifulSoup


def get_programming_language_ranking():
    url = "https://www.tiobe.com/tiobe-index/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'table table-striped table-top20'})
            rows = table.find_all('tr')[1:] # 跳过表头行
            for row in rows:
                cols = row.find_all('td')
                rank = cols[0].text.strip()
                language = cols[4].text.strip()
                print(f"排名: {rank}, 语言: {language}")
        else:
            print(f"Failed to get data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_programming_language_ranking()

