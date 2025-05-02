import unittest
import numpy as np
from famine_prediction_model import FaminePredictionModel
from sklearn.ensemble import RandomForestClassifier
from unittest.mock import patch, MagicMock

class TestFaminePredictionModel(unittest.TestCase):

    def setUp(self):
        self.model = FaminePredictionModel()
        self.features = [
            [0.1, 0.2, 0.3],
            [0.4, 0.1, 0.5],
            [0.3, 0.6, 0.2],
            [0.9, 0.8, 0.7],
            [0.5, 0.4, 0.6]
        ]
        self.labels = [0, 0, 1, 1, 0]

    def test_init(self):
        self.assertIsInstance(self.model.model, RandomForestClassifier)
        self.assertEqual(self.model.model.n_estimators, 100)
        self.assertEqual(self.model.model.random_state, 42)

    def test_load_data(self):
        self.model.load_data(self.features, self.labels)
        np.testing.assert_array_equal(self.model.X, np.array(self.features))
        np.testing.assert_array_equal(self.model.y, np.array(self.labels))

    @patch('famine_prediction_model.train_test_split')
    @patch.object(RandomForestClassifier, 'fit')
    @patch.object(RandomForestClassifier, 'predict')
    def test_train(self, mock_predict, mock_fit, mock_train_test_split):
        mock_train_test_split.return_value = (np.array(self.features[:4]), np.array(self.features[4:]),
                                              np.array(self.labels[:4]), np.array(self.labels[4:]))
        mock_predict.return_value = np.array([0]) # Mock prediction for the single test sample
        self.model.load_data(self.features, self.labels)
        self.model.train() # classification_report output is printed, not asserted here
        mock_fit.assert_called_once()
        mock_predict.assert_called_once()
