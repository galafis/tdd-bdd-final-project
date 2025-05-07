Feature: The product store service back-end
    As a Product Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my products

Background:
    Given the following products
        | name        | description              | price   | available | category   | image_url                               |
        | Hat         | A red fedora             | 59.95   | True      | CLOTHS     | http://example.com/images/hat.jpg       |
        | Shoes       | Blue shoes               | 120.50  | False     | CLOTHS     | http://example.com/images/shoes.jpg     |
        | Big Mac     | 1/4 lb burger            | 5.99    | True      | FOOD       | http://example.com/images/bigmac.jpg    |
        | Sheets      | Full bed sheets          | 87.00   | True      | HOUSEWARES | http://example.com/images/sheets.jpg    |
        | Laptop      | High-performance laptop  | 1200.00 | True      | ELECTRONICS| http://example.com/images/laptop.jpg    |
        | Coffee Maker| Drip coffee maker        | 49.99   | True      | HOUSEWARES | http://example.com/images/coffeemaker.jpg|
        | T-Shirt     | Cotton T-Shirt           | 19.99   | True      | CLOTHS     | http://example.com/images/tshirt.jpg    |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Product Catalog Administration" in the title
    And I should not see "404 Not Found"

Scenario: Create a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hammer"
    And I set the "Description" to "Claw hammer"
    And I select "True" in the "Available" dropdown
    And I select "TOOLS" in the "Category" dropdown
    And I set the "Price" to "34.95"
    And I set the "Image URL" to "http://example.com/images/hammer.jpg"
    And I press the "Create" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    Then the "Id" field should be empty
    And the "Name" field should be empty
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hammer" in the "Name" field
    And I should see "Claw hammer" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "TOOLS" in the "Category" dropdown
    And I should see "34.95" in the "Price" field
    And I should see "http://example.com/images/hammer.jpg" in the "Image URL" field

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see "Hat" in the search results
    And I should see "A red fedora" in the search results
    When I press the "Retrieve" button for the first product in search results
    And I change the "Description" to "A stylish red fedora"
    And I change the "Price" to "65.00"
    And I press the "Update" button
    Then I should see the message "Success"
    When I press the "Clear" button
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see "Hat" in the search results
    And I should see "A stylish red fedora" in the search results
    And I should see "65.00" in the search results

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Shoes"
    And I press the "Search" button
    Then I should see "Shoes" in the search results
    When I press the "Retrieve" button for the first product in search results
    And I press the "Delete" button
    Then I should see the message "Success"
    And the "Id" field should be empty
    When I press the "Clear" button
    And I set the "Name" to "Shoes"
    And I press the "Search" button
    Then I should not see "Shoes" in the search results

Scenario: List All Products
    When I visit the "Home Page"
    And I press the "Search" button
    Then I should see at least 7 products in the search results
    And I should see "Hat" in the search results
    And I should see "Shoes" in the search results
    And I should see "Big Mac" in the search results
    And I should see "Sheets" in the search results
    And I should see "Laptop" in the search results
    And I should see "Coffee Maker" in the search results
    And I should see "T-Shirt" in the search results

Scenario: Search Products by Name
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see "Hat" in the search results
    And I should not see "Shoes" in the search results
    And I should see "A red fedora" in the search results

Scenario: Search Products by Category
    When I visit the "Home Page"
    And I select "CLOTHS" in the "Category" dropdown for search
    And I press the "Search" button
    Then I should see "Hat" in the search results
    And I should see "Shoes" in the search results
    And I should see "T-Shirt" in the search results
    And I should not see "Big Mac" in the search results

Scenario: Search Products by Availability
    When I visit the "Home Page"
    And I select "True" in the "Available" dropdown for search
    And I press the "Search" button
    Then I should see "Hat" in the search results
    And I should see "Big Mac" in the search results
    And I should not see "Shoes" in the search results

