
class Queue:
    def __init__(self,tickets:list,k):
        self.time = 0
        self.tickets = tickets
        self.item = self.tickets[k]
        self.memory_address = id(tickets[k])

    def isEmpty(self):
        if self.tickets:
            return False
        return True

    def enqueue(self,item):

    def dequeue(self):


    def calculate(self):

        while self.item != 0:





class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        pass


if __name__ == "__main__":


