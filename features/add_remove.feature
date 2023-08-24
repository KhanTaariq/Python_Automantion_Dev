Feature: Add and Remove Elements

  Scenario: Add and Remove Elements
    Given the "add_remove_elements_page" page is open with title "The Internet"
    When on page "add_remove_elements_page" the user clicks the "add_btn"
    Then on page "add_remove_elements_page" the user clicks the "delete_btn"
