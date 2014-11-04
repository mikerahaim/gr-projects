#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: USRP Signal Generator (QT)
# Author: MR
# Description: Generate a signal and send to the USRP
# Generated: Tue Nov  4 13:11:22 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
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
class TestTx_QT(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "USRP Signal Generator (QT)")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("USRP Signal Generator (QT)")
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

        self.settings = Qt.QSettings("GNU Radio", "TestTx_QT")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sig_freq_r = sig_freq_r = 100000
        self.sig_freq_c = sig_freq_c = 0
        self.sig_amp_r = sig_amp_r = 1
        self.sig_amp_c = sig_amp_c = 0
        self.samp_rate = samp_rate = 2000000
        self.car_freq = car_freq = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.tab_widget = Qt.QTabWidget()
        self.tab_widget_widget_0 = Qt.QWidget()
        self.tab_widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_0)
        self.tab_widget_grid_layout_0 = Qt.QGridLayout()
        self.tab_widget_layout_0.addLayout(self.tab_widget_grid_layout_0)
        self.tab_widget.addTab(self.tab_widget_widget_0, "Real")
        self.tab_widget_widget_1 = Qt.QWidget()
        self.tab_widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_widget_1)
        self.tab_widget_grid_layout_1 = Qt.QGridLayout()
        self.tab_widget_layout_1.addLayout(self.tab_widget_grid_layout_1)
        self.tab_widget.addTab(self.tab_widget_widget_1, "Complex")
        self.top_layout.addWidget(self.tab_widget)
        self._sig_freq_r_layout = Qt.QHBoxLayout()
        self._sig_freq_r_layout.addWidget(Qt.QLabel("Real Signal Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._sig_freq_r_counter = qwt_counter_pyslot()
        self._sig_freq_r_counter.setRange(0, 1000000, 50000)
        self._sig_freq_r_counter.setNumButtons(2)
        self._sig_freq_r_counter.setMinimumWidth(200)
        self._sig_freq_r_counter.setValue(self.sig_freq_r)
        self._sig_freq_r_layout.addWidget(self._sig_freq_r_counter)
        self._sig_freq_r_counter.valueChanged.connect(self.set_sig_freq_r)
        self.tab_widget_layout_0.addLayout(self._sig_freq_r_layout)
        self._sig_freq_c_layout = Qt.QHBoxLayout()
        self._sig_freq_c_layout.addWidget(Qt.QLabel("Complex Signal Frequency"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._sig_freq_c_counter = qwt_counter_pyslot()
        self._sig_freq_c_counter.setRange(0, 1000000, 50000)
        self._sig_freq_c_counter.setNumButtons(2)
        self._sig_freq_c_counter.setMinimumWidth(200)
        self._sig_freq_c_counter.setValue(self.sig_freq_c)
        self._sig_freq_c_layout.addWidget(self._sig_freq_c_counter)
        self._sig_freq_c_counter.valueChanged.connect(self.set_sig_freq_c)
        self.tab_widget_layout_1.addLayout(self._sig_freq_c_layout)
        self._sig_amp_r_layout = Qt.QHBoxLayout()
        self._sig_amp_r_layout.addWidget(Qt.QLabel("Real Signal Amplitude"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._sig_amp_r_counter = qwt_counter_pyslot()
        self._sig_amp_r_counter.setRange(0, 1, 0.05)
        self._sig_amp_r_counter.setNumButtons(2)
        self._sig_amp_r_counter.setMinimumWidth(200)
        self._sig_amp_r_counter.setValue(self.sig_amp_r)
        self._sig_amp_r_layout.addWidget(self._sig_amp_r_counter)
        self._sig_amp_r_counter.valueChanged.connect(self.set_sig_amp_r)
        self.tab_widget_layout_0.addLayout(self._sig_amp_r_layout)
        self._sig_amp_c_layout = Qt.QHBoxLayout()
        self._sig_amp_c_layout.addWidget(Qt.QLabel("Complex Signal Amplitude"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._sig_amp_c_counter = qwt_counter_pyslot()
        self._sig_amp_c_counter.setRange(0, 1, 0.05)
        self._sig_amp_c_counter.setNumButtons(2)
        self._sig_amp_c_counter.setMinimumWidth(200)
        self._sig_amp_c_counter.setValue(self.sig_amp_c)
        self._sig_amp_c_layout.addWidget(self._sig_amp_c_counter)
        self._sig_amp_c_counter.valueChanged.connect(self.set_sig_amp_c)
        self.tab_widget_layout_1.addLayout(self._sig_amp_c_layout)
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
        self.top_layout.addLayout(self._car_freq_layout)
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
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sig_freq_c, sig_amp_c, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, sig_freq_r, sig_amp_r, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TestTx_QT")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sig_freq_r(self):
        return self.sig_freq_r

    def set_sig_freq_r(self, sig_freq_r):
        self.sig_freq_r = sig_freq_r
        self.analog_sig_source_x_0.set_frequency(self.sig_freq_r)
        Qt.QMetaObject.invokeMethod(self._sig_freq_r_counter, "setValue", Qt.Q_ARG("double", self.sig_freq_r))

    def get_sig_freq_c(self):
        return self.sig_freq_c

    def set_sig_freq_c(self, sig_freq_c):
        self.sig_freq_c = sig_freq_c
        Qt.QMetaObject.invokeMethod(self._sig_freq_c_counter, "setValue", Qt.Q_ARG("double", self.sig_freq_c))
        self.analog_sig_source_x_0_0.set_frequency(self.sig_freq_c)

    def get_sig_amp_r(self):
        return self.sig_amp_r

    def set_sig_amp_r(self, sig_amp_r):
        self.sig_amp_r = sig_amp_r
        Qt.QMetaObject.invokeMethod(self._sig_amp_r_counter, "setValue", Qt.Q_ARG("double", self.sig_amp_r))
        self.analog_sig_source_x_0.set_amplitude(self.sig_amp_r)

    def get_sig_amp_c(self):
        return self.sig_amp_c

    def set_sig_amp_c(self, sig_amp_c):
        self.sig_amp_c = sig_amp_c
        Qt.QMetaObject.invokeMethod(self._sig_amp_c_counter, "setValue", Qt.Q_ARG("double", self.sig_amp_c))
        self.analog_sig_source_x_0_0.set_amplitude(self.sig_amp_c)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_car_freq(self):
        return self.car_freq

    def set_car_freq(self, car_freq):
        self.car_freq = car_freq
        Qt.QMetaObject.invokeMethod(self._car_freq_counter, "setValue", Qt.Q_ARG("double", self.car_freq))
        self.uhd_usrp_sink_0.set_center_freq(self.car_freq, 0)

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
    tb = TestTx_QT()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
