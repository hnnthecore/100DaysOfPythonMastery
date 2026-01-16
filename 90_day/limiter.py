import time

class RateLimiter:
    def __init__(self, capacity, refill_rate):
        """
        capacity     → max tokens
        refill_rate  → tokens per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_checked = time.time()

    def allow_request(self):
        """
        Returns True if request is allowed,
        False if rate-limited.
        """
        now = time.time()
        elapsed = now - self.last_checked
        self.last_checked = now

        # Refill tokens based on elapsed time
        self.tokens += elapsed * self.refill_rate
        self.tokens = min(self.tokens, self.capacity)

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
