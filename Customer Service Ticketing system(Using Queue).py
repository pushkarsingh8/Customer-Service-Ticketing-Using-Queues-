#Customer Service Ticketing Sytem (Using Queue):-
from prettytable import PrettyTable 
from datetime import datetime
import random

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
        
    
    def main(self):
        #it show first On Terminal
        print(
           """\n\t\t*Customer Services Ticketing System*\n\n1.Generate New Ticket
              \n2.Remove and Process a Ticket
              \n3.Pending Tickets Show
              \n4.Mark Ticket as Urgent
              \n5.Exit
          """)
        
        while True:
            try:
                print("Enter Your choice:-")
                user = int(input(">> "))

                if user == 1:
                    q.generate_ticket()
                    break
                
                elif user == 2:
                    q.remove_ticket()
                
                elif user == 3:
                    pass

                elif user == 4:
                    pass

                elif user == 5:
                    pass
                
                else:
                    print(f"Invalid Data Entered {user}\n")
                    
            except(ValueError):
                print(f"Invalid Date Entered {user}\n")
        
        
        
        
        
        
        
        
        
        
        
        
        
    def is_empty(self):
        return self.front == None
    
    def len(self):
        return self.size
    
    
    
    
    def generate_ticket(self):
        
        #id always generated randomaly 
        id = random.randint(1100,1500)
        
        #ticket raise date & time always mention
        curr_time = datetime.now()
        curr_time = curr_time.strftime("%Y-%m-%d %H:%M")
        
        while True:
                
            print("Enter Your Name")
            name = input(">>").capitalize()
            
            if name.isalpha():
                break
            
            elif len(name) < 2:
                print("Please Enter Only Name\n")
            
            else:
                print("Only Enter valid Statements!!!")
                
        print("Write Down Details what issue?")
                
        desp = input(">>")
            
        q.push(id,curr_time,name,desp) 
        q.traverse()
        q.main()
        
        
        
        
    
    def remove_ticket(self):
        if self.is_empty():
            print("List is Empty")
            return None
        
        print(f"Id: {self.front.issue_id} Name:{self.front.name} Time: {self.front.date_time}")
        q.pop()        
            
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
q.main()
q.push(1123,12354,"Pushar","ROg")
q.push(1124,12354,"Pushar","ROg")
q.pop()
q.push(1125,12354,"Pushar","ROg")
q.push(1123,12354,"Pushar","ROg")
# q.traverse()
        
            