import numpy as np
import pandas as pd

# Generate synthetic dataset
np.random.seed(42)
n_samples = 10000  # adjust for more/less

data = {
    'Time': np.random.randint(0, 100000, size=n_samples),
    'V1': np.random.normal(0, 1, n_samples),
    'V2': np.random.normal(0, 1, n_samples),
    'V3': np.random.normal(0, 1, n_samples),
    'V4': np.random.normal(0, 1, n_samples),
    'V5': np.random.normal(0, 1, n_samples),
    'V6': np.random.normal(0, 1, n_samples),
    'V7': np.random.normal(0, 1, n_samples),
    'V8': np.random.normal(0, 1, n_samples),
    'V9': np.random.normal(0, 1, n_samples),
    'V10': np.random.normal(0, 1, n_samples),
    'V11': np.random.normal(0, 1, n_samples),
    'V12': np.random.normal(0, 1, n_samples),
    'V13': np.random.normal(0, 1, n_samples),
    'V14': np.random.normal(0, 1, n_samples),
    'V15': np.random.normal(0, 1, n_samples),
    'V16': np.random.normal(0, 1, n_samples),
    'V17': np.random.normal(0, 1, n_samples),
    'V18': np.random.normal(0, 1, n_samples),
    'V19': np.random.normal(0, 1, n_samples),
    'V20': np.random.normal(0, 1, n_samples),
    'V21': np.random.normal(0, 1, n_samples),
    'V22': np.random.normal(0, 1, n_samples),
    'V23': np.random.normal(0, 1, n_samples),
    'V24': np.random.normal(0, 1, n_samples),
    'V25': np.random.normal(0, 1, n_samples),
    'V26': np.random.normal(0, 1, n_samples),
    'V27': np.random.normal(0, 1, n_samples),
    'V28': np.random.normal(0, 1, n_samples),
    'Amount': np.random.uniform(1, 1000, n_samples),
    'Class': np.random.choice([0, 1], size=n_samples, p=[0.985, 0.015])
}

df = pd.DataFrame(data)
df.to_csv("large_transaction_log.csv", index=False)
print("✅ Saved large_transaction_log.csv")
