"""Core Skills Drill — Descriptive Analytics

Compute summary statistics, plot distributions, and create a correlation
heatmap for the sample sales dataset.

Usage:
    python drill_eda.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("output", exist_ok=True)

def compute_summary(df):
    """Compute summary statistics for all numeric columns.

    Args:
        df: pandas DataFrame with at least some numeric columns

    Returns:
        DataFrame containing count, mean, median, std, min, max
        for each numeric column. Save the result to output/summary.csv.
    """
    # TODO: Compute descriptive statistics (count, mean, median, std, min, max)
    #       for all numeric columns and save to output/summary.csv
    numeric_df = df.select_dtypes(include='number')
    summary = numeric_df.agg(['count', 'mean', 'median', 'std', 'min', 'max'])

    # Save to CSV
    summary.to_csv("output/summary.csv")
    return summary


def plot_distributions(df, columns, output_path):
    """Create a 2x2 subplot figure with histograms for the specified columns.

    Args:
        df: pandas DataFrame
        columns: list of 4 column names to plot (use numeric columns)
        output_path: file path to save the figure (e.g., 'output/distributions.png')

    Returns:
        None — saves the figure to output_path
    """
    # TODO: Create a 2x2 figure with sns.histplot (KDE overlay) for each column
    #       Add titles, labels, and tight layout before saving
    plt.figure(figsize=(12, 10))

    for i, col in enumerate(columns, 1):
        plt.subplot(2, 2, i)
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_correlation(df, output_path):
    """Compute Pearson correlation matrix and visualize as a heatmap.

    Args:
        df: pandas DataFrame with numeric columns
        output_path: file path to save the figure (e.g., 'output/correlation.png')

    Returns:
        None — saves the figure to output_path
    """
    # TODO: Compute the correlation matrix for numeric columns and
    #       visualize it as an annotated Seaborn heatmap
    numeric_df = df.select_dtypes(include='number')

    corr_matrix = numeric_df.corr(method='pearson')

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main():
    """Load data, compute summary, and generate all plots."""
    os.makedirs("output", exist_ok=True)

    # TODO: Load the CSV from data/sample_sales.csv
    df = pd.read_csv("data/sample_sales.csv")
    # TODO: Call compute_summary and save the result
    compute_summary(df)
    # TODO: Choose 4 numeric-friendly columns and call plot_distributions
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    selected_cols = numeric_cols[:4]  # first 4 numeric columns
    plot_distributions(df, selected_cols, "output/distributions.png")
    # TODO: Call plot_correlation
    plot_correlation(df, "output/correlation.png")


if __name__ == "__main__":
    main()
