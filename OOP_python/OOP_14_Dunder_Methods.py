# Dunder Methods

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'John',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}' # modified

    def __len__(self):
        return 5 # modified

    # def __del__(self):
    #     print('deleted!')  # modified

    def __call__(self):
        return('Alo?')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure)) # now returns red when called, but only on this
print(len(action_figure))
print(action_figure()) # call
print(action_figure['name']) # == __getitem__ 


