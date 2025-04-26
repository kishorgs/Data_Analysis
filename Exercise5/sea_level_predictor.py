import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data from epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot: Year vs CSIRO Adjusted Sea Level
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # 3. Line of best fit for all data (1880 to latest year)
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = range(df['Year'].min(), 2051)  # Extend to 2050
    y_all = slope_all * x_all + intercept_all
    ax.plot(x_all, y_all, color='red', label='Fit (1880-latest)')

    # 4. Line of best fit for data from 2000 to latest year
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = range(2000, 2051)  # From 2000 to 2050
    y_recent = slope_recent * x_recent + intercept_recent
    ax.plot(x_recent, y_recent, color='green', label='Fit (2000-latest)')

    # 5. Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return the figure
    fig.savefig('sea_level_plot.png')
    return fig

# For testing in main.py
if __name__ == "__main__":
    draw_plot()