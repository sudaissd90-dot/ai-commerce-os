from workflow_manager import workflow_manager


# Auto Listing Workflow Registration

workflow_manager.register_workflow(
    "auto_listing_workflow",
    [
        "listing_agent"
    ]
)