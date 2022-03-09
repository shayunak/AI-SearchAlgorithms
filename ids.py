import time, abc
from utility import Base_algorithm

class IDS(Base_algorithm):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
        self.explored = {}
        self.searched_depth = 0

    def search_for_specific_depth(self, current_state):
        #base condition
        if current_state.is_goal_state():
            return False, current_state
        if current_state.depth == self.searched_depth:
            return True, None
        
        tot_cutoff_reached = True
        # Case Up
        child_up = current_state.go_up()
        if child_up is not None:
            child_up_hash = child_up.hash()
            cost_to_reach = self.explored.get(child_up_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_up.depth < cost_to_reach)):
                self.explored[child_up_hash] = child_up.depth
                child_up.parent = current_state
                cutoff_reached, up_result = self.search_for_specific_depth(child_up)
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif up_result is not None:
                    return False, up_result
        
        #Case Left
        child_left = current_state.go_left()
        if child_left is not None:
            child_left_hash = child_left.hash()
            cost_to_reach = self.explored.get(child_left_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_left.depth < cost_to_reach)):
                self.explored[child_left_hash] = child_left.depth
                child_left.parent = current_state
                cutoff_reached, left_result = self.search_for_specific_depth(child_left)
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif left_result is not None:
                    return False, left_result
        
        #Case Down
        child_down = current_state.go_down()
        if child_down is not None:
            child_down_hash = child_down.hash()
            cost_to_reach = self.explored.get(child_down_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_down.depth < cost_to_reach)):
                self.explored[child_down_hash] = child_down.depth
                child_down.parent = current_state
                cutoff_reached, down_result = self.search_for_specific_depth(child_down)
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif down_result is not None:
                    return False, down_result
        
        #Case Right
        child_right = current_state.go_right()
        if child_right is not None:
            child_right_hash = child_right.hash()
            cost_to_reach = self.explored.get(child_right_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_right.depth < cost_to_reach)):
                self.explored[child_right_hash] = child_right.depth
                child_right.parent = current_state
                cutoff_reached, right_result = self.search_for_specific_depth(child_right)
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif right_result is not None:
                    return False, right_result
        
        if tot_cutoff_reached:
            return True, None
        return False, None
        
    def run(self):
        t = time.time()
        output = ""
        while True:
            cutoff_reached ,found_goal = self.search_for_specific_depth(self.initial_state)
            if not cutoff_reached:
                output = self.calculate_route(found_goal)
                break
            self.explored.clear()
            self.searched_depth += 1
        return output, time.time() - t