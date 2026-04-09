import pytest
from unittest.mock import patch, mock_open
from parse_wps_fixed import get_items

def test_get_items_missing_end_marker():
    """Test that missing end marker falls back to rest of string."""
    mock_content = """\\item {\\bf Start Here}
\\subitem First item
\\subitem Second item
"""
    with patch("builtins.open", mock_open(read_data=mock_content)):
        # end_marker provided but not found, triggering ValueError
        items = get_items(r'\item {\bf Start Here}', r'\item {\bf End Here}')

    assert items == ['First item', 'Second item']

def test_get_items_no_end_marker_provided():
    """Test when no end_marker is provided."""
    mock_content = """\\item {\\bf Start Here}
\\subitem First item
\\subitem Second item
"""
    with patch("builtins.open", mock_open(read_data=mock_content)):
        # no end_marker provided (None)
        items = get_items(r'\item {\bf Start Here}')

    assert items == ['First item', 'Second item']

def test_get_items_start_marker_not_found():
    """Test when start marker is not found."""
    mock_content = """\\item {\\bf Something Else}
\\subitem First item
"""
    with patch("builtins.open", mock_open(read_data=mock_content)):
        # start_marker not found, triggering ValueError and returning []
        items = get_items(r'\item {\bf Start Here}')

    assert items == []
