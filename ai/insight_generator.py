import pandas as pd
from transformers import pipeline

class InsightGenerator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline('text-generation', model=model_name)

    def generate_insights(self, trades):
        insights = []
        for trade in trades:
            prompt = f"Trade: {trade['symbol']}, Status: {trade['status']}, Profit: {trade['signal_gained_profit']}%"
            insight = self.generator(prompt, max_length=50)
            insights.append(insight[0]['generated_text'])
        return insights

if __name__ == "__main__":
    # Example usage
    trades = [
        {"symbol": "BTC/USD", "status": "All Targets Achieved", "signal_gained_profit": "3.3769"},
        {"symbol": "ETH/USD", "status": "Cancelled", "signal_gained_profit": "0"}
    ]
    generator = InsightGenerator()
    insights = generator.generate_insights(trades)
    for insight in insights:
        print(insight)