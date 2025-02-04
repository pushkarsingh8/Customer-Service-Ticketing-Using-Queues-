#Customer Service Ticketing Sytem (Using Queue):-
from prettytable import PrettyTable 
from datetime import datetime
import time
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
        
        
            
    def is_empty(self):
        #checks queue is empty or not
        return self.front == None
    
    
    def len(self):
        #it's return only size of queues
        return self.size
    
    
    
    
    def push(self,id,date_time,name,desp):
        #inserting a node in a queue
        
        new_node = Node(id,date_time,name,desp) 
        
 
        
        if self.front == None:
            self.front = new_node
            self.rear = new_node

            
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
            
            
    
            
    def pop(self):
        #delete a node in a queue
        if self.is_empty():
            print("Empty List")
            return None
        self.front = self.front.next
        
        if self.front == None:
            self.rear = None
            
        self.size -= 1
            
        
        
        
    
    
    def main(self):
        #it show first On Terminal
        
        
        while True:
            print(
           """\n\t\t*Customer Services Ticketing System*\n\n1.Generate New Ticket
              \n2.Remove and Process a Ticket
              \n3.Pending Tickets Show
              \n4.Mark Ticket as Urgent
              \n5.Exit
          """)

            
            try:
                print("\nEnter Your choice:-")
                user = int(input(">> "))

                if user == 1:
                    q.generate_ticket()                
                elif user == 2:
                    q.remove_ticket()
                elif user == 3:
                    q.show_ticket()
                elif user == 4:
                    q.urgent_ticket()
                elif user == 5:
                    print("Goodbye!")
                    break
                
                else:
                    print("Please Enter valid choice(1-5).")
                                        
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        
        
    
    
    
    
    def generate_ticket(self):
        
        #id always generated randomaly 
        id = random.randint(1100,1500)
        
        #ticket raise date & time always mention
        curr_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        while True:
                
            print("\nEnter Your Name")
            name = input(">>").capitalize()
            
            if name.isalpha():
                break
            
            else:
                print("Please Enter a Valid Name (at least 1 characters)")
                
                
        print("Write Down Details of the issue:")
                
        desp = input(">>")
            
        self.push(id,curr_time,name,desp) 
        print("Tickets generated successfully")
        
        
        while True:
                
            print("Going to Inventory for (1) // New Ticket for (0)\n")
            try:
                dec = int(input(">>"))
                
                if dec == 1:
                    self.main()
                    break
                
                elif (dec == 0):
                    q.generate_ticket()
                    break
                else:
                    print("Please Enter 1 or 0")
            
            except ValueError:
                print("Invalid input. Please enter a number")
                        
                
        
        
        
        
        
        
    
    def remove_ticket(self):
        #it's directly delete a ticket on based of Old 
        if self.is_empty():
            print("List is Empty")
            q.main()
            return None
        
        print(f"Id: {self.front.issue_id} Name:{self.front.name} Time: {self.front.date_time}\n")
        count = 3
        print("Processing ",end="")
        while count !=1:
            
            print(".",end="",flush=True)
            time.sleep(1)
            print(".",end="",flush=True)
            time.sleep(0.5)
            print(".",end="",flush=True)
            count -= 1 
            
        print("\nDeleted")
            
        q.pop()
        
        print("Going to Inventory for (1) // New Ticket for (0)\n")
        while True:
                
            dec = int(input(">>"))
            
            if dec == 1:
                q.main()
            
            elif (dec == 0):
                q.generate_ticket()
            else:
                print("\nPlease Enter valid details!!!")        
        
        
        
        
    def urgent_ticket(self):
        
        if self.is_empty():
            print("List is Empty")
            return None
        
        print("Enter Customer Name")
        cust_name = input(">>").capitalize()
        
            
        if not cust_name.isalpha():
            print("Please Enter valid Details")
            return
        
        if self.front.name == cust_name:
            print("Ticket is already at the front")
                
            
        curr = self.front
        prev = None
                
        while curr!=None:
             
            if curr.name == cust_name:
                if prev is not None:
                    prev.next = curr.next
                        
                else:
                    self.front = curr.next
                    
                
                curr.next = self.front
                self.front = curr
                
                print("Ticket marked as urgent and moved to the front")
                return
            
            
            prev = curr
            curr = curr.next
            
        print("Ticket not found.")
            
                    
                    
                    
                          
                          
                          
                          
                          
    def show_ticket(self):
        if self.is_empty():
            print("No pending tickets")
            return 
        
        status = "Pending"
        table = PrettyTable(["S_No","id","date","Name","Desp","Status"])
        count = 0
        
        curr = self.front
        
        while curr!=None:
            count+=1
            table.add_row([count,curr.issue_id,curr.date_time,curr.name,curr.issue_desp,status])

            curr = curr.next
            
        print(table)
    
                
            
                
                
            
            
            
            
            
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
 
 
            
            
q = issue()
q.main()

        
            