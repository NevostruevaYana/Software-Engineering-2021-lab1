import argparse
from converter import USDEURConverter

if __name__ == "__main__":
    parser = argparse.ArgumentParser("python main.py", description="USD EUR Converter")
    parser.add_argument("-v", "--value", help="the value to be converted from dollar to euro",
                        type=str, default="1")
    args = parser.parse_args()

    currency = USDEURConverter.check_currency().replace(",", ".")
    float_currency = float(currency)
    answer = USDEURConverter.calculate_value(float_currency, float(args.value))
    print("Current USD -> EUR exchange rate: " + currency)
    print(args.value + " USD = " + str(answer) + " EUR")