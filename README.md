# darwin-game

Quick implementation of the Darwin Game.

`run_sim.py` runs the simulation. To add new policies, create a class in `policies.py` with the following properties and methods:
- `__init__()` should assign a `self.type` for naming purposes
- All policies require a `get_action()` method, which can only take `self` as an input, and must return an int between 0 and 5.
- All policies require a `give_result()` method, which takes `self` and `opponent_action` as input. This should not return any output.

Once the policy class has been defined, add a new entry to the `all_pols` dictionary in `run_sim.py`, with a key equal to `self.type` and value equal to an instance of the class.
