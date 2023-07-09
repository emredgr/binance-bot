import argparse
from datetime import datetime
from typing import Union
from logging import info
import textwrap

class ArgumentParser(object):

    def __init__(self) -> None:
        
        self.parser = argparse.ArgumentParser(
        description="This Python script fetches data for the given coin name using Binance APIs.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
            usage: script.py [-h] [-c COIN_NAME]

        This Python script fetches data for a specific coin using Binance APIs.

        optional arguments:
        -h, --help            show this help message and exit
        -c COIN_NAME, --coin COIN_NAME
                                Specify the coin name. Example: BTC
            '''))
        
        
    def getScriptArguments(self):
        
        self.addArgument()

        args = self.parser.parse_args()
        arguments = self.editArgumentFormat(args)
        
        info(f"Arguments passed to the script: {arguments}")
        return arguments
        
    def addArgument(self):
        self.parser.add_argument("-c", "--coin", type=str, required=True, help="Specify the coin parameter (e.g. -> BTC, ETH)") # Coin parameter

    def editArgumentFormat(self, args)-> dict:
        arguments= {
            "coin": args.coin,
        }
        return arguments