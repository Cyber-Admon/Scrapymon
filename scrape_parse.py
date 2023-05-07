import urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
from inputs import link, entire, data_format, file_name
import json
import csv

if __name__ == '__main__':
    # scraping data
    try:
        response = urlopen(link)
        soup = BeautifulSoup(response, 'html.parser')
        # look up content
        if entire.lower() == 'y':
            content = soup.find('body').get_text()
        else:
            tag = input('which tag are u looking for: ')
            identity = input('tag id: ')
            content = soup.find(tag, {'id': identity}).get_text()

        # saving scraped file

        # saving to text format
        if data_format.lower() == 'txt':
            with open(f'{file_name}.txt', 'w') as txt:
                txt.write(content)

            # saving to html format
        elif data_format.lower() == 'html':
            with open(f'{file_name}.html', 'w') as htm:
                htm.write(str(soup))

            # saving to json format
        elif data_format.lower() == 'json':
            with open(f'{file_name}.json', 'w') as js:
                json.dump(content, js)

            # saving to csv format
        elif data_format.lower() == 'csv':
            with open(f'{file_name}.csv', 'w') as cs:
                csv.writer(cs, content)

    # exceptions
    except csv.Error:
        print('cant write to csv format')
    except urllib.error.HTTPError:
        print('You are not allowed to scrape this website')
    except urllib.error.URLError:
        print('url not correct, try again!!')
