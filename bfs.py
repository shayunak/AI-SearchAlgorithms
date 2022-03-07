import time, abc
from utility import Base_algorithm

class BFS(Base_algorithm):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
        self.frontier = []
        self.frontier_set = set()
        self.explored = set()
        self.frontier.append(self.initial_state)
        self.frontier_set.add(self.initial_state.hash())

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
        child_state_hash = child_state.hash()
        if (child_state_hash not in self.explored) and (child_state_hash not in self.frontier_set):
            child_state.parent = parent_state
            self.frontier.append(child_state)
            self.frontier_set.add(child_state_hash)

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
        while True:
            if len(self.frontier) == 0:
                break
            state_to_expand = self.frontier.pop(0)
            self.frontier_set.remove(state_to_expand.hash())
            if state_to_expand.is_goal_state():
                output = self.calculate_route(state_to_expand)
                break
            self.expand(state_to_expand)
        return output, time.time() - t

test_set = ['test_00.txt', 'test_01.txt', 'test_02.txt', 'test_03.txt']
for i in range(len(test_set)):
    alg = BFS(test_set[i])
    output, time_taken = alg.run()
    print("Running Test " + str(i + 1) + ":")
    print("output: " + output)
    print("output cost: " + str(len(output)))
    print("Execution Time: " + str(int(time_taken*1000)) + " ms")
