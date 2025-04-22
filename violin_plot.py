import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def darken_color(color, factor=0.5):
    """This function darkens a given color by reducing its brightness."""
    # Convert RGB to HSV (Hue, Saturation, Value)
    rgb = mcolors.to_rgb(color)  # Convert to RGB
    hsv = mcolors.rgb_to_hsv(rgb)  # Convert RGB to HSV

    # Decrease the Value to darken the color
    hsv[2] *= factor  # Darken by adjusting the Value (brightness)

    # Convert back to RGB
    darkened_rgb = mcolors.hsv_to_rgb(hsv)
    return darkened_rgb


def data2violin(file, color='Blues'):
    """The function data2violin takes an excel file and generates a violin plot with the data given.
    input: csv file and color preference, output: violin plot"""

    # Read the Excel file
    df = pd.read_excel(file)

    # Since different days are included in the Excel file, we have to melt it
    df_long = pd.melt(df, var_name='Day', value_name='Value')

    # Generate violin plot
    sns.set_theme(style='darkgrid')
    sns.violinplot(x='Day', y='Value', data=df_long, hue='Day', palette=color, inner='quartile')

    # Overlay data points on top of the violin plot with a darker color
    # For each hue, we'll darken the corresponding color
    palette = sns.color_palette(color)

    # Loop through each unique "Day" to apply the darker shade for dots
    for i, day in enumerate(df_long['Day'].unique()):
        # Get the corresponding color for this "Day"
        violin_color = palette[i % len(palette)]

        # Darken the color more
        dark_color = darken_color(violin_color, factor=0.3)  # Darken by a factor of 0.3

        # Overlay the dots for the current "Day"
        sns.stripplot(x='Day', y='Value', data=df_long[df_long['Day'] == day],
                      color=dark_color, jitter=True, dodge=True, marker='o', alpha=0.7, size=3)

    # Set title and axis details
    plt.title("Size of Spheroids (in μm)", fontsize=14)
    plt.xlabel('Timepoint', fontsize=12, fontweight='bold')
    plt.ylabel('Size (in μm)', fontsize=12, fontweight='bold')

    # Show the plot
    plt.show()





data2violin('P:/shared_spaces/WetLab/Magdalena Unterberger/Miura protocol/PS8/Results-AW1.xlsx', 'Reds')
