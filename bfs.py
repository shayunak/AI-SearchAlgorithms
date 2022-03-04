class Point:
    def __init__(self, Row, Column):
        self.Row = Row
        self.Column = Column
    
    def print_out(self):
        print(self.Row, self.Column)

class Orc:
    def __init__(self, Position, Rank):
        self.Position = Position
        self.Rank = Rank

class Fellowship_member:
    def __init__(self, Position):
        self.Position = Position
        self.Goal = None
    
    def set_goal(self, goal_str):
        self.Goal = Point(int(goal_str[0]), int(goal_str[1]))


class Base_algorithm:
    def read_next_line(self):
        return self.input_file.readline().strip().split(' ')

    def new_orc(self, orc_desc_str):
        return Orc(Point(int(orc_desc_str[0]), int(orc_desc_str[1])), int(orc_desc_str[2]))
    
    def new_member(self, member_desc_str):
        return Fellowship_member(Point(int(member_desc_str[0]), int(member_desc_str[1])))

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
        self.Orcs = [self.new_orc(self.read_next_line()) for i in range(self.number_of_orcs)]
        self.fellowship_members = [self.new_member(self.read_next_line()) for i in range(self.number_of_fellowship_members)]
        self.fellowship_members = [member.set_goal(self.read_next_line()) for member in self.fellowship_members]

        
alg = Base_algorithm('test_00.txt')
