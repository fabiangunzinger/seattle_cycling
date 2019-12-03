import os
import ssl
from urllib.request import urlretrieve
import pandas as pd

fremont_url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='fremont.csv', url=fremont_url,
                      force_download=False):
    """ Download and cache the fremont bridge data
    
    Parameters
    ----------
    filename : string (optional)
        location to store the data
    url : string (optional)
        web location of the data
    force_download : Boolean (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.DataFrame
        The fremont bridge data
    """
    # Solve problem with SSL certificate verification
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
    # Download and prepare data
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ['total', 'west', 'east']
    return data