# To-string conversion

Today we are going to look at the two methods that control how an object is converted into a string object. When we just print an object, we won't get a useful representation. For example, when doing:

```python
bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
print(bromley)
```

We get this output: ```<__main__.CastleKilmereMember object at 0x7f81853bfc50>```. It contains the name of the class an the ID of the object (its memory address). This is not very useful when we want to know what the object is. But there is a simple solution to our problem!
   
We can control how objects of our classes are converted into string objects. Specifically, the to-string conversion is controlled by two methods: ```__repr__``` and ```__str__ ``` that serve different purposes:   

The result of the ```__repr__``` method should be as *unambiguous* as possible. It should function as a debugging aid for developers. Therefore, it should be explicit about what the object is.   
   
The result of the ```__str__``` method should be *readable*.   
   
By defining these special Python methods we can control how our objects will be represented when converting them into strings. Whenever you create your own class you should at least implement the ```__repr__``` method. Why ```__repr__```? Because it will ensure a useful conversion of objects to strings. When Python looks for the ```__str__``` method but ```__str__``` hasn't been implemented, it will fall back to using ```__repr__```. So as long as ```__repr__``` is defined we will get a helpful representation of our object.   
   
Let's add a ```__repr__``` method to our CastleKilmereMember class!

```python
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})"

```

Now, the output of 
```python
print(bromley)
```

will look as follows: ```CastleKilmereMember(Bromley Huckabee, birthyear: 1959)```. This is much better!   
   
Since our other classes inherit all methods from the parent class we don't have to implement the ```__repr__``` method again for the other classes. But we want the output of ```__repr__``` to be as unambiguous as possible. So we will add separate ```__repr__``` methods to ensure that we use all information we have about the objects.

```python
class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    ...

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, subject: {self.subject})")


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    ...

    def __repr__(self):
        return (f"{self.__class__.__name__}({self._name}, "
                f"birthyear: {self.birthyear}, year of death: {self.year_of_death})")


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    ...

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"({self._name}, birthyear: {self.birthyear}, house: {self.house})")

```
