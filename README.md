# Grey Gandalf and Fellowship of the ring
Gandalf wishes to reach the fellowship members on different positions in a board, and transfer each of them to their inteneded destination. The board contains territoris under the watch of the orc commanders. The military rank of each orc commander determines the vastness of its territory. Our goal is to propose a solution based on search algorithms.

![image](https://user-images.githubusercontent.com/41966479/190249337-c664a9c8-b1d9-4ed7-9169-be246179f912.png)


## Input Structure
* Line 1: (n, m) are the number of rows and columns of our board.
* Line 2, 3: Gandalf initial and final positions.
* Line 4: (k, l) are the number of orcs and fellowship members.
* k Lines: (x, y, c) are the location of an specific orc with c as its rank.
* l lines: specific fellowship member initial position
* l lines: specific index corresponding fellowship member final position



## Output Structure
With default actions of L, R, U, D as Left, Right, Up and Down, we have to present an string with these four characters that represents consecutive actions for a valid goal state.

## Model
* Goal state: Gandalf and all fellowship members in their corresponding destinations without staying too long in orc territories. (more than ''c''(rank)  actions)
* Action: moving Left, Right, Up or Down
* Initial State: based on given parameters
* Invalid State: entering orc cell or staying more than ''c'' cells in an orc territory, or moving out of board
* State: Gandalf Position + Fellowship members positions + cells passed in an orc territory + carrying member(or no member carrying)

## Solution
Using search algorithms:
- DFS: Depth First search(not optimal and slow but low space consumption)
- BFS: Breadth First search(fast and optimal but high space consumption)
- IDS: Iterated Depth search(slow and optimal but low space consumption)
- A*: optimal and fast with addmissible and consistent heuristic of maximum manhatan distance of a fellowhip member to its destination
- weighted A*: with alpha coefficient 2, 3

## Time and results for all test cases

Achievable by running "test.py"
