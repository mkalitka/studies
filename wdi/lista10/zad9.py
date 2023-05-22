class ListItem:
    
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)
    L.next.prev = L

def pop_first_element(L):
    while L.prev != None:
        L = L.prev
    L.next.prev = None
    del L

def pop_last_element(L):
    while L.next != None:
        L = L.next
    L.prev.next = None
    del L
