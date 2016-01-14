#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Two Channel PRB Sequence
# Generated: Thu Jan 14 14:24:24 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sys
import time


class PRBS_Two_Channel(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Two Channel PRB Sequence")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Two Channel PRB Sequence")
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

        self.settings = Qt.QSettings("GNU Radio", "PRBS_Two_Channel")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 3000000
        self.my_rate = my_rate = 100000
        self.my_amp2 = my_amp2 = 0.5
        self.my_amp1 = my_amp1 = 0.7
        self.interp = interp = samp_rate/my_rate

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_options = (1500000, 3000000, 6000000, 12000000, 20000000, )
        self._samp_rate_labels = ("1.5M", "3M", "6M", "12M", "20M", )
        self._samp_rate_group_box = Qt.QGroupBox("Sample Rate (NOTE: Keep Sample Rate higher than symbol rate!)")
        self._samp_rate_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._samp_rate_button_group = variable_chooser_button_group()
        self._samp_rate_group_box.setLayout(self._samp_rate_box)
        for i, label in enumerate(self._samp_rate_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._samp_rate_box.addWidget(radio_button)
        	self._samp_rate_button_group.addButton(radio_button, i)
        self._samp_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._samp_rate_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._samp_rate_options.index(i)))
        self._samp_rate_callback(self.samp_rate)
        self._samp_rate_button_group.buttonClicked[int].connect(
        	lambda i: self.set_samp_rate(self._samp_rate_options[i]))
        self.top_layout.addWidget(self._samp_rate_group_box)
        self._my_amp2_range = Range(0, 1, 0.05, 0.5, 200)
        self._my_amp2_win = RangeWidget(self._my_amp2_range, self.set_my_amp2, "Amplitude 2", "counter_slider", float)
        self.top_layout.addWidget(self._my_amp2_win)
        self._my_amp1_range = Range(0, 1, 0.05, 0.7, 200)
        self._my_amp1_win = RangeWidget(self._my_amp1_range, self.set_my_amp1, "Amplitude 1", "counter_slider", float)
        self.top_layout.addWidget(self._my_amp1_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_rate(200e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self._my_rate_options = (100000, 500000, 1000000, 2000000, 4000000, )
        self._my_rate_labels = ("100K", "500K", "1M", "2M", "4M", )
        self._my_rate_group_box = Qt.QGroupBox("Symbol Rate")
        self._my_rate_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._my_rate_button_group = variable_chooser_button_group()
        self._my_rate_group_box.setLayout(self._my_rate_box)
        for i, label in enumerate(self._my_rate_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._my_rate_box.addWidget(radio_button)
        	self._my_rate_button_group.addButton(radio_button, i)
        self._my_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._my_rate_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._my_rate_options.index(i)))
        self._my_rate_callback(self.my_rate)
        self._my_rate_button_group.buttonClicked[int].connect(
        	lambda i: self.set_my_rate(self._my_rate_options[i]))
        self.top_layout.addWidget(self._my_rate_group_box)
        self.blocks_vector_source_x_0 = blocks.vector_source_f((0, my_amp1), True, 1, [])
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, interp)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_int*1, interp)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1/my_amp2)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_int_to_float_0, 0))    
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PRBS_Two_Channel")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self._samp_rate_callback(self.samp_rate)
        self.set_interp(self.samp_rate/self.my_rate)

    def get_my_rate(self):
        return self.my_rate

    def set_my_rate(self, my_rate):
        self.my_rate = my_rate
        self._my_rate_callback(self.my_rate)
        self.set_interp(self.samp_rate/self.my_rate)

    def get_my_amp2(self):
        return self.my_amp2

    def set_my_amp2(self, my_amp2):
        self.my_amp2 = my_amp2
        self.blocks_int_to_float_0.set_scale(1/self.my_amp2)

    def get_my_amp1(self):
        return self.my_amp1

    def set_my_amp1(self, my_amp1):
        self.my_amp1 = my_amp1
        self.blocks_vector_source_x_0.set_data((0, self.my_amp1), [])

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.blocks_repeat_0_0.set_interpolation(self.interp)
        self.blocks_repeat_0.set_interpolation(self.interp)


def main(top_block_cls=PRBS_Two_Channel, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
