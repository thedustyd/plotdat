plotdat
=======

1. Brief:

'gnuplot' command line wrapper for plotting data from many data files. Ideal for use alongside LabView.


2. Description:

'plotdat' takes the arguments and data files provided to create single graphs for each data file by def-
ault, or a single graph representing all data files. Further capabilities such as 3D are to be implemen-
ted.

'plotdat' is written in Python. It invokes 'gnuplot' with a set of generated arguments and variables cr-
eated from the options passed to 'plotdat'. There are 'gnuplot' command source files for each operational
mode which contain a predefined sequence of commands. These files can be easily edited to adapt the output to
one's needs.

There are a number of practical human problems that arise when using computers to do smart things. Spec-
ifically, when trying to understand or represent masses of data it becomes extremely difficult to handle
the variations in the data that are due to human made choices. For instance if one conducts ten experim-
ents and uses a different format for each experiment, software that has to conceptually group all that
data will be difficult to create, and will likely be buggy. The simplest way for a program to have this
capability is to require consistency from the user with respect to how the software should behave. Howe-
ver it is difficult to require consistency of humans as we strive for progress and better aesthetics.

Thus when a program such as this one attempts to gather data consistently, it is best to use it with co-
nsistent data files, for instance the typical LabView data output written to '.dat' files. In such files
the x-axis data is usually written as a first column, and measured values are written in subsequent col-
umns. For details of the expected format see the synopsis.

To aid in the conceptual grouping of data, a number of consistency-requiring (to a varying degree) capa-
bilities are implemented:

	- Curve label generation from file names. Used for naming output files in the default mode.
	
		Consistency problems: Inconsistent data columns will yield false curve labels.
	
	- Group information from directory names present in file paths. (TODO)
		
		Consistency problems: Not sure yet.
		
	- Header information parsing for annotations and labels. (TODO)
		
		Consistency problems: Difficult to extract meaningful information from varying headers.

It is possible to cover many permutations of how the files are formated by using Unix tools to catenate
data files or rearrange columns to get the desired graph output. Regular expressions are very powerful
for selecting specific data files. Also it is of course possible to use the plot program in a batch file
of any kind as long the 'python' and 'gnuplot' are invocable.


3. Requirements:

		- gnuplot version 	>= 4.6:				Certain features will not work with lower versions.
		- python version	>= 2.6:				2.7 recommended.


4. Use cases supported:

	At the moment, 'plotdat' only handles numerical data that has a specific format. It is most useful
for use with large amounts of data.


5. Notes:

6. Future improvements:

	- 3D plotting mode supporting special features.
	- Plotting statistical data with dates and times.
	- Internal rearrangement of data files and columns.


7. Synopsis:

	See the file plotdat.1 in mandb/ with "man -l plotdat.1"

