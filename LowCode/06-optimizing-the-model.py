#
#
#   The book example, page 172, shows a line graph just by using the optimize_threshold() method,
#       this did not show a graph for me.
#
#   I asked google ai mode for help and after the other inline matplotlib and plot_method failed
#       to show up any graph like the one shown in the book, google provided the code below.
#       Only modified with adding my jupyter notebook variables pcc on lines 22/23 and best on line 27
#
#   This provides me with a similar graph that is show in the book.
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score, roc_auc_score, recall_score, 
    precision_score, f1_score, cohen_kappa_score, matthews_corrcoef
)

# 1. Extract test features and true target labels from the active experiment
X_test = pcc.get_config('X_test')
y_test = pcc.get_config('y_test')

# 2. Predict raw probability arrays for Logistic Regression (class 1)
# (Adjust 'best_lr_model' to match your actual variable name)
probabilities = best.predict_proba(X_test)[:, 1]

# 3. Compute the unchanging AUC score for reference
auc_score = roc_auc_score(y_test, probabilities)

# 4. Cycle through thresholds from 0.0 up to 1.0 to compute cutoff metrics
thresholds = np.linspace(0, 1, 100)
metrics_data = []

for t in thresholds:
    preds = (probabilities >= t).astype(int)
    metrics_data.append({
        'Threshold': t,
        'Accuracy': accuracy_score(y_test, preds),
        'Recall': recall_score(y_test, preds, zero_division=0),
        'Precision': precision_score(y_test, preds, zero_division=0),
        'F1-Score': f1_score(y_test, preds, zero_division=0),
        'Kappa': cohen_kappa_score(y_test, preds),
        'MCC': matthews_corrcoef(y_test, preds)
    })

df_metrics = pd.DataFrame(metrics_data)

# 5. Build and render the multi-metric optimization graph
plt.figure(figsize=(12, 7))

# Plot the threshold-dependent curves
plt.plot(df_metrics['Threshold'], df_metrics['Accuracy'], label='Accuracy', color='#1f77b4', linewidth=2)
plt.plot(df_metrics['Threshold'], df_metrics['Precision'], label='Precision', color='#2ca02c', linewidth=2)
plt.plot(df_metrics['Threshold'], df_metrics['Recall'], label='Recall', color='#ff7f0e', linewidth=2)
plt.plot(df_metrics['Threshold'], df_metrics['F1-Score'], label='F1-Score', color='#d62728', linestyle='--', linewidth=2)
plt.plot(df_metrics['Threshold'], df_metrics['Kappa'], label='Kappa (Cohen)', color='#9467bd', linestyle='-.')
plt.plot(df_metrics['Threshold'], df_metrics['MCC'], label='MCC', color='#17becf', linestyle=':')

# Draw AUC as a static horizontal reference line
plt.axhline(y=auc_score, color='#7f7f7f', linestyle='-', alpha=0.5, label=f'AUC Baseline ({auc_score:.3f})')

# Find and pinpoint the optimal threshold (using MCC as an example of a balanced metric)
best_mcc_idx = df_metrics['MCC'].idxmax()
best_thresh = df_metrics.loc[best_mcc_idx, 'Threshold']
plt.axvline(x=best_thresh, color='#8c564b', linestyle='-', alpha=0.7, 
            label=f'Optimal MCC Threshold ({best_thresh:.2f})')

# Graph aesthetics
plt.title('Logistic Regression Full Metric Threshold Optimization', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Probability Threshold', fontsize=12)
plt.ylabel('Metric Score', fontsize=12)
plt.xlim(0, 1)
plt.ylim(-0.1, 1.05) # Lower bound accommodates negative MCC/Kappa if they occur
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=4, frameon=True)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

