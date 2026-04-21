'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
'''
def ftaplots(charge_counts, charge_counts_by_offense):
    
    Produces various types of bar plots using the given datasets

    Parameters:
    - charge_counts dataframe
    - charge_counts_by_offense dataframe

    Returns:
    - Vertical barplot
    - Horizontal barplot
    - Vertical barplot with hue based on offense category
    '''
# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Extracts arrest data CSVs into dataframes
pred_universe = pd.read_csv('https://www.dropbox.com/scl/fi/a2tpqpvkdc8n6advvkpt7/universe_lab9.csv?rlkey=839vsc25njgfftzakr34w2070&dl=1')
arrest_events = pd.read_csv('https://www.dropbox.com/scl/fi/n47jt4va049gh2o4bysjm/arrest_events_lab9.csv?rlkey=u66usya2xjgf8gk2acq7afk7m&dl=1')

# Creates two additional dataframes using groupbys
charge_counts = arrest_events.groupby(['charge_degree']).size().reset_index(name='count')
charge_counts_by_offense = arrest_events.groupby(['charge_degree', 'offense_category']).size().reset_index(name='count')
# %%
# 1. Using the pre_universe data frame, create a bar plot for the fta column.

'''
Produces fta bar plot

Parameters:
- pred_universe dataframe

Returns:
- Vertical barplot
'''
sns.countplot(data=pred_universe, 
            x='fta',
            hue = 'sex')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/fta_barplot.png', bbox_inches='tight')

sns.countplot(data=pred_universe, 
            x='fta')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/fta_barplot.png', bbox_inches='tight')

# %%
sns.histplot(data=pred_universe, 
                x='age_at_arrest')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/age_at_arrest_histogram.png', bbox_inches='tight')

# %%
sns.histplot(data=pred_universe, 
                x='age_at_arrest', 
                bins=[18, 21, 30, 40, 100])
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/age_bins_histogram.png', bbox_inches='tight')

# %%
felony_charge = (
    arrest_events
    .groupby("arrest_id")
    .apply(lambda df: ((df["charge_degree"] == "felony").sum() > 0))
    .reset_index(name="has_felony_charge")
)
# %%
merged = pred_universe.merge(
    felony_charge,
    on="arrest_id",
    how="left"
)

# %%
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def cat_plots(merged_df):
    '''
    Produces different types of categorical plots using the given datasets

    Parameters:
    - charge_counts dataframe
    - pred_universe dateframe

    Returns:
    - Categorical bar plot for charge degree counts
    - Categorical bar plot for non-felony predictions by sex
    '''
sns.catplot(data=merged, 
            x='has_felony_charge',
            y='prediction_felony', 
            kind='bar')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part4_plots/felony_prediction.png', bbox_inches='tight')

sns.catplot(data=merged, 
            x='has_felony_charge',
            y='prediction_felony', 
            kind='bar',
            hue = 'y_felony')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part4_plots/nonfelony_prediction.png', bbox_inches='tight')

print('''
      Bar charts suggest that having any felony charge is associated with an 
      increased likelihood of rearrest for both felony and nonfelony charges. However, the difference in
      this relationship is much larger for felony rearrests, suggesting that there is an interaction effect
      between charge type at arrest and rearrest for felonies versus nonfelonies. 
''')



# %%
def scatterplot(pred_universe):
    '''
    Produces different types of scatter plots using the given dataset

    Parameters:
    - pred_universe dataframe

    Returns:
    - Scatterplot without a regression line
    - Scatterplot with a regression line
    - Scatterplot with a custom diagonal line
    - Scatterplot with hue by race
    - Scatterplot faceted by sex with hue by race
    '''
    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony',
               fit_reg=False)
    plt.savefig('./data/part2_plots/scatterplot1.png', bbox_inches='tight')

    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony')
    plt.savefig('./data/part2_plots/scatterplot2.png', bbox_inches='tight')

    sp = sns.lmplot(data=pred_universe, 
                    x='prediction_felony', 
                    y='prediction_nonfelony')
    sp.ax.axline(xy1=(0, 0), 
                 xy2=(1, 1),
                 color='g',
                 dashes=(2, 2))
    plt.savefig('./data/part2_plots/scatterplot3.png', bbox_inches='tight')

    sp = sns.lmplot(data=pred_universe, 
                    x='prediction_felony', 
                    y='prediction_nonfelony', 
                    hue='race')
    sp.ax.axline(xy1=(0, 0), 
                 xy2=(1, 1), 
                 color='b', 
                 dashes=(2, 2))
    plt.savefig('./data/part2_plots/scatterplot4.png', bbox_inches='tight')

    sp = sns.lmplot(data=pred_universe, 
                    x='prediction_felony', 
                    y='prediction_nonfelony', 
                    hue='race', 
                    col='sex')
    sp.axes[0][0].axline(xy1=(1, 1), 
                         slope=1, 
                         color='b', 
                         dashes=(2, 2))
    sp.axes[0][1].axline(xy1=(1, 1), 
                         slope=1, 
                         color='b', 
                         dashes=(2, 2))
    plt.savefig('./data/part2_plots/scatterplot5.png', bbox_inches='tight')

sns.lmplot(data=merged, 
           x='prediction_felony', 
           y='prediction_nonfelony',
           fit_reg=False,
           hue = 'has_felony_charge')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part5_plots/rearrest_predictions.png', bbox_inches='tight')

sns.lmplot(data=merged, 
        x='prediction_felony', 
        y='y_felony')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part5_plots/felony_rearrest_scatter.png', bbox_inches='tight')

sns.set_theme()
sns.set(rc={'figure.figsize':(6, 4)})

sns.countplot(data=pred_universe, 
        x='fta',
        hue = 'sex')
plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/fta_sex_barplot.png', bbox_inches='tight')
