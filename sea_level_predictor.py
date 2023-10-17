import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  line_of_best_fit = res.slope * df['Year'] + res.intercept

  future_line = np.arange(1880, 2051)
  line_of_best_fit_2050 = res.slope * future_line + res.intercept

  df1 = df.copy()
  df1 = df1[df1['Year'] >= 2000]

  res1 = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
  new_lobf = res1.slope * df1['Year'] + res1.intercept

  df1_2050 = np.arange(2000, 2051)
  new_lobf_2050 = res1.slope * df1_2050 + res1.intercept

  # Create scatter plot
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  ax.plot(future_line, line_of_best_fit_2050)

  # Create second line of best fit
  ax.plot(df1_2050, new_lobf_2050)

  # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')
  ax.set_ylim(-1, 20)
  ax.set_xlim(1870, 2060)

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
