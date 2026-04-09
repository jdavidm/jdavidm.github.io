import pytest
from parse_wps_fixed import clean_item

def test_clean_item_href():
    # Test href extraction
    item = r'\href{http://example.com}{Example Link}'
    expected = '<a href="http://example.com" target="_blank" rel="noopener noreferrer">Example Link</a>'
    assert clean_item(item) == expected

def test_clean_item_formatting():
    # Test removal of \textbf, \emph, {, }, \$
    item = r'\textbf{Bold Text} \emph{Emphasized} \$100'
    expected = 'Bold Text Emphasized 100'
    assert clean_item(item) == expected

def test_clean_item_accents():
    # Test latex accents conversion
    item = r"J\'er\'ome, L\'opez, Schr\"odinger"
    expected = 'Jéróme, López, Schrödinger'
    assert clean_item(item) == expected

def test_clean_item_quotes():
    # Test double quote replacement
    item = r"``Hello'', said the world"
    expected = '"Hello", said the world'
    assert clean_item(item) == expected

def test_clean_item_whitespace():
    # Test removal of \\ and stripping
    item = r"  Some text with \\ newline  "
    expected = 'Some text with  newline'
    assert clean_item(item) == expected

def test_clean_item_complex():
    # Test a mix of formatting
    item = r"``\textbf{Title}'' by J\'er\'ome, \href{http://link}{Link} \$ \emph{end}\\"
    expected = '"Title" by Jéróme, <a href="http://link" target="_blank" rel="noopener noreferrer">Link</a>  end'
    assert clean_item(item) == expected
