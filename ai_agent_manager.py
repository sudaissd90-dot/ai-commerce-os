class AIAgentManager:

    def __init__(self):

        self.agents = {}

    def register_agent(self, name, agent):

        self.agents[name] = agent

        print(f"✅ Agent Registered: {name}")

    def get_agent(self, name):

        return self.agents.get(name)

    def remove_agent(self, name):

        if name in self.agents:
            del self.agents[name]
            print(f"✅ Agent Removed: {name}")
        else:
            print("❌ Agent Not Found")

    def list_agents(self):

        return list(self.agents.keys())

    def run_agent(self, name, *args, **kwargs):

        agent = self.get_agent(name)

        if not agent:
            print("❌ Agent Not Found")
            return

        if hasattr(agent, "run"):
            return agent.run(*args, **kwargs)

        print("❌ Agent Has No 'run' Method")


ai_agent_manager = AIAgentManager()