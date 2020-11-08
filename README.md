# npuzzle :jigsaw:

[ The game](http://mypuzzle.org/sliding) begins with a square board consisting of tiles with numbers from 1 to N and an empty tile represented by the number 0. The goal is to arrange the tiles according to any numbers. Relocation is used, and in place of the empty tile you can replace the tile at the top, bottom, left and right.

When entering, enter the number N - the number of tiles with numbers (8, 15, 24, etc.), number I - index of the position of zero in the solution (at -1 set the default index - bottom right ) and then enter the arrangement of the board. Using the `IDA * algorithm` and the `Manhattan distance` heuristic print:

1) In the first line of search for the `optimal path` from the beginning to the target state.

2) Relevant steps (new line for each one) that are performed to reach the final state. The steps are `left`, `right`, `up` and `down`

```
Sample input:

8

-1

1 2 3
4 5 6
0 7 8

Example output:

2

left

left
```