# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:45:01 2021

@author: Seema S Kanaje
"""

import unittest
import Mfgx

class ChripViewsTest(unittest.TestCase):
    def testChripViewFormat(self):
        '''should properly format a normal chirp view'''
       
        self.assertEqual(Mfgx.chripViewsFormat({
        "message": 'Hello World!',
        "author": 'Jack Daniels',
        "views": 99999,
        "date": '2021-06-28T07:00:00.000Z',
      }), 'Hello World! 06/28/2021 99999 Jack Daniels')
        
    def testAddFireEmoji(self):
        '''should properly add fire emoji when views exceed 100,000'''
        self.assertEqual(Mfgx.chripViewsFormat({
        "message": "This chirp probably won't get a lot of attention.",
        "author": 'Jane Doe',
        "views": 251236,
        "date": '2021-03-04T04:00:00.000Z',
      }), "This chirp probably won't get a lot of attention. 03/04/2021 251236 Jane Doe 🔥")
        self.assertEqual(Mfgx.chripViewsFormat({
        "message":
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam consequat quis turpis non consectetur. Sed accumsan dui rhoncus, cursus quis.',
        "author": 'Lorem Ipsum',
        "views": 1000001,
        "date": '2021-01-01T00:00:00.000Z',
      }), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam consequat quis turpis non consectetur. Se... 01/01/2021 1000001 Lorem Ipsum 🔥')
    
    def testMaxLength(self):
        '''should properly format long chirp messages'''
        self.assertEqual(Mfgx.chripViewsFormat({
        "message":
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam consequat quis turpis non consectetur. Sed accumsan dui rhoncus, cursus quis.',
        "author": 'Lorem Ipsum',
        "views": 1000001,
        "date": '2021-01-01T00:00:00.000Z',
      }), 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam consequat quis turpis non consectetur. Se... 01/01/2021 1000001 Lorem Ipsum 🔥')
            
        self.assertEqual(Mfgx.chripViewsFormat ( {"message":
          "This is a maximum length chirp because I like writing long chirps. Why? I'm not really sure. Maybe I'm just a rebel.. or maybe it's a phase?",
        "author": 'John Smith',
        "views": 100,
        "date": '2021-04-22T00:00:00.000Z',}),  "This is a maximum length chirp because I like writing long chirps. Why? I'm not really sure. Maybe I'm just a r... 04/22/2021 100 John Smith")    


if __name__ == "__main__":
   unittest.main()