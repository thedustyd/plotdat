# Reset gnuplot
reset

# Set output
set macros
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
if (graph_title ne '') set title graph_title

# Set legend properties
unset key
if (legend_spec ne '') set key @legend_spec

# Plot the provided data file with options provided
plot for [i=1:words(data_col_numbers)] data_file_name every ::int(header_length) using 1:int(word(data_col_numbers,i)) with lines title word(data_col_names,i)." ".parser_data



