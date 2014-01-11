#!/usr/bin/python -E
#
#	All options: (not all implemented yet)
#
#	--3D-mode							: Use 3D plotting mode
#
#	-a [axis names...]					: Axis names, first three strings delimited by '\' characters
#	example: -a "Current (A)\Voltage (V)" or -a "X\Y\Z"
#
#	--axis-name-delim [character]		: Delimiter character for axis names string in '-a'
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
#	--gnuplot-options [options]			: Pass options to gnuplot invocations
#
#	-h									: Help output
#
#	--header-length [number]			:
#	--header-parser [parser options]	:
#
#	-m [column spec]					: Specify data columns to plot from data file
#	example: -m "3" or -m "1 2 5"
#	-M [column names...]				: Specify the names of data columns specified with '-m'
#	example: -M "Metres Millimeters" (spaces delimit)
#	TODO: Fix the inability to have spaces in the column names
#
#	-o [output image name]				: Specify output image name
#	--output-terminal					:
#	--image-font [fontspec]				:
#	--image-size [sizespec]				:
#
#	-l [legend pos]						: Allows the legend to be rendered and where
#
#	-s [value separator]				: Specify value delimiting character in data files
#
#	-t [graph title]					: Specify graph title, omitted if not specified
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





