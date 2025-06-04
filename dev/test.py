import numpy as np
import matplotlib.pyplot as plt
from drude_oscillator import DrudeOscillator

if __name__ == "__main__":
    t1 = DrudeOscillator(mass=1.0, charge=1.0, frequency=1.0, position=[0.0], state=3)
    x = np.linspace(-10, 10, 1000)
    psi = [t1.wavefunction(np.array([xi])) for xi in x]  # Fixed: use psi, pass xi correctly
    plt.plot(x, psi)
    plt.xlabel("Position")
    plt.ylabel("Wavefunction")
    plt.title("Drude Oscillator Wavefunction (state=0)")
    plt.grid(True)
    plt.savefig("drude_wavefunction.pdf")  # Save as PDF
    plt.close()