# import json
import sys

from Objects.product import Product

sys.path.append(".")

from Utils.utility import Utility


class Data:
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    # USERNAME = 'locked_out_user'
    # USERNAME = 'problem_user'
    # USERNAME = 'performance_glitch_user'
    # USERNAME = 'user'
    PASSWORD = 'secret_sauce'
    # PASSWORD = 'secret_sauce!'
    BROWSER = 'Chrome'

    PRODUCTS_CSV_FILE = 'Testdata/products.csv'
    # PRODUCTS_JSON_FILE = 'Testdata/products.csv'
    PRODUCTS_JSON_FILE = '/Users/hongngan/Desktop/SauceDemo-master/Testdata/products.json'

    # def get_account_csv(self):
    #     utility = Utility()
    #     return utility.read_csv(Data.ACCOUNT_CSV_FILE)

    # def get_account_json(self):
    #     utility = Utility()
    #     return utility.read_json(Data.ACCOUNT_JSON_FILE)

    # def get_message_json(self):
    #    utility = Utility()
    #     return utility.read_json(Data.MESSAGE_JSON_FILE)

    def getProducts_json(self):
        products = []
        data = Utility.read_json(Data.PRODUCTS_JSON_FILE)
        for item in data['products']:
            product = Product(item['name'], item['desc'], item['price'])
            products.append(product)
        return products

    # def read_products_from_json(self):
    #     products = []
    #
    #     with open(Data.PRODUCTS_JSON_FILE) as jsonfile:
    #         reader = json.load(jsonfile)
    #         for row in reader['products']:
    #             product = Product(row['name'], row['desc'], row['price'])
    #             products.append(product)
    #     jsonfile.close()
    #
    #     return products
