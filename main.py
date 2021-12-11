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

    currency = USDEURConverter.check_currency().replace(",", ".")
    float_currency = float(currency)
    answer = USDEURConverter.calculate_value(float_currency, float(args.value))
    print("Current USD -> EUR exchange rate: " + currency)
    print(args.value + " USD = " + str(answer) + " EUR")