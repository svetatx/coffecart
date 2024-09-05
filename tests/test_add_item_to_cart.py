from components import add_item_to_cart


def test_add_espresso_to_cart():
    add_item_to_cart.visit()
    add_item_to_cart.add_espresso_to_cart()
    add_item_to_cart.go_to_cart()
    add_item_to_cart.should_have_espresso_in_cart()