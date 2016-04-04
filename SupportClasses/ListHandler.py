
class ListHanlder():

    def __init__(self):
        pass

    def create_list(self, a_list_name):
        a_list_name = []
        return a_list_name

    def add_to_list(self, a_list_name, a_value):
        a_list_name.append(a_value)

    def del_from_list_if_len_of_str_is_less_than(self, a_list_name, a_number):
        for word in a_list_name:
            if len(word) < a_number:
                a_list_name.remove(word)

    def del_from_list_if_len_of_str_is_greater_than(self, a_list_name, a_number):
        index = 0
        while index < len(a_list_name):
            if len(a_list_name[index]) > a_number:
                del a_list_name[index]
            index +=1


if __name__ == '__main__':
    f = ListHanlder()
    Bob = f.create_list("Bob")
    print(Bob)
    f.add_to_list(Bob ,"George")
    print(Bob)
    f.add_to_list(Bob, "Bob")
    f.add_to_list(Bob, "Fellow123")
    f.add_to_list(Bob, "Fellow1234")
    print(Bob)
    f.del_from_list_if_len_of_str_is_less_than(Bob, 4)
    print(Bob)
    f.del_from_list_if_len_of_str_is_greater_than(Bob, 4)
    print(len(Bob[0]))
    print(Bob)
