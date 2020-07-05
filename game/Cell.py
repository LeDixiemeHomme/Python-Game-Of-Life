class Cell:
    

    def __init__(self, n, status='alive'):
        self.status = status
        self.n = n
        self.address = {'x':'unset', 'y': 'unset'}
    
    def __str__(self):
        return self.status + ' x : ' + str(self.address['x']) + ' y : ' + str(self.address['y']) + ' ' + str(self.n)
    
    def revive(self):
        self.status = 'alive'
    
    def die(self):
        self.status = 'dead'
    
    def set_address(self, x, y):
        self.address['x'] = x
        self.address['y'] = y
