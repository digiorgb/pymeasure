#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2019 PyMeasure Developers
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

import warnings
from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import strict_discrete_set

MIN_RAMP_TIME = 0.1  # seconds


class YokogawaGS200(Instrument):
    """
    Represents the Yokogawa GS200 source and provides a high-level interface for interacting with the instrument.
    """
    source_enabled = Instrument.control("OUTPut:STATe?", "OUTPut:STATe %d",
                                        """A boolean property that controls whether the source is enabled, takes """
                                        """values True or False. """,
                                        validator=strict_discrete_set, values={True: 1, False: 0}, map_values=True)

    source_mode = Instrument.control(":SOURce:FUNCtion?", ":SOURce:FUNCtion %s",
                                     """String property that controls the source mode. Can be either 'current' or """
                                     """'voltage'.""",
                                     validator=strict_discrete_set, values={'current': 'CURR', 'voltage': 'VOLT'},
                                     map_values=True, get_process=lambda s: s.strip())

    source_level = Instrument.control(":SOURce:LEVel?", "SOURce:LEVel %g",
                                      """Floating point number that controls the output level, either a voltage or a """
                                      """current, depending on the source mode.""")

    source_range = Instrument.control(":SOURce:RANGe?", "SOURce:RANGe %g",
                                      """Floating point number that controls the range (either in voltage or """
                                      """current) of the output. "Range" refers to the maximum source level.""")

    voltage_limit = Instrument.control("SOURce:PROTection:VOLTage?", "SOURce:PROTection:VOLTage %g",
                                       """Floating point number that controls the voltage limit. "Limit" refers to """
                                       """maximum value of the electrical value that is conjugate to the """
                                       """mode (current is conjugate to voltage, and vice versa). Thus, voltage """
                                       """limit is only applicable when in 'current' mode""")

    current_limit = Instrument.control("SOURce:PROTection:CURRent?", "SOURce:PROTection:CURRent %g",
                                       """Floating point number that controls the current limit. "Limit" refers to """
                                       """maximum value of the electrical value that is conjugate to the """
                                       """mode (current is conjugate to voltage, and vice versa). Thus, current """
                                       """limit is only applicable when in 'voltage' mode""")

    def __init__(self, adapter, **kwargs) -> None:
        super().__init__(adapter, "Yokogawa GS200 Source", **kwargs)

    def trigger_ramp_to_level(self, level: float, ramp_time: float) -> None:
        """
        Ramp the output level from its current value to "level" in time "ramp_time". This method will NOT wait until
        the ramp is finished (thus, it will not block further code evaluation).

        :param float level: final output level
        :param float ramp_time: time in seconds to ramp
        :return: None
        """
        if not self.source_enabled:
            raise ValueError("YokogawaGS200 source must be enabled in order to ramp to a specified level. Otherwise, "
                             "the Yokogawa will reject the ramp.")
        if level > self.source_range * 1.2:
            raise ValueError("Level must be within 1.2 * source_range, otherwise the Yokogawa will produce an error.")
        if ramp_time < MIN_RAMP_TIME:
            warnings.warn(f'Ramp time of {ramp_time}s is below the minimum ramp time of {MIN_RAMP_TIME}s,'
                          f'so the Yokogawa will instead be instantaneously set to the desired level.')
            self.source_level = level
        else:
            # Use the Yokogawa's "program" mode to create the ramp
            ramp_program = ":program:edit:start;" \
                           f":source:level {level};" \
                           ":program:edit:end;"
            # set "interval time" equal to "slope time" to make a continuous ramp
            ramp_program += f":program:interval {ramp_time};" \
                            f":program:slope {ramp_time};"
            # run it once
            ramp_program += ":program:repeat 0;" \
                            ":program:run"
            self.write(ramp_program)


