# Kaitlyn Forsberg - this program uses Songs(2).txt, Albums(2).txt, and Commands(2).txt and
# creates a doubly linked list to hold a playlist of songs and performs commands on the playlist,
# such as "skip forward", "beginning", "skip backward", etc. Python's OOP capability was used in the
# implementation of this program.

import sys
import time
import itertools

skip_forward = 0
skip_back = 0
beg_forward = 0
end_forward = 0
play_track = 0

def use_commands(command_list, linked_list):
    # declare that this function will update the global variables above
    global beg_forward
    global end_forward
    global skip_forward
    global skip_back
    global play_track
    # The cur_node is used to keep track of the current song in the playlist.
    # The loop below changes the cur_node depending upon the command and
    # it iterates the global variables above.
    cur_node = None
    for comm in command_list:
        if comm == "beginning":
            cur_node = linked_list.first_node
            beg_forward += 1
        elif comm == "end":
            cur_node = linked_list.last_node
            end_forward += 1
        elif comm == "skip forward":
            cur_node = cur_node.get_next()
            skip_forward += 1
        elif comm == "skip backward":
            cur_node = cur_node.get_prev()
            skip_back += 1
        elif comm == "play track":
            play_track += 1

        # prints out the current node depending on if the command if to "play" or switch songs throughout the list
        if cur_node is not None:
            if comm != "play track":
                print(f"Now At: {cur_node.get_value()}")
            else:
                print(f"Now Playing: {cur_node.get_value()}")


# pass in linked list of unordered songs and a list of the ordered songs so that the unordered
# linked list can be ordered.
def sort_list(linked_list, ordered_album):
    index = 0
    while index < len(ordered_album):
        # insert nodes in the correct ordered spot depending upon if the node being inserted is
        # at the beginning, middle, or end of the list.
        if index == 0:
            linked_list.insert_beg(ordered_album[index])
        elif index == (len(ordered_album)-1):
            linked_list.append_to_end(ordered_album[index])
        else:
            prev = linked_list.find_node(ordered_album[index-1])
            linked_list.insertAfter(prev, ordered_album[index])

        # finds the node to be deleted in the current linked list
        temp_node = linked_list.find_node(ordered_album[index])
        # print(linked_list.list_to_str())
        linked_list.delete_node(temp_node)
        index += 1

    # returns the ordered linked list
    return linked_list

# define Node object
class Node:

    # initialize the next_node and prev_node to None if no argument is given when the function is called. (Constructor)
    def __init__(self, val, next_node=None, prev_node=None):
        self.value = val
        self.next = next_node
        self.prev = prev_node

    # set pointer for the "next" variable for the Node object
    def set_next(self, next_node):
        self.next = next_node

    # returns a pointer to the next node from the current node. Must use get_value() to get the value of the pointer.
    def get_next(self):
        return self.next

    def set_prev(self, prev_node):
        self.prev = prev_node

    def get_prev(self):
        return self.prev

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    # returns a string of the current node (song).
    def to_str(self):
        return f"Current Song: {self.value}\n"

    # returns a boolean value as to whether or not the current node has a next node.
    def has_next(self):
        if self.next is not None:
            return True
        else:
            return False

    # returns a boolean value as to whether or not the current node has a previous node.
    def has_prev(self):
        if self.prev is not None:
            return True
        else:
            return False


