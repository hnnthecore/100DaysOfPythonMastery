from agent import Agent
from environment import Environment
import time

agent = Agent()
env = Environment()

turn = 0

print("🤖 AI Survival Simulation Started")
print("-" * 40)

while agent.is_alive():
    turn += 1

    env.tick()
    action = agent.decide(env)
    agent.act(action, env)

    print(f"Turn {turn}")
    print(f"Action: {action}")
    print(f"Agent → Hunger: {agent.hunger}, Energy: {agent.energy}")
    print(f"World → Food: {env.food}, Danger: {env.danger}")
    print("-" * 40)

    time.sleep(0.5)

print("💀 Agent did not survive.")
