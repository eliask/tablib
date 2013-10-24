# -*- coding: utf-8 -*-

""" Tablib - HTML export support.
"""

import sys
import tablib
from tablib.compat import markup, StringIO

BOOK_ENDINGS = 'h3'

title = 'html'
extensions = ('html', )


def export_set(dataset):
	"""HTML representation of a Dataset."""

	stream = StringIO()

	page = markup.page()
	page.table.open()

	if dataset.headers is not None:
		new_header = [item if item is not None else '' for item in dataset.headers] 

		page.thead.open()
		headers = markup.oneliner.th(new_header)
		page.tr(headers)
		page.thead.close()

	for row in dataset:
		new_row = [item if item is not None else '' for item in row] 

		html_row = markup.oneliner.td(new_row)
		page.tr(html_row)

	page.table.close()

	stream.writelines(str(page))

	return stream.getvalue()


def export_book(databook):
	"""HTML representation of a Databook."""

	stream = StringIO()

	for i, dset in enumerate(databook._datasets):
		title = (dset.title if dset.title else 'Set %s' % (i))
		stream.write('<%s>%s</%s>\n' % (BOOK_ENDINGS, title, BOOK_ENDINGS))
		stream.write(dset.html)
		stream.write('\n')

	return stream.getvalue()
