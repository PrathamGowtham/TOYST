# 🧠MultiAgent orchestration for assissting in hardware verification

This repository hosts a modular multi-agent system built with [Langflow](https://github.com/langflow-ai/langflow) designed for interacting with Large Language Models (LLMs). It includes agents such as:

- GeneralQueryAgent – For general technical queries and explanations.
  GeneratorAgent – For generating code, testbenches, and other artifacts.
- AnalysisAgent – For log analysis, simulation result interpretation, and verification feedback.
- irectorAgent – Orchestrates the system, intelligently routing queries to the correct agent.

# 📁 Repository Structure


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langflow-multiagent-system.git
cd langflow-multiagent-system

Make sure you have Langflow installed. If not:
pip install langflow
langflow run
This will launch the Langflow interface in your browser at http://localhost:7860.

3. Load the Agents
Go to the Langflow UI.

Click File → Import Flow.

Upload the desired .json file from the agents/ directory (e.g., DirectorAgent.json).

Click Run.

You can also load all agents in parallel in different tabs or by chaining them in a unified flow.

4. Interact via Playground
Once your agent is running:

Click Playground in Langflow.

Type your query.

The agent will respond based on its capabilities (e.g., DirectorAgent will invoke the appropriate sub-agent and return its result).

🛠️ Customization
Each agent is configurable via Langflow’s visual interface. You can:

Modify prompts

Add custom tools and chains

Attach file context (e.g., using RAG)

📌 Notes
Ensure all required agents are accessible when loading DirectorAgent.json.

If deploying on a server, consider using persistent sessions and LangChain’s ToolCalling support.

Avoid naming collisions by using unique tool names even if reusing the same base component.

