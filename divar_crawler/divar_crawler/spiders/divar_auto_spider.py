# import time
#
# import scrapy
#
# class DivarSpider(scrapy.Spider):
#     name = 'divar_auto'
#     allowed_domains = ['divar.ir']
#     start_urls = ['https://divar.ir/s/shiraz/auto']
#     download_delay = 1
#     page_number = 1
#
#     def parse(self, response):
#         items = response.xpath('//div[@class="post-list__widget-col-c1444"]')
#         for item in items:
#             time.sleep(2)
#             title = item.xpath('.//h2/text()').get()
#             price = item.xpath('.//div[@class="kt-post-card__description"][2]/text()').get()
#             yield {
#                 'title': title,
#                 'price': price if price else None,
#             }
#         self.page_number += 1
#         next_page = f'https://divar.ir/s/shiraz/auto?page={self.page_number}'
#         yield scrapy.Request(next_page, callback=self.parse)


# ///////////crawlinf by filter:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get('https://divar.ir/s/shiraz/car')


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'kt-selector-row'))
    )

    brand_buttons = driver.find_elements(By.CLASS_NAME, 'kt-selector-row')
    for button in brand_buttons:
        button.click()
        time.sleep(2)

        all_models = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'همه‌ی مدل‌های')]"))
        )
        all_models.click()

        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(span/text(),'تأیید')]"))
        )
        confirm_button.click()
        time.sleep(3)


        car_cards = driver.find_elements(By.CLASS_NAME,"post-list__widget-col-c1444")
        for card in car_cards:
            model = card.find_element(By.CSS_SELECTOR, 'h2.title').text
            price = card.find_element(By.CSS_SELECTOR, "kt-post-card__description"][2]).text
            print(f'Model: {model}, Price: {price}')

        driver.back()
        time.sleep(2)

finally:
    driver.quit()
