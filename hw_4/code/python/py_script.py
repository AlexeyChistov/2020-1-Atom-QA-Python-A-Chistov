import pandas as pd
from data_frame.path import DATA_PATH
import json


HTTP_METHODS = [
    'GET',
    'PUT',
    'DELETE',
    'HEAD',
    'POST',
    'CONNECT',
    'OPTIONS',
    'TRACE',
    'PATH'
]


def read_and_strip():
    df = pd.read_table(
        DATA_PATH,
        delimiter=' - - | "|" ',
        engine='python',
        names=['ip', 'date', 'req', 'codes', '1', '2', '3']
    )
    df[df.columns] = df.apply(lambda x: x.str.strip('"'))
    regex = '(?P<resp_codes>.*)\s(?P<codes>.*)'
    df = df.codes.str.extract(regex, expand=True).combine_first(df)
    regex = '(?P<meth>.*)\s(?P<url>.*)\s(?P<http>.*)'
    df = df.req.str.extract(regex, expand=True).combine_first(df)
    return df


def request_methods_counter(df):
    """Реализовали вывод всех мтодов запросов и их количество"""
    new_list = []
    for method in HTTP_METHODS:
        if df.meth.str.startswith(method).sum() != 0:
            new_list.append([method, df.meth.str.startswith(method).sum()])
    return sorted(new_list, key=lambda num: num[1], reverse=True)


def top_clients_errors(df):
    new_df = df[['resp_codes', 'ip', 'url']]
    new_df = new_df.query('resp_codes >= "400" & resp_codes<="499"')
    new_df = new_df.groupby(new_df.columns.tolist()).size().reset_index().rename(columns={0: 'count'})
    new_df = new_df.sort_values(by='count', ascending=False).head(10)
    return new_df[['ip', 'url', 'count']]


def top_server_errors(df):
    new_df = df[['resp_codes', 'ip', 'url']]
    new_df = new_df.query('resp_codes >= "500" & resp_codes<="599"')
    new_df = new_df.groupby(new_df.columns.tolist()).size().reset_index().rename(columns={0: 'count'})
    new_df = new_df.sort_values(by='count', ascending=False).head(10)
    return new_df[['ip', 'url', 'count']]


def tob_biggest_request(df):
    new_df = df[['codes', 'url']]
    new_df = new_df.query('codes != "-"')
    new_df = new_df.groupby(new_df.columns.tolist()).size().reset_index().rename(columns={0: 'count'})
    new_df.codes = new_df.codes.astype('int64')
    new_df = new_df.sort_values(by='codes', ascending=False, kind='heapsort').head(10)
    return new_df[['codes', 'url', 'count']]


data_frame = read_and_strip()
print("\nТоп клиентских ошибок: \n", top_clients_errors(data_frame))
print("\nТоп самых больших запросов: \n", tob_biggest_request(data_frame))
print("\nОбщее число запросов: \n", len(data_frame))
print("\nТоп серверных ошибок: \n", top_server_errors(data_frame))
print("\nКоличество запросов GET, POST и т.п.: \n", request_methods_counter(data_frame))

with open("client_errors.json", "w") as file:
    top_clients_errors(data_frame).to_json(file)
with open("top_biggest_requests.json", "w") as file:
    tob_biggest_request(data_frame).to_json(file)
with open("top_biggest_requests.json", "w") as file:
    top_server_errors(data_frame).to_json(file)
