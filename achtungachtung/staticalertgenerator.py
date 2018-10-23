#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import achtungachtung.alert

class StaticAlertGenerator(achtungachtung.alert.AlertGenerator):
    ''' Generates one static alert for a static area in every run '''

    def run(self):
        ''' return one static alert for testing'''
        myAlert = achtungachtung.alert.Alert(subject='Static Alert',
                            description='Test',
                            area='StaticArea',
                            source='StaticData')
        return [myAlert]
