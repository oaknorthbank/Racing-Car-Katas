from telemetry_system.telemetry import TelemetryDiagnostics


class TelemetryDiagnosticControlsTest():
    def test_foo(self):
        diagnostics = TelemetryDiagnostics()
        diagnostics.check_transmission()
