import random
import unittest

from telemetry import *

class TestTelemetryDiagnosticControlsTest():
    def test_foo(self, monkeypatch):
        def return_one(x, y):
            return 1
        monkeypatch.setattr(random, 'randint', return_one)
        diagnostics = TelemetryDiagnostics()
        diagnostics.check_transmission()

if __name__ == "__main__":
    unittest.main()
