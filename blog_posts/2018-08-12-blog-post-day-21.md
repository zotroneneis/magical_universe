# What is ```if __name__ == "__main__"``` doing?

I always wanted to dig into the statement ```if __name__ == "__main__"``` that is used in so many programs. I have used it for a long time already but until recently I had no idea what exactly it is doing. To make the topic as understandable as possible, I will divide the explanation into three steps.

### Step 1: Two ways of running code

We saved our Magical Universe in a file named ```magical_universe.py```. First of all, we have to distinguish the two ways in which we can run our code:   
1. We can run the file directly, as in ```python magical_universe.py```   
2. We can import the file from another module. In this case we would have a different script, for example 'simulate_house_game.py'. In that script, we can use our Cleon Bery classes by importing them at the beginning of the script. For example using: ```from magical_universe import CastleKilmereMember, Pupil, Professor```.   
    
### Step 2: Setting up special variables

In both cases, the Python interpreter will read the source file ```magical_universe.py```. But, as outlined in [this post](https://stackoverflow.com/questions/419163/what-does-if-name-main-do), the interpreter will first define a few special variables. One of them is the ```__name__``` variable. In case 1, so when running our file as the main program, the value of ```__name__``` is set to ```"__main__"```. In case 2, the value of ```__name__``` is set to the name of the module, which is ```"magical_universe"```. 

### Step 3: Executing the code

The interpreter has finished setting up the special variables, so the value of ```__name__``` is either ```"__main__"``` (case 1) or ```"magical_universe"``` (case 2). In a next step, the interpreter will read the file and execute all *top-level code* in the file. 'Top-level' code refers to all code at indentation level 0. So in our case, the import statements at the beginning of the ```magical_universe.py``` file will be executed and all classes will be defined. However, none of the code inside the classes will be executed. At the end of the file we have an ```if``` block as top-level code. The ```if``` block starts with the line ```if __name__ == "__main__"```. With the knowledge from the previous steps we should be able to understand what this statement represents: it tests whether the current module, that is 'magical_universe', is being run directly (case 1) or imported by another module (case 2)! In case 1, the output of ```__name__ == "__main__"``` will be ```True```, so the code within the ```if``` block will be executed. In case 2, the ```if``` clause won't be executed because the required condition is not met.


### Why "main"?

In case 1, the value of ```__name__``` is set to ```"__main__"``` because "magical_universe.py" is run as the *main program*.



## Further reading:
- [Python Docs](https://docs.python.org/3/library/__main__.html)   
- [Stackoverflow post](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

