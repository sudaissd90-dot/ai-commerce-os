# ============================================
# AI STORE MANAGER - DECISION ENGINE
# ============================================

class DecisionEngine:

    def __init__(self):
        print("🧠 Decision Engine Loaded")

    def approve_product(self, product):

        name = product.get("name", "Unknown Product")
        score = product.get("score", 0)

        print(f"\n📦 Product: {name}")
        print(f"⭐ Score: {score}")

        if score >= 80:
            decision = "APPROVED ✅"

        elif score >= 60:
            decision = "REVIEW ⚠️"

        else:
            decision = "REJECTED ❌"

        print(f"🤖 AI Decision: {decision}")

        return decision


# ============================================
# TEST
# ============================================

if __name__ == "__main__":

    engine = DecisionEngine()

    product = {
        "name": "Mini Car Vacuum",
        "score": 87
    }

    result = engine.approve_product(product)

    print("\nFinal Result:", result)