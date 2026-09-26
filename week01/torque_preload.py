"""Week 1: first data plot.

Simulates a torque-preload tightening test using the short-form torque
equation T = K * F * d, adds measurement noise, then fits K back from the
"measured" data. Later, swap the simulated data for a real CSV from the thesis.
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=0)

# Test setup (M12 bolt, nut factor from the thesis)
d = 0.012            # nominal bolt diameter [m]
K_true = 0.24        # nut factor [-]

# "Experiment": 7 torque steps, 5 repeats each
torque = np.repeat(np.arange(30, 100, 10), 5).astype(float)       # [N*m]
preload = torque / (K_true * d)                                    # [N]
preload_measured = preload + rng.normal(0, 300, size=preload.size) # load cell noise

# Fit K by least squares through the origin: F = (1 / (K d)) * T
slope = np.sum(torque * preload_measured) / np.sum(torque**2)
K_fit = 1 / (slope * d)
print(f"True K = {K_true:.3f}, fitted K = {K_fit:.3f}")

# Plot
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.scatter(torque, preload_measured / 1000, alpha=0.6, label="measured (simulated)")
t_line = np.linspace(0, 100, 50)
ax.plot(t_line, slope * t_line / 1000, "r-", label=f"fit: K = {K_fit:.3f}")
ax.set_xlabel("Tightening torque [N·m]")
ax.set_ylabel("Clamping force [kN]")
ax.set_title("Torque vs. preload")
ax.grid(alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig("week01/torque_preload.png", dpi=150)
print("Saved week01/torque_preload.png")
