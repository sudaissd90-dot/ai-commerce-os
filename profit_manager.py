class ProfitManager:


    def __init__(self):

        self.records = []



    def add_record(self, product, cost_price, selling_price, quantity):


        revenue = selling_price * quantity

        cost = cost_price * quantity

        profit = revenue - cost



        record = {

            "product": product,
            "revenue": revenue,
            "cost": cost,
            "profit": profit

        }



        self.records.append(record)



        print(f"✅ Profit Record Added: {product}")
        print(f"💰 Profit: ${profit}")




    def get_reports(self):

        return self.records




    def total_profit(self):

        return sum(
            item["profit"]
            for item in self.records
        )




    def total_revenue(self):

        return sum(
            item["revenue"]
            for item in self.records
        )




# Object

profit_manager = ProfitManager()