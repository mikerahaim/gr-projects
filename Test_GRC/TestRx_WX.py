#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: WX GUI signal reader (from USRP)
# Author: MR
# Description: Read input from USRP and display output with and without filtering
# Generated: Tue Nov  4 13:20:34 2014
##################################################

from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class TestRx_WX(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="WX GUI signal reader (from USRP)")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2000000
        self.filter_transition = filter_transition = 10000
        self.filter_gain = filter_gain = 1
        self.co_freq = co_freq = samp_rate/2
        self.car_freq = car_freq = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Signal")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Freq")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Signal (Filtered)")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Freq (Filtered)")
        self.GridAdd(self.notebook_0, 0, 0, 1, 4)
        _filter_transition_sizer = wx.BoxSizer(wx.VERTICAL)
        self._filter_transition_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_filter_transition_sizer,
        	value=self.filter_transition,
        	callback=self.set_filter_transition,
        	label="Filter Transition Width",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._filter_transition_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_filter_transition_sizer,
        	value=self.filter_transition,
        	callback=self.set_filter_transition,
        	minimum=1000,
        	maximum=100000,
        	num_steps=99,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_filter_transition_sizer, 2, 0, 1, 2)
        _filter_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._filter_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_filter_gain_sizer,
        	value=self.filter_gain,
        	callback=self.set_filter_gain,
        	label="Filter Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._filter_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_filter_gain_sizer,
        	value=self.filter_gain,
        	callback=self.set_filter_gain,
        	minimum=1,
        	maximum=32,
        	num_steps=31,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_filter_gain_sizer, 2, 2, 1, 2)
        _co_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._co_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_co_freq_sizer,
        	value=self.co_freq,
        	callback=self.set_co_freq,
        	label="Filter Cutoff Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._co_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_co_freq_sizer,
        	value=self.co_freq,
        	callback=self.set_co_freq,
        	minimum=0,
        	maximum=samp_rate/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_co_freq_sizer, 1, 0, 1, 2)
        _car_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._car_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_car_freq_sizer,
        	value=self.car_freq,
        	callback=self.set_car_freq,
        	label="Carrier Frequency",
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
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_car_freq_sizer, 1, 2, 1, 2)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(2).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(3).GetWin(),
        	baseband_freq=0,
        	y_per_div=5,
        	y_divs=10,
        	ref_level=-80,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(3).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=5,
        	y_divs=10,
        	ref_level=-80,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(car_freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	filter_gain, samp_rate, co_freq, filter_transition, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_scopesink2_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.filter_transition, firdes.WIN_HAMMING, 6.76))
        self.set_co_freq(self.samp_rate/2)

    def get_filter_transition(self):
        return self.filter_transition

    def set_filter_transition(self, filter_transition):
        self.filter_transition = filter_transition
        self._filter_transition_slider.set_value(self.filter_transition)
        self._filter_transition_text_box.set_value(self.filter_transition)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.filter_transition, firdes.WIN_HAMMING, 6.76))

    def get_filter_gain(self):
        return self.filter_gain

    def set_filter_gain(self, filter_gain):
        self.filter_gain = filter_gain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.filter_transition, firdes.WIN_HAMMING, 6.76))
        self._filter_gain_slider.set_value(self.filter_gain)
        self._filter_gain_text_box.set_value(self.filter_gain)

    def get_co_freq(self):
        return self.co_freq

    def set_co_freq(self, co_freq):
        self.co_freq = co_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.filter_transition, firdes.WIN_HAMMING, 6.76))
        self._co_freq_slider.set_value(self.co_freq)
        self._co_freq_text_box.set_value(self.co_freq)

    def get_car_freq(self):
        return self.car_freq

    def set_car_freq(self, car_freq):
        self.car_freq = car_freq
        self.uhd_usrp_source_0.set_center_freq(self.car_freq, 0)
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
    tb = TestRx_WX()
    tb.Start(True)
    tb.Wait()
