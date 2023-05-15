from Models.AmountIn import AmountIn


def main():
    example = {
        "blockchain": "avalanche",
        "exchange": "lydia_finance_avalanche",
        "tokenIn": "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7",
        "tokenOut": "0xde3A24028580884448a5397872046a019649b084",
        "amountIn": 843047442340946,
        "amountOut": 10000
    }

    print(AmountIn(**example))

if __name__ == "__main__":
    main()
