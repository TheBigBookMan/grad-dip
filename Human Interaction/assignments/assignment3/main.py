import pandas as pd
from statsmodels.stats.anova import AnovaRM

import pingouin as pg
import researchpy

df = pd.read_excel('ExperimentData.xlsx', engine='openpyxl')

# Statistical summary
# -------------------------
# pd.set_option('display.max_columns', None)


# # Summary stats: mean, SD, SE, CI for Time grouped by CursorType and Block
# pd_summary = researchpy.summary_cont(
#     df.groupby(['CursorType', 'Block'])['Time']
# ).round(2).reset_index()

# print(pd_summary)


# -------------------------
# Normal Cursor
# -------------------------
# df_normal = df[df['CursorType'] == 'NormalCursor']

# res_normal = AnovaRM(data=df_normal,
#                      depvar='Time',
#                      subject='Participant',
#                      within=['Block'],
#                      aggregate_func='mean')
# print("Learning effect analysis for Normal Cursor")
# print(res_normal.fit())


# # Post-hoc pairwise comparisons for Normal Cursor
# post_hocs_normal = pg.pairwise_tests(dv='Time',
#                                      within='Block',
#                                      subject='Participant',
#                                      padjust='bonf',
#                                      data=df_normal)

# print("\nPost-hoc comparisons (Normal Cursor)")
# print(post_hocs_normal)

# -------------------------
# Buubkle Cursor
# -------------------------
df_bubble = df[df['CursorType'] == 'BubbleCursor']

# res_bubble = AnovaRM(data=df_bubble,
#                      depvar='Time',
#                      subject='Participant',
#                      within=['Block'],
#                      aggregate_func='mean')
# print("Learning effect analysis for Bubble Cursor")
# print(res_bubble.fit())


# # Post-hoc pairwise comparisons for Bubble Cursor
post_hocs_bubble = pg.pairwise_tests(dv='Time',
                                     within='Block',
                                     subject='Participant',
                                     padjust='bonf',
                                     data=df_bubble)

print("\nPost-hoc comparisons (Bubble Cursor)")
print(post_hocs_bubble)