import numpy as np
import mogp_emulator

theta_design = mogp_emulator.LatinHypercubeDesign([(-np.pi/30, np.pi/30), (-np.pi/30, np.pi/30), (-np.pi/30, np.pi/30)])

n_simulations = 100
simulation_points = theta_design.sample(n_simulations)
simulation_output = np.array([simulator(p) for p in simulation_points])
