from pages.login_page import LoginPage

def test_odoo_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("odoo16@gmail.com", "admin")

    print("loginn in")

    browser.implicitly_wait(10)

    assert "Odoo" in browser.title 
