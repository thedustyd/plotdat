# plotdat_functions.py:
#
# functions for plotdat.py program
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

import getopt				# argument parsing
import subprocess as sp		# command line access
import re					# regular expressions
import sys
import plotdat_strings as pds

#
#------------------------------------------------------------------------------------------
#							Plotdat Functions and Global Variables
#------------------------------------------------------------------------------------------
#

verbose = False
debug = False
_3D_mode = False
axis_names = ''
axis_names_delim = ''
annotate = False
annotate_sel = ''
catenate = False
data_file_sep = ''
gen_dirmode_delim = ''
gen_dirmode_spec = ''
gen_filemode_delim = ''
gen_filemode_spec = ''
gnuplot_options = ''
header_delim = ''
header_length = ''
header_parser_opts = ''
legend_spec = ''
line_style = ''
output_file_name = ''
graph_title = ''
number_format = ''
sel_col_numbers = ''
sel_col_names = ''
xaxis_range = ''
yaxis_range = ''
zaxis_range = ''

# Printing
def vprint(message):
	if verbose == True or debug == True:
		print message

def dprint(message):
	if debug == True:
		print message

# Parse options, activate switches and assign option argument variables
# Only this function can write to the option argument variables
def parse_opts(cmd_args):
	global verbose
	global debug
	global _3D_mode
	global axis_names
	global axis_names_delim
	global annotate
	global annotate_sel
	global catenate
	global data_file_sep
	global sel_col_numbers
	global sel_col_names
	global gen_dirmode_delim
	global gen_dirmode_spec
	global gen_filemode_delim
	global gen_filemode_spec
	global gnuplot_options
	global header_delim
	global header_length
	global header_parser_opts
	global legend_spec
	global line_style
	global output_file_name
	global graph_title
	global number_format
	global xaxis_range
	global yaxis_range
	global zaxis_range
	optlist = []
	args = []
	
	# Get options and file names
	try:
		optlist, args = getopt.gnu_getopt(cmd_args,pds.short_options,pds.long_options)
	except getopt.GetoptError as e:
		print "ERROR: getopt: '%s'." % (e.msg)
		return (None,None)
	
	# Check files were passed and that they exist
	if len(args) == 0:
		print "ERROR: parse_opts: No data files specified."
		return (None,None)
	
	for f in args:
		try:
			fd = open(f,"r")
			fd.close()
		except IOError as e:
			errno,msg = e
			print "ERROR: open: '[%i] %s'." % (errno,msg)
			return (None,None)
	
	# Reformat option and argument list
	ret = {}
	for opt,arg in optlist:
		ret[opt] = arg
	
	# Handle short options
	
	# -a
	try:
		x = ret["-a"]
		axis_names = x
	except KeyError:
		print "ERROR: parse_opts: -a option is required."
		return (None,None)
	
	# -c
	try:
		x = ret["-c"]
		catenate = True
	except KeyError:
		pass
	
	# -D
	try:
		x = ret["-D"]
		debug = True
	except KeyError:
		debug = False
	
	# -f
	try:
		x = ret["-f"]
		number_format = x
	except KeyError:
		number_format = "\\\\"
	
	# -m
	try:
		x = ret["-m"]
		sel_col_numbers = x
		if x == "":
			print "ERROR: parse_opts: -m option is empty."
			return (None,None)
	except KeyError:
		print "ERROR: parse_opts: -m option is required."
		return (None,None)
	
	# -M
	try:
		x = ret["-M"]
		sel_col_names = x
		if x == "":
			print "ERROR: parse_opts: -M option is empty."
			return (None,None)			
	except KeyError:
		print "ERROR: parse_opts: -M option is required."
		return (None,None)
	
	# -o
	try:
		x = ret["-o"]
		output_file_name = x
	except KeyError:
		output_file_name = ''
	
	# -l
	try:
		x = ret["-l"]
		legend_spec = x
	except KeyError:
		legend_spec = ""
	
	# -s
	try:
		x = ret["-s"]
		data_file_sep = x
	except KeyError:
		data_file_sep = '\t'
	
	# -t
	try:
		x = ret["-t"]
		graph_title = x
	except KeyError:
		pass
	
	# -v
	try:
		x = ret["-v"]
		verbose = True
	except KeyError:
		verbose = False
	
	# -V
	try:
		x = ret["-V"]
		print pds.version_info
		return (None,None)
	except KeyError:
		pass
	
	# -x
	try:
		x = ret["-x"]
		xaxis_range = x
	except KeyError:
		xaxis_range = ''
	
	# -y
	try:
		x = ret["-y"]
		yaxis_range = x
	except KeyError:
		yaxis_range = ''
	
	# -z
	try:
		x = ret["-z"]
		zaxis_range = x
	except KeyError:
		zaxis_range = ''
	
	# Handle long options
	try:
		x = ret["--3D-mode"]
		_3D_mode = True
	except KeyError:
		_3D_mode = False
	
	try:
		x = ret["--annotate"]
		annotate = True
		annotate_sel = x
	except KeyError:
		annotate = False
	
	try:
		x = ret["--axis-name-delim"]
		axis_names_delim = x
	except KeyError:
		axis_names_delim = '\\'
	
	try:
		x = ret["--catenate"]
		catenate = True
	except KeyError:
		pass
	
	try:
		x = ret["--dirmode-gen-delim"]
		gen_dirmode_delim = x
	except KeyError:
		gen_dirmode_delim = '/'
	
	try:
		x = ret["--dirmode-gen"]
		gen_dirmode_spec = x
	except KeyError:
		gen_dirmode_spec = ''
	
	try:
		x = ret["--filemode-gen-delim"]
		gen_filemode_delim = x
	except KeyError:
		gen_filemode_delim = '_'
	
	try:
		x = ret["--filemode-gen"]
		gen_filemode_spec = x
	except KeyError:
		gen_filemode_spec = ''
	
	try:
		x = ret["--gnuplot-options"]
		gnuplot_options = x
	except KeyError:
		gnuplot_options = '-noraise'
	
	try:
		x = ret["--header-delim"]
		header_delim = x
	except KeyError:
		header_delim = '\n'
	
	try:
		x = ret["--header-length"]
		header_length = x
	except KeyError:
		header_length = '0'
	
	try:
		x = ret["--header-parser"]
		header_parser_opts = x
	except KeyError:
		header_parser_opts = ''
	
	return (ret,args)



