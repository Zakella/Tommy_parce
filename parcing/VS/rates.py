import requests
import json
from bs4 import BeautifulSoup, element
from datetime import datetime


def get_exchange_rate(currency):
    response = requests.get("http://pki.maib.md/rates/")
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find('pre')
    list_rates = []
    add_ref = False
    for el in data:

        if isinstance(el, element.NavigableString):
            new_list = []
            day_date = "/".join(list(map(lambda x: "0" + x if len(x) == 1 else x, el.string.split()[0].split("/"))))
            h_date = ":".join(list(map(lambda x: "0" + x if len(x) == 1 else x, el.string.split()[1].split(":"))))
            date_time_obj = datetime.strptime(f"{day_date} {h_date}", '%m/%d/%Y %H:%M')
            new_list.append(date_time_obj)
            add_ref = True
        elif isinstance(el, element.Tag):
            for ref in el:
                if add_ref:
                    new_list.append(f"http://pki.maib.md/rates/{ref}")
                    list_rates.append(new_list)
                    add_ref = False

    response = requests.get(sorted(list_rates)[-1][1])
    currents_data = response.json()
    cur_dict = {}
    for el in currents_data:
        cur_dict[el.get("currencies_name")] = float(el.get("sell"))

    return cur_dict.get(currency)

# a = get_exchange_rate("RON")
# print(a)
