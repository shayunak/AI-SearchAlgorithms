import time

class Point:
    def __init__(self, Row, Column):
        self.Row = Row
        self.Column = Column
    
    def __eq__(self, another_point):
        return self.Row == another_point.Row and self.Column == another_point.Column

    def hash(self):
        return str(self.Row) + '/' + str(self.Column)

    def get_copy(self):
        return Point(self.Row, self.Column)

    def print_out(self):
        print(self.Row, self.Column)

class Orc:
    def __init__(self, Position, Rank):
        self.Position = Position
        self.Rank = Rank

class Fellowship_member:
    def __init__(self, Position, Goal):
        self.Position = Position
        self.Goal = Goal
    
    def hash(self):
        return self.Position.hash() + '-' + self.Goal.hash()

    def get_copy(self):
        return Fellowship_member(self.Position.get_copy(), self.Goal.get_copy())

    def __eq__(self, member):
        return self.Position == member.Position and self.Goal == member.Goal
        
class State:
    board_dimensions = None
    orc_table = []
    orcs = []
    initial_number_of_members = 0
    gondor_position = None

    def hash(self):
        hashed = ""
        hashed = hashed + self.gandalf_position.hash() + '#' + str(self.passed_through_orc_cells) + '#' + str(self.accompanying_member)
        for member in self.fellowship_members:
            hashed = hashed + '#' + member.hash()
        return hashed

    def __init__(self, gandalf_position, fellowship_members, cost, in_orc_area, passed_through_orc_cells, accompanying_member):
        self.cost = cost
        self.parent = None
        self.reached_by_action = None
        self.gandalf_position = gandalf_position
        self.fellowship_members = fellowship_members
        self.in_orc_area = in_orc_area
        self.passed_through_orc_cells = passed_through_orc_cells
        self.accompanying_member = accompanying_member

    def in_bound(self, position):
        if position.Column >= 0 and position.Column < State.board_dimensions.Column and position.Row >= 0 and position.Row < State.board_dimensions.Row:
            return True
        return False
    
    def __eq__(self, state):
        if self.gandalf_position != state.gandalf_position:
            return False
        if self.passed_through_orc_cells != state.passed_through_orc_cells:
            return False
        if self.accompanying_member != state.accompanying_member:
            return False
        if len(self.fellowship_members) != len(state.fellowship_members):
            return False
        for i in range(len(self.fellowship_members)):
            if self.fellowship_members[i] != state.fellowship_members[i]:
                return False
        return True

    def get_copy(self):
        copied_gandalf_position = self.gandalf_position.get_copy()
        copied_fellowship_members = []
        for i in range(len(self.fellowship_members)):
            copied_fellowship_members.append(self.fellowship_members[i].get_copy())
        copied_cost = self.cost
        copied_in_orc_area = self.in_orc_area
        copied_passed_through_orc_cells = self.passed_through_orc_cells
        copied_accompanying_member = self.accompanying_member
        return State(gandalf_position= copied_gandalf_position, fellowship_members= copied_fellowship_members, 
            cost= copied_cost, in_orc_area= copied_in_orc_area, passed_through_orc_cells= copied_passed_through_orc_cells, accompanying_member= copied_accompanying_member)

    def is_illegal_state_by_gandalf_position(self, new_gandalf_position):
        if not self.in_bound(new_gandalf_position):
            return True
        if State.orc_table[new_gandalf_position.Row][new_gandalf_position.Column] == 0:
            return True
        return False

    def is_illegal_state_by_orc_area(self, in_orc_area, passed_through_orc_cells):
        if State.orcs[in_orc_area - 1].Rank < passed_through_orc_cells:
            return True
        return False

    def is_goal_state(self):
        if self.gandalf_position != State.gondor_position:
            return False
        if len(self.fellowship_members) != 0:
            return False    
        return True

    def check_orc_area(self, new_state_gandalf_position, former_state_in_orc_area, former_state_passed_through_orc_cells):
        new_cell_orc_status = State.orc_table[new_state_gandalf_position.Row][new_state_gandalf_position.Column]
        if new_cell_orc_status is not None:
            if new_cell_orc_status == former_state_in_orc_area:
                return former_state_in_orc_area, former_state_passed_through_orc_cells + 1
            else:
                return new_cell_orc_status, 1
        else:
            return 0, 0

    def has_met_member_in_cell(self, state):
        for i in range(len(state.fellowship_members)):
            if state.fellowship_members[i].Position == state.gandalf_position:
                return i
        return None

    def check_accompanying_member(self, new_state):
        if self.accompanying_member is not None:
            new_state.fellowship_members[self.accompanying_member].Position = new_state.gandalf_position
            if new_state.fellowship_members[self.accompanying_member].Position == new_state.fellowship_members[self.accompanying_member].Goal:
                new_state.accompanying_member = None
                del new_state.fellowship_members[self.accompanying_member]
        else:
            new_state.accompanying_member = self.has_met_member_in_cell(new_state)

    def go_up(self): #Action 1
        new_gandalf_position = Point(self.gandalf_position.Row - 1, self.gandalf_position.Column)
        if self.is_illegal_state_by_gandalf_position(new_gandalf_position):
            return None
        new_in_orc_area, new_passed_through_cells = self.check_orc_area(new_gandalf_position, self.in_orc_area, self.passed_through_orc_cells)
        if self.is_illegal_state_by_orc_area(new_in_orc_area, new_passed_through_cells):
            return None
        new_state = self.get_copy()
        new_state.gandalf_position = new_gandalf_position
        new_state.reached_by_action = 'U'
        new_state.cost = self.cost + 1
        new_state.in_orc_area = new_in_orc_area
        new_state.passed_through_orc_cells = new_passed_through_cells
        self.check_accompanying_member(new_state)
        return new_state
    
    def go_left(self): #Action 2
        new_gandalf_position = Point(self.gandalf_position.Row, self.gandalf_position.Column - 1)
        if self.is_illegal_state_by_gandalf_position(new_gandalf_position):
            return None
        new_in_orc_area, new_passed_through_cells = self.check_orc_area(new_gandalf_position, self.in_orc_area, self.passed_through_orc_cells)
        if self.is_illegal_state_by_orc_area(new_in_orc_area, new_passed_through_cells):
            return None
        new_state = self.get_copy()
        new_state.gandalf_position = new_gandalf_position
        new_state.reached_by_action = 'L'
        new_state.cost = self.cost + 1
        new_state.in_orc_area = new_in_orc_area
        new_state.passed_through_orc_cells = new_passed_through_cells
        self.check_accompanying_member(new_state)
        return new_state
    
    def go_down(self): #Action 3
        new_gandalf_position = Point(self.gandalf_position.Row + 1, self.gandalf_position.Column)
        if self.is_illegal_state_by_gandalf_position(new_gandalf_position):
            return None
        new_in_orc_area, new_passed_through_cells = self.check_orc_area(new_gandalf_position, self.in_orc_area, self.passed_through_orc_cells)
        if self.is_illegal_state_by_orc_area(new_in_orc_area, new_passed_through_cells):
            return None
        new_state = self.get_copy()
        new_state.gandalf_position = new_gandalf_position
        new_state.reached_by_action = 'D'
        new_state.cost = self.cost + 1
        new_state.in_orc_area = new_in_orc_area
        new_state.passed_through_orc_cells = new_passed_through_cells
        self.check_accompanying_member(new_state)
        return new_state
    
    def go_right(self): #Action 4
        new_gandalf_position = Point(self.gandalf_position.Row, self.gandalf_position.Column + 1)
        if self.is_illegal_state_by_gandalf_position(new_gandalf_position):
            return None
        new_in_orc_area, new_passed_through_cells = self.check_orc_area(new_gandalf_position, self.in_orc_area, self.passed_through_orc_cells)
        if self.is_illegal_state_by_orc_area(new_in_orc_area, new_passed_through_cells):
            return None
        new_state = self.get_copy()
        new_state.gandalf_position = new_gandalf_position
        new_state.reached_by_action = 'R'
        new_state.cost = self.cost + 1
        new_state.in_orc_area = new_in_orc_area
        new_state.passed_through_orc_cells = new_passed_through_cells
        self.check_accompanying_member(new_state)
        return new_state

