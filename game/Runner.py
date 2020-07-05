from Cell import Cell


class Runner:
    to_revive = []
    to_kill = []

    def __init__(self, density=100, size=10, initial_status='alive', rounds=10):
        self.density = density
        self.size = size
        self.map = self.generate_map(initial_status, size)
        self.set_addresses()
        self.rounds = rounds

    def generate_map(self, initial_status, size):
        return [[Cell((i + 1) * (_ + 1), initial_status) for i in range(size)] for _ in range(size)]

    
    def set_addresses(self):
        for i in range(len(self.map)):
            y = i
            for j in range(len(self.map[i])):
                cell = self.map[i][j]
                x = j
                cell.set_address(x, y)

    def run(self):
        if self.rounds < 0:
            return

        for cell_line in self.map:
            for cell in cell_line:
                self.try_kill(cell) if cell.status == 'alive' else self.try_revive(cell)
        self.update()
        self.reset()

    def try_kill(self, cell):
        neighbourhood = self.get_neighborhood(cell)
        if len(neighbourhood) is not 2 or 3:
            self.to_kill.append(cell)

    def try_revive(self, cell):
        neighbourhood = self.get_neighborhood(cell)
        if len(neighbourhood) is 3:
            self.to_revive.append(cell)

    def get_neighborhood(self, cell):
        neigbhors = []
        top_y_index = cell.address['y'] - 1 if cell.address['y'] > 0 else self.size - 1
        bot_y_index = cell.address['y']+ 1 if cell.address['y'] < self.size - 1 else 0
        for y in [top_y_index, cell.address['y'], bot_y_index]:
            left_x_index = cell.address['x'] - 1 if cell.address['x'] > 0 else self.size - 1
            right_x_index = cell.address['x'] + 1 if cell.address['x'] < self.size - 1 else 0
            for x in [left_x_index, cell.address['x'], right_x_index]:
                neigbhors.append(self.map[y][x])
        return [n for n in neigbhors if n.status == 'alive']

    def update(self):
        for cell in self.to_revive:
            cell.revive()
        
        for cell in self.to_kill:
            cell.die()

    def reset(self):
        self.to_kill = []
        self.to_revive = []

    def __str__(self):
        return ('\ndensity = ' + str(self.density) + '\nsize = ' + str(self.size) + '\npopulation = ' + self.stringify_map())

    def stringify_map(self):
        return str([[str(cell) for cell in cell_array] for cell_array in self.map])
