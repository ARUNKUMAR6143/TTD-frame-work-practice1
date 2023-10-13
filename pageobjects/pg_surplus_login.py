from testdata import td_surplus_login1 as testdata
from helpers import commonmethods as helper


sur_subtitle_locator = "//*[@id='root']/div/nav/div[1]/a/div/h2"
gust_login = "//*[@id='root']//button[2]"
#alpy_filters = "(//*[@class='btn btn-text filter-button'])[2]"
#clot_catg = "//*[@id='men-category']"
#rating = "//*[@id='four-stars']"

check_boxs = "//*[@class='check-lists']//input"
def verify_text(driver):
    try:
        txt = helper.get_element(driver, sur_subtitle_locator).text
        assert txt == testdata.sub_title
        helper.log("sub title verified","info")
    except AssertionError as e:
        helper.log("Error in sub title verification - "+str(e),"error")

def verify_gust_login(driver):
    try:
        helper.get_element(driver, gust_login).click()
        #helper.get_element(driver, alpy_filters).click()
        #helper.get_element(driver, clot_catg).click()


        all_boxes = helper.get_elements(driver, check_boxs)

        for i in range(len(all_boxes)):
            all_boxes[i].click()


        helper.log("login verified", "info")
    except AssertionError as e:
        helper.log("Error in login verification - " + str(e), "error")