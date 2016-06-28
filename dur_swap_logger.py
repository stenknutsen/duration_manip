import sys

##############################################
#
#   Logs some of the data captured/manipulated
#   by dur_swap.py in a txt file
#
#
##############################################


def create_log(actname, passname, actdur, passdur, actpd, passpd, newactdur, newpassdur, percact, percpass):

    file_name = ("/Users/stenknutsen/Desktop/IO_folder/hurt_"+ actname.split(".")[0]+"_log.txt")
    file = open(file_name,'a')
    file.write("ACTIVE FILE NAME: " + actname + "\n")
    file.write("DURATION: " + str(actdur) + "\n")
    file.write("PERIOD: " +str(actpd) + "\n")
    file.write("NEW DURATION:" + str(newactdur) + "\n")
    file.write("PERCENT LENGTHENED: " + str(percact) + "\n")
    file.write("..." + "\n")
    file.write("PASSIVE FILE NAME: " + passname + "\n")
    file.write("DURATION: " + str(passdur) + "\n")
    file.write("PERIOD: " +str(passpd) + "\n")
    file.write("NEW DURATION:" + str(newpassdur) + "\n")
    file.write("PERCENT LENGTHENED: " + str(percpass) + "\n")
    file.write("..." + "\n")
    file.close()




