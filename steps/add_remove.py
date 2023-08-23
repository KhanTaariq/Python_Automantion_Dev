import time
from behave import given, when, then
from pageobjects.add_remove import AddRemovePageObject


@given('Add/Remove Element page is open')
def step_impl(context):
    context.current_page = AddRemovePageObject()
    context.current_page.open()

@when('the user clicks on the Add Element button')
def step_impl(context):
    context.current_page = context.current_page.add_elem()
    context.current_page = context.current_page.add_elem()

@then('the user clicks on the Delete Element button')
def step_impl(context):
    context.current_page = context.current_page.delete_elem()
    context.current_page = context.current_page.delete_elem()
