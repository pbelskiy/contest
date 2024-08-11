"""
359. Logger Rate Limiter (Easy)

Design a logger system that receives a stream of messages along
with their timestamps. Each unique message should only be printed
at most every 10 seconds (i.e. a message printed at timestamp t
will prevent other identical messages from being printed until
timestamp t + 10).

All messages will come in chronological order. Several messages
may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message)
Returns true if the message should be printed in the given
timestamp, otherwise returns false.
"""
class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.d:
            self.d[message] = timestamp
            return True

        if timestamp - self.d[message] < 10:
            return False

        self.d[message] = timestamp
        return True
