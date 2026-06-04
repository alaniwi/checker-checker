#!/bin/sh

. ./paths.sh

user=matt

for util in wget ncatted
do
    which $util > /dev/null || { echo "need $util installed"; exit 1; }
done

fname=$(basename $url)

for dir in $good_data_dir $warn_data_dir $fail_data_dir
do
    [ -d $dir ] || mkdir -p $dir
done

if [ ! -e $good_path ]
then
    wget --user $user --ask-password -O $good_path $url
fi

if [ ! -e $warn_path ]
then
    cp $good_path $warn_path
    ncatted -O -a calendar,time,o,c,"JUNK" $warn_path
fi

if [ ! -e $fail_path ]
then
    cp $good_path $fail_path
    ncatted -O -a experiment_id,global,o,c,"JUNK" $fail_path
fi

