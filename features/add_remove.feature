Feature: Add and Remove Elements

  Scenario: Add and Remove Elements
    Given the "add_remove_elements_page" page is open with title "The Internet"
    When on page "add_remove_elements_page" the user clicks the "add_btn"
    Then on page "add_remove_elements_page" the user clicks the "delete_btn"


    
    # Given Add/Remove Element page is open
    # When the user clicks on the Add Element button
    # Then the user clicks on the Delete Element button