import pytest
import warnings
from rpy2.robjects import vectors
from rpy2.robjects.packages import importr

try:
    import IPython
except ModuleNotFoundError as no_ipython:
    warnings.warn(str(no_ipython))
    IPython = None

if IPython is None:
    html = None
else:
    from rpy2.ipython import html
    
base = importr('base')

@pytest.mark.skipif(Ipython is None, 'The optional package IPython cannot be imported.')
@pytest.mark.parametrize(
    'o,func',
    [(vectors.IntVector([1, 2, 3]), html.html_vector_horizontal),
     (vectors.FloatVector([1, 2, 3]), html.html_vector_horizontal),
     (vectors.StrVector(['a', 'b' 'c']), html.html_vector_horizontal),
     (vectors.FactorVector(['a', 'b' 'c']), html.html_vector_horizontal),
     (vectors.ListVector({'a': 1, 'b': 2}), html.html_rlist),
     (vectors.DataFrame({'a': 1, 'b': 'z'}), html.html_rdataframe),
     ('x <- c(1, 2, 3)', html.html_sourcecode),
     (base.c, html.html_ridentifiedobject)])
def test_html_func(o, func):
    res = func(o)
    assert isinstance(res, str)