# Return 	
def parse_dirmode(file_list):
	ret = []
	
	for file_path in file_list:
		isel = []
		
		# Convert string list to int list
		try:
			isel = [int(x) for x in gen_dirmode_spec.split(" ")]
		except ValueError as e:
			print "ERROR: plotdat: Invalid directory mode specs."
			return None
		
		# Separate directories
		file_path_chunks = file_path.split(gen_dirmode_delim)
		
		# Remove file name
		file_path_chunks.pop()
		
		# Check if there is a directory
		if len(file_path_chunks) == 0:
			ret.append([])
			continue
		
		# Make selection
		dsel = [x for x in file_path_chunks if (file_path_chunks.index(x) + 1) in isel]
		
		ret.append(dsel)
	
	return ret

def parse_filemode(file_list):
	ret = []
	
	for file_path in file_list:
		filename = ""
		isel = []
		
		# Convert string list to int list
		try:
			isel = [int(x) for x in gen_filemode_spec.split(" ")]
		except ValueError as e:
			print "ERROR: plotdat: Invalid file mode specs."
			return None
		
		# Separate filename
		file_path_chunks = file_path.split(gen_dirmode_delim)
		
		# Choose file name and strip extension
		file_name = file_path_chunks.pop().split('.')[0]
		
		# Make selection and split file name
		file_name_chunks = file_name.split(gen_filemode_delim)
		fsel = [x for x in file_name_chunks if (file_name_chunks.index(x) + 1) in isel]
		
		ret.append(fsel)
		
	return ret

# Create gnuplot variables
def get_gnuplot_variables():
	gnuplot_variables = []
	
	# Get output file name
	gnuplot_variables.append(output_file_name)

	# Get axis labels REQUIRED
	labels = axis_names.split(axis_names_delim)
	try:
		gnuplot_variables.append(labels[0])
		gnuplot_variables.append(labels[1])
		if _3D_mode == True:
			gnuplot_variables.append(labels[2])
	except IndexError as e:
		print "ERROR: plotdat: Incomplete axis names list."
		return None

	# Get axis number format OPTIONAL
	number_formats = number_format.split('\\')
	try:
		gnuplot_variables.append(number_formats[0])
		gnuplot_variables.append(number_formats[1])
		if _3D_mode == True:
			gnuplot_variables.append(number_formats[2])
	except IndexError as e:
		print "ERROR: plotdat: Incomplete number format specification."
		return None
	
	# Get axis ranges
	gnuplot_variables.append(xaxis_range)
	gnuplot_variables.append(yaxis_range)
	if _3D_mode == True:
		gnuplot_variables.append(zaxis_range)
	
	# Get column specs and column names
	gnuplot_variables.append(sel_col_numbers)
	gnuplot_variables.append(sel_col_names)
	
	# Get graph title
	gnuplot_variables.append(graph_title)
	
	# Get legend spec
	gnuplot_variables.append(legend_spec)
	
	# Get annotate switch
	if annotate == True:
		gnuplot_variables.append("True")
	else:
		gnuplot_variables.append("False")
	
	return gnuplot_variables

