import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def CDFify(marray):
  farray = map(float, marray)
  outlist1 = []
  outlist2 = []
  ds = {}
  for x in farray:
    if x in ds:
      ds[x] = ds[x] + 1
    else:
      ds[x] = 1
  dkeys = ds.keys()
  dkeys = sorted(dkeys)
  tot = sum(ds.values())
  partsum = 0
  for k in dkeys:
    partsum = partsum + ds[k]
    outlist1.append(k)
    outlist2.append(float(partsum) / float(tot))
  return [outlist1, outlist2]


def drawPlot(
  r,
  ylabel,
  title,
  labels,
  leg_loc,
  ymin=None,
  ymax=None,
  xmax=None,
  xticks=None,
  yticks=None,
  rotatex=True,
  xlabel=None,
  xvline=None,
  yhline=None,
  set_logx=False,
  set_logy=False,
  time_plot=False,
  return_plt=False,
  outside_legend=False,
  above_legend=False,
  special_line=False,
  marker=False,
  trend=False,
  alpha=1,
  text=None,
  colors=None,
  lines=None,
  fontsize=12,
):
  """
  r is a list of lists [[[x],[y]], ...]
  """
  # fig = plt.figure()
  ax = plt.subplot(111)
  if xlabel is not None:
    ax.set_xlabel(xlabel, fontsize=fontsize)

  ax.set_ylabel(ylabel, fontsize=fontsize)

  if title is not None:
    ax.set_title(title, fontsize=fontsize)
  ax.grid(False)

  # Set line color
  # ax.grid(color='black', linestyle='-')

  # Set background color
  ax.set_facecolor('white')

  if time_plot:
    plt.xticks(rotation=70)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.gcf().autofmt_xdate()

  ind = -1
  # num_plots = len(r)
  for rec in r:
    ind = ind + 1
    ls = '-'

    if special_line and ind == 0:
      ls = '--'

    if marker:
      if colors is not None:
        ls = '-'
        if lines is not None:
          ls = lines[ind]
        ax.plot(
          rec[0],
          rec[1],
          linewidth=2,
          linestyle=ls,
          marker='o',
          label='%s' % (labels[ind]),
          alpha=alpha,
          color=colors[ind],
          ls=ls,
        )
      else:
        ax.plot(
          rec[0],
          rec[1],
          linewidth=2,
          linestyle=ls,
          marker='o',
          label='%s' % (labels[ind]),
          alpha=alpha,
        )
    else:
      if colors is not None:
        ls = '-'
        if lines is not None:
          ls = lines[ind]
        ax.plot(
          rec[0],
          rec[1],
          linewidth=2,
          linestyle=ls,
          label='%s' % (labels[ind]),
          alpha=alpha,
          color=colors[ind],
          ls=ls,
        )
      else:
        ax.plot(
          rec[0],
          rec[1],
          linewidth=2,
          linestyle=ls,
          label='%s' % (labels[ind]),
          alpha=alpha,
        )
    if trend:
      # Create a temp x-axis vs datetime
      tmp_x = []
      for xnum in range(0, len(rec[1])):
        tmp_x.append(xnum)

      # calc the trendline (it is simply a polynomial fitting)
      z = np.polyfit(tmp_x, rec[1], deg=30)
      p = np.poly1d(z)
      ax.plot(
        rec[0],
        p(rec[1]),
        '-.',
      )

  # ax.set_ylim(ymin=0)

  if ymin is not None and ymax is not None:
    ax.set_ylim(ymin, ymax)

  if xmax is not None:
    ax.set_xlim(right=xmax)

  if outside_legend:
    # bbox_to_anchor forces legend to the right side of the plot
    ax.legend(bbox_to_anchor=(1.05, 1), loc=leg_loc)
  elif above_legend:
    ax.legend(
      bbox_to_anchor=(0., 1.02, 1., .102),
      loc=3,
      ncol=2,
      mode="expand",
      borderaxespad=2,
      fontsize=fontsize,
    )
  else:
    ax.legend(loc=leg_loc, fontsize=fontsize)

  if set_logx:
    ax.set_xscale('log')

  if set_logy:
    ax.set_yscale('log')

  # Set the fontsize for both axis
  ax.tick_params(axis='both', labelsize=fontsize)

  if xticks:
    # If custom x-axis specificed use it
    # Set number of ticks for x-axis
    ax.set_xticks(xticks, fontsize=fontsize)
    # Set ticks labels for x-axis
    if rotatex:
      ax.set_xticklabels(xticks, rotation=70, fontsize=fontsize)

  if yticks:
    # If custom y-axis specificed use it
    # Set number of ticks for y-axis
    ax.set_yticks(yticks)


  # Add verticle lines to plot
  if xvline:
    for l in xvline:
      # ax.axvline(
      #   x=dt.date(2017, 8, 23),
      #   color='black',
      #   linewidth=2,
      #   linestyle='-'
      # )
      plt.axvline(x=l, color='black', ls='-')

  # Add a horrizontal line to plot
  if yhline:
    for l in yhline:
      plt.axhline(y=l, ls='-.')

  if text:
    for v in text:
      xloc = v[0]
      yloc = v[1]
      value = v[2]
      ax.text(xloc, yloc, value, fontsize=fontsize)

  if return_plt:
    return plt

  plt.show()
  plt.clf()


