from components import payment


def test_payment_form():
    payment.visit()
    payment.fill_payment_details("Svetlana", "lana.zubrilinq@gmail.com")
    payment.should_see_success_message()