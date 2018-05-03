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

def containerTest(container):
    container.addData()
    container.getData()
    container.resetData()

if __name__ == '__main__':
    c = container()
    containerTest(c)
    q = queue()
    containerTest(q)
