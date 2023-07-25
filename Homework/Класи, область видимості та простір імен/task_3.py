# TV controller

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

#     first_channel() - turns on the first channel from the list.
#     last_channel() - turns on the last channel from the list.
#     turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#     next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#     previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
#     current_channel() - returns the name of the current channel.
#     is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, 
#     or "No" - in the other case.

# The default channel turned on before all commands is №1.



CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    n = 1
    
    def __init__(self, CHANNELS: list):
        self.CHANNELS = CHANNELS
    
    def first_channel(self):
        print(self.CHANNELS[0])
    
    def last_channel(self):
        print(self.CHANNELS[-1])

    def turn_channel(self, n):
        self.n = n
        print(self.CHANNELS[self.n - 1])
        TVController.n = self.n - 1

    def next_channel(self):
        if TVController.n >= len(CHANNELS):
            TVController.n = 1
            print(self.CHANNELS[TVController.n])
        else:
            print(self.CHANNELS[TVController.n + 1])
            TVController.n += 1

    def previous_channel(self):
        if TVController.n == -len(CHANNELS):
            TVController.n = len(CHANNELS) - 1
            print(self.CHANNELS[TVController.n - 1])
        else:
            print(self.CHANNELS[TVController.n - 1])
            TVController.n -= 1  

    def current_channel(self):
        print(self.CHANNELS[TVController.n])

    def is_exist(self, argument):
        if isinstance(argument, str) is True:
            if argument in self.CHANNELS:
                print('Yes')
            else:
                print('No')
        else:
            try:
                self.CHANNELS[argument]
                print('Yes')
            except IndexError:
                print('No')                     



controller = TVController(CHANNELS)

controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
