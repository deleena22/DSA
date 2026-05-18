from collections import deque
class Logger(object):

    def __init__(self):
        self.mapping = {}
        self.q = deque([])
        

        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if self.mapping.get(message) is not None:
            last_seen = self.mapping[message]
            if timestamp - last_seen >= 10:
                while self.q and self.q[0] != message:
                    delmessage = self.q.popleft()
                    del self.mapping[delmessage]
                m = self.q.popleft()
                self.q.append(m)
                self.mapping[message] = timestamp
                return True
            else:
                return False
        else:
            self.q.append(message)
            self.mapping[message] = timestamp
            return True




        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)