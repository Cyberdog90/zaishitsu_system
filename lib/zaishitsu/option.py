import argparse
from zaishitsu.plugin import Plugin


def args():
    parser = argparse.ArgumentParser()
    plugin = Plugin()
    for instance in plugin.plugins:
        parser.add_argument(f"--{instance.args.name}", type=instance.args.type, default=instance.args.default)
    return parser.parse_args()
