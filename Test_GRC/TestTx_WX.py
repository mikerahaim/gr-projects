#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: USRP Signal Generator (WX)
# Author: MR
# Description: Generate a signal and send to the USRP
# Generated: Tue Nov  4 13:12:35 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class TestTx_WX(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="USRP Signal Generator (WX)")

        ##################################################
        # Variables
        ##################################################
        self.sig_freq_c = sig_freq_c = 0
        self.sig_freq = sig_freq = 100000
        self.sig_amp_c = sig_amp_c = 0
        self.sig_amp = sig_amp = 1
        self.samp_rate = samp_rate = 2000000
        self.car_freq = car_freq = 1000000

        ##################################################
        # Blocks
        ##################################################
        _sig_freq_c_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sig_freq_c_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sig_freq_c_sizer,
        	value=self.sig_freq_c,
        	callback=self.set_sig_freq_c,
        	label="Complex Signal Freq",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sig_freq_c_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sig_freq_c_sizer,
        	value=self.sig_freq_c,
        	callback=self.set_sig_freq_c,
        	minimum=0,
        	maximum=1000000,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sig_freq_c_sizer)
        _sig_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sig_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sig_freq_sizer,
        	value=self.sig_freq,
        	callback=self.set_sig_freq,
        	label="Real Signal Freq",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sig_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sig_freq_sizer,
        	value=self.sig_freq,
        	callback=self.set_sig_freq,
        	minimum=0,
        	maximum=1000000,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sig_freq_sizer)
        _sig_amp_c_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sig_amp_c_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sig_amp_c_sizer,
        	value=self.sig_amp_c,
        	callback=self.set_sig_amp_c,
        	label="Complex Signal Amp",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sig_amp_c_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sig_amp_c_sizer,
        	value=self.sig_amp_c,
        	callback=self.set_sig_amp_c,
        	minimum=0,
        	maximum=1,
        	num_steps=20,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sig_amp_c_sizer)
        _sig_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sig_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sig_amp_sizer,
        	value=self.sig_amp,
        	callback=self.set_sig_amp,
        	label="Real Signal Amp",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sig_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sig_amp_sizer,
        	value=self.sig_amp,
        	callback=self.set_sig_amp,
        	minimum=0,
        	maximum=1,
        	num_steps=20,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_sig_amp_sizer)
        _car_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._car_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_car_freq_sizer,
        	value=self.car_freq,
        	callback=self.set_car_freq,
        	label="car_freq_slider",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._car_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_car_freq_sizer,
        	value=self.car_freq,
        	callback=self.set_car_freq,
        	minimum=0,
        	maximum=5000000,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_car_freq_sizer)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(car_freq, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sig_freq_c, sig_amp_c, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sig_freq, sig_amp, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_float_to_complex_0, 1))



    def get_sig_freq_c(self):
        return self.sig_freq_c

    def set_sig_freq_c(self, sig_freq_c):
        self.sig_freq_c = sig_freq_c
        self._sig_freq_c_slider.set_value(self.sig_freq_c)
        self._sig_freq_c_text_box.set_value(self.sig_freq_c)
        self.analog_sig_source_x_0_0.set_frequency(self.sig_freq_c)

    def get_sig_freq(self):
        return self.sig_freq

    def set_sig_freq(self, sig_freq):
        self.sig_freq = sig_freq
        self.analog_sig_source_x_0.set_frequency(self.sig_freq)
        self._sig_freq_slider.set_value(self.sig_freq)
        self._sig_freq_text_box.set_value(self.sig_freq)

    def get_sig_amp_c(self):
        return self.sig_amp_c

    def set_sig_amp_c(self, sig_amp_c):
        self.sig_amp_c = sig_amp_c
        self._sig_amp_c_slider.set_value(self.sig_amp_c)
        self._sig_amp_c_text_box.set_value(self.sig_amp_c)
        self.analog_sig_source_x_0_0.set_amplitude(self.sig_amp_c)

    def get_sig_amp(self):
        return self.sig_amp

    def set_sig_amp(self, sig_amp):
        self.sig_amp = sig_amp
        self._sig_amp_slider.set_value(self.sig_amp)
        self._sig_amp_text_box.set_value(self.sig_amp)
        self.analog_sig_source_x_0.set_amplitude(self.sig_amp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_car_freq(self):
        return self.car_freq

    def set_car_freq(self, car_freq):
        self.car_freq = car_freq
        self.uhd_usrp_sink_0.set_center_freq(self.car_freq, 0)
        self._car_freq_slider.set_value(self.car_freq)
        self._car_freq_text_box.set_value(self.car_freq)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = TestTx_WX()
    tb.Start(True)
    tb.Wait()
