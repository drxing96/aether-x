import time
import random

# Hypothetical aether-framework imports
from aether_framework.src.agents.ai_agent import AIAgent
from aether_framework.src.core.modular_agent import ModularAgent
from aether_framework.src.marketplace.agent_marketplace import AgentMarketplace
from aether_framework.src.democracy.proposal_manager import ProposalManager


class HierarchicalAgentPipeline:
    """
    Demonstrates a multi-stage approach to agent orchestration, where:
      1) AI and ModularAgents co-exist, each assigned specific roles.
      2) A marketplace is used to exchange tasks or resources among agents.
      3) A democracy-based proposal mechanism finalizes key decisions.
    """

    def __init__(self, num_modular_agents=3):
        # We'll store a single AIAgent as the 'coordinator'
        self.coordinator = AIAgent(agent_id="Coordinator-AI")

        # A set of modular agents, each simulating specialized capabilities
        self.modular_agents = [
            ModularAgent(agent_id=f"ModAgent-{i+1}") for i in range(num_modular_agents)
        ]

        # Marketplace to simulate agent-based transactions
        self.marketplace = AgentMarketplace()

        # A democracy-based manager for proposals
        self.proposal_manager = ProposalManager()

    def initialize_pipeline(self):
        """
        Prepares the AI coordinator, registers modular agents in the marketplace,
        and sets up an initial context for the pipeline flow.
        """
        print("\n[Pipeline] Initializing agent pipeline.")
        for mod_agent in self.modular_agents:
            self.marketplace.register_agent(mod_agent)
        print(f"[Pipeline] Registered {len(self.modular_agents)} agents in the marketplace.")

        # Simulate coordinator analyzing the environment
        analysis = self.coordinator.analyze_context("Initial pipeline setup.")
        print(f"[Coordinator Analysis] {analysis}")

    def run_proposal_phase(self):
        """
        Demonstrates the creation and voting process of proposals, 
        leveraging the democracy/ProposalManager.
        """
        proposal_text = "Should we enable advanced synergy optimization for all modular agents?"
        print(f"[Proposal] Creating new proposal: '{proposal_text}'")
        proposal_id = self.proposal_manager.create_proposal(proposal_text)

        # Simulate each modular agent 'voting' or 'commenting'
        for agent in self.modular_agents:
            vote = random.choice(["YES", "NO", "ABSTAIN"])
            self.proposal_manager.cast_vote(proposal_id, agent.agent_id, vote)
            time.sleep(0.3)

        # Check final result
        result = self.proposal_manager.finalize_proposal(proposal_id)
        print(f"[ProposalManager] Final result for proposal '{proposal_text}': {result}")

    def run_agent_exchange(self):
        """
        Demonstrates a scenario where each agent puts a 'service' or 'resource'
        in the marketplace, and we simulate a transaction or exchange among them.
        """
        print("[Marketplace] Agents listing resources.")
        for agent in self.modular_agents:
            resource = f"Resource-{random.randint(100, 999)}"
            self.marketplace.list_resource(agent.agent_id, resource)
            time.sleep(0.2)

        # Let the coordinator attempt to 'purchase' a resource from one agent
        chosen_agent = random.choice(self.modular_agents)
        resource_id = self.marketplace.find_random_resource(chosen_agent.agent_id)
        if resource_id:
            print(f"[Coordinator] Attempting to acquire {resource_id} from {chosen_agent.agent_id}.")
            self.marketplace.execute_transaction(
                buyer_id=self.coordinator.agent_id,
                seller_id=chosen_agent.agent_id,
                resource_id=resource_id
            )
        else:
            print("[Marketplace] No resource found for coordinator to acquire.")

    def finalize_pipeline_state(self):
        """
        Final summary or cleanup step, showing each agent's final state
        after the synergy, marketplace transactions, and proposals.
        """
        print("\n=== Final Pipeline State ===")
        print("[Coordinator State]:")
        print(f"   Agent ID: {self.coordinator.agent_id} | Internal Log: {self.coordinator.internal_log}")

        for mod_agent in self.modular_agents:
            print(f"[ModularAgent State] {mod_agent.agent_id} => {mod_agent.state}")

        print("============================\n")


def main():
    print("=== Hierarchical Agent Pipeline Demo ===")

    pipeline = HierarchicalAgentPipeline(num_modular_agents=4)
    pipeline.initialize_pipeline()
    time.sleep(1)

    pipeline.run_proposal_phase()
    time.sleep(1)

    pipeline.run_agent_exchange()
    time.sleep(1)

    pipeline.finalize_pipeline_state()

    print("=== Pipeline Execution Complete ===\n")

if __name__ == "__main__":
    main()