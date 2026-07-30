from ai_agent_manager import ai_agent_manager
from database import db
from ebay_manager import ebay

print("🔥 NEW AUTOPILOT FILE LOADED")


class AutoPilotWorkflow:

    def run(self):

        print("\n🚀 AI AUTOPILOT STARTED")


        products = ai_agent_manager.run_agent(
            "product_hunter_agent",
            None
        )


        approved = []


        for product in products:


            print("\n🧠 Checking Product:")
            print(product)



            # ==========================
            # PRICING AI
            # ==========================

            pricing = ai_agent_manager.run_agent(
                "pricing_agent",
                product
            )


            print("\n💰 Pricing Result:")
            print(pricing)



            # Update Product With Pricing

            product["cost"] = pricing["supplier_cost"]

            product["price"] = pricing["selling_price"]



            # ==========================
            # PRODUCT ANALYSIS AI
            # ==========================

            analysis = ai_agent_manager.run_agent(
                "product_analysis_agent",
                product
            )


            print(analysis)



            # Merge Analysis Data

            product.update(analysis)



            # ==========================
            # AUTO LIST DECISION
            # ==========================

            if analysis["decision"] == "AUTO_LIST ✅":


                print("✅ AI Approved")



                # Duplicate Check

                existing = db.fetchone(
                    """
                    SELECT * FROM products
                    WHERE LOWER(name)=LOWER(?)
                    """,
                    (product["name"],)
                )



                if existing:


                    print(
                        "⚠️ Product Already Exists - Testing Listing"
                    )


                    listing = ai_agent_manager.run_agent(
                        "listing_agent",
                        product
                    )


                    ebay.create_listing(listing)



                    approved.append(
                        {
                            "product": product,
                            "analysis": analysis,
                            "listing": listing
                        }
                    )


                    continue




                # ==========================
                # SAVE NEW PRODUCT
                # ==========================

                db.execute(
                    """
                    INSERT INTO products(name, price, stock)
                    VALUES (?, ?, ?)
                    """,
                    (
                        product["name"],
                        product["price"],
                        product["stock"]
                    )
                )


                print("✅ New Product Saved")

                # ==========================
                # LISTING AI
                # ==========================

                listing = ai_agent_manager.run_agent(
                    "listing_agent",
                    product
                )

                # Upload to eBay
                ebay.create_listing(listing)

                approved.append(
                    {
                        "product": product,
                        "analysis": analysis,
                        "listing": listing
                    }
                )

            else:

                print(
                    f"❌ Product Skipped ({analysis['decision']})"
                )

        print("\n✅ AUTOPILOT COMPLETED")

        return approved


autopilot_workflow = AutoPilotWorkflow()