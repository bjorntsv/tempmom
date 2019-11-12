# -*- coding: utf-8 -*-

from _tempmom import TemporalMoments
import numpy as np
import unittest


class TemporalMomentsTestCase(unittest.TestCase):
    """Class for test all temporal moments."""

    def setUp(self):
        """Test case using an exponential function as a signal.

        See reference for information of the test signal.
        """

        # Signal
        self.alpha = 20
        self.fs = 2048
        self.t = np.arange(0, 1, 1/self.fs)
        self.data = np.exp(-self.alpha*self.t)

        # Theoretical parameters and temporal moments
        self.peak = np.max(abs(self.data))
        self.E = 1/(2*self.alpha)
        self.T = 1/(2*self.alpha)
        self.D2 = (1/(2*self.alpha))**2
        self.D = 1/(2*self.alpha)
        self.Ae = 1
        self.St = 1/((4**(1/3))*self.alpha)
        self.S = 2**(1/3)
        self.Kt = np.sqrt(3)/(2*self.alpha)
        self.K = np.sqrt(3)

    def test_peak_value(self):
        """Testing peak value."""
        peak = TemporalMoments(self.data, self.fs).peak_value()
        self.assertAlmostEqual(self.peak, peak, places=10)

    def test_energy(self):
        """Testing energy."""
        E = TemporalMoments(self.data, self.fs).energy()
        self.assertAlmostEqual(self.E, E, places=5)

    def test_central_time(self):
        """Testing central time."""
        T = TemporalMoments(self.data, self.fs).central_time()
        self.assertAlmostEqual(self.T, T, places=5)

    def test_ms_duration(self):
        """Testing mean-square duration."""
        D2 = TemporalMoments(self.data, self.fs).ms_duration()
        self.assertAlmostEqual(self.D2, D2, places=7)

    def test_rms_duration(self):
        """Testing root-mean-square duration."""
        D = TemporalMoments(self.data, self.fs).rms_duration()
        self.assertAlmostEqual(self.D, D, places=6)

    def test_rea(self):
        """Testing root energy amplitude."""
        Ae = TemporalMoments(self.data, self.fs).rea()
        self.assertAlmostEqual(self.Ae, Ae, places=4)

    def test_central_skew(self):
        """Testing central skewness."""
        St = TemporalMoments(self.data, self.fs).central_skew()
        self.assertAlmostEqual(self.St, St, places=10)

    def test_norm_skew(self):
        """Testing normalized skewness."""
        S = TemporalMoments(self.data, self.fs).norm_skew()
        self.assertAlmostEqual(self.S, S, places=4)

    def test_central_kurt(self):
        """Testing central kurtosis."""
        Kt = TemporalMoments(self.data, self.fs).central_kurt()
        self.assertAlmostEqual(self.Kt, Kt, places=6)

    def test_norm_kurt(self):
        """Testing normalized kurtosis."""
        K = TemporalMoments(self.data, self.fs).norm_kurt()
        self.assertAlmostEqual(self.K, K, places=4)

if __name__ == '__main__':
    unittest.main()
