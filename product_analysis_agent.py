from ai_agent_manager import ai_agent_manager


class ProductAnalysisAgent:

    def __init__(self):
        self.name = "AI Product Analysis Agent V3"

    def run(self, product):

        name = product["name"]
        price = product.get("price", 0)
        cost = product.get("cost", 0)

        # ==========================
        # AI Scores
        # ==========================

        demand_score = 18
        trend_score = 17
        competition_score = 16
        supplier_score = 18

        # ==========================
        # Profit Score
        # ==========================

        profit = price - cost

        if profit >= 30:
            profit_score = 20

        elif profit >= 20:
            profit_score = 15

        elif profit >= 10:
            profit_score = 10

        else:
            profit_score = 5

        # ==========================
        # Final Score
        # ==========================

        final_score = (
            demand_score +
            trend_score +
            competition_score +
            supplier_score +
            profit_score
        )

        # ==========================
        # AI Decision
        # ==========================

        if final_score >= 80:
            decision = "AUTO_LIST ✅"

        elif final_score >= 65:
            decision = "REVIEW ⚠️"

        else:
            decision = "REJECT ❌"

        return {

            "product": name,
            "price": price,
            "cost": cost,
            "profit": profit,

            "demand_score": demand_score,
            "trend_score": trend_score,
            "competition_score": competition_score,
            "supplier_score": supplier_score,
            "profit_score": profit_score,

            "final_score": final_score,
            "decision": decision
        }


product_analysis_agent = ProductAnalysisAgent()

ai_agent_manager.register_agent(
    "product_analysis_agent",
    product_analysis_agent
)