import pandas as pd

from statsmodels.stats.anova import AnovaRM
import pingouin as pg
import researchpy

pd.set_option('display.max_columns', None)

df = pd.read_excel('./ExperimentData.xlsx')

pd_summary = researchpy.summary_cont(df.groupby(['CursorType'])['Time']).round(2).reset_index()

print(pd_summary)


res_time = AnovaRM(
    data=df,
    depvar='Time',
    subject='Participant',
    within=['CursorType', 'TargetWidth', 'TargetDistance', 'DistractorNumber'],
    aggregate_func='mean'
)

print(res_time.fit())

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
df = pd.read_excel('ExperimentData.xlsx')
ax = sns.pointplot(
    data=df,
    x='CursorType',
    y='Time',
    hue='TargetWidth',
    dodge=True,
    capsize=.1,
    err_kws={'linewidth': 1},
    palette='colorblind'
)

plt.title("Interaction Effect: Cursor Type × Target Width")
plt.ylabel("Mean Task Time (ms)")
plt.show()