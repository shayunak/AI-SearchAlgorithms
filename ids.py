import time, abc
from utility import Base_algorithm

class IDS(Base_algorithm):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
        self.explored = set()
        self.searched_depth = 0

    def search_for_specific_depth(self, current_state):
        #base condition
        if current_state.is_goal_state():
            return current_state
        if current_state.depth == self.searched_depth:
            return None
        
        # Case Up
        child_up = current_state.go_up()
        if child_up is not None:
            child_up_hash = child_up.hash() 
            if child_up_hash not in self.explored:
                self.explored.add(child_up_hash)
                child_up.parent = current_state
                up_result = self.search_for_specific_depth(child_up)
                if up_result is not None:
                    return up_result
        
        #Case Left
        child_left = current_state.go_left()
        if child_left is not None:
            child_left_hash = child_left.hash() 
            if child_left_hash not in self.explored:
                self.explored.add(child_left_hash)
                child_left.parent = current_state
                left_result = self.search_for_specific_depth(child_left)
                if left_result is not None:
                    return left_result
        
        #Case Down
        child_down = current_state.go_down()
        if child_down is not None:
            child_down_hash = child_down.hash() 
            if child_down_hash not in self.explored:
                self.explored.add(child_down_hash)
                child_down.parent = current_state
                down_result = self.search_for_specific_depth(child_down)
                if down_result is not None:
                    return down_result
        
        #Case Right
        child_right = current_state.go_right()
        if child_right is not None:
            child_right_hash = child_right.hash() 
            if child_right_hash not in self.explored:
                self.explored.add(child_right_hash)
                child_right.parent = current_state
                right_result = self.search_for_specific_depth(child_right)
                if right_result is not None:
                    return right_result

        return None
        
    def run(self):
        t = time.time()
        output = ""
        while True:
            found_goal = self.search_for_specific_depth(self.initial_state)
            if found_goal is not None:
                output = self.calculate_route(found_goal)
                break
            self.explored.clear()
            self.searched_depth += 1
        return output, time.time() - t