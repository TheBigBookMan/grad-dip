import researchpy
import pandas as pd

df = pd.read_excel('./ExperimentData.xlsx')


pd_summary_error = researchpy.summary_cont(
    df.groupby(['CursorType'])['Error']
).round(2).reset_index()

print(pd_summary_error)

from statsmodels.stats.anova import AnovaRM


res_error = AnovaRM(
    data=df,
    depvar='Error',
    subject='Participant',
    within=['CursorType', 'TargetWidth', 'TargetDistance', 'DistractorNumber'],
    aggregate_func='mean'
)

print(res_error.fit())

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

ax = sns.pointplot(
    data=df,
    x='CursorType',
    y='Error',
    hue='TargetWidth',
    dodge=True,
    capsize=.1,
    err_kws={'linewidth': 1},
    palette='colorblind'
)

plt.title("Interaction Effect: Cursor Type × Target Width (Errors)")
plt.ylabel("Mean Error Rate")
plt.show()