@regression_tests
Feature: Validate element created dropdown column

  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The page "should" contain the next elements
      | name              | type  |
      | menu_item_flights | a     |
      | menu_item_stays   | a     |
      | menu_item_cars    | a     |
      | destination       | input |
      | origin            | input |

  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should contain the "https://www.kayak.com" url

  Scenario Outline: Navigate between countries and validate the URL
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I navigate to the "<url>" URL
    Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |

  Scenario Outline: Validate lateral menu items
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    When I open the lateral menu
    And I click the "<name>" "<type>" element
    Then The url page should contain the "<path>" url

    Examples:
      | name                        | type | path                          |
      | lateral_menu_flights        | a    | /flights                      |
      | lateral_menu_stays          | a    | /stays                        |
      | lateral_menu_cars           | a    | /cars                         |
      | lateral_menu_ai_mode        | a    | /aimode                       |
      | lateral_menu_explore        | a    | /explore                      |
      | lateral_menu_blogs          | a    | /news                         |
      | lateral_menu_direct_flights | a    | /direct                       |
      | lateral_menu_discover       | a    | /el-mejor-momento-para-viajar |
      | lateral_menu_business       | a    | /business                     |
      | lateral_menu_trips          | div  | /trips                        |
