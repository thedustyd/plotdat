#!/usr/bin/python -E

# Available Options:
#
#  -m [column spec]		: Specify columns to use as dependent variable (y) from data file 
#  example column spec: "3" or "1 2 4"
#  -M [col names ...]	: Specify column names
#  example column name: "E_a E_b"
#  -o [out file name]	: Specify output image file name without extension
#  -c					: Catenate all plots into one image
#  -f [gen spec]		: File name generation pattern specification using 
#  -F [gen spec]		: 
#  example gen spec: "1" or "2,9"
#  -d [delim char]		: Specify file name generation delimiter character
#  -D [delim char]		:
#  default delim char: "_"
#  -h					: Data files contain header lines
#  -H [py options]		: Data files contain header lines with useful info
#  -x "[label1 ...]"	: Specify axis labels
#  example labels: "energy time"
#  -l [gplot 'with' cmd]: Set the linestyle in GNUPLOT syntax
#  -p [gp options]		: Options to pass to gnuplot for every invocation
#  -v					: Verbose
#  -V					: Super verbose (useful for debug)
#
# Specific 3D plotting options
#
#  -3					: Set 3D plot mode
#  -w [xa,ya,sc,scz]	: Set view properties
#  example view properties: "60,30,0.5,1"
#  -i					: Set number of isolines

#
#	All options:
#
#	--3D-mode							: Turn on 3D plotting mode
#
#	-a [axis names...]					: Axis names, first three strings delimited by '\' characters
#	example: -a "Current (A)\Voltage (V)" or -a "X\Y\Z"
#
#	--axis-name-delim [character]		: Delimiter character for axis names string in '-a' option
#
#	-c									: Create single image from data files
#	--catenate							: Create single image from data files long form
#
#	-D									: Debug output
#
#	-f [number format]					: Axis number format
#
#	--gen-dirmode-delim [delim char]	: Delimiter character for selecting portions of strings in directories
#	--gen-dirmode-spec [gen pattern]	: Selection
#	example: --gen-dirmode-spec="3 5" or --gen-dirmode-spec "2"
#
#	--gen-filemode-delim [delim char]	: Delimiter character for selecting portions of strings in file names
#	--gen-filemode-spec [gen pattern]	:
#	example: --gen-filemode-spec="4" or --gen-filemode-spec "2 3"
#
#	--gnuplot-options [options]			:
#
#	-h									: Help output
#
#	--header-length [number]			:
#	--header-parser [parser options]	:
#
#	-m [column spec]					: Specify data columns to plot from data file
#	example: -m "3" or -m "1 2 5"
#	-M [column names...]				: Specify the names of data columns specified with '-m'
#	example: -M "Metres Millimeters"
#
#	-o [output image name]				: Specify output image name
#	--output-terminal					:
#	--image-font [fontspec]				:
#	--image-size [sizespec]				:
#
#	-s [value separator]				: Specify value delimiting character in data files
#
#	-v									: Verbose output
#	-V									: Version information
#
#	--viewer-position [xa,ya,sc,sca]	: Set viewer position (3D mode only)
#
#	-x [range]							: Set x-range
#	-y [range]							: Set y-range
#	-z [range]							: Set z-range (3D mode only)
#
#	-X [xaxis_num]						:
#	-Y [yaxis_num]						:
#	-Z [zaxis_num]						:
#

# Python specific
import os
import sys

# Application specific
import plotdat_strings as pds
import plotdat_functions as pdf

optlist = []		# Options and arguments returned by getopt
args = []
optdict = {}		# Returned options and arguments
dir_gen = []		# File name and directory name generation output
file_gen = []

# Parse options
optdict,args = pdf.parse_opts(sys.argv[1:])
if optdict == None:
	sys.exit(-1)

pdf.vprint("%i Files to Process.\n%i Options Passed." % (len(args),len(optdict)))
pdf.dprint("sel_col_numbers: %s.\nsel_col_names: %s." % (pdf.sel_col_numbers,pdf.sel_col_names))

# Get file name and directory name generation output (to identify data uniquely)
if pdf.gen_dirmode_spec != '':
	dir_gen = pdf.parse_dirmode(args)
	if dir_gen == None:
		sys.exit(-1)
if pdf.gen_filemode_spec != '':
	file_gen = pdf.parse_filemode(args)
	if file_gen == None:
		sys.exit(-1)

# Get gnuplot variables
gnuplot_variables = pdf.get_gnuplot_variables()
if gnuplot_variables == None:
	sys.exit(-1)

# Invoke gnuplot
result = pdf.gnuplot_command(gnuplot_variables,args,(file_gen,dir_gen))
if result != 0:
	sys.exit(-1)

# Information
pdf.vprint("Finished: '%i'." % (result))





