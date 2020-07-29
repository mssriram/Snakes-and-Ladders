# Snakes-and-Ladders
In this project, I have coded a simple game of snakes and ladders using python and have done some mathematical analysis on it.

In the file titled "snake_and_ladder.py3", I have provided the main code for the game which simulates n number of games with the inputs being the number of snakes and ladders. You can also change the min and max length of the snakes and ladders. While I have only coded it to have 2 inputs, you can change the rest of the variables however you like.

In the file titled "transition_matrix.py3", I have created a transition probability matrix based on a dictionary of snakes and ladders. Then I have created a initial vector and multiplied both of them itiratively. This essentially does the same thing the above code does but in a different method. Both of them have their pros and cons. 

The first method is known as the Monte Carlo method where a system is modeled and the executed with random inputs. The second method uses Markov chains. The first method is more practical while the second one is purely theoretical.

I have also included a shell script which you can use in case you want to run it multiple times.
