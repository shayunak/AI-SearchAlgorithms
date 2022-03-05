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

    def create_orc_table(self, orcs):
        table = []
        for i in range(self.board_dimensions.Row):
            new_row = []
            for j in range(self.board_dimensions.Column):
                new_row.append(None)
            table.append(new_row)
        
        for i in range(len(orcs)):
            orc_loc = orcs[i].Position
            orc_rank = orcs[i].Rank
            for j in range(orc_loc.Row - orc_rank, orc_loc.Row + orc_rank + 1):
                for k in range(orc_loc.Column - orc_rank, orc_loc.Column + orc_rank + 1):
                    if k >= 0 and k < self.board_dimensions.Column and j >= 0 and j < self.board_dimensions.Row and abs(orc_loc.Row - j) + abs(orc_loc.Column - k) <= orc_rank:
                        table[j][k] = i + 1
            table[orc_loc.Row][orc_loc.Column] = 0

        return table

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
        self.Orc_table = self.create_orc_table([self.new_orc(self.read_next_line()) for i in range(self.number_of_orcs)])
        self.fellowship_members = [self.new_member(self.read_next_line()) for i in range(self.number_of_fellowship_members)]
        for i in range(len(self.fellowship_members)):
            self.fellowship_members[i].set_goal(self.read_next_line())
        self.input_file.close()
        
class State:
    def __init__(self, gandalf_position, gondor_position, fellowship_members, cost, in_orc_area, passed_through_orc_cells, orc_table):
        self.cost = cost
        self.gandalf_position = gandalf_position
        self.gondor_position = gondor_position
        self.fellowship_members = fellowship_members
        self.in_orc_area = in_orc_area
        self.passed_through_orc_cells = passed_through_orc_cells
        self.orc_table = orc_table

alg = Base_algorithm('test_02.txt')
for row in alg.Orc_table:
    print(row)  