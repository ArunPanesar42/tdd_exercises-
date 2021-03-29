# TDD Exercises 
## BREAD FACTORY - TASK 1
#### USER CASES
1. As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

2. As a user, I can use the bake dough with dough to get naan.

3. As a user, I can use the run factory with water and flour and get naan.

#### Acceptance Criteria

- you have written tests
- test pass
- you have written more test to make sure everything works as indented
- all user stories are satisfied
- code does not break
- code has exit condition
- DOD if followed

#### The program 
- first we have the class we use to see if the user has right ingredients 

- Makes a class that checks naan ingredients
```python
class run_factory():

    def make_dough(self, item1, item2):
        if item1 == "water" and item2 == "flour":   #checks if each item is equal to correct ingredients
        #item1 == "water"
        #item2 == "flour"
            return "dough"

    def bake_dough(self, item1):
        if item1 == "dough":
            return "naan"
        else:
            return "incorrect ingredients"
```
- We then have to create a python file that allows us to test 
```python
from naan_factory import run_factory
import unittest

class makeNaanTest(unittest.TestCase):
    naanf = run_factory()

    def test_make_dough(self):
        self.assertEqual(self.naanf.make_dough("water", "flour"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.naanf.bake_dough("dough"), "naan")
```
- after this we go to the terminal and enter `python -m unittest discover -v` to unit test program 

````
test_bake_dough (test_naan.makeNaanTest) ... ok
test_make_dough (test_naan.makeNaanTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
````


