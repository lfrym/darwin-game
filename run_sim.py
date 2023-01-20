import pandas as pd
import numpy as np

import utils
import policies

def main():
    nrounds = 50
    nturns = 85
    all_pols = {
        "always_2": policies.AlwaysN(n=2),
        "always_3": policies.AlwaysN(n=3),
        "random": policies.RandomInRange(),
        "copycat": policies.Copycat(),
        "titfortat": policies.TitForTat()
    }
    gp = utils.GenePool(all_pols, nturns)
    for _ in range(nrounds):
        policy_points = gp.run_round()
        gp.update_policies(policy_points)
        print(policy_points)

if __name__ == "__main__":
    main()