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