import json
import os

from tabulate import tabulate


def sort(data):
    def get_datetime(entry):
        """Parse and return the date and time for an exam entry."""
        date = entry['date'].split(' ')[1]
        time = entry['time'].split(' ')[0]

        # in the case that dates are equivalent, 'A' > 'B' > 'C'
        return date + ('A' if time == 'AM' else 'B' if time == 'PM' else 'C')

    return sorted(data, key=lambda date: get_datetime(date))


def output(data, format_, fn):
    render = None
    if format_ == 'json':
        fn, render = fn.format('json'), render_json
    elif format_ == 'table':
        fn, render = fn.format('txt'), render_table

    if render is not None:
        f = open(os.path.expanduser('~/Desktop/{}'.format(fn)), 'w')
        print('Writing data as {}...'.format(format_), end="")
        f.write(render(sort(data)))
        print(' Done!')
        return f.close()
    return print(render_table(sort(data)))


def render_json(data):
    return json.dumps(data, indent=2)


def render_table(data):
    return tabulate(data, headers='keys', tablefmt='fancy_grid')
