import pandas as pd
from statsmodels.stats.anova import AnovaRM

import pingouin as pg
import researchpy

df = pd.read_excel('./ExperimentData.xlsx', engine='openpyxl')

pd.set_option('display.max_columns', None)


pd_summary = researchpy.summary_cont(
    df.groupby(['CursorType', 'Block'])['Time']
).round(2).reset_index()

print(pd_summary)