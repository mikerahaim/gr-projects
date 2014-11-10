#!/bin/bash
###############################################################
# stream_video.sh
# Author: Michael Rahaim
#
# DescriptionThis is the bash script with various gstreamer
#   programs to play video / audio files. The python GMSK 
#   transmitter is run in the background and gstreamer sends
#   its output file to a pipe which is read and processed for
#   trasmission over the USRP.
#
###############################################################
clear
echo "Beginning Video Stream"

python SV_transmitter_GMSK.py &

#Webcam Video Stream
gst-launch v4l2src device=/dev/video0 ! queue ! videorate ! video/x-raw-yuv,width=320,height=240,framerate=17/1 ! tee name=tvid ! queue ! xvimagesink sync=false tvid. ! theoraenc ! queue ! oggmux ! filesink location=txfifo.ogg 


#Playback the online video (with audio)
#gst-launch-0.10 souphttpsrc location=http://docs.gstreamer.com/media/sintel_trailer-480p.webm ! matroskademux name=d ! queue ! vp8dec ! ffmpegcolorspace ! autovideosink d. ! queue ! vorbisdec ! audioconvert ! audioresample ! autoaudiosink


#Stream Online Video
#gst-launch-0.10 uridecodebin uri=http://docs.gstreamer.com/media/sintel_trailer-480p.webm name=d ! queue ! videoscale ! video/x-raw-yuv,width=320,height=200 ! queue ! theoraenc ! oggmux name=m ! filesink location=txfifo.ogg d. ! queue ! audioconvert ! audioresample ! flacenc ! m.


#Webcam Video Stream
#gst-launch v4l2src device=/dev/video0 ! queue ! videorate ! video/x-raw-yuv,width=320,height=240,framerate=17/1 ! queue ! xvimagesink sync=false


#Webcam Audio Stream
#gst-launch alsasrc ! audioconvert ! vorbisenc ! oggmux ! filesink location=txfifo.ogg


#music Audio Stream
#gst-launch filesrc location=music.mp3 ! mad ! audioconvert ! audioresample ! vorbisenc ! oggmux ! filesink location=txfifo.ogg


#Webcam Video and Audio Stream
#gst-launch v4l2src device=/dev/video0 ! \
#tee name=t_vid ! queue ! xvimagesink sync=false t_vid. ! queue ! videorate ! \
#video/x-raw-yuv,width=320,height=240,framerate=18/1 ! theoraenc ! queue ! mux. \
#alsasrc ! audio/x-raw-int,rate=48000,channels=2,depth=16 ! \
#queue ! audioconvert ! queue ! vorbisenc ! queue ! mux. \
#oggmux name=mux ! filesink location=txfifo.ogg

