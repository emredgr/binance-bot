from argparse import ArgumentParser as ArgParser, RawDescriptionHelpFormatter
from logging import info
from textwrap import dedent

class ArgumentParser(object):

    def __init__(self) -> None:
        
        self.parser = ArgParser( description="This Python script fetches data for the given coin name using Binance APIs.",
        formatter_class= RawDescriptionHelpFormatter,
        epilog=dedent('''\
            usage: script.py [-h] [-c COIN_NAME]

        This Python script fetches data for a specific coin using Binance APIs.

        optional arguments:
        -h, --help            show this help message and exit
        -c COIN_NAME, --coin COIN_NAME
        -o OUTPUT_PATH, --output_path
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
        self.parser.add_argument("-o", "--output_path", type=str, required=False, help="To output the data, the path will be csv, and the output format will be csv.")
    
    def editArgumentFormat(self, args)-> dict:
        
        arguments = {"coin": args.coin}
        output_path: str = args.output_path
        
        if  output_path is not None:
            if output_path.endswith(".csv") is True:
                arguments["output_path"]= output_path
            else:
                arguments["output_path"] = output_path.__add__(".csv")
                
        return arguments
        