# option-convergence
Project exploring how Monte Carlo methods can be used for European option pricing, and compares the results against the analytical Black-Scholes-Merton formula.
Plots paths of stock prices under Geometric Brownian Motion, and demonstrates the lognormal distribution of these prices.

---

## Summary

  - Simulated stock prices using Geometric Brownian Motion (GBM).
  - Implemented Monte Carlo estimation of option prices by discounting expected payoffs.
  - Compared simulated prices to analytical closed-form Black-Scholes prices to show convergence.
  - Includes scripts for visualising GBM paths and the lognormal distribution of terminal prices. 

---

## Example Results
```bash
          Simulated Monte Carlo Price  Analytical BSM price  Absolute Difference  Percentage Difference
n
10000                        5.545381              5.411455            -0.133926              -2.474864
50000                        5.467213              5.411455            -0.055757              -1.030357
100000                       5.400444              5.411455             0.011011               0.203484
500000                       5.435111              5.411455            -0.023655              -0.437137
1000000                      5.413025              5.411455            -0.001570              -0.029004
```
---

## Installation 
```bash
git clone https://github.com/sam-x-li/option-convergence.git
cd option-convergence
pip install -r requirements.txt
```

## Usage
Run individual scripts to see results:
```bash
cd src
python convergence.py
python lognorm.py
python GBMPlotter.py
python GBMComparison.py
```

---

## Images

<img width="1620" height="850" alt="stockpaths1" src="https://github.com/user-attachments/assets/c55d4032-85f0-481b-a3e0-4079785b7fd8" />
<img width="1620" height="870" alt="lognormal" src="https://github.com/user-attachments/assets/a3becf33-c6bf-4b59-91bc-0b080f9bc452" />
