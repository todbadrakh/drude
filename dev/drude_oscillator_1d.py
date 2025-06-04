# Drude oscillator class
# Tuguldur T. Odbadrakh
# 06/02/2025

# Imports
import numpy as np
import math

# Class
class DrudeOscillator:
  """
  A class representing a Drude oscillator.
  Attributes:
    mass (float): Mass of the oscillator in atomic units.
    charge (float): Charge of the oscillator in atomic units.
    frequency (float): Frequency of the oscillator.
    position (np.ndarray): Position of the oscillator in space.
    state (int): State of the oscillator, default is 0.
  
  """

  def __init__(self, mass, charge, frequency, position, state=0):
    self.m = mass
    self.q = charge
    self.w = frequency
    self.position = np.array(position, dtype=float)
    self.state = state

  def update_position(self, displacement):
    self.position += np.array(displacement)

  def set_state(self, new_state):
    self.state = new_state

  def wavefunction(self, position, state=None):
    from numpy.polynomial.hermite import hermval
    if state is None:
        state = self.state
    norm = ((self.m * self.w ) / math.pi)**0.25
    coeff = 1 / math.sqrt(2**state * math.factorial(state))
    xi = math.sqrt(self.m * self.w) * (position - self.position)
    herm = hermval(xi, [0]*state + [1])  # This gives H_state(xi)
    exponential = np.exp(-self.m * self.w * (position - self.position)**2 / 2)
    return norm * coeff * herm * exponential
  
  def plot_wavefunction(self, x_range=(-10, 10), num_points=1000, state=None, filename="drude_wavefunction.pdf"):
        """
        Plot and save the wavefunction as a PDF.
        """
        from matplotlib import pyplot as plt
        
        if state is None:
            state = self.state
        x = np.linspace(x_range[0], x_range[1], num_points)
        psi = [self.wavefunction(np.array([xi]), state=state) for xi in x]
        plt.plot(x, psi)
        plt.xlabel("Position")
        plt.ylabel("Wavefunction")
        plt.title(f"Drude Oscillator Wavefunction (state={state})")
        plt.grid(True)
        plt.savefig(filename)
        plt.close()