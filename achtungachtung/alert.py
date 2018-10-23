#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Alert(object):

    def __init__(self, subject, description, area, source):
        self.subject = subject
        self.description = description
        self.area = area
        self.source = source

    def __str__(self):
        return self.subject + ' in ' + self.area

    def __eq__(self, other):
        # source is not part of the compare
        return self.subject == other.subject and self.area == other.area and self.description == other.description

    def __hash__(self):
        return hash((self.subject, self.description, self.area))

class AlertGenerator(object):
    ''' Base class to generate alerts for whatever reason '''

    def run(self):
        ''' returns a list of alerts '''
        raise NotImplementedError('Have to implement run()')
