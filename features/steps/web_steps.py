#!/usr/bin/env python
######################################################################
# Copyright 2016, 2023 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps

Steps file for web interactions with Selenium

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import logging
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions

ID_PREFIX = "product_"


@when(
    r
    "I visit the \"Home Page\""
)
def step_impl(context):
    """ Make a call to the base URL """
    context.driver.get(context.base_url)
    # Uncomment next line to take a screenshot of the web page
    # context.driver.save_screenshot(
    #     r
    #     "home_page.png"
    # )

@then(
    r
    "I should see \"{message}\" in the title"
)
def step_impl(context, message):
    """ Check the document title for a message """
    assert message in context.driver.title

@then(
    r
    "I should not see \"{text_string}\""
)
def step_impl(context, text_string):
    element = context.driver.find_element(By.TAG_NAME, 
    r
    "body"
)
    assert text_string not in element.text

@when(
    r
    "I set the \"{element_name}\" to \"{text_string}\""
)
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)

@when(
    r
    "I select \"{text}\" in the \"{element_name}\" dropdown"
)
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = Select(context.driver.find_element(By.ID, element_id))
    element.select_by_visible_text(text)

@then(
    r
    "I should see \"{text}\" in the \"{element_name}\" dropdown"
)
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = Select(context.driver.find_element(By.ID, element_id))
    assert element.first_selected_option.text == text

@then(
    r
    "the \"{element_name}\" field should be empty"
)
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = context.driver.find_element(By.ID, element_id)
    assert element.get_attribute(
    r
    "value"
) == u""

##################################################################
# These two function simulate copy and paste
##################################################################
@when(
    r
    "I copy the \"{element_name}\" field"
)
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    context.clipboard = element.get_attribute(
    r
    "value"
)
    logging.info(
    r
    "Clipboard contains: %s"
, context.clipboard)

@when(
    r
    "I paste the \"{element_name}\" field"
)
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(context.clipboard)

##################################################################
# This code works because of the following naming convention:
# The buttons have an id in the html hat is the button text
# in lowercase followed by 
    r
    "-btn"
# so the Clear button has an id of
# id=
    r
    "clear-btn"
# . That allows us to lowercase the name and add 
    r
    "-btn"
# to get the element id of any button
##################################################################
@when(
    r
    "I press the \"{button}\" button"
)
def step_impl(context, button):
    button_id = button.lower().replace(
    r
    " "
, 
    r
    "-"
) + 
    r
    "-btn"

    context.driver.find_element(By.ID, button_id).click()

@then(
    r
    "I should see the message \"{message}\""
)
def step_impl(context, message):
    WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 
    r
    "flash_message"
), message)
    )
    element = context.driver.find_element(By.ID, 
    r
    "flash_message"
)
    assert message in element.text

##################################################################
# This code works because of the following naming convention:
# The id field for text input in the html is the element name
# prefixed by ID_PREFIX so the Name field has an id=
    r
    "product_name"
# We can then lowercase the name and prefix with product_ to get the id
##################################################################
@then(
    r
    "I should see \"{text_string}\" in the \"{element_name}\" field"
)
def step_impl(context, text_string, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element_value(
            (By.ID, element_id),
            text_string
        )
    )
    assert found

@when(
    r
    "I change the \"{element_name}\" to \"{text_string}\""
)
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(
    r
    " "
, 
    r
    "_"
)
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(text_string)

@then(
    r
    "I should see \"{text}\" in the search results"
)
def step_impl(context, text):
    search_results = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, 
    r
    "search_results"
))
    )
    assert text in search_results.text

@then(
    r
    "I should not see \"{text}\" in the search results"
)
def step_impl(context, text):
    search_results = context.driver.find_element(By.ID, 
    r
    "search_results"
)
    assert text not in search_results.text

