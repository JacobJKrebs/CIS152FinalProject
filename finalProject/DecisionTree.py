"""
This is a basic implementation of a binary decision tree. It is largely the same as the search tree,
but the use case is different. Adding to the tree no longer requires a weight, and left/right nodes
are manually set on creation. A method has been created to allow for traversal.
Jacob Krebs
oct 31 22
"""


class BSTNode:
    def __init__(self, sData, NodeLeft = None, NodeRight = None, root = None):
        self.sData = sData
        self.NodeLeft = NodeLeft
        self.NodeRight = NodeRight
        self.root = root # Allows for access of root for deletion
    def print(self):
        return f"{self.sData}"


class BDT:
    def __init__(self):
        self.items = []
        self.userIn = ""
        self.place = 0

    def add(self, sData, pos=None):
        b = BSTNode(sData)
        if self.isEmpty():
            self.items.append(b)
            return
        else:
            if pos == "L":
                if self.items[len(self.items) - 1].NodeLeft != None:
                    print("No can do.")
                    return
                self.items[len(self.items) - 1].NodeLeft = b
                self.items.append(b)
                return
            if pos == "R":
                if self.items[len(self.items) - 1].NodeRight != None:
                    print("No can do.")
                    return
                self.items[len(self.items) - 1].NodeRight = b
                self.items.append(b)
                return





    def isEmpty(self):
        return len(self.items) == 0

    def remove(self, val):
        index = -1
        for i in self.items:
            index += 1
            if i.sData == val:
                if i.root.iData > i.iData:
                    i.root.LeftNode = None
                    self.items.pop(index)
                    return
                if i.root.iData < i.iData:
                    i.root.RightNode = None
                    self.items.pop(index)
                    return
    def removeMax(self):
        val = BSTNode("",0)
        for i in self.items:
            if i.iData > val.iData:
                val = i
        index = -1
        for i in self.items:
            index += 1
            if i.iData == val.iData:
                self.items.pop(index)
                return


    def print(self):
        ans = False
        counter = 0
        if not ans:
            uin = print(f"{self.items[counter].sData}")
            if self.userIn =="y":
                counter += 1
            if self.userIn =="n":
                counter += 2
            if self.userIn == "end":
                return


#TODO: write unit tests for decision tree


    def height(self):
        return len(self.items) // 2


# dt = BDT()
# dt.add("Do you want to take the class?")
# dt.add("Do it!","R")
# dt.add("Then don't", "L")



# dt.print()
