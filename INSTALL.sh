#!/bin/sh
#
# Linux installation script. Need root permissions to install.
#
# Compatible with:
#
#	- Debian 7.4
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
usage="plotdat installer usage:\
\n -c [config directory]. Default: /home/$USERNAME/.plotdat\
\n -e [executable target directory]. Default: /usr/local/bin\
\n -E [env-var definitions file]. Default: /home/$USERNAME/.bashrc\
\n -l [library target directory]. Default: /usr/local/lib/plotdatlib\
\n -m [man-db target directory]. Default: /usr/local/man/man1"
config_dir=/home/$USERNAME/.plotdat
source_dir=`pwd`/src
lib_dir=/usr/local/lib/plotdatlib
exec_dir=/usr/local/bin
man_dir=/usr/local/man/man1
env_config=/home/$USERNAME/.bashrc

# Get installer options
while getopts "hc:e:E:l:m:" flag; do
	case $flag in
		c ) config_dir=$OPTARG;;
		e ) exec_dir=$OPTARG;;
		E ) env_config=$OPTARG;;
		l ) lib_dir=$OPTARG;;
		m ) man_dir=$OPTARG;;
		h ) echo $usage; exit 0;;
	esac
done;

echo -n "Installing 'plotdat'...";

# Try to create config directory
if [ ! -d $config_dir ]; then
	mkdir $config_dir
fi

# Try to create lib directory
if [ ! -d $config_dir ]; then
	mkdir $lib_dir
fi

# Try to create executable dir
if [ ! -d $exec_dir ]; then
	mkdir $exec_dir
fi

# Try to create lib dir
if [ ! -d $lib_dir ]; then
	mkdir $lib_dir
fi

# Try to create man dir
if [ ! -d $man_dir ]; then
	mkdir $man_dir
fi

# Copy the gnuplot source files to the config directory
install --mode go-w,ugo+rx $source_dir/*.plt $config_dir

# Copy the library files
install --mode go-w,ugo+rx $source_dir/*.py $lib_dir

# Copy the executables
install --mode go-w,ugo+rx $source_dir/plotdat $source_dir/plotdat_hp $exec_dir
sed -i "/import sys/a\sys.path.append('$lib_dir')" $exec_dir/plotdat
sed -i "/import sys/a\sys.path.append('$lib_dir')" $exec_dir/plotdat_hp

# Copy man pages to man directory
install --mode go-w,ugo+rx mandb/plotdat.1 mandb/plotdat_hp.1 $man_dir
gzip $man_dir/plotdat.1
gzip $man_dir/plotdat_hp.1

# Update PATH if required
echo $PATH | grep $exec_dir
if [ $? -eq 1 ]; then
	sed -i "$ a\export PATH=$PATH:$exec_dir" $env_config
fi
echo " Done."
