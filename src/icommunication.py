from abc import ABC, abstractmethod

class icommunication(object):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass