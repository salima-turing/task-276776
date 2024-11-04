import unittest
import pandas as pd
import numpy as np


class TestAggregatedData(unittest.TestCase):
    def setUp(self):
        # Sample data from individual sources
        self.source_data1 = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
        self.source_data2 = pd.DataFrame({'value': [6, 7, 8, 9, 10]})

        # Aggregated data from the real-time processing environment
        self.aggregated_data = pd.DataFrame({'value': [11, 18]})  # Assume aggregation of source_data1 and source_data2

    def test_aggregation_correctness(self):
        expected_count = len(self.source_data1) + len(self.source_data2)
        actual_count = len(self.aggregated_data)
        self.assertEqual(expected_count, actual_count, "Aggregation result does not match the expected count.")


def test_aggregated_sum(self):
    expected_sum = self.source_data1['value'].sum() + self.source_data2['value'].sum()
    actual_sum = self.aggregated_data['value'].sum()
    self.assertAlmostEqual(expected_sum, actual_sum, places=2, msg="Aggregated sum does not match the expected value.")


def test_min_max_values(self):
    expected_min = self.source_data1['value'].min()
    expected_max = self.source_data2['value'].max()
    actual_min = self.aggregated_data['value'].min()
    actual_max = self.aggregated_data['value'].max()
    self.assertEqual(expected_min, actual_min, "Minimum value in aggregated data is incorrect.")
    self.assertEqual(expected_max, actual_max, "Maximum value in aggregated data is incorrect.")


def test_data_consistency(self):
    self.assertTrue(pd.api.types.is_numeric_dtype(self.aggregated_data['value']),
                    "Data type of 'value' column is incorrect.")
    self.assertEqual(len(self.aggregated_data.columns), 1, "Aggregated data contains unexpected columns.")


def test_statistical_validation(self):
    # Perform additional statistical tests if needed
    np.testing.assert_almost_equal(self.aggregated_data['value'].mean(), 9.5, decimal=2)


if __name__ == '__main__':
    unittest.main()
