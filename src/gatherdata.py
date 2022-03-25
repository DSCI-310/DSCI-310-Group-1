import urllib.request
import zipfile

"""
gets data from web and saves it at a certain location
Usage: src/gatherdata.py <website URL> <output_file>

Options:
<input_file>     website of URL
<output_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt

opt = docopt(__doc__)

def downloadwebdata(url, location):
    #inspiration for learning how to download from web taken from https://stackoverflow.com/questions/41218216/using-pandas-to-download-load-zipped-csv-file-from-url
    URL = url
    urllib.request.urlretrieve(URL, "../data/raw/student.zip")
    compressed_file = zipfile.ZipFile('../data/raw/student.zip')
    csv_file = compressed_file.open('student-mat.csv')


def main():
    downloadwebdata(url, location)

