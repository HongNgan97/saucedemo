import json
import os
import re
# from Objects.product import Product


class Utility:

    def get_browser(self):
        try:
            return os.environ['BROWSER']
        except:
            return 'chrome'

    def read_json(file_name):
        with open(file_name, 'r') as jsonfile:
            reader = json.load(jsonfile)
            jsonfile.close()
        return reader

    # def read_json(self, fileName):
    #     data = []
    #     with open(fileName) as jsonfile:
    #         reader = json.load(jsonfile)
    #         # temp = reader.items()
    #         # for key, value in temp:
    #         #     print(key)
    #         #     print(value)
    #         for row in reader:
    #             data.append(row)
    #             print(row)
    #     jsonfile.close()
    #
    #     print(data['products'])
    #     return data

    def convert_string_to_float(self, str):
        try:
            return float(re.findall('\d+\.\d+', str)[0])
        except:
            return 0.00

    def multiple(self, quantity, price):
        temp_price = self.convert_string_to_float(price)
        result = int(quantity) * temp_price
        return result
