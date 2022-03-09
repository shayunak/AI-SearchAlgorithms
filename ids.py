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
            return False, current_state, 1
        if current_state.depth == self.searched_depth:
            return True, None, 1
        
        states_seen = 1
        tot_cutoff_reached = True
        # Case Up
        child_up = current_state.go_up()
        if child_up is not None:
            child_up_hash = child_up.hash()
            cost_to_reach = self.explored.get(child_up_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_up.depth < cost_to_reach)):
                self.explored[child_up_hash] = child_up.depth
                child_up.parent = current_state
                cutoff_reached, up_result, up_states_seen = self.search_for_specific_depth(child_up)
                states_seen += up_states_seen
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif up_result is not None:
                    return False, up_result, states_seen
        
        #Case Left
        child_left = current_state.go_left()
        if child_left is not None:
            child_left_hash = child_left.hash()
            cost_to_reach = self.explored.get(child_left_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_left.depth < cost_to_reach)):
                self.explored[child_left_hash] = child_left.depth
                child_left.parent = current_state
                cutoff_reached, left_result, left_states_seen = self.search_for_specific_depth(child_left)
                states_seen += left_states_seen
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif left_result is not None:
                    return False, left_result, states_seen
        
        #Case Down
        child_down = current_state.go_down()
        if child_down is not None:
            child_down_hash = child_down.hash()
            cost_to_reach = self.explored.get(child_down_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_down.depth < cost_to_reach)):
                self.explored[child_down_hash] = child_down.depth
                child_down.parent = current_state
                cutoff_reached, down_result, down_states_seen = self.search_for_specific_depth(child_down)
                states_seen += down_states_seen
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif down_result is not None:
                    return False, down_result, states_seen
        
        #Case Right
        child_right = current_state.go_right()
        if child_right is not None:
            child_right_hash = child_right.hash()
            cost_to_reach = self.explored.get(child_right_hash)
            if (cost_to_reach is None) or ((cost_to_reach is not None) and (child_right.depth < cost_to_reach)):
                self.explored[child_right_hash] = child_right.depth
                child_right.parent = current_state
                cutoff_reached, right_result, right_states_seen = self.search_for_specific_depth(child_right)
                states_seen += right_states_seen                
                if cutoff_reached:
                    tot_cutoff_reached = True
                elif right_result is not None:
                    return False, right_result, states_seen
        
        if tot_cutoff_reached:
            return True, None, states_seen
        return False, None, states_seen
        
    def run(self):
        t = time.time()
        output = ""
        states_expanded = 0
        while True:
            cutoff_reached ,found_goal, states_seen_this_depth = self.search_for_specific_depth(self.initial_state)
            states_expanded += states_seen_this_depth
            if not cutoff_reached:
                output = self.calculate_route(found_goal)
                break
            self.explored.clear()
            self.searched_depth += 1
        return output, time.time() - t, states_expanded