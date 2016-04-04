##########
#Handles all dict related actions
#Creation, deletion of items and maybe more
############
class DictHandler():

    def __init__(self):
        pass

    def create_dict(self, a_dict_name):
        a_dict_name = {}
        return a_dict_name

    def add_to_dictionary(self, a_dict_name, a_key, a_value):
        a_dict_name[a_key] = a_value

    def delete_key(self, a_dict, a_key):
        del a_dict[a_key]



#Runs tests on the functions to make sure that they work
if __name__ == '__main__':
    d = DictHandler()
    Bob = d.create_dict("Bob")
    print(Bob)
    d.add_to_dictionary(Bob, 1, "George")
    print(Bob)
    d.add_to_dictionary(Bob, 2, "Bob")
    d.add_to_dictionary(Bob, 3, "Fellow123")
    print(Bob)
    d.delete_key(Bob, 1)
    print(Bob)



