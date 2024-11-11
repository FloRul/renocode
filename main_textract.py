import boto3
from textractcaller import call_textract, Textract_Features
from textractprettyprinter.t_pretty_print import get_text_from_layout_json
import json
import os


def main():
    textract_json = call_textract(input_document="code_batiment_2022.pdf"

if __name__ == '__main__':
    main()