class NationalPark:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise Exception
        
    
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.instances if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitor_counts = {}
        for trip in self.trips():
            visitor = trip.visitor
            visitor_counts[visitor] = visitor_counts.get(visitor, 0) + 1
        if visitor_counts:
            return max(visitor_counts, key=visitor_counts.get)
        else:
            return None
        
        