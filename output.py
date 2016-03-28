import json
import os
from tabulate import tabulate
import pprint


def sort(data):
    # currently working on getting sort working, broken unless
    # next line is uncommented

    # return data

    def get_datetime(entry):
        """Parse and return the date and time for an exam entry."""
        return entry['date'].split(' ')[1], entry['time'].split(' ')[0]

    new = []
    for e in data:
        if len(new) == 0:
            new.append(e)
        else:
            pass
    pprint.pprint(new)
    return new


def output(data, format_, fn):
    render = None
    if format_ == 'json':
        fn, render = fn.format('json'), render_json
    elif format_ == 'table':
        fn, render = fn.format('txt'), render_table

    if render is not None:
        f = open(os.path.expanduser('~/Desktop/{}'.format(fn)), 'w')
        # print('Preparing data as {}...'.format(format_), end='')
        f.write(render(sort(data)))
        # print(' Done!')
        return f.close()
    return print(render_table(sort(data)))


def render_json(data):
    return json.dumps(data, indent=2)


def render_table(data):
    return tabulate(data, headers='keys', tablefmt='fancy_grid')
