# Duck typing, EAFP principle

## Easier to ask for forgiveness than permission

Today we are going to look at a common coding style in Python called 'Easier to ask for forgiveness than permission' or in short 'EAFP'. The idea of EAFP is that we assume that valid keys (or attributes) exist. If this assumption proves false, we catch and handle the exceptions that are raised. We actually used this principle already. Can you guess where? Take a close look at the ```@elms.setter``` method of the ```Pupil``` class:

```python
@elms.setter
def elms(self, subject_and_grade):

    try:
        subject, grade = subject_and_grade
    except ValueError:
        raise ValueError("Pass and iterable with two items: subject and grade")

    passed = self.passed(grade)

    if passed:
        self._elms[subject] = True
    else:
        print('The exam was not passed so no ELM was awarded!')
```

The ```try ... except ... ``` code block implements the EAFP principle. We assume that the ```subject_and_grade``` tuple exists. If it does, we unpack its values into ```subject, grade```. If ```subject_and_grade``` is not a valid tuple, a ```ValueError``` will be raised. We catch this error in the ```except``` block and handle it appropriately.  
   
To add another example of the EAFP principle to our Magical Universe we first extend our ```CastleKilmereMember``` class with a ```_traits``` attribute and two methods for adding and printing traits:

```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    ...
```

Let's add a few traits to bromley:
```python
bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
bromley.add_trait("kind")
bromley.add_trait("tidy-minded")
bromley.add_trait("impatient", value=False)

bromley.print_traits()
```

This prints the following text: *Bromley Huckabee is kind, tidy-minded but not impatient*. Let's add another method that checks if a Castle Kilmere member exhibits a certain character trait:

```python
def exhibits_trait(self, trait):
    try:
        value = self._traits[trait]
    except KeyError:
        print(f"{self._name} does not have a character trait with the name '{trait}'")
        return

    if value:
        print(f"Yes, {self._name} is {trait}!")
    else:
        print(f"No, {self._name} is not {trait}!")
```

The ```try ... except ... ``` code block assumes that the given trait exists as a key. If this assumption proves false (i.e. a ```KeyError```is raised) it handles the missing key.

## Look before you leap (LBYL)
The opposite of the EAFP principle is called 'Look before you leap' (LBYL). When using LBYL we would first test if a key exists before performing the look-up operation. So our code from above would rather look as follows:

```python
def exhibits_trait(self, trait):
    if trait in self._traits:
        value = self._traits[trait]
        if value:
            print(f"Yes, {self._name} is {trait}!")
        else:
            print(f"No, {self._name} is not {trait}!")
        
    else:
        print(f"{self._name} does not have a character trait with the name '{trait}'")
        return
```

As mentioned in [this stackoverflow post](https://stackoverflow.com/questions/11360858/what-is-the-eafp-principle-in-python): "The LBYL version has to search the key inside the dictionary twice, and might also be considered slightly less readable."




