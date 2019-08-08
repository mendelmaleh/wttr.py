"""
usage: wttr [<location>] [-h] [-m | -u] [-TF] [-f FORMAT]

    -h , --help             help message
    -m, --metric            use metric units
    -u, --uscs              use uscs units
    -f, --format FORMAT     use a format string, [default: 3]
    -T, --no-terminal       remove ANSI color codes
    -F, --follow-line       add back follow line

"""
import httpx
from docopt import docopt, DocoptExit

BASE_URL = 'https://wttr.in/'

def wttr(args):
    try:
        a = docopt(__doc__, argv=args, help=False)
    except DocoptExit as e:
        return e.usage
    
    if a['--help']:
        return __doc__

    location = a['<location>'] or 'New York'

    units = 'm' if a['--metric'] else 'u' if a['--uscs'] else ''
    terminal = 'T' if a['--no-terminal'] else ''
    follow = 'F' if not a['--follow-line'] else ''

    q = units + terminal + follow
    p = {
            q: '',
            'format': a['--format'],
    }

    url = BASE_URL + location

    h = {'user-agent': 'httpie'}
    r = httpx.get(url, headers=h, params=p)

    return r.text


if __name__ == '__main__':
    w = wttr(args=None)
    print(w)

