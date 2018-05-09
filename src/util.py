#!/usr/bin/env python

import threading

def singletonFunc(cls, *args, **kwargs):
    '''one of singleton usage definition by closure'''
    instances = {}
    def _wrapper():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _wrapper

class SingletonCls(object):
    '''one of singleton usage definition by class'''
    def __init__(self, cls):
        self.cls = cls
        self._instances = None
    def __call__(self, *args, **kwargs):
        if not self._instances:
            kwargs['cls'] = self.cls
            self._instances = self.cls(*args, **kwargs)
        return self._instances

class SngltnClsThrdSf(object):
    '''one of thread safe singleton usage definition by class'''
    def __init__(self, cls):
        self.cls = cls
        self._instances = None
    def __call__(self, *args, **kwargs):
        if not self._instances:
            self._instances = self.cls(*args, **kwargs)
        return self._instances