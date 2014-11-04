#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: QT GUI signal reader (from USRP)
# Author: MR
# Description: Read input from USRP and display output with and without filtering
# Generated: Tue Nov  4 13:11:30 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
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
class TestRx_QT(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QT GUI signal reader (from USRP)")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QT GUI signal reader (from USRP)")
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

        self.settings = Qt.QSettings("GNU Radio", "TestRx_QT")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2000000
        self.trans_width = trans_width = 10000
        self.gain = gain = 1
        self.co_freq = co_freq = samp_rate/2
        self.car_freq = car_freq = 1000000

        ##################################################
        # Blocks
        ##################################################
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
        self.top_grid_layout.addLayout(self._trans_width_layout, 4,1,1,1)
        self.tab_widget = Qt.QTabWidget()
        self.tab_widget_widget_0 = Qt.QWidget()
        self.tab_widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_0)
        self.tab_widget_grid_layout_0 = Qt.QGridLayout()
        self.tab_widget_layout_0.addLayout(self.tab_widget_grid_layout_0)
        self.tab_widget.addTab(self.tab_widget_widget_0, "Unfiltered")
        self.tab_widget_widget_1 = Qt.QWidget()
        self.tab_widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_1)
        self.tab_widget_grid_layout_1 = Qt.QGridLayout()
        self.tab_widget_layout_1.addLayout(self.tab_widget_grid_layout_1)
        self.tab_widget.addTab(self.tab_widget_widget_1, "Filtered")
        self.top_grid_layout.addWidget(self.tab_widget, 1,1,1,1)
        self._gain_layout = Qt.QHBoxLayout()
        self._gain_layout.addWidget(Qt.QLabel("Filter Gain"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._gain_counter = qwt_counter_pyslot()
        self._gain_counter.setRange(1, 10, 1)
        self._gain_counter.setNumButtons(2)
        self._gain_counter.setMinimumWidth(200)
        self._gain_counter.setValue(self.gain)
        self._gain_layout.addWidget(self._gain_counter)
        self._gain_counter.valueChanged.connect(self.set_gain)
        self.top_grid_layout.addLayout(self._gain_layout, 5,1,1,1)
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
        self.top_grid_layout.addLayout(self._co_freq_layout, 3,1,1,1)
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
        self.top_grid_layout.addLayout(self._car_freq_layout, 2,1,1,1)
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
        self.tab_widget_layout_1.addWidget(self._qtgui_sink_x_0_0_win)
        
        self.qtgui_sink_x_0_0.enable_rf_freq(False)
        
        
          
        self.qtgui_sink_x_0 = qtgui.sink_c(
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
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_widget_layout_0.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	gain, samp_rate, co_freq, trans_width, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TestRx_QT")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))
        self.set_co_freq(self.samp_rate/2)

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))
        Qt.QMetaObject.invokeMethod(self._trans_width_counter, "setValue", Qt.Q_ARG("double", self.trans_width))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))
        Qt.QMetaObject.invokeMethod(self._gain_counter, "setValue", Qt.Q_ARG("double", self.gain))

    def get_co_freq(self):
        return self.co_freq

    def set_co_freq(self, co_freq):
        self.co_freq = co_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.gain, self.samp_rate, self.co_freq, self.trans_width, firdes.WIN_HAMMING, 6.76))
        Qt.QMetaObject.invokeMethod(self._co_freq_counter, "setValue", Qt.Q_ARG("double", self.co_freq))

    def get_car_freq(self):
        return self.car_freq

    def set_car_freq(self, car_freq):
        self.car_freq = car_freq
        self.uhd_usrp_source_0.set_center_freq(self.car_freq, 0)
        Qt.QMetaObject.invokeMethod(self._car_freq_counter, "setValue", Qt.Q_ARG("double", self.car_freq))

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
    tb = TestRx_QT()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
