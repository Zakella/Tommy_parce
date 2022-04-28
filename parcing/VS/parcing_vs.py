import requests
import os
from fake_useragent import UserAgent
import json
import vs_config


def parce_vs():
    for key, val in vs_config.dict_url.items():
        get_data(val, key)


def get_data(val, key):
    headers = {"user-agent": UserAgent().chrome
               }
    url = val["url"]
    response = requests.session().get(url=url, headers=headers)  # # print(response.json())
    data = response.json()

    if not os.path.exists("data"):
        os.mkdir("data")

    with open( key + ".json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    domen = "https://www.victoriassecret.com/"
    dict_all = {}
    count = 0
    with open( key + ".json") as mists:
        data = json.load(mists)
        # print(data)

        for el in data['stacks']:
            for item in el["list"]:
                count += 1
                if item['salePrice'] or not item['altPrices'] == None:

                    if not item['productImages']:
                        pict_ref = ""
                    else:
                        pict_ref = item['productImages']

                    dict_all[item['id']] = {
                        "name": item['name'],
                        "price": item['price'],
                        "url": domen + item['url'],
                        "altPrices": item['altPrices'],
                        "salePrice": item['salePrice'],
                        "collectionShortDescription": item['collectionShortDescription'],
                        "special_price_1": None,
                        "special_price_2": None,
                        "pict_ref": pict_ref,
                        "min_price": float(item['price'].split("$")[1])
                    }
                    if not item['altPrices'] == None:
                        for price in item['altPrices']:
                            alt_price = price.split("/$")

                            try:
                                quant_1 = alt_price[0][-1]
                                amount_1 = alt_price[1].split()[0].replace(",", "")
                                dict_all[item['id']]["special_price_1"] = {
                                    "amount": float(amount_1),
                                    "quant": float(quant_1),
                                    "price": float(amount_1) / float(quant_1)
                                }
                            except Exception:
                                pass

                            try:
                                quant_2 = alt_price[-2].replace(",", "")[-1]
                                amount_2 = alt_price[-1]
                                dict_all[item['id']]["special_price_2"] = {
                                    "amount": float(amount_2),
                                    "quant": float(quant_2),
                                    "price": float(amount_2) / float(quant_2)
                                }

                            except Exception:
                                pass
                    else:
                        dict_all[item['id']]["special_price_1"] = {
                            "amount": float(dict_all[item['id']]["salePrice"].split("$")[-1]),
                            "quant": 1,
                            "price": float(dict_all[item['id']]["salePrice"].split("$")[-1]),

                        }
                    if dict_all[item['id']]["special_price_2"] == None:
                        min_price = min(dict_all[item['id']]["min_price"],
                                        dict_all[item['id']]["special_price_1"]["price"])
                        dict_all[item['id']]["min_price"] = min_price
                    else:
                        min_price = min(dict_all[item['id']]["special_price_2"]["price"],
                                        dict_all[item['id']]["special_price_1"]["price"])
                        dict_all[item['id']]["min_price"] = min_price

    with open( key + "_sale.json", "w", encoding="utf-8") as file:
        json.dump(dict_all, file, indent=4, ensure_ascii=False)
        print(f'Total items in {key} {count}')


if __name__ == "__main__":
    parce_vs()
