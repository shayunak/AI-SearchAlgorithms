class Point:
    def __init__(self, Row, Column):
        self.Row = Row
        self.Column = Column
    
    def print_out(self):
        print(self.Row, self.Column)

class Base_algorithm:
    def read_next_line(self):
        return self.input_file.readline().strip().split(' ')


    def __init__(self, path_to_file):
        self.input_file = open(path_to_file)
        board_dimensions_str = self.read_next_line()
        self.board_dimensions = Point(int(board_dimensions_str[0]), int(board_dimensions_str[1]))
        gandalf_position_str = self.read_next_line()
        self.gandalf_position = Point(int(gandalf_position_str[0]), int(gandalf_position_str[1]))
        gondor_position_str = self.read_next_line()
        self.gondor_position = Point(int(gondor_position_str[0]), int(gondor_position_str[1]))
        number_of_subsidiary_actors = self.read_next_line()
        self.number_of_orcs = int(number_of_subsidiary_actors[0])
        self.number_of_fellowship_members = int(number_of_subsidiary_actors[1])
        

