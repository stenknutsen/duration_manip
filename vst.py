import sys

##############################################
#
#   Calculates the "curve" for the Duration
#   Tier from data extracted by dur_swap.py
#   and creates a new Praat duration tier
#   file.
#
#
#
#
##############################################


def vowel_strectching_time(file_name, begin_v, end_v, percent_legnthen):

    dif = end_v - begin_v
    perc = float(dif*0.40)
    begin_vowel = begin_v+perc
    end_vowel = end_v - perc

    total_area = end_v - begin_v
    midpoint = float((end_v-begin_v)/2.0)+begin_v
    new_area = float(percent_legnthen*total_area)
    x = float((end_vowel-begin_vowel)/2.0)
    y = float(new_area/x)

    tier_name = ("dur_"+ file_name.split(".")[0])

    file_name = ("/Users/stenknutsen/Desktop/IO_folder/dur_"+file_name.split(".")[0]+".praat")
    
    file = open(file_name,'a')
    file.write('Create DurationTier: \"'+tier_name+'\", '+ str(begin_vowel)+', '+str(end_vowel)+'\n')
    file.write('Add point: '+str(begin_vowel)+', 1\n')
    file.write('Add point: '+str(midpoint)+', '+str(y+1.0)+'\n')
    file.write('Add point: '+str(end_vowel)+', 1\n')

    file.close()

