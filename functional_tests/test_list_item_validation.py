#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"))

        self.get_item_input_box().send_keys('Buy Milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')

        self.browser.find_element_by_id('id-new-item').send_keys(Keys.ENTER)
        self.wait_for(lambda:
                      self.assertEqual(self.browser.find_element_by_css_selector('.has-error').text,
                                       "You can't have an empty list item"))

        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box(j).send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')
        self.wait_for_row_in_list_table('2: Make tea')
