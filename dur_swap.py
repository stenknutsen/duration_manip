import sys
from os import listdir
from open_and_extract import extract_xmin_xmax
from open_and_extract import extract_period
from vst import vowel_strectching_time
from dur_swap_logger import create_log

##############################################
#
#   Extracts active/passive verb stem vowel 
#   information from Praat TextGrid files and
#   creates new Duration Tiers which will
#   effectively "swap" the duration of the
#   active and passive verb stems.
#
#
#
##############################################


input_filenames_raw = listdir("/Users/stenknutsen/Desktop/IO_folder")


input_filenames=[]
for f in input_filenames_raw:
    if f.startswith("."):
        continue
    else:
        input_filenames.append(f)


active_filename = input_filenames[0]
passive_filename = input_filenames[1]


active_xmin_xmax = extract_xmin_xmax("/Users/stenknutsen/Desktop/IO_folder/"+ active_filename)
passive_xmin_xmax = extract_xmin_xmax("/Users/stenknutsen/Desktop/IO_folder/"+ passive_filename)

active_xmin = active_xmin_xmax["xmin"]
active_xmax = active_xmin_xmax["xmax"]

passive_xmin = passive_xmin_xmax["xmin"]
passive_xmax = passive_xmin_xmax["xmax"]


active_vowel_dur = active_xmax - active_xmin
passive_vowel_dur = passive_xmax - passive_xmin


active_period = extract_period("/Users/stenknutsen/Desktop/IO_folder/" + active_filename)

passive_period = extract_period("/Users/stenknutsen/Desktop/IO_folder/" + passive_filename)


#let the swapping begin!
#
new_active_vowel_dur = active_vowel_dur
new_passive_vowel_dur = passive_vowel_dur

while (new_active_vowel_dur<passive_vowel_dur):
    new_active_vowel_dur = new_active_vowel_dur + active_period


while (new_passive_vowel_dur>active_vowel_dur):
    new_passive_vowel_dur = new_passive_vowel_dur - passive_period


#Find percentage increase/decrease for active/passive
#
percent_lengthen_active = (new_active_vowel_dur/active_vowel_dur)-1

percent_shorten_passive = (-1)*(1-(new_passive_vowel_dur/passive_vowel_dur))


#Create log for set of files
#
create_log(active_filename,passive_filename,active_vowel_dur,passive_vowel_dur,active_period,
           passive_period,new_active_vowel_dur,new_passive_vowel_dur,percent_lengthen_active,percent_shorten_passive)


#Create Durataion Tiers
#
vowel_strectching_time(active_filename, active_xmin, active_xmax, percent_lengthen_active)
vowel_strectching_time(passive_filename, passive_xmin, passive_xmax, percent_shorten_passive)








