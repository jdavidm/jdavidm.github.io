import unittest
from unittest.mock import patch, mock_open
import parse_wps_fixed

class TestParseWpsFixed(unittest.TestCase):

    def test_get_items_both_markers(self):
        mock_content = "START_MARKER\n\\subitem item1\n\\subitem item2\nEND_MARKER"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            items = parse_wps_fixed.get_items("START_MARKER", "END_MARKER")
            self.assertEqual(items, ["item1", "item2"])

    def test_get_items_no_end_marker(self):
        mock_content = "START_MARKER\n\\subitem item1\n\\subitem item2\nSome other text"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            items = parse_wps_fixed.get_items("START_MARKER")
            self.assertEqual(items, ["item1", "item2 Some other text"])

    def test_get_items_end_marker_not_found(self):
        mock_content = "START_MARKER\n\\subitem item1\n\\subitem item2\nSome other text"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            items = parse_wps_fixed.get_items("START_MARKER", "NON_EXISTENT_END_MARKER")
            self.assertEqual(items, ["item1", "item2 Some other text"])

    def test_get_items_start_marker_not_found(self):
        mock_content = "Some content without the start marker"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            items = parse_wps_fixed.get_items("NON_EXISTENT_START_MARKER", "END_MARKER")
            self.assertEqual(items, [])

    def test_get_items_multiline(self):
        mock_content = "START_MARKER\n\\subitem item1\npart2 of item1\n\\subitem item2\nEND_MARKER"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            items = parse_wps_fixed.get_items("START_MARKER", "END_MARKER")
            self.assertEqual(items, ["item1 part2 of item1", "item2"])

    def test_get_items_with_subitem_numbers(self):
        mock_content = "START_MARKER\n\\subitem[16] item1\n\\subitem[2] item2\nEND_MARKER"
        with patch('builtins.open', mock_open(read_data=mock_content)):
            items = parse_wps_fixed.get_items("START_MARKER", "END_MARKER")
            self.assertEqual(items, ["item1", "item2"])

if __name__ == '__main__':
    unittest.main()
