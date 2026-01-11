from agent import Agent
from environment import Environment
import time

env = Environment()

agents = [
    Agent("Alpha"),
    Agent("Bravo"),
    Agent("Charlie"),
    Agent("Delta")
]

turn = 0

print("🏟 Multi-Agent Survival Arena")
print("-" * 40)

while len([a for a in agents if a.alive]) > 1:
    turn += 1
    env.tick()

    print(f"\nTurn {turn}")
    print(f"World → Food: {env.food}, Water: {env.water}, Danger: {env.danger}")

    for agent in agents:
        if not agent.alive:
            continue

        action = agent.decide(env)
        agent.act(action, env)

        print(
            f"{agent.name} | Action: {action} | "
            f"Hunger: {agent.hunger} | Energy: {agent.energy}"
        )

    time.sleep(0.6)

winner = [a for a in agents if a.alive]

if winner:
    print(f"\n🏆 Winner: {winner[0].name}")
else:
    print("\n💀 No survivors.")
