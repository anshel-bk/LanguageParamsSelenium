link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" # урл должен быть именно такой если брать скопированный он всегда будет по умолчанию ru

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.implicitly_wait(5) # конкретно у меня драйвер работает как говно можно убрать
    basket = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert basket.text == "Añadir al carrito"