from selene import browser, by, be
from selene.support.shared.jquery_style import s

def visit():
    browser.open("https://coffee-cart.app/")


def add_espresso_to_cart():
    s(by.xpath("//div[@data-test='Espresso')]")).click()

def go_to_cart():
    s(by.css("//a[href='/cart']")).click()


def should_have_espresso_in_cart():
    s(by.xpath("//h2[contains(text(),'Espresso')]")).should(be.visible)