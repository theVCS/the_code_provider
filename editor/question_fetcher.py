import requests
from bs4 import BeautifulSoup


def codeforces(url):
    # Connect to the URL
    response = requests.get(url)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # title of the problem
    title = soup.find('div', attrs={'class', 'title'}).text

    # question statement
    statement = soup.find('div', attrs={'class', 'problem-statement'}).find('p').parent()

    # input constraints
    input_const = soup.find('div', attrs={'class': 'input-specification'}).findAll('p')

    # output statement
    output = soup.find('div', attrs={'class': 'output-specification'})

    # examples statement
    examples = soup.find('div', attrs={'class': 'sample-tests'})

    # notes
    notes = soup.find('div', 'note')

    params = {
        'title': title,
        'statement': statement,
        'input_const': input_const,
        'output': output,
        'examples': examples,
        'notes': notes,
    }
    return params
