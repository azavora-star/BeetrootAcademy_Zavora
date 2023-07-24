# TV controller

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

#     first_channel() - turns on the first channel from the list.
#     last_channel() - turns on the last channel from the list.
#     turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#     next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#     previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
#     current_channel() - returns the name of the current channel.
#     is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

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
        TVController.n = self.n

    def next_channel(self):
        print(self.CHANNELS[TVController.n])







controller = TVController(CHANNELS)


controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel() 
print(TVController.n)

# controller.previous_channel() == "BBC"

# controller.current_channel() == "BBC"

# controller.is_exist(4) == "No"

# controller.is_exist("BBC") == "Yes"
