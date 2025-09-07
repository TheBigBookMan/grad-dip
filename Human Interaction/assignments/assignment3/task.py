import pandas as pd

from statsmodels.stats.anova import AnovaRM
import pingouin as pg
import researchpy

pd.set_option('display.max_columns', None) # display all columns

df = pd.read_excel('ExperimentData.xlsx')

pd_summary = researchpy.summary_cont(df.groupby(['CursorType'])['Time']).round(2).reset_index()

# print(pd_summary)

# Repeated measures ANOVA for Task Time
res_time = AnovaRM(
    data=df,
    depvar='Time',
    subject='Participant',
    within=['CursorType', 'TargetWidth', 'TargetDistance', 'DistractorNumber'],
    aggregate_func='mean'
)

print(res_time.fit())