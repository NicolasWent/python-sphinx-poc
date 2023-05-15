from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AmountIn:
    """The AmountIn model"""

    blockchain: str
    """The id of blockchain on which the exchange is taking place
    
    example: "avalanche"
    """
    exchange: str
    """The id of the exchange used for this trade
    
    example: "lydia_finance_avalanche"
    """
    tokenIn: str
    """The address of the token that you sell
    
    example: "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"
    """
    tokenOut: str
    """The address of the token that you buy
    
    example: "0xde3A24028580884448a5397872046a019649b084"
    """
    amountIn: str
    """The amount of tokenIn that you have to sell in order to get amountOut tokenOut
    
    example: 843047442340946
    """
    amountOut: str
    """The amount of tokenOut that you wish to buy
    
    example: 10000
    """

    def __init__(self, blockchain: str, exchange: str, tokenIn: str, tokenOut: str, amountIn: str, amountOut: str, **_):
        """Creates an AmountIn model

        :param blockchain: The id of blockchain on which the exchange is taking place
        :type blockchain: str
        :param exchange: The id of the exchange used for this trade
        :type exchange: str
        :param tokenIn: The address of the token that you sell
        :type tokenIn: str
        :param tokenOut: The address of the token that you buy
        :type tokenOut: str
        :param amountIn: The amount of tokenIn that you have to sell in order to get amountOut tokenOut
        :type amountIn: str
        :param amountOut: The amount of tokenOut that you wish to buy
        :type amountOut: str
        """
        self.blockchain = blockchain
        self.exchange = exchange
        self.tokenIn = tokenIn
        self.tokenOut = tokenOut
        self.amountIn = amountIn
        self.amountOut = amountOut
