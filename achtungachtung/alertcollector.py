#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from achtungachtung import staticalertgenerator
from achtungachtung import bundalertgenerator
from achtungachtung import alert
import json

def getAlerts(area=''):
    ''' Collect alerts from all AlertGenerators an return them

    area -- return only alerts for areas containing this argument (default is all current alerts)
    '''
    generators = [staticalertgenerator.StaticAlertGenerator(), bundalertgenerator.BundGenerator()]
    alerts = []
    # gather alerts
    for generator in generators:
        alerts.extend(generator.run())
    return [al for al in alerts if area in al.area]

class AlertEncoder(json.JSONEncoder):

    def default(self, al):
        if isinstance(al, alert.Alert):
            return al.__dict__
        else:
            super().default(self, al)

def main():
    print('main')
    parser = argparse.ArgumentParser(description='Check for alerts')
    parser.add_argument('--area', '-a', type=str,
                        help='only alerts for areas containing this argument (default is all current alerts)',
                        default='')
    args = parser.parse_args()
    alerts = getAlerts(area=args.area)
    print(json.dumps(alerts, cls=AlertEncoder))

if __name__ == '__main__':
    main()
