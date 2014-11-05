#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: QPSK Receiver
# Author: MR
# Description: Receiver from GNU Radio tutorial 7, implemented with the USRP
# Generated: Wed Nov  5 13:29:46 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import sip
import sys
import time

from distutils.version import StrictVersion
class QPSK_Rx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QPSK Receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QPSK Receiver")
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

        self.settings = Qt.QSettings("GNU Radio", "QPSK_Rx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sym_rate = sym_rate = 500000
        self.samp_rate = samp_rate = 4000000
        self.sps = sps = int(samp_rate/sym_rate)
        self.nfilts = nfilts = 32
        self.trans_width = trans_width = 10000
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.sps_out = sps_out = 2
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw = phase_bw = 6.28/100.0
        self.filter_gain = filter_gain = 1
        self.eq_gain = eq_gain = 0.01
        self.co_freq = co_freq = 2*int(samp_rate*sym_rate/samp_rate)
        self.car_freq = car_freq = 1000000
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self.param_tabs = Qt.QTabWidget()
        self.param_tabs_widget_0 = Qt.QWidget()
        self.param_tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.param_tabs_widget_0)
        self.param_tabs_grid_layout_0 = Qt.QGridLayout()
        self.param_tabs_layout_0.addLayout(self.param_tabs_grid_layout_0)
        self.param_tabs.addTab(self.param_tabs_widget_0, "LPF")
        self.param_tabs_widget_1 = Qt.QWidget()
        self.param_tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.param_tabs_widget_1)
        self.param_tabs_grid_layout_1 = Qt.QGridLayout()
        self.param_tabs_layout_1.addLayout(self.param_tabs_grid_layout_1)
        self.param_tabs.addTab(self.param_tabs_widget_1, "Receiver")
        self.top_grid_layout.addWidget(self.param_tabs, 2,1,1,1)
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
        self.param_tabs_grid_layout_0.addLayout(self._trans_width_layout, 1,0,1,1)
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
        self.param_tabs_grid_layout_1.addLayout(self._timing_loop_bw_layout, 0,0,1,1)
        self._phase_bw_layout = Qt.QHBoxLayout()
        self._phase_bw_layout.addWidget(Qt.QLabel("Phase Loop BW  "+": "))
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
        self.param_tabs_grid_layout_1.addLayout(self._phase_bw_layout, 2,0,1,1)
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
        self.param_tabs_grid_layout_0.addLayout(self._filter_gain_layout, 2,0,1,1)
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
        self.top_grid_layout.addWidget(self.fig_tabs, 1,1,1,1)
        self._eq_gain_layout = Qt.QHBoxLayout()
        self._eq_gain_layout.addWidget(Qt.QLabel("Equalizer Gain    "+": "))
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
        self.param_tabs_grid_layout_1.addLayout(self._eq_gain_layout, 1,0,1,1)
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
        self.param_tabs_grid_layout_0.addLayout(self._co_freq_layout, 0,0,1,1)
        self._car_freq_layout = Qt.QHBoxLayout()
        self._car_freq_layout.addWidget(Qt.QLabel("Carrier Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._car_freq_counter = qwt_counter_pyslot()
        self._car_freq_counter.setRange(0, 5000000, 100000)
        self._car_freq_counter.setNumButtons(2)
        self._car_freq_counter.setMinimumWidth(200)
        self._car_freq_counter.setValue(self.car_freq)
        self._car_freq_layout.addWidget(self._car_freq_counter)
        self._car_freq_counter.valueChanged.connect(self.set_car_freq)
        self.top_grid_layout.addLayout(self._car_freq_layout, 3,1,1,1)
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
        self.qtgui_sink_x_0_2 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps_out/sps, #bw
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_2.set_update_time(1.0/10)
        self._qtgui_sink_x_0_2_win = sip.wrapinstance(self.qtgui_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.fig_tabs_layout_2.addWidget(self._qtgui_sink_x_0_2_win)
        
        self.qtgui_sink_x_0_2.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*sps_out/sps, #bw
        	"QT GUI Plot", #name
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
        	"QT GUI Plot", #name
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
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.fig_tabs_layout_3.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	filter_gain, samp_rate, co_freq, trans_width, firdes.WIN_RECTANGULAR, 6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 2, sps_out)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(11, 1, eq_gain, sps_out)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((10, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_sink_x_0_2, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QPSK_Rx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate
        self.set_sps(int(self.samp_rate/self.sym_rate))
        self.set_co_freq(2*int(self.samp_rate*self.sym_rate/self.samp_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(int(self.samp_rate/self.sym_rate))
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0_2.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))
        self.set_co_freq(2*int(self.samp_rate*self.sym_rate/self.samp_rate))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.qtgui_sink_x_0_2.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
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
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))
        Qt.QMetaObject.invokeMethod(self._trans_width_counter, "setValue", Qt.Q_ARG("double", self.trans_width))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        Qt.QMetaObject.invokeMethod(self._timing_loop_bw_counter, "setValue", Qt.Q_ARG("double", self.timing_loop_bw))
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_sps_out(self):
        return self.sps_out

    def set_sps_out(self, sps_out):
        self.sps_out = sps_out
        self.qtgui_sink_x_0_2.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.samp_rate*self.sps_out/self.sps)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.set_taps((self.rrc_taps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)
        Qt.QMetaObject.invokeMethod(self._phase_bw_counter, "setValue", Qt.Q_ARG("double", self.phase_bw))

    def get_filter_gain(self):
        return self.filter_gain

    def set_filter_gain(self, filter_gain):
        self.filter_gain = filter_gain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))
        Qt.QMetaObject.invokeMethod(self._filter_gain_counter, "setValue", Qt.Q_ARG("double", self.filter_gain))

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_cma_equalizer_cc_0.set_gain(self.eq_gain)
        Qt.QMetaObject.invokeMethod(self._eq_gain_counter, "setValue", Qt.Q_ARG("double", self.eq_gain))

    def get_co_freq(self):
        return self.co_freq

    def set_co_freq(self, co_freq):
        self.co_freq = co_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.filter_gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_RECTANGULAR, 6.76))
        Qt.QMetaObject.invokeMethod(self._co_freq_counter, "setValue", Qt.Q_ARG("double", self.co_freq))

    def get_car_freq(self):
        return self.car_freq

    def set_car_freq(self, car_freq):
        self.car_freq = car_freq
        self.uhd_usrp_source_0.set_center_freq(self.car_freq, 0)
        Qt.QMetaObject.invokeMethod(self._car_freq_counter, "setValue", Qt.Q_ARG("double", self.car_freq))

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
    tb = QPSK_Rx()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
