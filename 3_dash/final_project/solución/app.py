



TU_TOKEN = 'pk_f9d70fa7902545439db45734b8289fc4'
import requests

def get_data_iex(tck, data_range='1y', only_close_data=True):
    url = f'https://cloud.iexapis.com/stable/stock/{tck}/chart/{data_range}'
    r = requests.get(url, params={'token': TU_TOKEN, 'chartCloseOnly': only_close_data})
    df = pd.DataFrame(r.json())
    if only_close_data:
        df = df.loc[:, [ 'close', 'date']]
        df.date = pd.to_datetime(df.date)
        df = df.set_index('date')
        serie_close = df.loc[:, 'close']
        serie_close.name = tck
        return serie_close
    else:
        df = df.loc[:, [ 'open', 'high', 'low', 'close',  'volume', 'date']]
        df.date = pd.to_datetime(df.date)
        df = df.set_index('date')

    return df

