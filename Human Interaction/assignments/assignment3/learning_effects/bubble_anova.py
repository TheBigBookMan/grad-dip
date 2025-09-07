import pandas as pd
from statsmodels.stats.anova import AnovaRM

import pingouin as pg
import researchpy

df = pd.read_excel('./ExperimentData.xlsx', engine='openpyxl')

df_bubble = df[df['CursorType'] == 'BubbleCursor']

res_bubble = AnovaRM(data=df_bubble,
                     depvar='Time',
                     subject='Participant',
                     within=['Block'],
                     aggregate_func='mean')
print("Learning effect analysis for Bubble Cursor")
print(res_bubble.fit())


# # Post-hoc pairwise comparisons for Bubble Cursor
post_hocs_bubble = pg.pairwise_tests(dv='Time',
                                     within='Block',
                                     subject='Participant',
                                     padjust='bonf',
                                     data=df_bubble)

print("\nPost-hoc comparisons (Bubble Cursor)")
print(post_hocs_bubble)