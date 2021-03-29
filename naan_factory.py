
# Makes a class that checks naan
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
