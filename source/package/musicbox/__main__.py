# Copyright (c) 2024 IHU Liryc, Université de Bordeaux, Inria.
# License: BSD-3-Clause


from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--gui', action='store_true')
parser.add_argument('--tests', action='store_true')
args = parser.parse_args()


if args.tests:
    from . import dev
    dev.run_tests()
else:
    from .app import run
    run(
        gui=args.gui,
    )