#!/usr/bin/env python

'''
Provide basic container to save data
currently should support 3 basic container
1. a singleton queue to pop and push data
2. a singleton SQL to save and read data
3. a singleton redis to save and read data

Basic operation as follow
1. open/close , provide with as method.
2. add data(for queue should be like push action)
3. get a data(for queue should be pop action)
4. clean(clean all data)
'''
import util
import threading

class container(object):
    """docstring for container"""
    def __init__(self):
        self.name = 'Basic Container'

    def addData(self, *args, **kwargs):
        '''To add a data into container'''
        print('%s method %s' % (self.name, 'addData'))
        

    def getData(self, *args, **kwargs):
        '''To get a data from container'''
        print('%s method %s' % (self.name, 'getData'))
        

    def resetData(self, *args, **kwargs):
        '''To reset a data into container'''
        print('%s method %s' % (self.name, 'resetData'))
    

class queue(container):
    """docstring for queue"""
    def __init__(self):
        super(queue, self).__init__()
        self.name = 'Queue Container'
        self._content = []

    def addData(self, *args, **kwargs):
        '''To add a data into container'''
        super(queue, self).addData()
        for arg in args:
            self._content.append(arg)
        
    def getData(self, *args, **kwargs):
        '''To get a data from container'''
        super(queue, self).getData()
        return self._content.pop() if self._content else None

    def resetData(self, *args, **kwargs):
        '''To reset a data into container'''
        super(queue, self).resetData()
        self._content = []

@util.SingletonCls
class webContentQueue(queue):
    def __init__(self, *args, **kwargs):
        #1.one possible super class call method
        #queue.__init__(self)
        #2.another possible super class call method
        super(kwargs['cls'], self).__init__()
        #This way will faled because wrapper will do webContentQueue = SingletonCls(webContentQueue)
        #so the webContentQueue have been change to SingletonCls, no longer webContentQueue. 
        self.name = 'webContentQueue Container'



def containerTest(container):
    container.addData("Test")
    msg = container.getData()
    if msg is not None:
        print(msg)
    else:
        print("Msg is None")
    msg = container.getData()
    if msg is not None:
        print(msg)
    else:
        print("Msg is None")
    container.resetData()

if __name__ == '__main__':
    c = container()
    containerTest(c)
    q = queue()
    containerTest(q)
    w = webContentQueue()
    containerTest(w)
