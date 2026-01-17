import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

customers = pd.DataFrame({
    'customer_id': range(1, 13),
    'tenure_months': [1,3,12,24,36,2,6,48,60,8,15,np.nan],
    'monthly_charges': [70,80,65,90,100,75,60,110,120,55,85,95],
    'contract_type': ['Month-to-month','Month-to-month','One year','Two year',
                       'Two year','Month-to-month','One year','Two year',
                       'Two year','Month-to-month','One year','Month-to-month'],
    'support_calls': [5,4,1,0,0,6,2,0,0,3,1,4],
    'internet_service': ['Fiber','Fiber','DSL','Fiber','Fiber',
                          'DSL','DSL','Fiber','Fiber','DSL','Fiber','DSL'],
    'churn': ['Yes','Yes','No','No','No','Yes','No','No','No','Yes','No','Yes']
})
sns.boxplot(data=movies, x="genre", y="rating")
plt.show()
