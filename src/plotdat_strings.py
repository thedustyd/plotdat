# strings.py:
#
# strings for plotdat.py program
#
# Author:       Louis Fry
# Date:         08/11/2013
#

# Version information
version_info = \
"plotdat version 2.0."

# Description
plotdat_desc = \
"plotdat.py takes given text data files and creates graphs with the specified characteristics. The format of data files can be partially adapted using options."

# Short options
short_options = \
'a:cDf:hl:m:M:o:s:vVx:y:z:'

# Long options
long_options = \
[
	'3D-mode',
	'axis-names-delim=',
	'catenate',
	'gen-dirmode-delim=',
	'gen-dirmode-spec=',
	'gen-filemode-delim=',
	'gen-filemode-spec=',
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
	"data_col_names="
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
	"data_col_names="
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
	"data_col_names="
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
	"data_col_names="
]


