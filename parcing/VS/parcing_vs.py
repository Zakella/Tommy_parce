import requests
from fake_useragent import UserAgent
import json
import vs_config


def parce_vs():
    for key, val in vs_config.dict_url.items():
        get_data(val, key)


def get_data(cat_name, url):
    headers = {"user-agent": UserAgent().chrome
               }

    response = requests.session().get(url=url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        items_list = []
        stacks = data.get("stacks")
        domen = "https://www.victoriassecret.com/"
        pict_domain = "https://www.victoriassecret.com/p/280x373/"
        counter = 0
        list_id = []
        for item in stacks:
            for list_item in item.get("list"):
                item_card = {}
                masterStyleId = list_item.get("masterStyleId")
                if not masterStyleId in list_id:
                    name = list_item.get("name")
                    family = list_item.get("family")
                    item_card["name"] = f" {family} {name}"
                    item_card["family"] = family
                    item_card["url"] = domen + list_item.get("url")
                    item_card["price"] = float(list_item.get("price").replace("$", ""))
                    sale_price = list_item.get("salePrice").replace("$", "")
                    item_card["images"] = []
                    if not sale_price:
                        item_card["sale_price"] = 0
                    else:
                        item_card["sale_price"] = float(sale_price)
                    item_card["altPrices"] = list_item.get("altPrices")
                    item_card["min_price"] = item_card["price"] if not item_card["sale_price"] else item_card[
                        "sale_price"]
                    item_card["alt_price1"] = 0
                    item_card["alt_price2"] = 0
                    if item_card["altPrices"] != None:
                        for price in item_card['altPrices']:
                            alt_price = price.split("/$")
                            try:
                                quant_1 = float(alt_price[0][-1])
                                amount_1 = float(alt_price[1].split()[0].replace(",", ""))
                                item_card["alt_price1"] = amount_1 / quant_1 if quant_1 != 0 else 0
                            except Exception:
                                pass

                        try:
                            quant_2 = alt_price[-2].replace(",", "")[-1]
                            amount_2 = alt_price[-1]
                            item_card["alt_price2"] = amount_2 / quant_2 if quant_2 != 0 else 0
                        except Exception:
                            pass

                    item_card["min_price"] = min(
                        filter(None, (item_card["min_price"], item_card["alt_price1"], item_card["alt_price2"])))

                    main_image = list_item.get("productImages")[0]
                    for image in list_item.get("swatches"):
                        try:
                            if main_image != image.get("productImage"):
                                item_card["images"].append(pict_domain + image.get("productImage") + ".jpg")

                        except:
                            item_card["images"].append(pict_domain + list_item.get("productImages")[0] + ".jpg")

                    item_card["main_image"] = pict_domain + main_image + ".jpg"
                    items_list.append(item_card)
                    list_id.append(masterStyleId)
                    counter += 1

        print(f"Total in {cat_name} {counter} items")
        return items_list
    else:
        return "Ups!, server is gone. Try again later"


# if __name__ == "__main__":
#     data = get_data("beauty", vs_config.dict_url["beauty"]["url"])
#     print(data)

    # print(data1)
# with open("test", "w") as file:
#     json.dump(data1, file, indent=4, ensure_ascii=False)
# for it in data:
#     print(it.get("images"))
