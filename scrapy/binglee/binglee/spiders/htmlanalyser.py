from bs4 import BeautifulSoup

class HtmlAnalyser:

    def scrape_product_pages_url(self, directory_file_name):
        """
        Scrape all product pages' url
        :param directory_file_name: directory page's file path
        """
        product_urls = []
        directory_page = open(directory_file_name, 'r')
        file_content = directory_page.read()
        directory_page.close()
        soup = BeautifulSoup(file_content, 'html.parser')
        for category_list in soup.find_all('div', {'class': 'category-products'}):
            category_products = category_list.find_all(
                'ul', {'class': 'products-grid'})
            for products_list in category_products:
                for product_name in products_list.find_all('div', {'class': 'product-name'}):
                    product_urls.append(product_name.a.get('href'))

        return product_urls
