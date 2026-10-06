class Task:
    next_id=1
    def __init__(self, description:str, programmer:str, workload:int):
        self.description=description
        self.programmer=programmer
        self.workload=workload
        self.id=Task.next_id
        Task.next_id+=1
        self.finito=False
    
    def is_finished(self):
        return self.finito
    
    def mark_finished(self):
        self.finito=True
        
    def __str__(self):
        if self.is_finished():
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
        else:
            return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"

class OrderBook:
    def __init__(self):
        self.list_of_orders=[]
        
    def add_order(self, description:str, programmer:str, workload:int):
        self.list_of_orders.append(Task(description,programmer,workload))
        
    def all_orders(self):
        return self.list_of_orders
        
    def programmers(self):
        programssss=[]
        for element in self.list_of_orders:
            programssss.append(element.programmer)
        return list(set(programssss))
    
    def mark_finished(self, id: int):
        found=False
        for order in self.list_of_orders:
            if order.id==id:
                order.mark_finished()
                found=True
        if not found:
            raise ValueError("Order Not Found")
    
    def finished_orders(self):
        finished=[]
        for order in self.list_of_orders:
            if order.is_finished():
                finished.append(order)
        return finished
        
    def unfinished_orders(self):
        unfinished=[]
        for order in self.list_of_orders:
            if not order.is_finished():
                unfinished.append(order)
        return unfinished
    
    def status_of_programmer(self, programmer: str):
        found=False
        countf=0
        countu=0
        sumf=0
        sumu=0
        for order in self.list_of_orders:
            if order.programmer==programmer:
                found=True
                if order.is_finished():
                    countf+=1
                    sumf+=order.workload
                else:
                    countu+=1
                    sumu+=order.workload
        if not found:
            raise ValueError("Programmer not found")
        return (countf,countu,sumf,sumu)
    
class OrderApplication:
    def __init__(self):
        self.orders=OrderBook()
        
    def go(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        while True:
            inputi=input("command: ")
            if inputi=="1":
                description=input("description: ")
                parts=input("programmer and workload estimate: ").split()
                if len(parts)==2:
                    programmer=parts[0]
                    workload=parts[1]
                    if not workload.isdigit():
                        print("erroneous input")
                    else:
                        workload=int(parts[1])
                        self.orders.add_order(description,programmer,workload)
                        print("added!")
                else:
                    print("erroneous input")
            elif inputi=="2":
                finished=self.orders.finished_orders()
                if len(finished)==0:
                    print("no finished tasks")
                else:
                    for order in finished:
                        print(order)
            elif inputi=="3":
                unfinished=self.orders.unfinished_orders()
                for order in unfinished:
                    print(order)
            elif inputi=="4":
                id=input("id: ")
                if not id.isdigit():
                    print("erroneous input")
                else:
                    id=int(id)
                    if id>len(self.orders.all_orders()):
                        print("erroneous input")
                    else:
                        self.orders.mark_finished(id)
                        print("marked as finished")
            elif inputi=="5":
                programmers=self.orders.programmers()
                for programmer in programmers:
                    print(programmer)
            elif inputi=="6":
                programmer=input("programmer: ")
                if programmer not in self.orders.programmers():
                    print("erroneous input")
                else:
                    countf,countu,sumf,sumu=self.orders.status_of_programmer(programmer)
                    print(f"tasks: finished {countf} not finished {countu}, hours: done {sumf} scheduled {sumu}")
            elif inputi=="0":
                break

ordersapp=OrderApplication()
ordersapp.go()