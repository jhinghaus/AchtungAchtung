#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .context import achtungachtung
from achtungachtung import bundalertgenerator
import unittest

example = [{u'status': u'Actual',
  u'info': [{u'category': [u'Safety'],
             u'responseType': [u'Monitor'],
             u'description': u'Wegen der aktuellen Wettersituation kommt es weiterhin zu Problemen im Abreiseverkehr im Umfeld des Eventgel\xe4ndes. Der Kreis Kleve hat das B\xfcrgertelefon eingestellt.',
             u'language': u'DE',
             u'area': [{u'areaDesc': u'Landkreis/Stadt: Kreis Kleve',
                        u'polygon': [u'6.4887,51.8118 6.4863,51.8128']},
                       {u'geocode': [{u'value': u'051540000000', u'valueName': u'GEOCODE'}],
                        u'areaDesc': u'Landkreis/Stadt: Kreis Kleve'}],
             u'headline': u'Entwarnung! Aktuelle Informationen zu FooBar',
             u'certainty': u'Observed',
             u'expires': u'2017-07-24T16:25:17+02:00',
             u'contact': u'B\xfcrgertelefon des Kreises Kleve und Internetauftritt FooBar -  01234-5678',
             u'web': u'warnung.bund.de',
             u'parameter': [{u'value': u'Leitstelle Kreis Kleve',
                             u'valueName': u'sender_langname'}],
             u'event': u'Gefahreninformation',
             u'urgency': u'Immediate',
             u'severity': u'Minor'}],
  u'code': [u'1.0', u'medien_regional', u'nina'],
  u'sender': u'DE-NW-KLE-S058',
  u'references': u'DE-NW-KLE-S058,DE-NW-KLE-S058-20170724-001,2017-07-24T00:00:00+00:00',
  u'scope': u'Public',
  u'msgType': u'Cancel',
  u'identifier': u'DE-NW-KLE-S058-20170724-002',
  u'sent': u'2017-07-24T10:25:17+02:00'}]

class BundTC(unittest.TestCase):

    def test_alertsFromData(self):
        generator = bundalertgenerator.BundGenerator()
        alert = generator.alertsFromData(example)[0]
        self.assertEqual(alert.subject, 'Entwarnung! Aktuelle Informationen zu FooBar')
        self.assertEqual(alert.description, 'Wegen der aktuellen Wettersituation kommt es weiterhin zu Problemen im Abreiseverkehr im Umfeld des Eventgel\xe4ndes. Der Kreis Kleve hat das B\xfcrgertelefon eingestellt.')
        self.assertEqual(alert.area, 'Landkreis/Stadt: Kreis Kleve')
        self.assertEqual(alert.source, 'warnung.bund.de')
