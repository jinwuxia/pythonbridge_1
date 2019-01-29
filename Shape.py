from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."

class Shape:
    __metaclass__ = ABCMeta

    drawing_api = None
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def resize_by_percentage(self, percent):
        raise NotImplementedError(NOT_IMPLEMENTED)
