# Awesome Python Features Explained Using the World of Magic

![](IMG_6623.jpg)

As outlined in [my blog post](http://www.alpopkes.com/posts/2018/07/blog-post-1), I decided to take on a new habit using a technique I found on the ['get disciplined' subreddit](https://www.reddit.com/r/getdisciplined/comments/1x99m6/im_a_piece_of_shit_no_more_games_no_more_lies_no/cf9dz72/).

As one of my new habits I chose: "Code for 15 minutes every day". As part of the habit I've started creating a series of **blog posts** on important and awesome **Python features**, including object oriented programming, properties, function annotations, duck typing, etc.

Since I was bored by the usual tutorial examples, I looked for a topic that would make it fun to study and implement the concepts. And since I absolutely love Harry Potter, I started creating my own magical universe around the topics. A short introduction into my magical universe - **The Tales of Castle Kilmere** can be found [here](http://alpopkes.com/posts/2018/07/the_tales_of_castle_kilmere/). So if you like magic and want to improve your Python knowledge and skills, get right into it!

A logbook of what I worked on each day can be found on my [website](http://www.alpopkes.com/year-archive/).

The code runs in **Python 3.6**, the [code on data classes](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_16_to_18.py) requires Python 3.7 (or you pip install data classes for Python 3.6).

Start date: 07/23/2018   

## Blog Posts

In case you can't access my website, the blog posts can also be found in this repository (see folder 'blog_posts').

## Running pytest

In case you get ```ImportError: no module named magical_universe``` when running pytest from within the test_code directory, take a look at [this post](https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada) and try running pytest from the root directory (which is the home directory in my case) using ```python -m pytest magical_universe/test_code/```.

## Overview

| Day   | Topics          | Blog post with explanations | Code for the day  |
| :---: |:--------------: | :--------------------------:| :----------------:|
| 1 | Intro to object oriented programming, classes, inheritance   | [Day 1](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-1/)  | [Code day 1](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_1.py) |
| 2 | Class methods, instance methods, static methods, using class methods as alternative constructors | [Day 2](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-2/)  | [Code day 2](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_2.py) |
| 3 |Function annotations|[Day 3](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-3/) |  [Code day 3](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_3.py) |
| 4 |To-string conversion, ```__repr__, __str__ ```|[Day 4](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-4/) |  [Code day 4](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_4.py) |
| 5 |Decorators|[Day 5](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-5/)    | No new code added |
| 6 |Properties, ```@property``` and ```property()```, setters, getters|[Day 6](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-6/)    | [Code day 6](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_6.py) |
| 7 |Underscore patterns for variable naming, ```_variable, __variable, __variable__, etc.```|[Day 7](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-7/)    | No new code added |
| 8 | New methods and classes added to the HP universe |[Day 8](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-8/) |  [Code day 8](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_8.py) |
| 9 | Duck typing, EAFP principle |[Day 9](http://www.alpopkes.com/posts/2018/07/coding-challenge-day-9/) |  [Code day 9](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_9.py) |
| 10 & 11| Namedtuples | [Day 10 & 11](http://www.alpopkes.com/posts/2018/08/coding-challenge-day-10-and-11/) | [Code day 10 & 11](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_10_and_11.py)|
| 12 - 15  | Abstract Base Classes | [Day 12 to 15](http://alpopkes.com/posts/2018/08/coding-challenge-day-12-to-15/) | [Code day 12 to 15](https://github.com/zotroneneis/100_days_of_code/blob/master/code_per_day/day_12_to_15.py)|
| 16 - 18  | Data Classes | [Day 16 to 18](http://alpopkes.com/posts/2018/08/coding-challenge-day-16-to-18/) | [Code day 16 to 18](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_16_to_18.py)|
| 19  | Immutable Data Classes | [Day 19](http://alpopkes.com/posts/2018/08/coding-challenge-day-19/) | [Code day 19](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_19.py)|
| 20  | Decorators within a class | [Day 20](http://alpopkes.com/posts/2018/08/coding-challenge-day-20/) | [Code day 20](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_20.py)|
| 21  | The mysterious ```if __name__ == "__main__"``` | [Day 21](http://alpopkes.com/posts/2018/08/coding-challenge-day-21/) | No new code added |
| 22 - 24  | Context managers and the ```with``` statement| [Day 22 to 24](http://alpopkes.com/posts/2018/08/coding-challenge-day-22-to-24/) | [Code day 22 to 24](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_22_to_24.py) |
| 25 - 28  | Testing code with pytest| [Day 25 to 28](http://alpopkes.com/posts/2018/08/coding-challenge-day-25-to-28/) | [Code day 25 to 28](https://github.com/zotroneneis/magical_universe/blob/master/test_code/test_hogwarts_member_class.py) |
| 29 - 31  | Iterators, iterables, iteration| [Day 29 to 31](http://alpopkes.com/posts/2018/08/coding-challenge-day-29-to-31/) | [Code day 29 to 31](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_29_to_31.py) |
| 32  | Test code for ```Professor``` class | No blog post, see [Day 25 to 28](http://alpopkes.com/posts/2018/08/coding-challenge-day-25-to-28/) for an introduction to testing| [Code day 32](https://github.com/zotroneneis/magical_universe/blob/master/test_code/test_professor_class.py) |
| 33  | Test code for ```Ghost``` class | No blog post, see [Day 25 to 28](http://alpopkes.com/posts/2018/08/coding-challenge-day-25-to-28/) for an introduction to testing| [Code day 33](https://github.com/zotroneneis/magical_universe/blob/master/test_code/test_ghost_class.py) |
| 34  | Counting objects with ```Collections.counter``` | [Day 34](http://alpopkes.com/posts/2018/08/coding-challenge-day-34/) | [Day 34](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_34.py) |
| 35  | Test code for ```DarkArmyMember``` class | No blog post, see [Day 25 to 28](http://alpopkes.com/posts/2018/08/coding-challenge-day-25-to-28/) for an introduction to testing| [Code day 35](https://github.com/zotroneneis/magical_universe/blob/master/test_code/test_dark_army_member_class.py) |
| 36  | Test code for ```Potion``` class | No blog post, see [Day 25 to 28](http://alpopkes.com/posts/2018/08/coding-challenge-day-25-to-28/) for an introduction to testing| [Code day 36](https://github.com/zotroneneis/magical_universe/blob/master/test_code/test_potion_class.py) |
| 37  | Extension of Magical Universe with classmethods for ```Charm, Hex, Curse```, etc. | [Day 37](http://alpopkes.com/posts/2018/08/coding-challenge-day-37/) | [Day 37](https://github.com/zotroneneis/magical_universe/blob/master/code_per_day/day_37.py) |

## Feedback

In case you find a mistake in the code or the blog posts, please let me know by opening an issue!
