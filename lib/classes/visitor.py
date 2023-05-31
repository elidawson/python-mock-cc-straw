class Visitor:
    
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not 1 <= len(value) <= 15:
            raise Exception("Name must be between 1 and 15 characters.")
        self._name = value
    