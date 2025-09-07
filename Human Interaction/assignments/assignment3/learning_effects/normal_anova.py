import pandas as pd
from statsmodels.stats.anova import AnovaRM

import pingouin as pg
import researchpy

df = pd.read_excel('./ExperimentData.xlsx', engine='openpyxl')


df_normal = df[df['CursorType'] == 'NormalCursor']

res_normal = AnovaRM(data=df_normal,
                     depvar='Time',
                     subject='Participant',
                     within=['Block'],
                     aggregate_func='mean')
print("Learning effect analysis for Normal Cursor")
print(res_normal.fit())

# # Post-hoc pairwise comparisons for Normal Cursor
post_hocs_normal = pg.pairwise_tests(dv='Time',
                                     within='Block',
                                     subject='Participant',
                                     padjust='bonf',
                                     data=df_normal)

print("\nPost-hoc comparisons (Normal Cursor)")
print(post_hocs_normal)