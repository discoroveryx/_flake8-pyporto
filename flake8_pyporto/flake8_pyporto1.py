from flake8.formatting import base


class PyPorto(base.BaseFormatter):
    """Flake8's PyPorto formatter."""

    def format(self, error):
        return 'Example formatter: {0!r}'.format(error)
