from sys import argv
from src.helper import command_parser

def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    
    file_path = argv[1]
    command_parser.Parser.commandParser(file_path)
    
if __name__ == "__main__":
    main()