# Create gnuplot command
def gnuplot_command(gnuplot_variables,file_list,gen_list):
	gnuplot_command = ""
	gnuplot_script_vars = ""
	gnuplot_label_vars = ""
	parser_output = []
	file_gen,dir_gen = gen_list
	
	# Create common variables string
	var = [x+'\'%s\';' % (gnuplot_variables[pds.script_onedf_opts.index(x)]) for x in pds.script_onedf_opts]
	
	# Run the parser for common values if required
	if annotate:
		varc = 0
		cmd = []
		if annotate_sel == '':
			cmd = ['./plotdat_hp','-c']
		else:
			cmd = ['./plotdat_hp','-ct',annotate_sel]
		for f in file_list:
			cmd.append(f)
		parser_output = run_header_parser_ext(cmd)
		
		for i in range(10):
			try:
				gnuplot_label_vars += "common_info%i='%s';" % (i+1,"".join(parser_output[i].split('\t')))
			except IndexError:
				gnuplot_label_vars += "common_info%i='%s';" % (i+1,"")
		
		#sys.exit(-1)
	
	# Handle operation modes
	if catenate == False and _3D_mode == False:
		ret = -1
		outfilename = ""
		
		# Call gnuplot for every data file
		for i in range(len(file_list)):
			
			# Run the header parser if required
			if header_parser_opts != '':
				parser_output = run_header_parser(header_parser_opts,file_list[i])
			
				if len(parser_output) == 0:
					print "ERROR: plotdat_hp: Unhandled exception. Please fix."
					sys.exit(-1)
			
				if len(parser_output) < 2:
					print "WARN: plotdat_hp: %s" % (parser_output[0].strip('\n'))
					parser_output.append["None"]
			else:
				parser_output.extend(["0",""])
			
			# Check if using file gen. if not use file name without extension
			if len(file_gen) == 0 or (len(file_gen) == len(file_list) and file_gen[i] == []):
				outfilename = file_list[i].split('/')[-1].split('.')[0]
			elif len(file_gen) == len(file_list) and file_gen[i] != []:
				outfilename = "_".join(file_gen[i])
			
			# Check if using dir gen
			if len(dir_gen) == len(file_list) and dir_gen[i] != []:
				outfilename = outfilename + '_' + "_".join(dir_gen[i])
			
			# Generate command string with all arguments. override previous definition of output_file_name
			gnuplot_script_vars = "-e \"%s%sdata_file_name='%s';output_file_name='%s';header_length='%s';parser_data='%s';\"" % ("".join(var),gnuplot_label_vars,file_list[i],outfilename,parser_output[0]," ".join(parser_output[1:]))
			gnuplot_command = "gnuplot %s %s %s" % (gnuplot_options,gnuplot_script_vars,pds.script_onedf)
			
			# Call gnuplot
			ret = sp.call(gnuplot_command,shell=True) # trusted input?? likely not, may need more sanitizing
			if ret != 0:
				print "ERROR: gnuplot: Bad exit status %i." % ret
				return ret
		return ret
	
	elif catenate == True and _3D_mode == False:
		parser_outlist = []
		file_gen_list = ["_".join(x) for x in file_gen]
		
		# Run the header parser if required
		for i in range(len(file_list)):
			if header_parser_opts != '':
				parser_output = run_header_parser(header_parser_opts,file_list[i])
			
				if len(parser_output) == 0:
					print "ERROR: plotdat_hp: Unhandled exception. Please fix."
					sys.exit(-1)
			
				if len(parser_output) < 2:
					print "WARN: plotdat_hp: %s" % (parser_output[0].strip('\n'))
					parser_output.append["None"]
			else:
				parser_output.extend(["0",""])
				
			parser_outlist.append(parser_output)
		
		# gnuplot array delimiter character is space character
		header_lengths = " ".join([x[0] for x in parser_outlist])
		header_info = " ".join(["_".join(x[1:]) for x in parser_outlist])
		
		gnuplot_script_vars = "-e \"%s%sfile_list='%s';file_gen_list='%s';header_lengths='%s';parser_data='%s';\"" % ("".join(var),gnuplot_label_vars," ".join(file_list)," ".join(file_gen_list),header_lengths,header_info)
		gnuplot_command = "gnuplot %s %s %s" % (gnuplot_options,gnuplot_script_vars,pds.script_multidf)
		
		ret = sp.call(gnuplot_command,shell=True) # trusted input?? likely not, may need more sanitizing
		if ret != 0:
			print "ERROR: gnuplot: Bad exit status %i." % ret
		return ret
		
	elif catenate == False and _3D_mode == True:
		gnuplot_script_vars = "-e \"%s\"" % ("".join(var))
		gnuplot_command = "gnuplot %s %s %s" % (gnuplot_options,gnuplot_script_vars,pds.script_3D_onedf)
		
		
	elif catenate == True and _3D_mode == True:
		var = [x+'\'%s\';' % (gnuplot_variables[pds.script_3D_multidf_opts.index(x)]) for x in pds.script_3D_multidf_opts]
		gnuplot_script_vars = "-e \"%s\"" % ("".join(var))
		gnuplot_command = "gnuplot %s %s %s" % (gnuplot_options,gnuplot_script_vars,pds.script_3D_multidf)
	
	return -1

