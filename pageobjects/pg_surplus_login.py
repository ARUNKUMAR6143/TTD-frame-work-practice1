import time

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from testdata import td_surplus_login1 as testdata
from helpers import commonmethods as helper
from helpers import commonmethods

sur_subtitle_locator = "//*[@id='root']/div/nav/div[1]/a/div/h2"
gust_login = "//*[@id='root']//button[2]"
add_card = "(//*[@id='root'])//button"
slides = "//*[@class='price-slider']"
links = "//*[@id='root']//a/img]"
wish_list = "//*[@class='fas fa-heart product-wishlist-icon']"
check_boxs = "//*[@class='check-lists']//input"
add_crd1 = "(//*[@class='btn primary card-button'])[1]"
add_crd2 = "(//*[@class='btn primary card-button'])[2]"

clk_card = "//*[@class='fas fa-cart-plus nav-icon ']"
wish_list1 = "(//*[@class='fas fa-heart product-wishlist-icon'])[1]"
wish_list2 = "(//*[@class='fas fa-heart product-wishlist-icon'])[2]"
wish_list3 = "(//*[@class='fas fa-heart product-wishlist-icon'])[3]"
wish_list_click = "//*[@class='far fa-heart nav-icon wish-icon']"
wishlist_add_card = "//*[@class='btn primary card-button']"
remv_f_card = "//*[@id='root']/div/div/div/div[1]/div[1]/div[2]/i"
quuantity_incrse = "(//*[@class='quantity-btn'])[2]"
size_incrse = "//*[@class='cart-size-wrapper']/select[1]"
cupn_btn = "//*[@class='btn coupon-btn']"
aply_cupn = "//*[@placeholder='cb20']"
place_ord = "//*[@class = 'btn primary order-btn']"
add_address = "//*[@class = 'btn primary']"
payment = "//*[@class = 'btn primary order-btn']"
def verify_text(driver):
    try:
        txt = helper.get_element(driver, sur_subtitle_locator).text
        assert txt == testdata.sub_title
        helper.log("sub title verified","info")
    except AssertionError as e:
        helper.log("Error in sub title verification - "+str(e),"error")

def verify_gust_login(driver,):
    try:
        helper.get_element(driver, gust_login).click()
        all_boxes = helper.get_elements(driver, check_boxs)
        for i in range(len(all_boxes)):
            all_boxes[i].click()

           # all add_to_card buttons or working or not
        all_btn = helper.get_elements(driver, add_card)
        for i in range(len(all_btn)):
            all_btn[i].is_enabled()

        max = helper.get_element(driver,slides,)
        print(max.location)

        act = ActionChains(driver)
        act.drag_and_drop_by_offset(max, 50, 0).perform()
    except AssertionError as e:
        helper.log("Error in login verification - " + str(e), "error")

def list_wish(driver):
    try:
        helper.get_element(driver, gust_login).click()
        list = helper.get_elements(driver, wish_list)
        for i in list:
            i.click()
    except AssertionError as e:
        helper.log("Error in sub title verification - "+str(e),"error")


def add_cart(driver):
    try:
        helper.get_element(driver, gust_login).click()
        helper.get_element(driver, wish_list1).click()
        helper.get_element(driver, wish_list2).click()
        helper.get_element(driver, wish_list3).click()
        helper.get_element(driver, wish_list_click).click()
        all_btn = helper.get_elements(driver, wishlist_add_card)
        for one_btn in all_btn:
            one_btn.click()
        helper.get_element(driver,clk_card).click()
        helper.get_element(driver,remv_f_card).click()
        helper.get_element(driver ,quuantity_incrse).click()
        helper.get_element(driver,quuantity_incrse).click()
        s_increase = Select(helper.get_element(driver,size_incrse))
        s_increase.select_by_value("L")
        helper.get_element(driver, cupn_btn).click()
        helper.get_element(driver,aply_cupn).send_keys(testdata.cupon)
        helper.get_element(driver, cupn_btn).click()
        helper.get_element(driver,place_ord).click()
        #helper.get_element(driver,add_address).click()
        helper.get_element(driver,payment).click()


    except AssertionError as e:
        helper.log("Error in sub title verification - "+str(e),"error")