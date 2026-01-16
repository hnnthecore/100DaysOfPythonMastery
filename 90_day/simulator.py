import random
import time

def simulate_traffic(limiter, requests=20):
    for i in range(requests):
        allowed = limiter.allow_request()

        status = "✅ ALLOWED" if allowed else "🚫 RATE LIMITED"
        print(f"Request {i+1}: {status}")

        # Random burst traffic
        time.sleep(random.uniform(0.05, 0.3))
