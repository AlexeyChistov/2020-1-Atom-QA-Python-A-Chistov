import pandas as pd
from data.data_path import FILES

DATA_FRAMES = {}


def read_and_strip(file):
    df: pd.DataFrame = pd.read_table(
        file,
        delimiter=' - - | "|" ',
        engine='python',
        names=['ip', 'date', 'req', 'codes', '1', '2', '3']
    )
    df[df.columns] = df.apply(lambda x: x.str.strip('"'))
    regex = '(?P<resp_code>.*)\s(?P<bytes_sent>.*)'
    df = df.codes.str.extract(regex, expand=True).combine_first(df)
    regex = '(?P<method>.*)\s(?P<url>.*)\s(?P<http>.*)'
    df = df.req.str.extract(regex, expand=True).combine_first(df)
    df.index += 1
    return df[['ip', 'date', 'method', 'url', 'http', 'resp_code', 'bytes_sent', '1', '2', '3']]


for file_name in FILES.keys():
    DATA_FRAMES[file_name.replace(".", "_")] = read_and_strip(FILES[file_name])
