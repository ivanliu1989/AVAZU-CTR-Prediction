"""
Unit tests for ensemble utilities
"""
import pytest
import tempfile
import csv
from utils.ensemble import (
    arithmetic_mean, harmonic_mean, geometric_mean, weighted_average,
    load_predictions, blend_predictions, calibrate_predictions
)


class TestMeanFunctions:
    """Test mean calculation functions"""

    def test_arithmetic_mean(self):
        """Test arithmetic mean"""
        values = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = arithmetic_mean(values)
        assert result == 3.0

    def test_arithmetic_mean_empty(self):
        """Test arithmetic mean with empty list"""
        result = arithmetic_mean([])
        assert result == 0.0

    def test_harmonic_mean(self):
        """Test harmonic mean"""
        values = [1.0, 2.0, 3.0, 4.0]
        result = harmonic_mean(values)
        # Harmonic mean = 4 / (1/1 + 1/2 + 1/3 + 1/4) = 4 / 2.083 ≈ 1.92
        assert 1.9 < result < 2.0

    def test_harmonic_mean_with_zeros(self):
        """Test harmonic mean handles near-zero values"""
        values = [0.0, 1.0, 2.0]
        result = harmonic_mean(values)
        assert result > 0  # Should handle zeros gracefully

    def test_geometric_mean(self):
        """Test geometric mean"""
        values = [1.0, 2.0, 4.0, 8.0]
        result = geometric_mean(values)
        # Geometric mean = (1 * 2 * 4 * 8)^(1/4) = 64^0.25 ≈ 2.83
        assert 2.8 < result < 2.9

    def test_weighted_average(self):
        """Test weighted average"""
        values = [1.0, 2.0, 3.0]
        weights = [0.5, 0.3, 0.2]
        result = weighted_average(values, weights)
        # 1*0.5 + 2*0.3 + 3*0.2 = 0.5 + 0.6 + 0.6 = 1.7
        assert abs(result - 1.7) < 0.01

    def test_weighted_average_invalid(self):
        """Test weighted average with invalid inputs"""
        with pytest.raises(ValueError):
            weighted_average([1.0, 2.0], [0.5])  # Mismatched lengths


class TestLoadPredictions:
    """Test loading prediction files"""

    def test_load_predictions(self):
        """Test loading predictions from CSV"""
        # Create temporary prediction file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'click'])
            writer.writerow(['id1', '0.15'])
            writer.writerow(['id2', '0.85'])
            writer.writerow(['id3', '0.50'])
            temp_file = f.name

        predictions = load_predictions(temp_file)

        assert len(predictions) == 3
        assert predictions['id1'] == 0.15
        assert predictions['id2'] == 0.85
        assert predictions['id3'] == 0.50


class TestBlendPredictions:
    """Test prediction blending"""

    def test_blend_arithmetic(self):
        """Test arithmetic blending"""
        # Create temporary prediction files
        files = []
        for i, preds in enumerate([
            [('id1', 0.1), ('id2', 0.2)],
            [('id1', 0.2), ('id2', 0.3)],
            [('id1', 0.3), ('id2', 0.4)]
        ]):
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'click'])
                for row_id, pred in preds:
                    writer.writerow([row_id, pred])
                files.append(f.name)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as f:
            output_file = f.name

        blended = blend_predictions(files, output_file, method='arithmetic')

        # Check arithmetic mean
        # id1: (0.1 + 0.2 + 0.3) / 3 = 0.2
        # id2: (0.2 + 0.3 + 0.4) / 3 = 0.3
        assert abs(blended['id1'] - 0.2) < 0.01
        assert abs(blended['id2'] - 0.3) < 0.01

    def test_blend_harmonic(self):
        """Test harmonic blending"""
        files = []
        for preds in [
            [('id1', 0.2)],
            [('id1', 0.4)]
        ]:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
                writer = csv.writer(f)
                writer.writerow(['id', 'click'])
                for row_id, pred in preds:
                    writer.writerow([row_id, pred])
                files.append(f.name)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as f:
            output_file = f.name

        blended = blend_predictions(files, output_file, method='harmonic')

        # Harmonic mean of 0.2 and 0.4 = 2 / (1/0.2 + 1/0.4) = 2 / 7.5 ≈ 0.267
        assert 0.26 < blended['id1'] < 0.27


class TestCalibration:
    """Test prediction calibration"""

    def test_calibrate_shift(self):
        """Test calibration with shift"""
        predictions = {'id1': 0.5, 'id2': 0.6, 'id3': 0.7}

        calibrated = calibrate_predictions(predictions, shift=-0.05)

        assert abs(calibrated['id1'] - 0.45) < 0.01
        assert abs(calibrated['id2'] - 0.55) < 0.01
        assert abs(calibrated['id3'] - 0.65) < 0.01

    def test_calibrate_scale(self):
        """Test calibration with scale"""
        predictions = {'id1': 0.5, 'id2': 0.6}

        calibrated = calibrate_predictions(predictions, scale=0.9)

        assert abs(calibrated['id1'] - 0.45) < 0.01
        assert abs(calibrated['id2'] - 0.54) < 0.01

    def test_calibrate_clipping(self):
        """Test that calibration clips to valid range"""
        predictions = {'id1': 0.99, 'id2': 0.01}

        calibrated = calibrate_predictions(predictions, shift=0.1)

        # Should be clipped
        assert calibrated['id1'] <= 1.0
        assert calibrated['id2'] >= 0.0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
