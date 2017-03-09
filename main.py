import scrapy
import uuid
import os
import json
from binglee import binglee


binglee = binglee.Binglee()


def main():
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'product_pages')
    product_details = binglee.get_product_details_list('/Users/chenxuzhao/Github/binglee/product_pages/')
    out_file = open('urlfile.txt', 'w')
    print(product_details)
    out_file.write(json.dumps(product_details))
    out_file.close()


if __name__ == '__main__':
    main()
