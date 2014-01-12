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

# Set annotation
if (annotate eq 'True') {
	if (common_info1 ne '') {
		set label 1 common_info1 at graph 0.02, 0.11 tc lt -1
	}
	if (common_info2 ne '') {
		set label 2 common_info2 at graph 0.02, 0.08 tc lt -1
	}
	if (common_info3 ne '') {
		set label 3 common_info3 at graph 0.02, 0.05 tc lt -1
	}
}

# Plot the provided data file with options provided
plot for [i=1:words(data_col_numbers)] data_file_name every ::int(header_length) using 1:int(word(data_col_numbers,i)) with lines title word(data_col_names,i)." ".parser_data



