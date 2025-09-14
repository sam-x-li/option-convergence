import pandas as pd
import numpy as np
import math
from statistics import NormalDist

'''
    ### BSM and Monte Carlo Option Price Convergence ###

    Displays convergence of simulated and analytical European option prices, calculated using Monte Carlo methods and the Black-Scholes-Merton
    model respectively. Change parameters in main(), such as volatility, initial underlying stock price, or option type. 

    Simulated option price is calculated by generating many potential stock paths using Geometric Brownian Motion, 
    and calculating the average payoff, before discounting at the risk-free rate. n dictates the number of stock paths generated. 
'''


def GBM1Step(s0, mu, sigma, T=1, n=10000):
    #   s - price
    #   s0 - initial price
    #   mu - expected return per year
    #   sigma - volatility of stock price per year
    #   T - time period in years
    #   n - number of trials

    #   Using lognormal distribution here
    z = np.random.standard_normal(n)
    expected = (mu - 0.5 * (sigma ** 2)) * T
    stdev = sigma * math.sqrt(T)
    endPrices = s0 * np.exp(expected + stdev * z)
    
    return endPrices
    
def getPayoff(mode, K, prices):
    zeroes = np.zeros(len(prices))
    if mode == 1: #call
        return np.maximum(prices - K, zeroes)
    elif mode == 2: #put
        return np.maximum(K - prices, zeroes)

def CalcOptionPrice(r, T, payoffs):
    meanPayoff = np.mean(math.exp(-r * T) *payoffs)
    return meanPayoff #discounting by risk-free rate

def monteCarlo(s0, mu, sigma, T, r, mode, K, n):
    endPrices = GBM1Step(s0, mu, sigma, T, n)
    payoffs = getPayoff(mode, K, endPrices)
    optionPrice = CalcOptionPrice(r, T, payoffs)
    return optionPrice

def BSM(s0, sigma, T, r, mode, K):
    d1 =(math.log(s0 / K) + (r + (0.5 * (sigma ** 2))) * T) / (sigma * math.sqrt(T))
    d2 = d1 - (sigma * math.sqrt(T))
    z = NormalDist(0, 1) #standard normal
    if mode == 1:
        return s0 * z.cdf(d1) - K * math.exp(-r * T) * z.cdf(d2)
    elif mode == 2:
        return K * math.exp(-r * T) * z.cdf(-d2) - s0 * z.cdf(-d1) 
    
def optionType(t):
    if t == 1:
        return 'Call'
    elif t == 2:
        return 'Put'

def main():
    s0, sigma, T = 100, 0.3, 0.5
    r, mode, K = 0.04, 1, 110
    mu = r
    trialRuns = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000]
    simulated = []
    analytical = []
    absDifferences = []
    pDifferences = []

    for n in trialRuns:
        currentSimulated = monteCarlo(s0, mu, sigma, T, r, mode, K, n)
        currentAnalytical = BSM(s0, sigma, T, r, mode, K)
        simulated.append(currentSimulated)
        analytical.append(currentAnalytical)
        absDifferences.append(currentAnalytical-currentSimulated)
        pDifferences.append((absDifferences[-1] * 100) / currentAnalytical)

    df = pd.DataFrame(list(zip(trialRuns, simulated, analytical, absDifferences, pDifferences)),
                        columns=['n', 'Simulated Monte Carlo Price', 'Analytical BSM price', 'Absolute Difference', 'Percentage Difference'])
    df.set_index('n', inplace=True)

    print(f'Convergence of simulated (Monte Carlo) and analytical (Black-Scholes-Merton) European option prices\n')
    print(f'Parameters: \n\nOption Type: {optionType(mode)}\nInitial Underlying Stock Price: {s0}\nAnnual Risk-free rate of return: {r}')
    print(f'Annual Volatility: {sigma}\nStrike Price: {K}\nYears Until Maturity: {T}\n\n')
    
    print(df)

if __name__ == '__main__':
    main()

