Feature: Locating buttons with dynamic id's

  Scenario: Dynamic locator buttons
    Given the "challenging_dom" page is open with title "The Internet"
    When on page "challenging_dom" the user clicks the "btn"
    Then on page "challenging_dom" the user clicks the "btn_alert"
    And on page "challenging_dom" the user clicks the "btn_success"
    And on page "challenging_dom" the user clicks the "btn_alert"
    And on page "challenging_dom" the user clicks the "btn_edit"
    And on page "challenging_dom" the user clicks the "btn_delete"