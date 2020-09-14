import requests
from bs4 import BeautifulSoup
import json
from functools import reduce


def codeforces(url):
    # Connect to the URL
    response = requests.get(url)
    print("prince")
    print(response)

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # title of the problem
    try:
        title = soup.find('div', attrs={'class', 'title'}).text
    except Exception as e:
        title = ""

    # question statement
    try:
        statement = soup.find('div', attrs={'class', 'problem-statement'}).find('p').parent()
        statement = reduce(lambda x, y: str(x) + str(y), statement)
    except Exception as e:
        statement = ""

    # input constraints
    try:
        input_const = soup.find('div', attrs={'class': 'input-specification'}).findAll('p')
        input_const = reduce(lambda x, y: str(x) + str(y), input_const)
    except Exception as e:
        input_const = ""

    # output statement
    try:
        output = soup.find('div', attrs={'class': 'output-specification'})
        output = reduce(lambda x, y: str(x) + str(y), output)
    except Exception as e:
        output = ""

    # examples statement
    try:
        examples = soup.find('div', attrs={'class': 'sample-tests'})
    except Exception as e:
        examples = ""

    # notes
    try:
        notes = soup.find('div', 'note')
    except Exception as e:
        notes = ""

    params = {
        'title': str(title),
        'statement': str(statement),
        'input_const': str(input_const),
        'output': str(output),
        'examples': str(examples),
        'notes': str(notes),
    }
    return json.dumps(params)
