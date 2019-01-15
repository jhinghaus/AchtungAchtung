#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from achtungachtung import alert
import requests

headers = {'Accept':'application/json, text/javascript, */*; q=0.01',
           'Cache-Control':'max-age=0',
           #'If-Modified-Since':'Fri, 04 Nov 2016 02:40:01 GMT',
}

warnung_url = 'https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json'

class BundGenerator(alert.AlertGenerator):
    ''' Generates alerts from warnung.bund.de '''

    def requestData(self):
        ''' get raw alert data from the web '''
        res = requests.get(url=warnung_url, headers=headers)
        # do something for bad status codes
        res.raise_for_status()
        try:
            objects = res.json()
        except Exception as ex:
            raise ex
        return objects

    def alertsFromData(self, raw_alerts):
        ''' create a list of alert objects from raw alert data'''
        alerts = []
        for item in raw_alerts:
            infos = item.get('info',[])
            for info in infos:
                desc = info.get('description','-')
                subject = info.get('headline','warnung.bund.de')
                areas = info.get('area',[])
                source = 'warnung.bund.de'
                for area in areas:
                    areaDesc = area.get('areaDesc','')
                    if areaDesc:
                        new_alert = alert.Alert(subject=subject,
                                                description=desc,
                                                area=areaDesc,
                                                source=source)
                        alerts.append(new_alert)
        return alerts

    def run(self):
        ''' return alerts from the website '''
        raw_alerts = self.requestData()
        alerts = self.alertsFromData(raw_alerts)
        return alerts
