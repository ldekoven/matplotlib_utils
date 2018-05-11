import argparse
import numpy as np

# Local imports
import plot


def computeStats(input_data):
  np_data = np.array(input_data)
  
  print('DATA STATS')
  print('-------------------------')
  print('\tMin:', np.min(np_data))
  print('\tMedian:', np.median(np_data))
  print('\tMax:', np.max(np_data), '\n')

  print('\tP10:', np.percentile(np_data, 10))
  print('\tP20:', np.percentile(np_data, 20))
  print('\tP30:', np.percentile(np_data, 30))
  print('\tP40:', np.percentile(np_data, 40))
  print('\tP50:', np.percentile(np_data, 50))
  print('\tP60:', np.percentile(np_data, 60))
  print('\tP70:', np.percentile(np_data, 70))
  print('\tP80:', np.percentile(np_data, 80))
  print('\tP90:', np.percentile(np_data, 90))
  print('\tP95:', np.percentile(np_data, 95))
  print('\tP99:', np.percentile(np_data, 99))
  print('-------------------------')


"""
Main entry point for stats and cdf. 
Requires input file path, output plot, and optional titles
"""
def main(
  input_data,
  output_plot_file,
  plot_title,
  xlabel,
  ylabel,
):
  # Simply creates a cdf of the input data. Input foramt one number per line.
  with open(input_data, 'r') as inf:
    print('Reading:', input_data)
    data = inf.read().split('\n')

  # Remove empty strings from list
  sanitizedList = list(filter(None, data))

  # Convert data to float and remove empty strings
  floatData = [float(x) for x in sanitizedList]

  # Print data stats
  computeStats(floatData)

  # CDFify
  cdfData = plot.CDFify(floatData)
  # Add a starting 0 to the x and y axis
  cdfData[0] = [0] + cdfData[0]
  cdfData[1] = [0] + cdfData[1]

  plotData = []
  plotData.append(cdfData)

  labels = []
  labels.append('CDF data')


  # Plot the data, and save results of specified outputpath + servicname
  plt = plot.drawPlot(
    r=plotData,
    xlabel=xlabel,
    ylabel=ylabel,
    title=plot_title,
    set_logx=0,
    set_logy=0,
    labels=labels,
    leg_loc='best',
    time_plot=False,
    return_plt=True,
    above_legend=True,
    outside_legend=True,
    special_line=False,
    marker=False,
    trend=False,
    yhline=None,
    text=None,
  )  

  # Save the figure
  plt.savefig(
    output_plot_file,
    bbox_inches='tight',
  )

  print('Saved plot for {} in {}'.format(input_data, output_plot_file))
  # Clear the figure
  plt.clf()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-if',
    '--input_data_file',
    help='Relateive path to input data file for CDF',
    type=str,
    required=True,
  )
  parser.add_argument(
    '-of',
    '--output_plot_file',
    help='Location and name of where to save plot',
    type=str,
    required=True,
  )
  parser.add_argument(
    '-t',
    '--plot_title',
    help='Plot title, otherwise default',
    type=str,
    required=False,
    default='CDF Plot',
  )
  parser.add_argument(
    '-xl',
    '--xlabel',
    help='X-label caption',
    type=str,
    required=False,
    default='X-data',
  )
  parser.add_argument(
    '-yl',
    '--ylabel',
    help='Y-label caption',
    type=str,
    required=False,
    default='Proportion',
  )

  args = parser.parse_args()
  input_data_file = args.input_data_file
  output_plot_file = args.output_plot_file
  plot_title = args.plot_title
  xlabel = args.xlabel
  ylabel = args.ylabel

  main(
    input_data_file,
    output_plot_file,
    plot_title,
    xlabel,
    ylabel,
  )