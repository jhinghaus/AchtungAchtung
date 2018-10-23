#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import achtungachtung
from achtungachtung import staticalertgenerator
import unittest

class StaticTC(unittest.TestCase):

    def test_run(self):
        generator = staticalertgenerator.StaticAlertGenerator()
        alert = generator.run()[0]
        self.assertEqual(alert.subject, 'Static Alert')
        self.assertEqual(alert.description, 'Test')
        self.assertEqual(alert.area, 'StaticArea')
        self.assertEqual(alert.source, 'StaticData')
