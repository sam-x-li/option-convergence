import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

'''
    GBMPlotter

    Plots a given number of stock paths for a set of given parameters, using Geometric Brownian Motion.
    This version also displays the expected value of the stock in red. 
'''

def GBMStockGenerator(s0, mu, sigma, dt, n=1):
    #   s - price
    #   s0 - initial price
    #   mu - expected rate of return
    #   sigma - volatility of stock price
    #   dt - length of time interval in days
    #   n - time period in years
    dt_actual = dt / 365 
    times = np.arange(0, n, dt_actual) # generates all the timestamps
    intervals = len(times)
    S = np.zeros(intervals)

    # formula - dS/s = mu * dt + sigma * z

    z = np.random.standard_normal(intervals - 1)
    dS_s = mu * dt_actual + sigma * z * math.sqrt(dt_actual)
    
    S[0] = s0
    for i in range(1, intervals):
        S[i] = S[i-1] * (1 + dS_s[i-1])

    return times, S

def zeroUncertainty(s0, mu, n):
    #   s0 - initial price
    #   mu - expected growth rate
    #   n - time period in years
    times = np.linspace(0, n, 1000)
    expected = s0 * np.exp(mu * times)
    return times, expected

def main():
    s0, mu, sigma, dt, n = 100, 0.2, 0.2, 1, 5
    stocks = 10 #number of stock paths

    for s in range(stocks):
        times, exampleStock = GBMStockGenerator(s0, mu, sigma, dt, n)
        plt.plot(times, exampleStock)

    e_times, e_intervals = zeroUncertainty(s0, mu, n)
    plt.plot(e_times, e_intervals, color='red')

    plt.title('Simulated Stock Path(s) Under GBM')
    plt.xlabel('Time/years')
    plt.ylabel('Price')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
