from ai_agent_manager import ai_agent_manager


class ProductHuntingWorkflow:

    def run(self):

        print("\n🔍 Finding Products...")


        products = ai_agent_manager.run_agent(
            "product_hunter_agent",
            None
        )


        approved_products = []


        for product in products:

            print("\n🧠 Analyzing:")
            print(product["name"])


            analysis = ai_agent_manager.run_agent(
                "product_analysis_agent",
                product
            )


            print(analysis)


            if analysis["decision"] == "APPROVED ✅":

                approved_products.append(
                    {
                        "product": product,
                        "analysis": analysis
                    }
                )


        return approved_products



product_hunting_workflow = ProductHuntingWorkflow()