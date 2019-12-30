#!/usr/bin/env python

import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('templates'))
TEMPLATE = ENV.get_template('index.html')


def title(filename):
    year, title, medium, end = filename.replace('-', ' ').split('_')
    dims = end.split('.')[0].replace('x', ' x ').replace('in', ' inches')
    return f"{title} / {year} / {medium} / {dims}"


def main():
    imagedirs = [Path(p).resolve() for p in sys.argv[1:]]
    for imdir in imagedirs:
        index = TEMPLATE.render(imdir=imdir, imagedirs=imagedirs,
                                sorted=sorted, title=title)
        outpath = imdir/'index.html'

        print(f'Writing to {outpath}')

        with outpath.open('w') as out:
            out.write(index)


if __name__ == "__main__":
    main()
