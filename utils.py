import random

class GenePool():
    def __init__(self, policies:dict, nturns:int) -> None:
        self.policies = policies
        self.policy_types = list(policies.keys())
        # create a list of policies where each type of policy is repeated 100 times
        self.genetic_pool = [policies[policy_type] for policy_type in policies for _ in range(100)]
        self.nturns = nturns

    def update_policies(self, policy_points:dict):
        # Create a list of policies where each type of policy is repeated according to the points it earned in the last round
        # Total number of policies in the gene pool is 100 times the number of policies
        self.genetic_pool = [self.policies[ptype] for ptype in self.policies for _ in range(int(policy_points[ptype]*100*len(policy_points)))]

        # If any policy type has no remaining policies, remove them for indexical purposes
        for policy_type in self.policy_types:
            if self.genetic_pool.count(self.policies[policy_type]) == 0:
                self.policy_types.remove(policy_type)
                self.policies.pop(policy_type)

    # Function to run a single turn of a matchup
    def run_turn(self, policy1, policy2):

        # Get actions from each policy
        actions = [policy1.get_action(), policy2.get_action()]

        # Update history for each policy
        policy1.get_result(actions[1])
        policy2.get_result(actions[0])

        # Return payoffs
        return actions if sum(actions) < 5 else [0, 0]

    # Get random pairwise matchups without replacement
    def assign_matchups(self):
        matchups = []
        remaining_policies = self.genetic_pool.copy()
        while len(remaining_policies) > 1:
            policy1 = random.choice(remaining_policies)
            remaining_policies.remove(policy1)
            policy2 = random.choice(remaining_policies)
            remaining_policies.remove(policy2)
            matchups.append({"p1":policy1, "p1_type":policy1.type, "p2":policy2, "p2_type":policy2.type})
        return matchups

    # Function to run the current round of the tournament
    def run_round(self):
        matchups = self.assign_matchups()
        outcomes = {}
        for _ in range(self.nturns):
            for matchup in matchups:
                # Run a single turn
                turn_outcomes = self.run_turn(matchup["p1"], matchup["p2"])
                # Add turn outcomes to policy outcomes
                for j in range(2):
                    outcomes[matchup["p{}_type".format(j+1)]] = outcomes.get(matchup["p{}_type".format(j+1)], []) + [turn_outcomes[j]]
        
        # Calculate total points for each policy
        points = {policy_type:sum(outcomes[policy_type]) for policy_type in outcomes}

        # Return policy points as a share of total points
        return {policy_type:points[policy_type]/sum(points.values()) for policy_type in points}
        