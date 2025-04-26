import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def draw_cat_plot():
    df = pd.read_csv('medical_examination.csv')

    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
    df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        value_name='value'
    )

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar',
        data=df_cat
    ).fig

    return fig

def draw_heat_map():
    df_heat = pd.read_csv('medical_examination.csv')

    df_heat = df_heat[
        (df_heat['ap_lo'] <= df_heat['ap_hi']) &
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
        (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
        (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        square=True,
        cmap='coolwarm',
        vmin=-1,
        vmax=1,
        center=0,
        ax=ax
    )

    return fig

if __name__ == "__main__":
    cat_fig = draw_cat_plot()
    cat_fig.savefig('catplot.png')
    heat_fig = draw_heat_map()
    heat_fig.savefig('heatmap.png')