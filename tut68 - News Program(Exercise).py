# Kind of Enquirer
import requests
import json

def printHeadlines(text):
    topHeadlines = json.loads(text)
    # print(topHeadlines)

    for i in range(0, topHeadlines.get('totalResults')):
        print(f'{i}.', end=' ')
        print(topHeadlines['articles'][i]['title'])
        print('\n\n')

if __name__ == "__main__":
    while True:
        if 'query' not in globals():
            query = ''

        url = f'https://newsapi.org/v2/top-headlines?{query}sources=google-news-in&apiKey=62985d45897d4677bdec4d8d162017fa'
        response = requests.get(url)
        text = response.text
        printHeadlines(text)

        queryInput = str(input('Search news: '))
        query = f'q={queryInput}&'


''' Check if a variable exists or not, as well as attribute exists or not
https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
'''