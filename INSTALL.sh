#!/bin/sh
echo -n "Installing 'plotdat'...";

config_dir=~/.plotdat
source_dir=src
lib_dir=/usr/local/lib
lib_dir_changed=false
exec_dir=/usr/local/bin
exec_dir_changed=false

# Get installer options
while getopts "e:l:" flag; do
	case $flag in
		e ) exec_dir=$OPTARG; exec_dir_changed=true ;;
		l ) lib_dir=$OPTARG; lib_dir_changed=false ;;
	esac
done;

# Check config directory exists
if [ ! -d $config_dir ]; then
	mkdir $config_dir
fi

# Check permissions on executable directory
if [ ! -w $exec_dir ] && [ ! $exec_dir_changed ]; then
	echo "You do not have write permission to '$exec_dir' or it doesn't exist. Choose an installation directory that you have write permission and update your '\$PATH'."
	exit -1
fi

# Check permissions on library directory
if [ ! -w $lib_dir ] && [ ! $lib_dir_changed ]; then
	echo "You do not have write permission to '$lib_dir' or it doesn't exist. Choose an installation directory that you have write permission and update your '\$PATH'."
	exit -1
fi

# Try to create executable dir
if [ ! -d $exec_dir ] && [ $exec_dir_changed ]; then
	mkdir $exec_dir
fi

# Try to create lib dir
if [ ! -d $lib_dir ] && [ $lib_dir_changed ]; then
	mkdir $lib_dir
fi

# Update PATH
export PATH=$PATH:$exec_dir

# Copy the gnuplot source files to the config directory
cp $source_dir/*.plt $config_dir

# Copy the library files
cp $source_dir/*.py $lib_dir

# Copy the executables
cp $source_dir/plotdat $source_dir/plotdat_hp $exec_dir

echo " Done."
