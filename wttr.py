#!/usr/bin/env python
"""
usage: wttr [<location>] [-h] [-m | -u] [-TF] [-d DAYS] [-f FORMAT]

    -h , --help             help message
    -m, --metric            use metric units
    -u, --uscs              use uscs units
    -d, --days DAYS         days for forecast (0-3)
    -f, --format FORMAT     use a format string
    -T, --no-terminal       remove ANSI color codes
    -F, --follow-line       add back follow line

"""
import asyncio
import httpx
from docopt import docopt

BASE_URL = 'https://wttr.in/'

async def wttr(args=None, defs={}):
    a = docopt(__doc__, argv=args, help=False)
    for k, v in defs.items():
        if not a[k]:
            a[k] = v
    
    if a['--help']:
        return __doc__.strip()

    location = a['<location>'] or 'Milano, Italy'

    units = 'm' if a['--metric'] else 'u' if a['--uscs'] else ''
    terminal = 'T' if a['--no-terminal'] else ''
    follow = 'F' if not a['--follow-line'] else ''
    days = str(a['--days'])
    days = days if days in list('0123') else ''

    q = units + terminal + follow + days
    fmt = a['--format']

    p = {
            q: '',
            **({'format': fmt} if fmt else {}),
    }

    url = BASE_URL + location

    h = {'user-agent': 'httpie'}
    c = httpx.AsyncClient()
    r = await c.get(url, headers=h, params=p)

    return r.text


if __name__ == '__main__':
    d = {'--days': '0'}
    w = asyncio.run(wttr(defs=d))
    print(w)
