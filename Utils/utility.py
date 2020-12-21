import json
import os

from Objects.product import Product


class Utility():

    def get_browser(self):
        try:
            return os.environ['BROWSER']
        except:
            return 'chrome'

    def read_json(self, fileName):
        data = []
        with open(fileName) as jsonfile:
            reader = json.load(jsonfile)
            # temp = reader.items()
            # for key, value in temp:
            #     print(key)
            #     print(value)
            for row in reader:
                data.append(row)
                print(row)
        jsonfile.close()

        print(data['products'])
        return data
