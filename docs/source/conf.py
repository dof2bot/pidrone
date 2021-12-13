# -*- coding: utf-8 -*-

project = u'mecarm'
copyright = u'2020, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.0'
release = u'https://github.com/dof2bot/mecarm/releases/'
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'mecarmdoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'mecarm.tex', u'mecarm Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(master_doc, 'mecarm', u'mecarm Documentation', [author], 1)]
texinfo_documents = [(
    master_doc, 'mecarm', u'mecarm Documentation', author, 'mecarm',
    'One line description of project.', 'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
