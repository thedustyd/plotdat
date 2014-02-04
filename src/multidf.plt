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

# Argument strings
fgl_string = ""
arg_string = ""
arg_prototype = "for [i=1:words(\"%s\")] \"%s\" every ::int(\"%s\") using 1:int(word(\"%s\",i)) with lines title word(\"%s\",i).\"%s\".\" \".\"%s\""

# Create gnuplot arguments
do for [j=1:words(file_list)] {
	if (file_gen_list ne '') {
		fgl_string = "_".word(file_gen_list,j)
	}
	#print word(parser_data,j)
	arg_string = arg_string.sprintf(arg_prototype,data_col_numbers,word(file_list,j),word(header_lengths,j),data_col_numbers,data_col_names,fgl_string,word(parser_data,j))
	
	if (j < words(file_list)) {
		arg_string=arg_string.", "
	}
}

# Issue command
s = "plot ".arg_string
eval s;

