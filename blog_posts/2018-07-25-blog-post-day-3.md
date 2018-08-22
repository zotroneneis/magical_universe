# Function annotations

Function annotations are a very cool Python 3 feature. They allow us to add arbitrary metadata to function arguments and the return value of a function. Why this is useful? First of all, it allows you to document of what type your function parameters are. Furthermore, they can be used for things like type checking. For more use cases, look [here](https://www.python.org/dev/peps/pep-3107/). 
   
   
Let's add annotations to our ```___init___``` constructors:

```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        ...


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house=None):
        ...


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house=None):
        ...


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet=None):

```

   
## How to use function annotations for arguments that have a default value
Some classes have attributes with default values. For example, the "pet" attribute of the Pupil class has a default value (as some pupils have a pet and others don't). Also the "house" attribute of the "Professor and "Ghost" class have a default value. So how do we correctly use function annotations for such arguments? I found a clear explanation in [this post](https://stackoverflow.com/questions/38727520/adding-default-parameter-value-with-type-hint-in-python).

In short, the syntax is as follows:
```
def __init__(..., pets: tuple = None):
    ...
```

## Where to put spaces when using function annotations

Since the post I mentioned above does not include whitespaces between the different parts of an annotation I checked the correct syntax of function annotations. As mentioned in [PEP8](https://www.python.org/dev/peps/pep-0008/?) the proper usage of spaces is as follows:   
   
Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present. 

Yes:

```
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
```

No:

```
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

When combining an argument annotation with a default value, use spaces around the = sign (but only for those arguments that have both an annotation and a default).

Yes:

```
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```

No:

```
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```
