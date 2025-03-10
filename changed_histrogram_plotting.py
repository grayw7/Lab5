import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Adjust
df = pd.read_csv('/Users/willgray/Desktop/McGill/Winter 2025/Phys-258/Lab 5/5Hz_data.csv')

trials = {}
for col in df.columns:
    
    if col.startswith('Time (s)'):
        trial_name = col.split('Time (s) ')[1].strip()
        trials[trial_name] = {'time_col': col, 'counts_col': None}
    
    elif col.startswith('Geiger Counts (counts/sample)'):
        trial_name = col.split('Geiger Counts (counts/sample) ')[1].strip()
        if trial_name in trials:
            trials[trial_name]['counts_col'] = col
        else:
            trials[trial_name] = {'time_col': None, 'counts_col': col}


for trial_name in trials:
    trial = trials[trial_name]
    if not trial['counts_col']:
        print(f"Skipping {trial_name} (missing counts column)")
        continue
    
    counts_data = df[trial['counts_col']].dropna()
    

    max_val = counts_data.max()
    bins = np.arange(0, np.ceil(max_val) + 3, 1)
    
    plt.figure(figsize=(8, 4))
    plt.hist(
        counts_data,
        bins=bins,
        alpha=0.7,
        color='skyblue',
        edgecolor="navy",
        density=False
    )
    
    plt.xticks(
        bins[:-1] + 0.5,
        [str(int(x)) for x in bins[:-1]]
    )
    
    plt.xlabel("Counts per Time Interval")
    plt.ylabel("Frequency")
    plt.title(f"Counts for {trial_name}")
    plt.grid(axis='y', linestyle='--')
    plt.xlim(left=0)
    plt.tight_layout()
    plt.show()
