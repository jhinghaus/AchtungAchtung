#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import achtungachtung
from achtungachtung import alertcollector
import unittest
import json

class CollectTC(unittest.TestCase):

    def test_get(self):
        alerts = achtungachtung.alertcollector.getAlerts()
        # there should be at least the static one
        self.assertGreaterEqual(len(alerts),1)
        alerts = achtungachtung.alertcollector.getAlerts(area='StaticArea')
        self.assertEqual(len(alerts), 1, 'filtered too much')
        alerts = achtungachtung.alertcollector.getAlerts(area='DiesenOrtGibtEsNichtDaBinIchSicher')
        self.assertEqual(len(alerts), 0, 'did not filter')

    def test_encoder(self):
        alerts = achtungachtung.alertcollector.getAlerts(area='StaticArea')
        dump = json.dumps(alerts, cls=achtungachtung.alertcollector.AlertEncoder)
        self.assertIn('StaticArea', dump)
