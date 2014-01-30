# strings.py:
#
# strings for plotdat.py program
#
# Copyright (C) {2013-2014}  {Louis Fry}
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

# Version information
version_info = \
"""plotdat version 0.1, Copyright (C) 2013-2014 Louis Fry
comes with ABSOLUTELY NO WARRANTY. This is free software,
and you are welcome to redistribute it under certain
conditions; see the license file provided for details."""

# Help
help = \
"""

"""

# Config files directory
config_path = "~/.plotdat"

# Description
plotdat_desc = \
"plotdat.py takes given text data files and creates graphs with the specified characteristics. The format of data files can be partially adapted using options."

# Short options
short_options = \
'a:cDf:hl:m:M:o:s:t:vVx:y:z:'

hp_short_options = \
'ct:r:R:'

# Long options
long_options = \
[
	'3D-mode',
	'annotate=',
	'axis-names-delim=',
	'catenate',
	'dirmode-gen-delim=',
	'dirmode-gen=',
	'filemode-gen-delim=',
	'filemode-gen=',
	'gnuplot-options=',
	'header-length=',
	'header-parser='
]

# gnuplot scripts
script_onedf = "onedf.plt"
script_multidf = "multidf.plt"
script_3D_onedf = "3Donedf.plt"
script_3D_multidf = "3Dmultidf.plt"

# gnuplot script variable declarations
# WARNING: each list must be in the right order and
# must be the same lenth as 'gnuplot_variables' in
# plotdat.py
script_onedf_opts = \
[
	"output_file_name=",
	"xaxis_label=",
	"yaxis_label=",
	"xnumber_format=",
	"ynumber_format=",
	"xaxis_range=",
	"yaxis_range=",
	"data_col_numbers=",
	"data_col_names=",
	"graph_title=",
	"legend_spec=",
	"annotate="
]

script_multidf_opts = \
[
	"output_file_name=",
	"xaxis_label=",
	"yaxis_label=",
	"xnumber_format=",
	"ynumber_format=",
	"xaxis_range=",
	"yaxis_range=",
	"data_col_numbers=",
	"data_col_names=",
	"graph_title=",
	"legend_spec=",
	"annotate="
]

script_3D_onedf_opts = \
[
	"output_file_name=",
	"xaxis_label=",
	"yaxis_label=",
	"zaxis_label=",
	"xnumber_format=",
	"ynumber_format=",
	"znumber_format=",
	"xaxis_range=",
	"yaxis_range=",
	"zaxis_range=",
	"data_col_numbers=",
	"data_col_names=",
	"graph_title=",
	"legend_spec=",
	"annotate="
]

script_3D_multidf_opts = \
[
	"output_file_name=",
	"xaxis_label=",
	"yaxis_label=",
	"zaxis_label",
	"xnumber_format=",
	"ynumber_format=",
	"znumber_format=",
	"xaxis_range=",
	"yaxis_range=",
	"zaxis_range=",
	"data_col_numbers=",
	"data_col_names=",
	"graph_title=",
	"legend_spec=",
	"annotate="
]


