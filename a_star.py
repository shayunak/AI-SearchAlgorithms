import time, abc
from utility import Base_algorithm
from min_heap import MinHeap

class A_STAR(Base_algorithm):
    def __init__(self, path_to_file, alpha):
        super().__init__(path_to_file)
        self.frontier = MinHeap()
        self.alpha = alpha
        self.frontier_set = set()
        self.explored = set()
        self.frontier.insert([self.initial_state, self.alpha*self.calculate_heuristic(self.initial_state)])
        self.frontier_set.add(self.initial_state.hash())

    def calculate_heuristic(self, state):
        if len(state.fellowship_members) > 0:
            return max(abs(member.Position.Row - member.Goal.Row) + abs(member.Position.Column - member.Goal.Column) for member in state.fellowship_members)
        else:
            return abs(state.gandalf_position.Row - state.gondor_position.Row) + abs(state.gandalf_position.Column - state.gondor_position.Column)

    def add_to_frontier_if_possible(self, child_state, parent_state):
        if child_state is None:
            return
        child_state_hash = child_state.hash()
        if (child_state_hash not in self.explored) and (child_state_hash not in self.frontier_set):
            child_state.parent = parent_state
            self.frontier.insert([child_state, child_state.depth + self.alpha*self.calculate_heuristic(child_state)])
            self.frontier_set.add(child_state_hash)
        elif child_state_hash in self.frontier_set:
            self.frontier.find_element_and_replace_value(child_state, child_state.depth + self.alpha*self.calculate_heuristic(child_state))

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
        output = "impossible to reach our goal!"
        states_expanded = 0
        while True:
            if self.frontier.size == 0:
                break
            state_to_expand = self.frontier.remove()
            states_expanded += 1
            self.frontier_set.remove(state_to_expand.hash())
            if state_to_expand.is_goal_state():
                output = self.calculate_route(state_to_expand)
                break
            self.expand(state_to_expand)
        return output, time.time() - t, states_expanded