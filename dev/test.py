import numpy as np
import matplotlib.pyplot as plt
from drude_oscillator_1d import DrudeOscillator

oscillator = DrudeOscillator(mass=1.0, charge=1.0, frequency=1.0, position=[0.0])
oscillator.plot_wavefunction(x_range=(-5, 5), num_points=1000, state=1, filename="drude_wavefunction.pdf")