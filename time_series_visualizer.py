import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    return df

# Line plot
def draw_line_plot(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='tab:red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# Bar plot
def draw_bar_plot(df):
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    fig.savefig('bar_plot.png')
    return fig

# Box plot
def draw_box_plot(df):
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig

# Main script to run the functions
if __name__ == "__main__":
    df = load_and_clean_data('fcc-forum-pageviews.csv')
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)
