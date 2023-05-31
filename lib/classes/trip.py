

class Trip:
    
    instances = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.instances.append(self)
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        from classes.visitor import Visitor
        if not isinstance(value, Visitor):
            raise Exception("Visitor must be an instance of Visitor.")
        self._visitor = value
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        from classes.national_park import NationalPark
        if not isinstance(value, NationalPark):
            raise Exception("NationalPark must be an instance of NationalPark.")
        self._national_park = value
        
    

    
    