# define class
class DoublyLinkedList:

    # constructor to the class.
    def __init__(self, first=None):
        self.first_node = first
        self.last_node = first
        self.ll_size = 0

    # returns the size of the linked list.
    def get_size(self):
        return self.ll_size

    # returns the value for the first node of the linked list.
    def get_FirstNode(self):
        return self.first_node.get_value()

    # returns the value for the last node of the linked list.
    def get_LastNode(self):
        return self.last_node.get_value()

    # append node to the end of the linked list.
    def append_to_end(self, val):
        # initialize Node object.
        new_node = Node(val)
        # increment size of the linked list.
        self.ll_size += 1
        # since at end of the list, the next of the node will be None.
        new_node.next = None

        # if the list is empty, then append a node to the beginning of the list.
        if self.first_node is None:
            new_node.prev = None
            self.first_node = new_node
            return

        # initialize a node that will be iterated through to the end of the list.
        last_node = self.first_node
        while last_node.next is not None:
            last_node = last_node.next

        # append node to the end of the list
        last_node.next = new_node
        new_node.prev = last_node
        self.last_node = new_node

    # function to insert a node to the beginning of the list.
    def insert_beg(self, value):
        # create Node object and increase size of the linked list
        new_node = Node(value)
        self.ll_size += 1

        # sets the new node's next equal to the current first node in the list
        new_node.next = self.first_node

        # if there is a first node in the list then set that node's prev equal to the previous node
        if self.first_node is not None:
            self.first_node.prev = new_node

        # sets the value of the first node of the list equal to the new node
        self.first_node = new_node

    # function to insert a node after a particular node
    def insertAfter(self, previous_node, value):
        # if there is no previous node, then a node cannot be placed after None
        if previous_node is None:
            print("Invalid prev node")
            return

        # create new Node object and increase the size of the linked list
        new_node = Node(value)
        self.ll_size += 1

        # if prev node's next is None then there is only one node already in the list
        if previous_node.next is None:
            self.last_node = new_node

        # set new node's next to the prev node's next, the prev node's next becomes the new node, and the new node's
        # prev is the previous node
        new_node.next = previous_node.next
        previous_node.next = new_node
        new_node.prev = previous_node

        # sets the next node's prev equal to the new node
        if new_node.next is not None:
            new_node.next.prev = new_node

    # deletes a node at any position in the linked list
    def delete_node(self, node):
        # if not the first node
        if node.get_prev() is not None:
            # if there is another node next
            if node.has_next():
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
            # if there is not another node, then set the previous node's next equal to None
            else:
                node.get_prev().set_next(None)
                self.last_node = node
        # if the first node then change the linked list's first_node variable and change the next node's prev
        else:
            self.first_node = node.next
            node.next.set_prev(None)
        self.ll_size -= 1

    # finds and returns the address of a certain node in the list based on its value
    def find_node(self, val):
        node = self.first_node
        while node is not None:
            if node.value == val:
                return node
            else:
                node = node.next

    # prints each node in the list
    def list_to_str(self):
        if self.first_node is None:
            return print("List is empty")

        node = self.first_node
        print(node.to_str())
        while node.has_next():
            node = node.get_next()
            print(node.to_str())


if len(sys.argv) != 4:
    raise ValueError('Please provide three file names.')

# open files
sys.argv[0] = sys.argv[0][0:len(sys.argv[0]) - sys.argv[0][::-1].find('/')]
inputFile1 = sys.argv[0]+sys.argv[1]
inputFile2 = sys.argv[0]+sys.argv[2]
inputFile3 = sys.argv[0]+sys.argv[3]
print("\nThe files that will be used for input are {0}, {1}, and "
      "{2}".format(sys.argv[1], sys.argv[2], sys.argv[3]), "\n")

filename1 = str(sys.argv[1])
filename2 = str(sys.argv[2])
filename3 = str(sys.argv[3])

file1 = open(filename1, "r")
file2 = open(filename2, "r")
file3 = open(filename3, "r")

# initialize list for the unordered and ordered songs and commands for each album
SuperTrouper = []
SuperTrouper_ordered = []
SuperTrouper_commands = []
ABBA = []
ABBA_ordered = []
ABBA_commands = []
VoulezVous = []
VoulezVous_ordered = []
VoulezVous_commands = []
Playlist = []
Playlist_commands = []

read_album2 = False
read_album3 = False
read_album4 = False

start = time.time()

# the two variables below are for the statistics portion at the end of the program
songs_read = 0
append_num = 0

# iterates through the Songs(2).txt and Albums(2).txt files and place the songs into their respective variables. Only
# one album is read in at a time. read_album1 is for Super Trouper, read_album2 is for ABBA, read_album3 is for
# Voulez-Vous, and read_album4 is for the playlist
for song, ord_song in itertools.zip_longest(file1, file2):
    if song != "\n" and song.count("Album: ") == 0 and\
            (read_album2 == False and read_album3 == False and read_album4 == False):
        SuperTrouper.append(song.strip('\n'))
        SuperTrouper_ordered.append(ord_song.strip('\n'))
        songs_read += 1
        append_num += 1
    elif song != "\n" and song.count("Album: ") == 0 and\
            (read_album2 == True and read_album3 == False and read_album4 == False):
        ABBA.append(song.strip('\n'))
        ABBA_ordered.append(ord_song.strip('\n'))
        songs_read += 1
        append_num += 1
    elif song != "\n" and song.count("Album: ") == 0 and\
            (read_album2 == False and read_album3 == True and read_album4 == False):
        VoulezVous.append(song.strip('\n'))
        VoulezVous_ordered.append(ord_song.strip('\n'))
        songs_read += 1
        append_num += 1
    elif song != "\n" and song.count("Playlist") == 0 and\
            (read_album2 == False and read_album3 == False and read_album4 == True):
        # strips the number from the name of the song in the playlist
        Playlist.append(song[1:].strip('\n'))

    # resets the read_album variables once a new-line is encountered.
    if song == "\n" and read_album2 == False and read_album3 == False and len(SuperTrouper) > 0:
        read_album2 = True
    elif song == "\n" and read_album2 == True and len(ABBA) > 0:
        read_album3 = True
        read_album2 = False
    elif song == "\n" and read_album3 == True and len(VoulezVous) > 0:
        read_album4 = True
        read_album3 = False

