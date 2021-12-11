from converter import USDEURConverter

if __name__ == "__main__":
    currency = USDEURConverter.check_currency().replace(",", ".")
    print("Current USD -> EUR exchange rate: " + currency)