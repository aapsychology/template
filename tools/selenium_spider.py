# -*- coding: utf-8 -*-

# from selenium import webdriver
# from scrapy.selector import Selector
#
# browser = webdriver.Chrome(executable_path="D:/tools/chromedriver/chromedriver.exe")
#
# browser.get("http://www.stats.gov.cn/")
# t_selector=Selector(text=browser.page_source)

# browser.find_element_by_css_selector(".view-signin input[name='account']").send_keys("18782902568")
# browser.find_element_by_css_selector(".view-signin input[name='password']").send_keys("admin125")
#
# browser.find_element_by_css_selector(".view-signin button.sign-button").click()
#selenium 完成微博模拟登录

# browser.get("https://www.oschina.net/blog")
# import time
# time.sleep(5)
# browser.find_element_by_css_selector("#loginname").send_keys("liyao198705@sina.com")
# browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("da_ge_da")
# browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()

# for i in range(3):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
# t_selector = Selector(text=browser.page_source)
# print (t_selector.css(".tm-promo-price .tm-price::text").extract())


#设置chromedriver不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_opt.add_experimental_option("prefs", prefs)
