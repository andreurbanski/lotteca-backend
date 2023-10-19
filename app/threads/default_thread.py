import time
from threading import Thread

class DefaultThread:
    status:int = 0
    thread =  None

    """
        status codes:
            0: Disabled
            1: Starting
            2: Running
    
    """

    def __init__(self) -> None:
        pass
        
    def change_status(self, status:int):
        self.status = status

    def thread(self):
        while True:
            match self.status:
                case 0:
                    # IDLE - DO Nothing
                    pass
                case 1:
                    self.start()
                case 2:
                    self.run()
                case 3:
                    self.kill()
            time.sleep(2)

    def start(self):

        try:
            self.change_status(2)
            self.thread = Thread(target=self.thread())
        except:
            print(f"Could not start the thread {self.name}")

    def kill(self):
        self.thread.join()
        pass