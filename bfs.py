class Point:
    def __init__(self, Row, Column):
        self.Row = Row
        self.Column = Column
    
    def equals(self, another_point):
        return self.Row == another_point.Row and self.Column == another_point.Column

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
        for i in range(State.board_dimensions.Row):
            new_row = []
            for j in range(State.board_dimensions.Column):
                new_row.append(None)
            table.append(new_row)
        
        for i in range(len(orcs)):
            orc_loc = orcs[i].Position
            orc_rank = orcs[i].Rank
            for j in range(orc_loc.Row - orc_rank, orc_loc.Row + orc_rank + 1):
                for k in range(orc_loc.Column - orc_rank, orc_loc.Column + orc_rank + 1):
                    if k >= 0 and k < State.board_dimensions.Column and j >= 0 and j < State.board_dimensions.Row and abs(orc_loc.Row - j) + abs(orc_loc.Column - k) <= orc_rank:
                        table[j][k] = i + 1
            table[orc_loc.Row][orc_loc.Column] = 0

        return table

    def __init__(self, path_to_file):
        self.input_file = open(path_to_file)
        board_dimensions_str = self.read_next_line()
        State.board_dimensions = Point(int(board_dimensions_str[0]), int(board_dimensions_str[1]))
        gandalf_position_str = self.read_next_line()
        gandalf_position = Point(int(gandalf_position_str[0]), int(gandalf_position_str[1]))
        gondor_position_str = self.read_next_line()
        State.gondor_position = Point(int(gondor_position_str[0]), int(gondor_position_str[1]))
        number_of_subsidiary_actors = self.read_next_line()
        number_of_orcs = int(number_of_subsidiary_actors[0])
        number_of_fellowship_members = int(number_of_subsidiary_actors[1])
        State.orcs = [self.new_orc(self.read_next_line()) for i in range(number_of_orcs)]
        State.orc_table = self.create_orc_table(State.orcs)
        fellowship_members = [self.new_member(self.read_next_line()) for i in range(number_of_fellowship_members)]
        for i in range(number_of_fellowship_members):
            fellowship_members[i].set_goal(self.read_next_line())
        self.initial_state = State(gandalf_position, fellowship_members, cost = 0, in_orc_area = 0, passed_through_orc_cells = 0, accompanying_member = None)
        self.input_file.close()
        
class State:
    board_dimensions = None
    orc_table = []
    orcs = []
    gondor_position = None

    def __init__(self, gandalf_position, fellowship_members, cost, in_orc_area, passed_through_orc_cells, accompanying_member):
        self.cost = cost
        self.gandalf_position = gandalf_position
        self.fellowship_members = fellowship_members
        self.in_orc_area = in_orc_area
        self.passed_through_orc_cells = passed_through_orc_cells
        self.accompanying_member = accompanying_member

    def in_bound(self, position):
        if position.Column >= 0 and position.Column < State.board_dimensions.Column and position.Row >= 0 and position.Row < State.board_dimensions.Row:
            return True
        return False

    def is_illegal_state(self):
        if not self.in_bound(gandalf_position):
            return True
        if State.orc_table[gandalf_position.Row][gandalf_position.Column] == 0:
            return True
        if State.orcs[in_orc_area - 1].Rank < passed_through_orc_cells:
            return True
        return False

    def is_goal_state(self):
        if not gandalf_position.equals(State.gondor_position):
            return False
        for member in self.fellowship_members:
            if not member.Position.equals(member.Goal):
                return False
        
        return True

    def go_up(self): #Action 1
        pass
    
    def go_left(self): #Action 2
        pass
    
    def go_down(self): #Action 3
        pass
    
    def go_right(self): #Action 4
        pass

        

alg = Base_algorithm('test_02.txt')
for row in State.orc_table:
    print(row)