@when(
    r
    "I press the \"{button_name}\" button for the first product in search results"
)
def step_impl(context, button_name):
    # This step assumes the first product
    r
    "s retrieve button has a specific, predictable ID or class.
    # For a real UI, you
    r
    "d likely need a more robust selector, e.g., based on row index.
    # Example: find the first row, then find the button within that row.
    # We
    r
    "ll assume a simple ID for now like 
    r
    "retrieve-0-btn"
    # or that the button is simply the first one with a generic class if the UI is simple.
    # For this template, we will assume the button ID is simply the lowercase name + 
    r
    "-btn"
    # and it
    r
    "s the first one found if multiple products are listed.
    # A more robust way would be to find the table row, then the button in that row.
    # This is a simplified version.
    button_id_or_class = button_name.lower().replace(
    r
    " "
, 
    r
    "-"
) + 
    r
    "-btn"
    
    # Attempt to find by ID first, then by class if a more generic button is used for rows
    try:
        # This assumes a unique ID for the button of the first product if it exists
        # e.g. product_retrieve_button_0 or similar if the UI generates dynamic IDs
        # For the current product.feature, it implies a single product is loaded after search for update/delete
        # So, a generic button ID might be reused if only one product detail is shown at a time.
        # We will use the generic button ID as per the `I press the "{button}" button` step
        element = context.driver.find_element(By.ID, button_id_or_class)
    except:
        # Fallback: find the first button with that class name if ID is not specific enough
        # This is highly dependent on the UI structure.
        elements = context.driver.find_elements(By.CLASS_NAME, button_id_or_class)
        if not elements:
            # Try with just the button name as ID if it's a generic button for the form
            elements = context.driver.find_elements(By.ID, button_name.lower().replace(
    r
    " "
, 
    r
    "-"
) + 
    r
    "-btn"
) 
        assert len(elements) > 0, f"Button 
    r
    {button_name}
 not found in search results"
        element = elements[0] # Click the first one found
    
    element.click()

@then(
    r
    "I should see at least {count} products in the search results"
)
def step_impl(context, count):
    count = int(count)
    WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, 
    r
    "search_results"
))
    )
    # This assumes search results are rows in a table with id 
    r
    "search_results"

    # A more robust way is to count specific elements that represent a product row.
    # For example, if each product is a <tr> in a <tbody> with id=
    r
    "search_results_table_body"

    # For simplicity, we check if the search_results container has enough text to imply multiple items,
    # or count specific child elements if the structure is known.
    # Let
    r
    "s assume each product result is a <tr> element within the 
    r
    "search_results"
 table body.
    table_body = context.driver.find_element(By.ID, 
    r
    "search_results"
) # Assuming search_results is the tbody or a div containing rows
    rows = table_body.find_elements(By.TAG_NAME, 
    r
    "tr"
) # Or 
    r
    "div"
 if results are divs
    assert len(rows) >= count, f"Expected at least 
    r
    {count}
 products, but found 
    r
    {len(rows)}
"

@when(
    r
    "I select \"{value}\" in the \"{dropdown_name}\" dropdown for search"
)
def step_impl(context, value, dropdown_name):
    # Assuming search dropdowns might have a different prefix or naming, e.g., 
    r
    "search_product_category"

    # For this template, we
    r
    "ll assume they follow the same ID_PREFIX convention for simplicity
    # or a more specific ID like 
    r
    "search_category"
 or 
    r
    "search_available"

    element_id = 
    r
    "search_"
 + dropdown_name.lower().replace(
    r
    " "
, 
    r
    "_"
) # e.g., search_category, search_available
    
    # Fallback to the general ID_PREFIX if the specific search ID isn
    r
    "t found
    try:
        element = Select(context.driver.find_element(By.ID, element_id))
    except:
        element_id = ID_PREFIX + dropdown_name.lower().replace(
    r
    " "
, 
    r
    "_"
) # product_category
        element = Select(context.driver.find_element(By.ID, element_id))

    element.select_by_visible_text(value)