# Draw a scatter plot
def drawScatterPlot(
    r,
    ylabel,
    title,
    labelArray,
    leg_loc,
    xlabel=None,
    return_plt=0,
    outside_legend=False, ):
  """
  r is a list of lists [[[x],[y]], ...]
  TODO: Extend to do subplots on a 4x grid
  """
  fig = plt.figure()
  ax = plt.subplot(111)
  if xlabel is not None:
    ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.set_title(title)
  ax.grid(True)
  # Set line color
  ax.grid(color='black', linestyle='-')
  # Set background color
  ax.set_axis_bgcolor('white')

  # Set the x-min to 0
  #ax.set_xlim(left=0, right=200)

  ind = -1
  for rec in r:
    ind = ind + 1
    # s is the area of the point
    ax.scatter(
      rec[0], rec[1], s=2, color='blue', label='%s' % (labelArray[ind]))

  if outside_legend is True:
    # bbox_to_anchor forces legend to the right side of the plot
    ax.legend(bbox_to_anchor=(1.05, 1), loc=leg_loc)
  else:
    #     ax.legend(loc=leg_loc)

    legend = ax.legend(loc=leg_loc, shadow=True, fontsize='x-large')

    # Put a nicer background color on the legend.
    legend.get_frame().set_facecolor('#00FFCC')

  if return_plt:
    return plt

  plt.show()
  plt.clf()


# Draw a heatmap plot
# Create own subplot function
def drawHeatmapPlot(
  r,
  ylabel,
  title,
  xlabel=None,
  return_plt=0,
  cmap='binary',  # Set color map
  interpolation='nearest',
  invert_y=False,
  grid=True,
  subplot=False,
):
  # If subplot just return the figure. We will set labels after plotting
  if subplot:
    subplot.imshow(
      r, cmap=cmap, interpolation=interpolation, aspect='auto'
    )

    if invert_y:
      subplot.invert_yaxis()
    if not grid:
      subplot.grid(False)

    return

  if not subplot:
    fig = plt.figure()
    ax = plt.subplot(111)

  if xlabel is not None:
    ax.set_xlabel(xlabel)

  ax.set_ylabel(ylabel)
  ax.set_title(title)

  if not grid:
    ax.grid(False)

  ax.imshow(r, cmap=cmap, interpolation=interpolation)

  if invert_y:
    ax.invert_yaxis()

  if return_plt:
    return plt

  plt.show()
  plt.clf()


def drawBarPlot(
  r,
  title,
  xlabel,
  ylabel,
  labels,
  leg_loc,
  return_plt=False,
  outside_legend=False,
  alpha=1,
):
  """
  r is a list of bar heights corresponding to the label x-axis i.e. [1,2,3]
  labels is the xticks values.
  """
  # fig = plt.figure()
  ax = plt.subplot(111)

  # Customzie backgournd
  # ax.set_axis_bgcolor('white')
  # ax.grid(color='black', linestyle='-')

  # Set y-label
  ax.set_ylabel(ylabel)

  # Set title
  ax.set_title(title)

  # Create a list of the number of bars we will plot
  x_pos = list(range(len(r)))

  # Set the width for each bar
  width = 0.35

  ax.bar(
    np.arange(len(r)),
    r,
    width,
    x_pos,
  )

  if outside_legend:
    # bbox_to_anchor forces legend to the right side of the plot
    ax.legend(bbox_to_anchor=(1.05, 1), loc=leg_loc)
  else:
    ax.legend(loc=leg_loc)

  # Set the x-axis labels
  plt.xticks(x_pos, labels)

  # Set ticks labels for x-axis
  ax.set_xticklabels(labels, rotation=70, fontsize=12)

  if return_plt:
    return plt

  plt.show()
  plt.clf()
