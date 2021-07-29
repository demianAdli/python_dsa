class Item:
    """Lightweight composite to store priority queue items."""
    slots = "key", "value"

    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __lt__(self, other):
        return self.key < other.key     # compare items based on their keys


class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    def is_empty(self):     # concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0