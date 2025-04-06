import langflow
import os
from pathlib import Path

# Load the flow automatically
def preload_flow():
    flow_path = "my_Latest_6_4_25.json"  # change this if you renamed it
    flow_name = "AutoLoadedFlow"

    from langflow.utils.utils import import_flow

    # Check if already imported to avoid duplicates
    flows_dir = Path("langflow_data/flows")
    flows_dir.mkdir(parents=True, exist_ok=True)
    target_path = flows_dir / f"{flow_name}.json"

    if not target_path.exists():
        # Copy flow into Langflow's storage
        import shutil
        shutil.copy(flow_path, target_path)
        print(f"Imported flow: {flow_name}")

# Start Langflow with preloaded flow
if __name__ == "__main__":
    preload_flow()
    langflow.run()
