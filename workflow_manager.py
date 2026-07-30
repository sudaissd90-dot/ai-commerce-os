from ai_agent_manager import ai_agent_manager


class WorkflowManager:

    def __init__(self):
        self.workflows = {}


    def register_workflow(self, name, agents):

        self.workflows[name] = agents

        print(f"✅ Workflow Registered: {name}")


    def list_workflows(self):

        return list(self.workflows.keys())


    def run_workflow(self, name, product):

        if name not in self.workflows:
            print("❌ Workflow Not Found")
            return None


        print(f"\n🚀 Running Workflow: {name}")

        results = {}


        for agent_name in self.workflows[name]:

            print(f"▶ Executing: {agent_name}")


            result = ai_agent_manager.run_agent(
                agent_name,
                product
            )


            results[agent_name] = result


            print(f"✅ {agent_name} Completed")


        print("✅ Workflow Completed")

        return results



workflow_manager = WorkflowManager()