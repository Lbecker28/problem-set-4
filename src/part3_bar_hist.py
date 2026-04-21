'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def fta_barplot(pred_universe):
    '''
    Produces fta bar plot

    Parameters:
    - pred_universe dataframe

    Returns:
    - Vertical barplot
    '''
    plt.close('all') 
    sns.countplot(data=pred_universe, 
                x='fta')
    plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/fta_barplot.png', bbox_inches='tight')

# 2. Hue the previous barplot by sex
def fta_sex_barplot(pred_universe):
    '''
    Produces fta bar plot by sex

    Parameters:
    - pred_universe dataframe

    Returns:
    - Vertical barplot
    '''
    plt.close('all') 
    sns.countplot(data=pred_universe, 
            x='fta',
            hue = 'sex')
    plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/fta_sex_barplot.png', bbox_inches='tight')


# 3. Plot a histogram of age_at_arrest
def age_at_arrest_histogram(pred_universe):
    '''
    Produces histogram of age at arrest

    Parameters:
    - pred_universe dataframe

    Returns:
    - histogram
    '''
    plt.close('all') 
    sns.histplot(data=pred_universe, 
                    x='age_at_arrest')
    plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/age_at_arrest_histogram.png', bbox_inches='tight')

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def age_bins_histogram(pred_universe):
    plt.close('all') 
    sns.histplot(data=pred_universe, 
                    x='age_at_arrest', 
                    bins=[18, 21, 30, 40, 100])
    plt.savefig('/Users/Admin/Documents/Data Science/problem-set-4/data/part3_plots/age_bins_histogram.png', bbox_inches='tight')