import pytest
from extract_other_pubs import parse_tex_section

def test_parse_tex_section_happy_path():
    content = r"""
\section{Working Papers}
\begin{itemize}
\item First paper
\item Second paper
with multiple lines
\end{itemize}
\section{Next Section}
"""
    items = parse_tex_section(content, "Working Papers")
    assert items == ["First paper", "Second paper with multiple lines"]

def test_parse_tex_section_not_found():
    content = r"""
\section{Publications}
\item Paper
"""
    items = parse_tex_section(content, "Working Papers")
    assert items == []

def test_parse_tex_section_no_items():
    content = r"""
\section{Working Papers}
Some intro text
\section{Next Section}
"""
    items = parse_tex_section(content, "Working Papers")
    assert items == []

def test_parse_tex_section_case_insensitive():
    content = r"""
\section{WORKING PAPERS}
\item Paper 1
\section{Next}
"""
    items = parse_tex_section(content, "Working Papers")
    assert items == ["Paper 1"]

def test_parse_tex_section_ignores_begin_end():
    content = r"""
\section{Working Papers}
\begin{itemize}
\item Paper 1
\begin{center}
Some center text
\end{center}
\item Paper 2
\end{itemize}
\section{Next}
"""
    items = parse_tex_section(content, "Working Papers")
    assert items == ["Paper 1 Some center text", "Paper 2"]

def test_parse_tex_section_eof():
    content = r"""
\section{Working Papers}
\item Paper 1
"""
    items = parse_tex_section(content, "Working Papers")
    assert items == ["Paper 1"]
