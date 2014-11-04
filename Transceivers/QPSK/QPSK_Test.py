#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: QPSK Test
# Author: MR (Edited from GNU Radio Tutorial 7)
# Description: QPSK Modulator / Receiver with simulated channel
# Generated: Tue Nov  4 15:03:50 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy
import sip
import sys

from distutils.version import StrictVersion
class QPSK_Test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QPSK Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QPSK Test")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "QPSK_Test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sym_rate = sym_rate = 500000
        self.samp_rate = samp_rate = 2000000
        self.sps = sps = int(samp_rate/sym_rate)
        self.nfilts = nfilts = 32
        self.trans_width = trans_width = 10000
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.time_offset = time_offset = 1.00
        self.taps = taps = [1.0 + 0.0j, ]
        self.sps_out = sps_out = 2
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.qpsk = qpsk = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.phase_bw = phase_bw = 6.28/100.0
        self.noise_volt = noise_volt = 0.0001
        self.freq_offset = freq_offset = 0
        self.filter_gain = filter_gain = 1
        self.excess_bw = excess_bw = 0.35
        self.eq_gain = eq_gain = 0.01
        self.co_freq = co_freq = samp_rate/2
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self.controls = Qt.QTabWidget()
        self.controls_widget_0 = Qt.QWidget()
        self.controls_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_0)
        self.controls_grid_layout_0 = Qt.QGridLayout()
        self.controls_layout_0.addLayout(self.controls_grid_layout_0)
        self.controls.addTab(self.controls_widget_0, "Channel")
        self.controls_widget_1 = Qt.QWidget()
        self.controls_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_1)
        self.controls_grid_layout_1 = Qt.QGridLayout()
        self.controls_layout_1.addLayout(self.controls_grid_layout_1)
        self.controls.addTab(self.controls_widget_1, "LPF")
        self.controls_widget_2 = Qt.QWidget()
        self.controls_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.controls_widget_2)
        self.controls_grid_layout_2 = Qt.QGridLayout()
        self.controls_layout_2.addLayout(self.controls_grid_layout_2)
        self.controls.addTab(self.controls_widget_2, "Receiver")
        self.top_grid_layout.addWidget(self.controls, 0,0,1,1)
        self._trans_width_layout = Qt.QHBoxLayout()
        self._trans_width_layout.addWidget(Qt.QLabel("Transition Width"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._trans_width_counter = qwt_counter_pyslot()
        self._trans_width_counter.setRange(1000, 100000, 1000)
        self._trans_width_counter.setNumButtons(2)
        self._trans_width_counter.setMinimumWidth(200)
        self._trans_width_counter.setValue(self.trans_width)
        self._trans_width_layout.addWidget(self._trans_width_counter)
        self._trans_width_counter.valueChanged.connect(self.set_trans_width)
        self.controls_grid_layout_1.addLayout(self._trans_width_layout, 1,0,1,1)
        self._timing_loop_bw_layout = Qt.QHBoxLayout()
        self._timing_loop_bw_layout.addWidget(Qt.QLabel("Timing Loop BW "+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._timing_loop_bw_counter = qwt_counter_pyslot()
        self._timing_loop_bw_counter.setRange(0.0, 0.2, 0.01)
        self._timing_loop_bw_counter.setNumButtons(2)
        self._timing_loop_bw_counter.setMinimumWidth(200)
        self._timing_loop_bw_counter.setValue(self.timing_loop_bw)
        self._timing_loop_bw_layout.addWidget(self._timing_loop_bw_counter)
        self._timing_loop_bw_counter.valueChanged.connect(self.set_timing_loop_bw)
        self.controls_grid_layout_2.addLayout(self._timing_loop_bw_layout,  0,0,1,1)
        self._time_offset_layout = Qt.QHBoxLayout()
        self._time_offset_layout.addWidget(Qt.QLabel("Timing Offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._time_offset_counter = qwt_counter_pyslot()
        self._time_offset_counter.setRange(0.995, 1.005, 0.0001)
        self._time_offset_counter.setNumButtons(2)
        self._time_offset_counter.setMinimumWidth(200)
        self._time_offset_counter.setValue(self.time_offset)
        self._time_offset_layout.addWidget(self._time_offset_counter)
        self._time_offset_counter.valueChanged.connect(self.set_time_offset)
        self.controls_grid_layout_0.addLayout(self._time_offset_layout,  1,0,1,1)
        self._phase_bw_layout = Qt.QHBoxLayout()
        self._phase_bw_layout.addWidget(Qt.QLabel("Phase Loop BW   "+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._phase_bw_counter = qwt_counter_pyslot()
        self._phase_bw_counter.setRange(0.0, 1.0, 0.01)
        self._phase_bw_counter.setNumButtons(2)
        self._phase_bw_counter.setMinimumWidth(200)
        self._phase_bw_counter.setValue(self.phase_bw)
        self._phase_bw_layout.addWidget(self._phase_bw_counter)
        self._phase_bw_counter.valueChanged.connect(self.set_phase_bw)
        self.controls_grid_layout_2.addLayout(self._phase_bw_layout,  2,0,1,1)
        self._noise_volt_layout = Qt.QHBoxLayout()
        self._noise_volt_layout.addWidget(Qt.QLabel("Noise Voltage"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._noise_volt_counter = qwt_counter_pyslot()
        self._noise_volt_counter.setRange(0, 1, 0.01)
        self._noise_volt_counter.setNumButtons(2)
        self._noise_volt_counter.setMinimumWidth(200)
        self._noise_volt_counter.setValue(self.noise_volt)
        self._noise_volt_layout.addWidget(self._noise_volt_counter)
        self._noise_volt_counter.valueChanged.connect(self.set_noise_volt)
        self.controls_grid_layout_0.addLayout(self._noise_volt_layout,  0,0,1,1)
        self._freq_offset_layout = Qt.QHBoxLayout()
        self._freq_offset_layout.addWidget(Qt.QLabel("Frequency Offset"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._freq_offset_counter = qwt_counter_pyslot()
        self._freq_offset_counter.setRange(-0.1, 0.1, 0.001)
        self._freq_offset_counter.setNumButtons(2)
        self._freq_offset_counter.setMinimumWidth(200)
        self._freq_offset_counter.setValue(self.freq_offset)
        self._freq_offset_layout.addWidget(self._freq_offset_counter)
        self._freq_offset_counter.valueChanged.connect(self.set_freq_offset)
        self.controls_grid_layout_0.addLayout(self._freq_offset_layout,  2,0,1,1)
        self._filter_gain_layout = Qt.QHBoxLayout()
        self._filter_gain_layout.addWidget(Qt.QLabel("Filter Gain"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._filter_gain_counter = qwt_counter_pyslot()
        self._filter_gain_counter.setRange(1, 10, 1)
        self._filter_gain_counter.setNumButtons(2)
        self._filter_gain_counter.setMinimumWidth(200)
        self._filter_gain_counter.setValue(self.filter_gain)
        self._filter_gain_layout.addWidget(self._filter_gain_counter)
        self._filter_gain_counter.valueChanged.connect(self.set_filter_gain)
        self.controls_grid_layout_1.addLayout(self._filter_gain_layout, 2,0,1,1)
        self.fig_tabs = Qt.QTabWidget()
        self.fig_tabs_widget_0 = Qt.QWidget()
        self.fig_tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.fig_tabs_widget_0)
        self.fig_tabs_grid_layout_0 = Qt.QGridLayout()
        self.fig_tabs_layout_0.addLayout(self.fig_tabs_grid_layout_0)
        self.fig_tabs.addTab(self.fig_tabs_widget_0, "LPF output")
        self.fig_tabs_widget_1 = Qt.QWidget()
        self.fig_tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.fig_tabs_widget_1)
        self.fig_tabs_grid_layout_1 = Qt.QGridLayout()
        self.fig_tabs_layout_1.addLayout(self.fig_tabs_grid_layout_1)
        self.fig_tabs.addTab(self.fig_tabs_widget_1, "PFB output")
        self.fig_tabs_widget_2 = Qt.QWidget()
        self.fig_tabs_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.fig_tabs_widget_2)
        self.fig_tabs_grid_layout_2 = Qt.QGridLayout()
        self.fig_tabs_layout_2.addLayout(self.fig_tabs_grid_layout_2)
        self.fig_tabs.addTab(self.fig_tabs_widget_2, "CMA output")
        self.fig_tabs_widget_3 = Qt.QWidget()
        self.fig_tabs_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.fig_tabs_widget_3)
        self.fig_tabs_grid_layout_3 = Qt.QGridLayout()
        self.fig_tabs_layout_3.addLayout(self.fig_tabs_grid_layout_3)
        self.fig_tabs.addTab(self.fig_tabs_widget_3, "Costas output")
        self.top_grid_layout.addWidget(self.fig_tabs, 1,0,1,2)
        self._eq_gain_layout = Qt.QHBoxLayout()
        self._eq_gain_layout.addWidget(Qt.QLabel("Equalizer Gain     "+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._eq_gain_counter = qwt_counter_pyslot()
        self._eq_gain_counter.setRange(0.0, 0.1, 0.001)
        self._eq_gain_counter.setNumButtons(2)
        self._eq_gain_counter.setMinimumWidth(200)
        self._eq_gain_counter.setValue(self.eq_gain)
        self._eq_gain_layout.addWidget(self._eq_gain_counter)
        self._eq_gain_counter.valueChanged.connect(self.set_eq_gain)
        self.controls_grid_layout_2.addLayout(self._eq_gain_layout,  1,0,1,1)
        self._co_freq_layout = Qt.QHBoxLayout()
        self._co_freq_layout.addWidget(Qt.QLabel("Cutoff Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._co_freq_counter = qwt_counter_pyslot()
        self._co_freq_counter.setRange(0, samp_rate/2, 100000)
        self._co_freq_counter.setNumButtons(2)
        self._co_freq_counter.setMinimumWidth(200)
        self._co_freq_counter.setValue(self.co_freq)
        self._co_freq_layout.addWidget(self._co_freq_counter)
        self._co_freq_counter.valueChanged.connect(self.set_co_freq)
        self.controls_grid_layout_1.addLayout(self._co_freq_layout, 0,0,1,1)
        self.qtgui_sink_x_0_2 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps_out/sps, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_2.set_update_time(1.0/10)
        self._qtgui_sink_x_0_2_win = sip.wrapinstance(self.qtgui_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.fig_tabs_layout_3.addWidget(self._qtgui_sink_x_0_2_win)
        
        self.qtgui_sink_x_0_2.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps_out/sps, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.fig_tabs_layout_1.addWidget(self._qtgui_sink_x_0_1_win)
        
        self.qtgui_sink_x_0_1.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.fig_tabs_layout_0.addWidget(self._qtgui_sink_x_0_0_win)
        
        self.qtgui_sink_x_0_0.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps_out/sps, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.fig_tabs_layout_2.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	filter_gain, samp_rate, co_freq, trans_width, firdes.WIN_RECTANGULAR, 6.76))
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=arity,
          mod_code="gray",
          differential=True,
          samples_per_symbol=sps,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 1.5, sps_out)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(11, 1, eq_gain, sps_out)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_volt,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(taps),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_psk_mod_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_sink_x_0_2, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QPSK_Test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate
        self.set_sps(int(self.samp_rate/self.sym_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(int(self.samp_rate/self.sym_rate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_2.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.set_co_freq(self.samp_rate/2)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_2.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width
        Qt.QMetaObject.invokeMethod(self._trans_width_counter, "setValue", Qt.Q_ARG("double", self.trans_width))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        Qt.QMetaObject.invokeMethod(self._timing_loop_bw_counter, "setValue", Qt.Q_ARG("double", self.timing_loop_bw))
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)
        Qt.QMetaObject.invokeMethod(self._time_offset_counter, "setValue", Qt.Q_ARG("double", self.time_offset))

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0.set_taps((self.taps))

    def get_sps_out(self):
        return self.sps_out

    def set_sps_out(self, sps_out):
        self.sps_out = sps_out
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_2.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.set_taps((self.rrc_taps))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)
        Qt.QMetaObject.invokeMethod(self._phase_bw_counter, "setValue", Qt.Q_ARG("double", self.phase_bw))

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        Qt.QMetaObject.invokeMethod(self._noise_volt_counter, "setValue", Qt.Q_ARG("double", self.noise_volt))
        self.channels_channel_model_0.set_noise_voltage(self.noise_volt)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        Qt.QMetaObject.invokeMethod(self._freq_offset_counter, "setValue", Qt.Q_ARG("double", self.freq_offset))
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_filter_gain(self):
        return self.filter_gain

    def set_filter_gain(self, filter_gain):
        self.filter_gain = filter_gain
        Qt.QMetaObject.invokeMethod(self._filter_gain_counter, "setValue", Qt.Q_ARG("double", self.filter_gain))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        Qt.QMetaObject.invokeMethod(self._eq_gain_counter, "setValue", Qt.Q_ARG("double", self.eq_gain))
        self.digital_cma_equalizer_cc_0.set_gain(self.eq_gain)

    def get_co_freq(self):
        return self.co_freq

    def set_co_freq(self, co_freq):
        self.co_freq = co_freq
        Qt.QMetaObject.invokeMethod(self._co_freq_counter, "setValue", Qt.Q_ARG("double", self.co_freq))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity

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
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = QPSK_Test()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
