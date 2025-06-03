# Drude oscillator class
# Tuguldur T. Odbadrakh
# 06/02/2025

# Imports
import numpy as np

# Class
class DrudeOscillator:

  def __init__(self, position, state=0):
    self.position = np.array(position, dtype=float)
    self.state = state

  def update_position(self, displacement):
    self.position += np.array(displacement)

  def set_state(self, new_state):
    self.state = new_state

  def __repr__(self):
    return f"DrudeOscillator(position={self.position.tolist()}, state={self.state})
