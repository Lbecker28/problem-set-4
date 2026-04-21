'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def rearrest_predictions(merged):
    plt.close('all') 
    sns.lmplot(data=merged, 
            x='prediction_felony', 
            y='prediction_nonfelony',
            fit_reg=False,
            hue = 'has_felony_charge')
    plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part5_plots/rearrest_predictions_scatter.png', bbox_inches='tight')

    # In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
    print('''
        What can you say about the group of dots on the right side of the plot?
        Individuals who were arrested on any felony charge generally have a higher predicted likelihood for 
        both felony and nonfelony rearrests, though this relationship is more apparent for predicted felony 
        rearrests.
    ''')

    # 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def felony_rearrest_predictions(merged):
    plt.close('all') 
    sns.lmplot(data=merged, 
            x='prediction_felony', 
            y='y_felony',
            fit_reg=False)
    plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part5_plots/felony_rearrest_scatter.png', bbox_inches='tight')
    # In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
    print('''
        Would you say based off of this plot if the model is calibrated or not?
        I don't think that this plot is a great way to identify model calibration, because it's 
        plotting all observations of a binary outcome across all predicted probabilities, but if I 
        had to assess calibration just based on this plot, I would say that the model is not well-calibrated.
        There does seem to be a small bit of clustering in the lower predicted felony rearrest range for actual 
        non-felony rearrests, but only slightly. 
    ''')