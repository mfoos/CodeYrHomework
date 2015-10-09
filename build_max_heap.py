from sys import * 

origArr = [5, 3, 17, 10, 84, 19, 6, 22, 9]

class Node(object):

    def __init__(self, value):
        self.value = value

    def add_child(self, child):
        if len(self.get_children) == 0:
            self.lchild = child
        elif len(self.get_children) == 1:
            self.rchild = child
        else:
            print "No room to add child"
            # needs to overflow into next row
        

    def get_children:
