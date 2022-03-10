import sys


def joonhyeon(stocks, cash):
    """

    :param stocks: 주가 정보
    :param cash: 현금
    :return: (보유 주식 수 * 주가 정보, 현금)
    """
    has_stocks, has_cash = 0, cash
    for idx, stock in enumerate(stocks):
        a, b = divmod(has_cash, stock)
        has_stocks += a
        has_cash = b
        print(idx + 1, stock, has_stocks, has_cash)
    return has_stocks * stocks[-1] + has_cash


def seongmin(stocks, cash):
    """
    전량 매수, 전량 매도
    3일 연속 상승할 경우 마지막 날 전량 매도
    3일 연속 하락할 경우 마지막 날 전량 매수

    :param stocks: 주가 정보
    :param cash: 현금
    :return: (보유 주식 수 * 주가 정보, 현금)
    """
    has_stocks, has_cash = 0, cash
    flag = 0
    for idx, stock in enumerate(stocks[1:]):
        if stock > stocks[idx]:
            if flag >= 0:
                flag += 1
            else:
                flag = 1
        elif stock < stocks[idx - 1]:
            if flag <= 0:
                flag += -1
            else:
                flag = -1
        else:
            flag = 0

        if flag >= 3:
            has_cash += has_stocks * stock
            has_stocks = 0
        elif flag <= -3:
            a, b = divmod(has_cash, stock)
            has_stocks += a
            has_cash = b
        print(idx + 2, stock, has_stocks, has_cash, flag)
    return has_stocks * stocks[-1] + has_cash


if __name__ == '__main__':
    cash = int(sys.stdin.readline().rstrip())
    stocks = list(map(int, sys.stdin.readline().rstrip().split()))

    j_result = joonhyeon(stocks, cash)
    print()
    s_result = seongmin(stocks, cash)
    print()

    print(j_result, s_result)
    if j_result > s_result:
        answer = "BNP"
    elif j_result < s_result:
        answer = "TIMING"
    else:
        answer = "SAMESAME"
    print(answer)
