import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import lognorm

'''
    ### Lognormal Distribution Of Stock Prices Under GBM ###

    Uses Geometric Brownian Motion to iteratively calculate stock paths up to a certain point in time. 
    Then plots the final prices on a histogram against the theoretically matching lognormal distribution
    to demonstrate how these are lognormally distributed. Also shows how the log of the stock price is normally
    distributed. Stock parameters can be changed in main(). 
'''

rng = np.random.default_rng(123)

def GBMStockGenerator(s0, mu, sigma, dt, n=1):
    #   s - price
    #   s0 - initial price
    #   mu - expected return per year
    #   sigma - volatility of stock price per year
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

def MonteCarlo(s0, mu, sigma, dt, n=1, runs=10):
    final_prices = []
    for run in range(runs):
        times, S = GBMStockGenerator(s0, mu, sigma, dt, n)
        final_prices.append(S[-1])
    return np.array(final_prices)

def getLogNormal(s0, mu, sigma, T, data):
    #   s - price
    #   s0 - initial price
    #   mu - expected return per year
    #   sigma - volatility of stock price per year
    #   T - time until endpoint in years
    #   max - maximum value of the data
    x = np.linspace(min(data), max(data), 1000)
    mean = math.log(s0) + ((mu - 0.5 * (sigma ** 2)) * T)
    variance = (sigma ** 2) * T
    pdf = lognorm.pdf(x, s=math.sqrt(variance), scale = np.exp(mean))
    return x, pdf

def main():
    s0, mu, sigma, dt, n = 100, 0.2, 0.1, 1, 3

    data = MonteCarlo(s0, mu, sigma, dt, n, 10000)
    x, pdf = getLogNormal(s0, mu, sigma, n, data)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].hist(data, 100, density=True)
    axes[0].plot(x, pdf, 'r', linewidth=2, label="Lognormal PDF")

    axes[1].hist(np.log(data), 100, density=True)
    axes[1].set_title('Log of Stock Price')

    plt.show()

if __name__ == '__main__':
    main()
