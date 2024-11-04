import unittest

def aggregate_data(data_sources):
	total_sum = sum(data for source in data_sources for data in source)
	return total_sum

class TestAggregatedData(unittest.TestCase):

	def test_aggregated_values(self):
		data_sources = [[1, 2, 3], [4, 5], [6]]
		expected_sum = 1 + 2 + 3 + 4 + 5 + 6
		result = aggregate_data(data_sources)
		self.assertEqual(result, expected_sum, "Aggregated sum failed")

	def test_data_type(self):
		data_sources = [[1, 2], [3]]
		result = aggregate_data(data_sources)
		self.assertIsInstance(result, int, "Aggregated result should be an integer")

	def test_with_empty_source(self):
		data_sources = [[1, 2], [], [3]]
		expected_sum = 1 + 2 + 3
		result = aggregate_data(data_sources)
		self.assertEqual(result, expected_sum, "Aggregation failed with empty source")

	def test_with_single_element_source(self):
		data_sources = [[1], [2, 3], [4]]
		expected_sum = 1 + 2 + 3 + 4
		result = aggregate_data(data_sources)
		self.assertEqual(result, expected_sum, "Aggregation failed with single element source")

	def test_type_error_for_non_numeric(self):
		data_sources = [[1, 2], ["a"], [3]]
		with self.assertRaises(TypeError):
			aggregate_data(data_sources)

if __name__ == '__main__':
	unittest.main()