class Base_algorithm:
    def read_next_line(self):
        return self.input_file.readline().strip().split(' ')

    def new_orc(self, orc_desc_str):
        return Orc(Point(int(orc_desc_str[0]), int(orc_desc_str[1])), int(orc_desc_str[2]))
    
    def new_member_position(self, member_desc_str):
        return Point(int(member_desc_str[0]), int(member_desc_str[1]))
    
    def new_member_goal(self, member_desc_str):
        return Point(int(member_desc_str[0]), int(member_desc_str[1]))

    def initialize_table(self):
        table = []
        for i in range(State.board_dimensions.Row):
            new_row = []
            for j in range(State.board_dimensions.Column):
                new_row.append(None)
            table.append(new_row)
        return table

    def create_orc_table(self, orcs):
        table = self.initialize_table()
        
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
        State.initial_number_of_members = int(number_of_subsidiary_actors[1])
        State.orcs = [self.new_orc(self.read_next_line()) for i in range(number_of_orcs)]
        State.orc_table = self.create_orc_table(State.orcs)
        fellowship_members_positions = [self.new_member_position(self.read_next_line()) for i in range(State.initial_number_of_members)]
        fellowship_members_goals = [self.new_member_goal(self.read_next_line()) for i in range(State.initial_number_of_members)]
        fellowship_members = []
        for i in range(State.initial_number_of_members):
            fellowship_members.append(Fellowship_member(fellowship_members_positions[i], fellowship_members_goals[i]))
        self.initial_state = State(gandalf_position, fellowship_members, cost = 0, in_orc_area = 0, passed_through_orc_cells = 0, accompanying_member = None)
        self.input_file.close()

class BFS(Base_algorithm):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
        self.frontier = []
        self.explored = set()
        self.frontier.append(self.initial_state)

    def calculate_route(self, goal_state):
        current_state = goal_state
        output_str = ""
        while current_state != self.initial_state:
            output_str = current_state.reached_by_action + output_str
            current_state = current_state.parent
        return output_str 

    def add_to_frontier_if_possible(self, child_state, parent_state):
        if child_state is None:
            return
        if child_state.hash() not in self.explored:
            child_state.parent = parent_state
            self.frontier.append(child_state)

    def expand(self, state_to_expand):
        self.explored.add(state_to_expand.hash())
        child_up = state_to_expand.go_up()
        child_left = state_to_expand.go_left()
        child_down = state_to_expand.go_down()
        child_right = state_to_expand.go_right()
        self.add_to_frontier_if_possible(child_up, state_to_expand)
        self.add_to_frontier_if_possible(child_left, state_to_expand)
        self.add_to_frontier_if_possible(child_down, state_to_expand)
        self.add_to_frontier_if_possible(child_right, state_to_expand)
        
    def run(self):
        t = time.time()
        while True:
            if len(self.frontier) == 0:
                print("impossible to reach our goal!")
                break
            state_to_expand = self.frontier.pop(0)
            if state_to_expand.is_goal_state():
                print(self.calculate_route(state_to_expand))
                break
            self.expand(state_to_expand)
        print(time.time() - t)

alg = BFS('test_02.txt')
alg.run()