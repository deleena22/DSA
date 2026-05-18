class Logger(object):

    def __init__(self):
        self.mapping = {}
        self.seen = set()

        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message in self.seen:
            last_seen = self.mapping[message]
            if timestamp - last_seen >= 10:
                self.mapping[message] = timestamp
                return True
            else:
                return False
        else:
            self.seen.add(message)
            self.mapping[message] = timestamp
            return True




        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)