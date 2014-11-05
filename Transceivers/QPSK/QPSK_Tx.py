#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: QPSK Tx
# Author: MR
# Description: QPSK Transmitter
# Generated: Wed Nov  5 13:57:27 2014
##################################################

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy
import sip
import sys
import time

from distutils.version import StrictVersion
class QPSK_Tx(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "QPSK Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("QPSK Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "QPSK_Tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sym_rate = sym_rate = 500000
        self.samp_rate = samp_rate = 2000000
        self.sps = sps = int(samp_rate/sym_rate)
        self.sig_amp = sig_amp = 0.5
        self.qpsk = qpsk = digital.constellation_rect(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 2, 3]), 4, 2, 2, 1, 1).base()
        self.car_freq = car_freq = 1000000
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._sig_amp_layout = Qt.QHBoxLayout()
        self._sig_amp_layout.addWidget(Qt.QLabel("Signal Amplitude"+": "))
        class qwt_counter_pyslot(Qwt.QwtCounter):
            def __init__(self, parent=None):
                Qwt.QwtCounter.__init__(self, parent)
            @pyqtSlot('double')
            def setValue(self, value):
                super(Qwt.QwtCounter, self).setValue(value)
        self._sig_amp_counter = qwt_counter_pyslot()
        self._sig_amp_counter.setRange(0, 1, 0.05)
        self._sig_amp_counter.setNumButtons(2)
        self._sig_amp_counter.setMinimumWidth(200)
        self._sig_amp_counter.setValue(self.sig_amp)
        self._sig_amp_layout.addWidget(self._sig_amp_counter)
        self._sig_amp_counter.valueChanged.connect(self.set_sig_amp)
        self.top_layout.addLayout(self._sig_amp_layout)
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
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(False)
        
        
          
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=qpsk,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((sig_amp, ))
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "QPSK_Tx")
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
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_sig_amp(self):
        return self.sig_amp

    def set_sig_amp(self, sig_amp):
        self.sig_amp = sig_amp
        Qt.QMetaObject.invokeMethod(self._sig_amp_counter, "setValue", Qt.Q_ARG("double", self.sig_amp))
        self.blocks_multiply_const_vxx_0.set_k((self.sig_amp, ))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_car_freq(self):
        return self.car_freq

    def set_car_freq(self, car_freq):
        self.car_freq = car_freq
        Qt.QMetaObject.invokeMethod(self._car_freq_counter, "setValue", Qt.Q_ARG("double", self.car_freq))
        self.uhd_usrp_sink_0.set_center_freq(self.car_freq, 0)

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
    tb = QPSK_Tx()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
