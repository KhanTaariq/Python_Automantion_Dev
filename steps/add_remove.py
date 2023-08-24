import time
from behave import given, when, then, step
from pageobjects.add_remove import AddRemovePageObject
from steps.common_ui_steps import get_element
from pageobjects.common import CommonPageObject


@step('on page "{page_name}" the user clicks the "{element_name}"')
def step_impl(context, page_name="", element_name=""):
    el = get_element(page_name, element_name)
    CommonPageObject().click_element(element_name, el)

# @step('the user clicks on the Add Element button')
# def step_impl(context):
#     context.current_page = context.current_page.add_elem()
#     context.current_page = context.current_page.add_elem()

# @step('the user clicks on the Delete Element button')
# def step_impl(context):
#     context.current_page = context.current_page.delete_elem()
#     context.current_page = context.current_page.delete_elem()
