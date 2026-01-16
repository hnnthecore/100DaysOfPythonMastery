from limiter import RateLimiter
from simulator import simulate_traffic

print("🚦 API Rate Limiter Simulation")
print("-" * 40)

# Allow 5 requests max, refill 1 token per second
limiter = RateLimiter(capacity=5, refill_rate=1)

simulate_traffic(limiter, requests=25)
