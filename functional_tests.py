#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser =  webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id-new-item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        inputbox.send_keys('Budy peacok feathers')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)
        table = self.browser.find_element_by_id('id-list-table')
        rows = table.find_element_by_tag_name('tr')

        self.assertTrue(any(row.text=='1: Buy peacock feathers' for row in rows))

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
