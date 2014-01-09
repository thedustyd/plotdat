# Reset gnuplot
reset

# Set output
set terminal png font "arial,14" size 1366,768
set output output_file_name.".png"

# Set axis properties
set xlabel xaxis_label
set ylabel yaxis_label
if (xnumber_format ne '') set format x xnumber_format
if (ynumber_format ne '') set format y ynumber_format
if (xaxis_range ne '') set xrange xaxis_range
if (yaxis_range ne '') set yrange yaxis_range

# Set title properties
set title data_file_name

# Plot the provided data file with options provided
plot for data_file_name using 1:4 with lines




