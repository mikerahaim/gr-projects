#!/bin/bash
######################################################################
# receive_video.sh                                                   #
# Author: Michael Rahaim                                             #
#                                                                    #
# Description: This is a simple bash script to run the GMSK receiver #
#   which outputs to rxfifo.ogg. The output is then played via       #
#   mplayer to show a real time video stream.                        #
#                                                                    #
######################################################################
python SV_receiver_GMSK.py &

mplayer -cache 500 -cache-min 20 rxfifo.ogg
