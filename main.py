import argparse
from converter import USDEURConverter

if __name__ == "__main__":
    parser = argparse.ArgumentParser("python main.py", description="USD EUR Converter")
    parser.add_argument("-v", "--value", help="the value to be converted",
                        type=str, default="1")
    parser.add_argument("-f", "--ffrom", help="from currency",
                        type=str, default="USD")
    parser.add_argument("-t", "--to", help="to currency",
                        type=str, default="EUR")
    args = parser.parse_args()

    from_currency = args.ffrom
    to_currency = args.to
    value = float(args.value)

    currency = USDEURConverter.check_currency(from_currency.lower(), to_currency.lower()).replace(",", ".")
    float_currency = float(currency)
    answer = USDEURConverter.calculate_value(float_currency, value)
    print("Current " + from_currency + " -> " + to_currency + " exchange rate: " + currency)
    print(args.value + " " + from_currency.upper() + " = " + str(answer) + " " + to_currency.upper())