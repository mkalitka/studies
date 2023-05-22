class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

#zad1
def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)

#zad2
def pop_element(L):
    previous = L
    while L.next != None:
        previous = L
        L = L.next
    del L
    previous.next = None

#zad3
def join_lists(L1, L2):
    while L1.next != None:
        L1 = L1.next
    L1.next = L2

#zad4
def remove_val(L, value):
    while L.next != None:
        previous = L
        L = L.next
        if L.val == value:
            previous.next = L.next

#zad6
def print_list_reversed(L):
    if L.next != None:
        print_list_reversed(L.next)
    print(L.val, end="")
