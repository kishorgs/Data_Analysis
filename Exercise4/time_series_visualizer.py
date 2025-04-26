import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import data and set index
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean the data: filter out top 2.5% and bottom 2.5% of page views
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Create a copy of the DataFrame
    df_line = df.copy()
    
    # Create the line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_line.index, df_line['value'], color='red')
    
    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save and return the figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Create a copy of the DataFrame
    df_bar = df.copy()
    
    # Extract year and month from index
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Group by year and month, calculate mean page views
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Reorder months for proper display (Jan to Dec)
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped[months_order]
    
    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 5))
    df_grouped.plot(kind='bar', ax=ax)
    
    # Set title and labels
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    
    # Save and return the figure
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Create a copy of the DataFrame
    df_box = df.copy()
    
    # Extract year and month for box plots
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')  # Short month names (Jan, Feb, etc.)
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Year-wise box plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    # Month-wise box plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2,
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Save and return the figure
    fig.savefig('box_plot.png')
    return fig

# For testing in main.py
if __name__ == "__main__":
    line_fig = draw_line_plot()
    bar_fig = draw_bar_plot()
    box_fig = draw_box_plot()