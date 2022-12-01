import Queue as q
import DecisionTree as dt
import tkinter as tk
from tkinter import StringVar
from tkinter import OptionMenu

class shoppingList:
    def __init__(self) -> None:
        self.timeToDecide = False #once tripped, this flag makes the decision tree logic activate
        self.list = q.Queue()
        self.disList = [] #display list, used by selection sort due to conflicts with the way the queue works.

    def add(self):
        val = chosen.get()
        pri = getInput()
        if int(pri) > 9: #had to change to 9 to avoid conflicts with sort
            return
        self.list.enqueue(val,pri) #take values from gui elements
        s.selSort()
        if len(self.disList) == 9: #disappear add button once list has reached maximum
            AddButton.destroy()
            warningLabel.destroy()
        listOfItems.config(text=f"{s.print_queueDis()}") #update label to portray list of items

    #add needs to work off of a list of preset items, but coldness value is determined by user

    def remove(self):
        AddButton.destroy() #disappear the add button once items start being deleted. 
        warningLabel.destroy()
        if len(self.disList) == 0: #error handling for empty queue, give user feedback
            listOfItems.config(text="Cart is already empty!")
            self.timeToDecide = True
            return
        self.list.dequeue()
        s.selSort()
        listOfItems.config(text=f"{s.print_queueDis()}") #update label to portray list of items


    def selSort(self): #TODO: fix this / self.dislist will be what is displayed to the user, the self.list.items will remain unchanged due to difficulties retrieving items based on index -- DONE
        newList = []
        self.disList = []
        for i in range(self.list.size):
            newList.append(self.list.items[i])
        lenCheck = len(newList) #need this to counteract infinite loop
        minimum = 0
        while len(self.disList) != lenCheck:
            minimum = 0
            for i in newList: #iterate through newlist
                if int(str(i)[-1]) < int(str(minimum)[-1]) or minimum == 0: #if item priority is smaller than previous then minimum = current item and indextrue is set to index
                    minimum = i
            self.disList.append(minimum)

            #debugging code    
            print("~")
            for i in newList:
                print(i)
            print("~~")
            for i in self.disList:
                print(i)
            #remove smallest item from list so that it does not just get added every time
            if len(newList) != 0:
                newList.pop(newList.index(minimum))
        

        
            

    def print_queueDis(self):
        stack_str = ""
        if not len(self.disList) == 0:
            for x in range(self.list.size):
                stack_str += str(self.disList[x]) + "\n"
            return stack_str;  
        else:
            stack_str = "Queue is Empty"
            return stack_str

    def printList(self):
        return self.list.print_queue()


def decideNo():
    endQuery.place = 2
    treeLabel.config(text=f"{endQuery.items[endQuery.place].sData}")

def decideYes():
    endQuery.place = 1
    treeLabel.config(text=f"{endQuery.items[endQuery.place].sData}")


s = shoppingList()



window = tk.Tk()
window.geometry("500x600")
window.title("Shopping Cart")

def getInput():
    ret = priEdit.get(1.0,"end-1c")
    return ret


#Dropdown menu code
options = [
    "Cheese",
    "Chips",
    "Milk"
]
chosen = StringVar()
chosen.set("Cheese")
dropDown = OptionMenu(window, chosen, *options)
dropDown.pack()

#priority change code
priEdit = tk.Text(window, height=1,width=20)
priEdit.pack()  
pr = getInput()

#adding items to list
warningLabel = tk.Label(window, text="List may only be nine items in length. Priority cannot exceed 9.")
warningLabel.pack()
AddButton = tk.Button(window,text="Add Item", command=s.add)
AddButton.pack()

# TODO: add remove functionality, add selection sort to sort list before it is shown to the user -- DONE
#deleting items from list
deleteButton = tk.Button(window, text="Delete Item", command=s.remove)
deleteButton.pack()

listOfItems = tk.Label(window,text = "") #this label holds the list of items
listOfItems.pack()
#decision tree code TODO: Fix the decision tree so that it can interface with the gui rather than breaking the program

endQuery = dt.BDT()

treeLabel = tk.Label(window, text="Test")
treeLabel.pack()

endQuery.add("Do you like the app?")
endQuery.add("Thank you!", "R")
endQuery.add("We will try to do better.", "L")
treeLabel.config(text=f"{endQuery.items[endQuery.place].sData}")
op1button = tk.Button(window, text="Yes", command=decideYes)
op1button.pack()
op2button = tk.Button(window, text="No", command=decideNo)
op2button.pack()




window.mainloop() 

