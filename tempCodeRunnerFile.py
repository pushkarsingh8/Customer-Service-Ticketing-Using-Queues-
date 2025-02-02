#Customer Service Ticketing Sytem (Using Queue):-
from prettytable import PrettyTable 
class Node:
    def __init__(self,id,date_time,name,desp):
        self.issue_id = id
        self.date_time =  date_time
        self.name = name
        self.issue_desp = desp
        self.next = None
        
            
class issue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
        
    def is_empty(self):
        return self.front == None
    
    def len(self):
        return self.size
    
    
    def push(self,id,date_time,name,desp):
        
        new_node = Node(id,date_time,name,desp) 
        
 
        
        if self.front == None:
            self.front = new_node
            self.rear = new_node

            
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
            
            
            
    def pop(self):
        if self.is_empty():
            print("Empty List")
            return None
        
        if self.front == None:
            self.rear = None
            self.size -= 1
            
        self.front = self.front.next
        self.size -= 1
        
        
        
    def traverse(self):
        if self.is_empty():
            print("Issues List Empty")
            return None
        
        table = PrettyTable(["S_No","id","date","Name","Desp"])
        count = 0
        
        curr = self.front
        
        while curr!=None:
            count+=1
            table.add_row([count,curr.issue_id,curr.date_time,curr.name,curr.issue_desp])

            curr = curr.next
            
        print(table)
        
            
            
q = issue()
q.push(1123,12354,"Pushar","ROg")
q.push(1124,12354,"Pushar","ROg")
q.push(1125,12354,"Pushar","ROg")
q.push(1123,12354,"Pushar","ROg")
q.traverse()
        
            