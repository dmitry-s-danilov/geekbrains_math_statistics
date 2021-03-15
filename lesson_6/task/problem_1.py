import numpy as np
import pandas as pd
from problem_1_lib import covariance, correlation_coefficient

# Set data.
x = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
y = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]

# Find covariances and correlations.
x = np.array(x)
y = np.array(y)
results = {
    'x-variance': [
        covariance(x, x),
        np.cov(x, bias=True),
        pd.DataFrame({'x': x, 'y': y}).cov(ddof=0).loc['x', 'x']
    ],

    'y-variance': [
        covariance(y, y),
        np.cov(y, bias=True),
        pd.DataFrame({'x': x, 'y': y}).cov(ddof=0).loc['y', 'y']
    ],
            
    'xy-covariance': [
        covariance(x, y),
        np.cov(x, y, bias=True)[0, 1],
        pd.DataFrame({'x': x, 'y': y}).cov(ddof=0).loc['x', 'y']
    ],
    
    'xy-correlation': [
        correlation_coefficient(x, y),
        np.corrcoef(x, y)[0, 1],
        pd.DataFrame({'x': x, 'y': y}).corr().loc['x', 'y']        
    ]
}

# Сheck the equality of results with the selected precision.
precision = 6
checks = {
    key: all([round(_ - value[0], precision) == 0 for _ in value[1:]])
    for key, value in results.items()
}

# Print results and checks.
for key in results:
    print(f'{key}: {results[key][0]:.6} {checks[key]}')
