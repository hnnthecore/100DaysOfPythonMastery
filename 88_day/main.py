from economy import Economy
from agents import Agent
import time

economy = Economy()

agents = [
    Agent("Farmer-1", "producer"),
    Agent("Farmer-2", "producer"),
    Agent("Citizen-1", "consumer"),
    Agent("Citizen-2", "consumer"),
    Agent("Citizen-3", "consumer"),
]

turn = 0

print("📈 Economic Simulation Started")
print("-" * 40)

while True:
    turn += 1
    demand = {"food": 0, "tools": 0}

    print(f"\nTurn {turn}")
    print(f"Supply: {economy.supply}")
    print(f"Prices: {economy.prices}")

    for agent in agents:
        agent.act(economy, demand)
        status = "Alive" if agent.alive else "Dead"
        print(
            f"{agent.name} | {agent.role} | "
            f"Money: {agent.money} | Hunger: {agent.hunger} | {status}"
        )

    economy.update_prices(demand)

    # End condition
    alive_consumers = [a for a in agents if a.alive and a.role == "consumer"]
    if not alive_consumers:
        print("\n💥 Economic collapse: No consumers survived.")
        break

    time.sleep(0.8)
