from collections import deque
import datetime as dt


class HistoryManager:
    def __init__(self):
        self.search_queue = deque(maxlen=100)
        self.filter_stack = []

    def log_search(self, query):
        # Append to the queue
        self.search_queue.append((dt.datetime.now(), query))

    def get_recent(self, n):
        # Return n queries from the right
        if not self.search_queue:
            return "Not performed any search"

        if n <= 0:
            return []

        return list(self.search_queue)[-n:]

    def apply_filter(self, filter_name):
        # Push to the stack
        self.filter_stack.append(filter_name)

    def undo_filter(self):
        # Pop and return last applied filter
        if self.filter_stack:
            return self.filter_stack.pop()
        else:
            return "No filter to undo"