# Invoke header parser
def run_header_parser(options,filename):
	# Create command
	command = ["./plotdat_hp"]
	command.extend(options.split(','))
	command.append(filename)
	
	# Call the parser
	proc = sp.Popen(command,stdout=sp.PIPE)
	output,err = proc.communicate()
	exit = proc.wait()
	output = output.split('\n')
	return output

# Invoke header parser
def run_header_parser_ext(command):
	# Call the parser
	proc = sp.Popen(command,stdout=sp.PIPE)
	output,err = proc.communicate()
	exit = proc.wait()
	output = output.split('\n')
	output = [x for x in output if x != '']
	return output

#
#------------------------------------------------------------------------------------------
#						Header Parser Functions and Global Variables
#------------------------------------------------------------------------------------------
#

# plotdat_hp global vars
auto = False						# auto tag detection
tags_list = []						# list of tags
tags_regex = "(.*)\:(.*)"			# regular expression for matching tags and their values
tag_regex = "(%s)\:(.*)"
get_common = False					# find common mode
header_delimit_line = "\n"			# line that delimits the header from the data

# header parser options
def hp_parse_opts(cmd_args):
	global auto
	global tags_list
	global tags_regex
	global tag_regex
	global get_common
	global header_delimit_line
	optlist = []
	args = []
	
	# Get options and file name(s)
	try:
		optlist, args = getopt.gnu_getopt(cmd_args,pds.hp_short_options)
	except getopt.GetoptError as e:
		print "ERROR: getopt: '%s'." % (e.msg)
		return (None,None)

	if len(args) == 0:
		print "ERROR: plotdat_hp: No files passed."
		return (None,None)
	
	for f in args:
		try:
			fd = open(f,"r")
			fd.close()
		except IOError as e:
			errno,msg = e
			print "ERROR: open: '[%i] %s'." % (errno,msg)
			return (None,None)

	# Reformat option list
	optdict = {}
	for opt,arg in optlist:
		optdict[opt] = arg

	# Handle options
	try:
		x = optdict["-c"]
		get_common = True
	except KeyError as e:
		pass

	try:
		x = optdict["-t"]
		tags_list = x.split('\\')
	except KeyError as e:
		if not get_common:
			print "ERROR: plotdat_hp: -t option is required."
			return (None,None)
		else:
			auto = True

	try:
		x = optdict["-r"]
		tag_regex = x
	except KeyError as e:
		pass
	
	try:
		x = optdict["-R"]
		tags_regex = x
	except KeyError as e:
		pass
	
	return (optdict,args)

# Get header length and it's string from one file
def header_data(filename):
	found_delim = False
	header_lines = []
	header_length = 0
	lines_read = 0
	fd = None
	
	try:
		fd = open(filename,'r')
	except IOError:
		print "ERROR: header_data: Invalid data file name '%s'." % filename
		return (None,None)
	
	# Get header lines
	for line in fd:
		if line == header_delimit_line:
			found_delim = True
		if not found_delim:
			header_lines.append(line)
			header_length += 1
		lines_read += 1
	header_string = "".join(header_lines)
	
	fd.close()
	
	# Analyse header lines
	if lines_read - header_length == 0:
		print "No header in data file '%s'." % filename
		return (None,None)
	elif lines_read - header_length == 1:
		print "Header delimiting line found at top of file '%s'." % filename
		return (None,None)
	
	return (header_length,header_string)

# Find requested tab values
def header_tag(header_string):
	tag_matches = []
	for tag in tags_list:
		res = re.findall(tag_regex % tag,header_string)
		if res == []:
			continue
		tag_matches.append(res)
	return tag_matches

# Find all tab values
def header_tags(header_string):
	return re.findall(tags_regex,header_string)
	
