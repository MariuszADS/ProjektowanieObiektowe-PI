from random import randint
from time import sleep

class Logger:
    log_id: int     #pole / field

    def __init__(self,log_id: int):
        self.log_id = log_id

    def log(self,msg: str):
        #to jest metoda
        print(f'Logger[{self.log_id}]: {msg}')



class BufferLogger(Logger):


    def __init__(self,buffer_size: int):
        super().__init__(randint(0,10 ** 9))     #jakis losowy ID
        self.buffer_size = buffer_size
        self.buffer = []

    def log(self, msg: str):
            self.buffer.append(msg)
            if len(self.buffer) >= self.buffer_size:
                self.flush()


    def flush(self):
        for l in self.buffer:
                print(l)
                print('-' * 80)
        self.buffer.clear()


if __name__ == '__main__':
    ll = BufferLogger(buffer_size=10)
    for i in range(1000):
        ll.log(f'Komunitkat {i}')