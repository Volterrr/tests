from selenium import webdriver

class pizza():

    driver = webdriver.Chrome("C:/Users/edava/Downloads/chromedriver.exe")
    driver.maximize_window()

    # User opens the page that offers pizza delivery
    def test_1(self):
        driver.get("https://pizza.com")
        q = driver.title
        assert q == "Pizza"

    # User chooses the pizza type
    def test_2(self):
        driver.find_element_by_id('pizza_type').click()
        q = driver.title
        assert q == "Type Pizza"

    # User confirms the order
    def test_3(self):
        driver.find_element_by_id('confirm').click()
        assert alert    

                                                        # SQL request for verifying order
                                                        # Select "order" from Orders