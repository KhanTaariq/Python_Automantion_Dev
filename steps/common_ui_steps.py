from behave import given, then, when, step
from asserts import *
from pageobjects.add_remove import AddRemovePageObject
from pageobjects.common import CommonPageObject
from pageobjects.login import LoginPageObject


def get_element(page_name, element_name):

    el = None
    if page_name.strip().lower() == "login_page":
        el = LoginPageObject().get_element(element_name)
    if page_name.strip().lower() == "add_remove_elements_page":
        el = AddRemovePageObject().get_element(element_name)
    return el

@step('the "{page_name}" page is open with title "{expected_title}"')
def step_impl(context, page_name="", expected_title=""):
    context.current_page = CommonPageObject()
    actual_title = context.current_page.open(page_name).strip().lower()
    expected_title = expected_title.strip().lower()
    assert_equal(actual_title,
                 expected_title, 
                 msg_fmt="expected title '{}' is not equal to the actual title '{}'".format(expected_title, actual_title))