read_album4 = False
# iterates through the commands for each album and puts the commands in their respective lists. The commands for
# one album is read in at a time. read_album1 is for Super Trouper, read_album2 is for ABBA, read_album3 is for
# Voulez-Vous, and read_album4 is for the playlist
for command in file3:
    temp_command = command.strip('\n')
    if command != "\n" and command.count("Playlist") == 0 and\
            (read_album2 == False and read_album3 == False and read_album4 == False):
        SuperTrouper_commands.append(temp_command.lower())
    elif command != "\n" and command.count("Playlist") == 0 and\
            (read_album2 == True and read_album3 == False and read_album4 == False):
        ABBA_commands.append(temp_command.lower())
    elif command != "\n" and command.count("Playlist") == 0 and\
            (read_album2 == False and read_album3 == True and read_album4 == False):
        VoulezVous_commands.append(temp_command.lower())
    elif command != "\n" and command.count("Playlist") == 0 and\
            (read_album2 == False and read_album3 == False and read_album4 == True):
        temp_command = temp_command.translate(str.maketrans("", "", "1"))
        Playlist_commands.append(temp_command.lower())

    # resets the read_album variables once a new-line is encountered.
    if command == "\n" and read_album2 == False and read_album3 == False and len(SuperTrouper_commands) > 0:
        read_album2 = True
    elif command == "\n" and read_album2 == True and len(ABBA_commands) > 0:
        read_album3 = True
        read_album2 = False
    elif command == "\n" and read_album3 == True and len(VoulezVous_commands) > 0:
        read_album4 = True
        read_album3 = False

# creates doubly-linked lists for each album and for the playlist
FirstLL = DoublyLinkedList()
for name1 in SuperTrouper:
    FirstLL.append_to_end(name1)

SecondLL = DoublyLinkedList()
for name2 in ABBA:
    SecondLL.append_to_end(name2)

ThirdLL = DoublyLinkedList()
for name3 in VoulezVous:
    ThirdLL.append_to_end(name3)

PlaylistLL = DoublyLinkedList()
for name4 in Playlist:
    PlaylistLL.append_to_end(name4)

# sorts each of the unordered doubly-linked lists into being ordered and saves the ordered list into their
# respective variable
sorted_Super = sort_list(FirstLL, SuperTrouper_ordered)
sorted_ABBA = sort_list(SecondLL, ABBA_ordered)
sorted_Voulez = sort_list(ThirdLL, VoulezVous_ordered)

# returns each node of every doubly linked list
# sorted_Super.list_to_str()
# sorted_ABBA.list_to_str()
# sorted_Voulez.list_to_str()
# PlaylistLL.list_to_str()

# iterates through the commands for each ordered album
print("Starting to process play commands...\n")
print("Executing commands for Album 'Super Trouper':\n")
use_commands(SuperTrouper_commands, sorted_Super)
print("\nExecuting commands for Album 'ABBA':\n")
use_commands(ABBA_commands, sorted_ABBA)
print("\nExecuting commands for Album 'Voulez-Vous':\n")
use_commands(VoulezVous_commands, sorted_Voulez)
print('\nExecuting commands for Playlist:\n')
use_commands(Playlist_commands, PlaylistLL)

end = time.time()

print('\n')
print("**********************\n"
      "***** Statistics *****\n"
      "**********************\n")
print(f"Total Songs Read: {songs_read}\n"
      f"Number of Skip Forward Commands: {skip_forward}\n"
      f"Number of Skip Backwards Commands: {skip_back}\n"
      f"Number of Play Next Track Commands: {play_track}\n"
      f"Number of Append Commands: {append_num}\n"
      f"Number of Beginning Forward Commands: {beg_forward}\n"
      f"Number of End Forward Commands: {end_forward}\n")

print("Time: ", end-start)
