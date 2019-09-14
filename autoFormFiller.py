import mechanize
import argparse
import formInfo as fI
import re

def main():
    # setting up command line argument parser
    parser = argparse.ArgumentParser(description="Autofill some forms.")
    parser.add_argument("url", type=str, nargs=1,
                        help="the website to autofill forms for")
    #parser.add_argument()
    args = parser.parse_args()

    # sets url to the one provided in the command line
    url = args.url[0]
    br = mechanize.Browser()
    header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
    br.set_header("User-agent", header)
    response = br.open(url)
    br.form = br.forms()[0]
    #print(br.form.controls[1].__dict__)
    #br.submit()
    for control in br.form.controls:
       print("name: %s, type: %s" % (control.name, control.type))

if __name__ == "__main__":
    main()
