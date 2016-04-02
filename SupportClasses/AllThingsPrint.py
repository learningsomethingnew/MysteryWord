from time import sleep
import sys

class AllThingsPrint:

#a_string is what is being passed into this class
#a_state_of_env determines if this is a dev environment or not. Is an int being passed.
    def __init__(self, a_state_of_env):
        self._state_of_env = a_state_of_env
        self._dev_banner = "*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^"

    def print_text(self, a_string):
        for words in a_string + "\n":
            sys.stdout.write(words)
            sys.stdout.flush()
            sleep(.03)

    def print_to_command_line(self, a_string):
        if self._state_of_env == 0:
            print(self._dev_banner)
            print(a_string+"\n")

        if self._state_of_env == 1:
            self.print_text(a_string)

if __name__ == '__main__':
    f = AllThingsPrint(1)
    f.print_to_command_line("This is a test")
    p = AllThingsPrint(0)
    p.print_to_command_line("This is a system message\n")

