"""gets data from web and saves it at a certain location

Usage: src/gatherdata.py <website_URL> <output_file>

Options:
<website_URL>     website of URL
<output_file>    Path (including filename) of where to locally write the file
"""

from docopt import docopt

opt = docopt(__doc__)
DELIMITERS = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()

import urllib.request
import zipfile
import pandas as pd
import os

def main(url, location):
    print("running")
    downloadwebdata(url, location)
    print("done")
    
def downloadwebdata(url, location):
    #inspiration for learning how to download from web taken from https://stackoverflow.com/questions/41218216/using-pandas-to-download-load-zipped-csv-file-from-url
    temp, _ = urllib.request.urlretrieve(url)
    compressed_file = zipfile.ZipFile(temp)
    csv_file = compressed_file.open('student-mat.csv')
    df = pd.read_csv(csv_file,sep = ";")
    df.to_csv(location)
    
    
if __name__ == '__main__':
    main(opt["<website_URL>"], opt["<output_file>"])
