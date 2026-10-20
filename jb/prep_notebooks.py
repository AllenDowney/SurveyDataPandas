"""Copy the solution notebook into jb/ and prepare it for the book.

For each ../soln/NN_name.ipynb, writes NN_name.ipynb here:
- code cells that start with "# Solution" get the hide-cell tag,
  so the solutions are collapsed on the page;
- the page description goes in the notebook metadata (see GreenTeaPress plans/seo.md).
"""

import nbformat

DESCRIPTIONS = {
    '01_simpson': "Analyze General Social Survey data with pandas and StatsModels: crosstabs, "
                  "LOWESS, pivot tables, logistic regression, cohorts, and Simpson's paradox.",
}


def prepare(name, description):
    nb = nbformat.read(f'../soln/{name}.ipynb', 4)

    for cell in nb.cells:
        if cell.cell_type == 'code' and cell.source.startswith('# Solution'):
            tags = cell.metadata.setdefault('tags', [])
            if 'hide-cell' not in tags:
                tags.append('hide-cell')

    nb.metadata['myst'] = {'html_meta': {'description': description}}
    nb.metadata['og:description'] = description
    nbformat.write(nb, f'{name}.ipynb')
    print(f'{name} ({len(description)} characters)')


for name, description in DESCRIPTIONS.items():
    prepare(name, description)
