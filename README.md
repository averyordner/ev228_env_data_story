# ev228_env_data_story
Repository for Avery and Morgan's Environmental Data Story Project

For this project, we focused on South Platte River stream gauge data from 2000-2025 (this includes the Hayman Fire of 2002 and the flooding of 2013). We then took averages by month in order to see how stream discharge has changed since the Hayman Fire of 2002. We expected to see a large spike in discharge following the floods of 2013, so we compared this to discharge value to surrounding years. 

In order to generate figures for this project, we imported a stream gauge csv dataset into python and ran functions until we could plot the data using matplotlib (see pushed code). 

# Code Index:
We first imported matplotlib.pyplot, pandas, numpy, and datetime in order to plot, calculate statistics, and convert date formats.
- loop_dates: a for loop that removes unreadable characters from python and formats columns for year, month, and mean value
- good_dates: uses readable dates from loop_dates from the given import of data
- column_names: man-made columns of month, year, and mean discharge
- annual_mean: using dateframe from pandas to arrange the data in rows in columns in order to make it easy to analyze, reorganize, and manipulate data
- df_graph: using pandas dateframe and defined x and y values within the annual_mean function to graph
- fig, ax: defined to plot and set color
- ticks: manually defined x axis tick values for plotting 

Generative AI Statement: We used generative AI as a starting point for helping us specify our x and y axis values because they were giving us trouble.

