"""
Unit tests for FTRL-Proximal model
"""
import pytest
import tempfile
import csv
from models.ftrl import FTRLProximal, logloss, load_data, train_ftrl


class TestFTRLProximal:
    """Test FTRL-Proximal model class"""

    def test_initialization(self):
        """Test model initialization"""
        learner = FTRLProximal(alpha=0.1, beta=1.0, L1=1.0, L2=1.0, D=100)

        assert learner.alpha == 0.1
        assert learner.beta == 1.0
        assert learner.L1 == 1.0
        assert learner.L2 == 1.0
        assert learner.D == 100
        assert len(learner.n) == 100
        assert len(learner.z) == 100

    def test_predict_range(self):
        """Test that predictions are in valid probability range"""
        learner = FTRLProximal(D=100)
        x = [1, 2, 3, 5, 8]

        p = learner.predict(x)

        assert 0 <= p <= 1, f"Prediction {p} out of range [0, 1]"

    def test_predict_initial(self):
        """Test that initial prediction is close to 0.5"""
        learner = FTRLProximal(D=100)
        x = [1, 2, 3]

        p = learner.predict(x)

        # Initial prediction should be close to sigmoid(0) = 0.5
        assert 0.4 < p < 0.6

    def test_update(self):
        """Test model update"""
        learner = FTRLProximal(D=100)
        x = [1, 2, 3]

        # Get initial prediction
        p1 = learner.predict(x)

        # Update with positive example
        learner.update(x, p1, 1.0)

        # Get new prediction
        p2 = learner.predict(x)

        # Prediction should increase after seeing positive example
        assert p2 > p1

    def test_update_negative(self):
        """Test model update with negative example"""
        learner = FTRLProximal(D=100)
        x = [1, 2, 3]

        # Get initial prediction
        p1 = learner.predict(x)

        # Update with negative example
        learner.update(x, p1, 0.0)

        # Get new prediction
        p2 = learner.predict(x)

        # Prediction should decrease after seeing negative example
        assert p2 < p1

    def test_feature_interactions(self):
        """Test feature interactions"""
        learner_no_int = FTRLProximal(D=100, interaction=False)
        learner_with_int = FTRLProximal(D=100, interaction=True)

        x = [1, 2, 3]

        # Count generated indices
        indices_no_int = list(learner_no_int._indices(x))
        indices_with_int = list(learner_with_int._indices(x))

        # With interactions should have more indices
        # Original: 1 (bias) + 3 (features) = 4
        # With interactions: 4 + 3 (pairs) = 7
        assert len(indices_with_int) > len(indices_no_int)


class TestLogLoss:
    """Test log loss function"""

    def test_perfect_prediction(self):
        """Test log loss with perfect predictions"""
        # Perfect prediction for positive example
        loss1 = logloss(1.0, 1.0)
        assert loss1 < 0.01  # Should be very small

        # Perfect prediction for negative example
        loss2 = logloss(0.0, 0.0)
        assert loss2 < 0.01

    def test_worst_prediction(self):
        """Test log loss with worst predictions"""
        # Wrong prediction for positive example
        loss1 = logloss(0.0, 1.0)
        assert loss1 > 10  # Should be large

        # Wrong prediction for negative example
        loss2 = logloss(1.0, 0.0)
        assert loss2 > 10

    def test_uncertain_prediction(self):
        """Test log loss with uncertain prediction"""
        loss = logloss(0.5, 1.0)
        assert 0.5 < loss < 1.0  # log(2) ≈ 0.693

    def test_symmetry(self):
        """Test that log loss is symmetric"""
        loss1 = logloss(0.3, 1.0)
        loss2 = logloss(0.7, 0.0)

        # Should be approximately equal
        assert abs(loss1 - loss2) < 0.01


class TestLoadData:
    """Test data loading function"""

    def test_load_data_with_label(self):
        """Test loading data with labels"""
        # Create temporary CSV file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'click', 'feature1', 'feature2'])
            writer.writerow(['id1', '1', 'val1', 'val2'])
            writer.writerow(['id2', '0', 'val3', 'val4'])
            temp_file = f.name

        # Load data
        data_list = list(load_data(temp_file, D=100, has_label=True))

        assert len(data_list) == 2

        # Check first row
        t, row_id, x, y = data_list[0]
        assert row_id == 'id1'
        assert y == 1.0
        assert len(x) == 2

        # Check second row
        t, row_id, x, y = data_list[1]
        assert row_id == 'id2'
        assert y == 0.0

    def test_load_data_without_label(self):
        """Test loading data without labels"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'feature1', 'feature2'])
            writer.writerow(['id1', 'val1', 'val2'])
            temp_file = f.name

        data_list = list(load_data(temp_file, D=100, has_label=False))

        assert len(data_list) == 1

        t, row_id, x, y = data_list[0]
        assert row_id == 'id1'
        assert y == 0.0  # Default label
        assert len(x) == 2


class TestIntegration:
    """Integration tests"""

    def test_full_training_cycle(self):
        """Test full training cycle on small dataset"""
        # Create temporary training data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'click', 'feature1', 'feature2'])
            for i in range(100):
                click = '1' if i % 3 == 0 else '0'
                writer.writerow([f'id{i}', click, f'val{i%5}', f'val{i%7}'])
            train_file = f.name

        # Create temporary test data
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'feature1', 'feature2'])
            for i in range(20):
                writer.writerow([f'test{i}', f'val{i%5}', f'val{i%7}'])
            test_file = f.name

        # Create output file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as f:
            output_file = f.name

        # Train model
        learner = FTRLProximal(alpha=0.1, D=100)
        stats = train_ftrl(
            learner=learner,
            train_files=[train_file],
            test_files=[test_file],
            output_file=output_file,
            epochs=1,
            holdout_interval=10,
            log_interval=50
        )

        # Check that training completed
        assert 'final_loss' in stats
        assert stats['final_loss'] > 0

        # Check that output file was created
        with open(output_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            assert header == ['id', 'click']

            predictions = list(reader)
            assert len(predictions) == 20

            # Check prediction format
            for row in predictions:
                row_id, pred = row
                pred_float = float(pred)
                assert 0 <= pred_float <= 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
