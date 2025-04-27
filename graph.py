import matplotlib.pyplot as plt
import numpy as np

# Timings Data for SQ, NQ, MQ (in ms)
timings_data = {
    "Small Sample": {"SQ": 0.06, "NQ": 0.02, "MQ": 0.02},
    "Medium Sample": {"SQ": 0.08, "NQ": 0.08, "MQ": 0.09},
    "Large Sample": {"SQ": 1.68, "NQ": 0.38, "MQ": 1.07}
}

# Prepare the data for plotting
samples = list(timings_data.keys())
sq_times = [timings_data[sample]["SQ"] for sample in samples]
nq_times = [timings_data[sample]["NQ"] for sample in samples]
mq_times = [timings_data[sample]["MQ"] for sample in samples]

# Plot Timings Comparison (SQ, NQ, MQ)
x = np.arange(len(samples))  # The position of bars
width = 0.2  # Bar width

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width, sq_times, width, label="SQ")
ax.bar(x, nq_times, width, label="NQ")
ax.bar(x + width, mq_times, width, label="MQ")

ax.set_xlabel('Sample Size')
ax.set_ylabel('Time (ms)')
ax.set_title('Timings Comparison (SQ, NQ, MQ)')
ax.set_xticks(x)
ax.set_xticklabels(samples)
ax.legend()

# Save the chart to a file
plt.tight_layout()
plt.savefig('timings_comparison.png')
plt.show()

# Data for Min-Transfers results (example)
min_transfers_data = {
    "Source 1 (Small)": {6: 0},
    "Source 1 (Medium)": {6: 0, 8: 1, 1: 1, 5: 1},
    "Source 1 (Large)": {10: 0, 6: 0, 4: 0, 9: 0, 5: 0, 2: 0, 7: 0, 8: 0, 3: 0, 1: 0},
    "Source 2 (Small)": {3: 0, 9: 1},
    "Source 2 (Medium)": {7: 0, 3: 0, 9: 0, 6: 0, 2: 1, 5: 1, 8: 1, 1: 1, 4: 1, 10: 2},
    "Source 2 (Large)": {4: 0, 1: 0, 5: 0, 3: 0, 7: 0, 10: 0, 8: 0, 9: 0, 6: 0, 2: 0},
    "Source 4 (Small)": {},
    "Source 4 (Medium)": {9: 0, 10: 0, 7: 0, 1: 0, 8: 0, 6: 1, 4: 1, 2: 1, 5: 1, 3: 1},
    "Source 4 (Large)": {6: 0, 10: 0, 5: 0, 2: 0, 3: 0, 8: 0, 7: 0, 9: 0, 1: 0, 4: 0}
}

# Example: Min-Transfers bar chart for Source 1 across different sample sizes
sources = ["Source 1 (Small)", "Source 1 (Medium)", "Source 1 (Large)"]
transfers = [list(min_transfers_data[source].values())[0] for source in sources]

# Plot Min-Transfers results
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(sources, transfers, color='skyblue')

ax.set_xlabel('Source')
ax.set_ylabel('Transfers')
ax.set_title('Min-Transfers for Source 1 Across Samples')

# Save the chart to a file
plt.tight_layout()
plt.savefig('min_transfers_source_1.png')
plt.show()
