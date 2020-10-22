#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2020 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pymeasure.instruments.spectrum_analyzer import SpectrumAnalyzer

class AgilentE4440A(SpectrumAnalyzer):
    REFERENCE_LEVEL_RANGE_MIN_dBm = -170
    REFERENCE_LEVEL_RANGE_MAX_dBm = 30
    REFERENCE_LEVEL_RANGE_dBm = [REFERENCE_LEVEL_RANGE_MIN_dBm, REFERENCE_LEVEL_RANGE_MAX_dBm]

    FREQUENCY_MIN_Hz = 1
    FREQUENCY_MAX_Hz = 26.5e9
    FREQUENCY_SPAN_RANGE_Hz = [10, FREQUENCY_MAX_Hz]

    RESOLUTION_BW_RANGE_MIN_Hz = 1
    RESOLUTION_BW_RANGE_MAX_Hz = 8e6
    RESOLUTION_BW_RANGE_Hz = [RESOLUTION_BW_RANGE_MIN_Hz, RESOLUTION_BW_RANGE_MAX_Hz]

    INPUT_ATTENUATION_RANGE_dB = [0, 70]

    SWEEP_POINTS_RANGE = [101, 8192]
    DETECTOR_VALUES=["NORM", "AVER", "POS", "SAMP", "NEG", "QPE", "EAV", "EPOS", "MPOS", "RMS"],

    def __init__(self, resourceName, **kwargs):
        super(AgilentE4440A, self).__init__(
            resourceName,
            "Agilent E4440A Spectrum Analyzer",
            **kwargs
        )


class AgilentE4445A(SpectrumAnalyzer):
    REFERENCE_LEVEL_RANGE_MIN_dBm = -170
    REFERENCE_LEVEL_RANGE_MAX_dBm = 30
    REFERENCE_LEVEL_RANGE_dBm = [REFERENCE_LEVEL_RANGE_MIN_dBm, REFERENCE_LEVEL_RANGE_MAX_dBm]

    FREQUENCY_MIN_Hz = 1
    FREQUENCY_MAX_Hz = 13.2e9
    FREQUENCY_SPAN_RANGE_Hz = [10, FREQUENCY_MAX_Hz]

    RESOLUTION_BW_RANGE_MIN_Hz = 1
    RESOLUTION_BW_RANGE_MAX_Hz = 8e6
    RESOLUTION_BW_RANGE_Hz = [RESOLUTION_BW_RANGE_MIN_Hz, RESOLUTION_BW_RANGE_MAX_Hz]

    INPUT_ATTENUATION_RANGE_dB = [0, 70]

    SWEEP_POINTS_RANGE = [101, 8192]

    DETECTOR_VALUES=["NORM", "AVER", "POS", "SAMP", "NEG", "QPE", "EAV", "EPOS", "MPOS", "RMS"],

    def __init__(self, resourceName, **kwargs):
        super(AgilentE4445A, self).__init__(
            resourceName,
            "Agilent E4445A Spectrum Analyzer",
            **kwargs
        )
