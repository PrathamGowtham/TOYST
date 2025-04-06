import langflow
from pathlib import Path
import shutil

def preload_flow():
    # Your exported flow
    source_flow = "my_Latest_6_4_25.json"
    flow_name = "MyAutoFlow"

    # Target location where Langflow looks for saved flows
    flows_dir = Path("langflow_data/flows")
    flows_dir.mkdir(parents=True, exist_ok=True)
    target_path = flows_dir / f"{flow_name}.json"

    # Copy flow if it doesn't already exist
    if not target_path.exists():
        shutil.copy(source_flow, target_path)
        print(f"Flow imported as: {flow_name}")

if __name__ == "__main__":
    preload_flow()
    langflow.run()
