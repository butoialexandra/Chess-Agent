# COM3240: Adaptive Intelligence 
### Assignment 2: Reinforcement Learning
#### Alexandra-Cristina Butoi

The folder "chess_student_python" contains all the code required in order to reproduce the results from the report. 
The file "chess_student.py" must be run in order to generate a new game and train the agent how to checkmate the opponent's King.
At the end, the program will store the values obtained for the reward per episode and the number of moves per episode. 

The following code must be modified so that the name of the files is modified in each run, ensuring that the results are not overwritten.

```python
    with open('rewards.pickle', 'wb') as file:
        pickle.dump(R_save, file)
    with open('moves.pickle', 'wb') as file:
        pickle.dump(N_moves_save, file)
```
