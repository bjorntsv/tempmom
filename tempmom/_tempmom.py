# -*- coding: utf-8 -*-

import numpy as np

__all__ = ['TemporalMoments', 'TemporalMomentsAll']


class TemporalMoments():
    """Class for calculation of temporal moments in discrete time signals.

    Temporal moments statistically characterizes transient dynamic signals and
    describe how the energy of a signal is distributed over time.

    All moments of order 2 and higher are calculated about the central time, T.

    Parameters
    ----------

    data : float
        Finite discrete time series
    fs : int
        Sampling frequency

    See also
    --------

    For more information, see:

        D. O. Sallwood, "Characterization and simulation of transient
        vibrations using band limited temporal moments," Shock and Vibration,
        vol. 1, no. 6, pp. 507-527, 1994.

    For more information of practical use and implementation, see:

    Acknowledgements
    ----------------

    """

    # Constructor
    def __init__(self, data, fs):

        # Variables
        self.data = data
        self.fs = fs
        self.n = len(data)
        self.dt = 1/fs

    def peak_value(self):
        """Peak value (peak amplitude) of the data."""

        peak = np.max(abs(self.data))

        return peak

    def energy(self):
        """Energy (E): central moment (order 0) of the data."""

        # Local variables
        n = self.n
        dt = self.dt
        E = 0

        for i in range(n-1):
            E += (dt/2)*(self.data[i]**2 + self.data[i+1]**2)

        return E

    def central_time(self):
        """Central time (T): normalized central moment (order 1) of the
        data.
        """

        # Local variables
        n = self.n
        dt = self.dt
        E = self.energy()
        T_sum = 0

        for i in range(n-1):
            T_sum += (dt*(i+0.5)) * dt*(self.data[i]**2 + self.data[i+1]**2)

        T = (0.5*T_sum)/E

        return T

    def ms_duration(self):
        """Mean-square duration (D2): normalized central moment (order 2) of
        the data about the central time, T.
        """

        # Local variables
        n = self.n
        dt = self.dt
        E = self.energy()
        T = self.central_time()
        D2_sum = 0

        for i in range(n-1):
            D2_sum += ((dt*(i+0.5)-T)**2 *
                       dt*(self.data[i]**2 + self.data[i+1]**2))

        D2 = (0.5*D2_sum)/E

        return D2

    def rms_duration(self):
        """Root-mean-square duation (D): normalized central moment (order 2)
        of the data about the central time, T.
        """

        D2 = self.ms_duration()
        D = np.sqrt(D2)

        return D

    def rea(self):
        """Root energy amplitude (Ae): central moment normalized by the RMS
        duration of the data.
        """

        E = self.energy()
        D = self.rms_duration()
        Ae = np.sqrt(E/D)

        return Ae

    def central_skew(self):
        """Central skewness (St): normalized central moment (order 3) of the
        data about the central time, T.
        """

        # Local variables
        n = self.n
        dt = self.dt
        E = self.energy()
        T = self.central_time()
        St3_sum = 0

        for i in range(n-1):
            St3_sum += ((dt*(i+0.5)-T)**3 *
                        dt*(self.data[i]**2 + self.data[i+1]**2))

        St3 = (0.5*St3_sum)/E
        St = np.cbrt(St3)

        return St

    def norm_skew(self):
        """Normalized skewness (S): normalized central moment (order 3) with
        respect to the RMS duration (D), of the data about the central time, T.
        """

        D = self.rms_duration()
        St = self.central_skew()
        S = St/D

        return S

    def central_kurt(self):
        """Central kurtosis (Kt): normalized central moment (order 4) of the
        data about the central time, T.
        """

        # Local variables
        n = self.n
        dt = self.dt
        E = self.energy()
        T = self.central_time()
        Kt4_sum = 0

        for i in range(n-1):
            Kt4_sum += ((dt*(i+0.5)-T)**4 *
                        dt*(self.data[i]**2 + self.data[i+1]**2))

        Kt4 = (0.5*Kt4_sum)/E
        Kt = Kt4**(1/4)

        return Kt

    def norm_kurt(self):
        """Normalized kurtosis (K): normalized central moment (order 4) with
        respect to the RMS duration (D), of the data about the central time, T.
        """

        D = self.rms_duration()
        Kt = self.central_kurt()
        K = Kt/D

        return K


class TemporalMomentsAll(TemporalMoments):
    """Class for returning the peak value and temporal moments in separate
    arrays of all or the most important parameters only.
    """

    # Constructor
    def __init__(self, data, fs):
        TemporalMoments.__init__(self, data, fs)

    def full(self):
        """Returning an array containing the peak value and all temporal
        moments.
        """

        full_array = np.array([self.peak_value(), self.energy(),
                               self.central_time(), self.ms_duration(),
                               self.rms_duration(), self.central_skew(),
                               self.norm_skew(), self.central_kurt(),
                               self.norm_kurt(), self.rea()])

        return full_array

    def semi(self):
        """Returning an array containing the most relevant temporal moments."""

        semi_array = np.array([self.energy(), self.central_time(),
                               self.rms_duration(), self.central_skew(),
                               self.central_kurt(), self.rea()])

        return semi_array
