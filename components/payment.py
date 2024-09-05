from selene import browser, by, be
from selene.support.shared.jquery_style import s


def visit():
    browser.open("https://coffee-cart.app/cart")

def fill_payment_details( name, email):
    s("#name").type(name)
    s("#email").type(email)
    s("#promotion").click()
    s("#submit-payment").click()

def should_see_success_message():
    s(".snackbar.success").should(be.visible)