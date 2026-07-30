from ai_agent_manager import ai_agent_manager
from product_analysis_agent import product_analysis_agent


ai_agent_manager.register_agent(
    "product_analysis_agent",
    product_analysis_agent
)