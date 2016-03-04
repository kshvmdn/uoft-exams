import json
import os
from pprint import pprint
from tabulate import tabulate


def output(data, format_, fn):
    render = None
    if format_ == 'json':
        fn, render = fn.format('json'), render_json
    elif format_ == 'table':
        fn, render = fn.format('txt'), render_table

    if render is not None:
        f = open(os.path.expanduser('~/Desktop/{}'.format(fn)), 'w')
        file_.write(render(data, f))
        return f.close()
    return pprint(data)


def render_json(data, file_):
    return json.dumps(data, indent=2)


def render_table(data, file_):
    return tabulate(data, headers='keys', tablefmt='fancy_grid')
