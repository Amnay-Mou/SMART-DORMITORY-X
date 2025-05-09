# # # # import matplotlib.pyplot as plt
# # # # import numpy as np
# # # #
# # # # # Define the data for the graph
# # # # gdp = np.linspace(0, 10, 100)
# # # # ad_initial = 10 - gdp
# # # # ad_new = 12 - gdp
# # # # sras = gdp
# # # # lras = np.full_like(gdp, 5)
# # # #
# # # # # Plotting the initial AD, new AD, SRAS, and LRAS curves
# # # # plt.figure(figsize=(10, 6))
# # # #
# # # # plt.plot(gdp, ad_initial, label='AD0 (Initial Aggregate Demand)', color='blue')
# # # # plt.plot(gdp, ad_new, label='AD1 (New Aggregate Demand)', color='blue', linestyle='--')
# # # # plt.plot(gdp, sras, label='SRAS (Short-Run Aggregate Supply)', color='green')
# # # # plt.axvline(x=5, label='LRAS (Long-Run Aggregate Supply)', color='red', linestyle='--')
# # # #
# # # # # Adding equilibrium points and annotations
# # # # plt.scatter([3.5, 5], [6.5, 5], color='black')  # Equilibrium points A and B
# # # # plt.text(3.5, 6.7, 'A', horizontalalignment='right')
# # # # plt.text(5, 5.2, 'B', horizontalalignment='right')
# # # # plt.axhline(y=6.5, color='gray', linestyle='--')
# # # # plt.axhline(y=5, color='gray', linestyle='--')
# # # # plt.axvline(x=3.5, color='gray', linestyle='--')
# # # # plt.axvline(x=5, color='gray', linestyle='--')
# # # #
# # # # # Adding labels and titles
# # # # plt.title("AD-AS Model: Self-Adjustment in a Closed Economy")
# # # # plt.xlabel("Real Output (GDP)")
# # # # plt.ylabel("Price Level")
# # # # plt.legend()
# # # # plt.grid(True)
# # # #
# # # # # Show the plot
# # # # plt.show()
# # #
# # # import matplotlib.pyplot as plt
# # #
# # # # Creating the graphs for the two solutions of the expansionary monetary policy
# # #
# # # # Graph 1: Increasing the Money Supply
# # # fig1, ax1 = plt.subplots()
# # # ax1.set_title('Effect of Increasing Money Supply')
# # # ax1.set_xlabel('Quantity of Money')
# # # ax1.set_ylabel('Interest Rate')
# # # # Original Money Supply curve
# # # ax1.plot([1, 2], [5, 5], label='Original Money Supply (MS1)')
# # # # Increased Money Supply curve
# # # ax1.plot([1.5, 2.5], [4, 4], label='Increased Money Supply (MS2)', linestyle='--')
# # # # Demand for Money curve
# # # ax1.plot([1, 2.5], [6, 3], label='Money Demand (MD)')
# # #
# # # # Equilibrium points
# # # ax1.plot(1.5, 4, 'ro')  # New equilibrium
# # # ax1.plot(1, 5, 'bo')  # Original equilibrium
# # # ax1.legend()
# # #
# # # # Graph 2: Directly Lowering Interest Rates
# # # fig2, ax2 = plt.subplots()
# # # ax2.set_title('Effect of Lowering Interest Rates')
# # # ax2.set_xlabel('Interest Rate')
# # # ax2.set_ylabel('Quantity of Loans')
# # # # Original Loan Demand curve
# # # ax2.plot([5, 4], [1, 2], label='Original Loan Demand (LD1)')
# # # # Increased Loan Demand curve
# # # ax2.plot([4, 3], [2, 3], label='Increased Loan Demand (LD2)', linestyle='--')
# # # # Loan Supply curve
# # # ax2.plot([5, 3], [1, 3], label='Loan Supply (LS)')
# # #
# # # # Equilibrium points
# # # ax2.plot(4, 2, 'ro')  # New equilibrium
# # # ax2.plot(5, 1, 'bo')  # Original equilibrium
# # # ax2.legend()
# # #
# # # plt.tight_layout()
# # # plt.show()
# #
# # # Creating a more detailed graph for the effect of lowering interest rates in an open economy with a fixed exchange rate
# # import matplotlib.pyplot as plt
# # import numpy as np
# # fig, ax = plt.subplots()
# # ax.set_title('Effect of Lowering Interest Rates (Open Economy with Fixed Exchange Rate)')
# # ax.set_xlabel('Interest Rate')
# # ax.set_ylabel('Quantity of Loans')
# #
# # # Original Loan Demand curve
# # ax.plot([5, 4], [1, 2], label='Original Loan Demand (LD1)', color='blue')
# # # Attempted Increased Loan Demand curve
# # ax.plot([4, 3], [2, 3], label='Attempted Increased Loan Demand (LD2)', linestyle='--', color='red')
# # # Real Loan Demand curve after intervention
# # ax.plot([5, 4], [1, 2], label='Real Loan Demand (LD1) after intervention', linestyle=':', color='green')
# #
# # # Loan Supply curve
# # ax.plot([5, 3], [1, 3], label='Loan Supply (LS)', color='black')
# #
# # # Equilibrium points
# # ax.plot(5, 1, 'bo', label='Original Equilibrium')  # Original equilibrium
# # ax.plot(4, 2, 'ro', label='Attempted New Equilibrium')  # Attempted new equilibrium
# # ax.plot(5, 1, 'go', label='Real Equilibrium after Intervention')  # Real equilibrium after intervention
# #
# # # Adding annotations for clarity
# # ax.annotate('Original Equilibrium', xy=(5, 1), xytext=(5.1, 1.2), arrowprops=dict(facecolor='black', arrowstyle='->'))
# # ax.annotate('Attempted New Equilibrium', xy=(4, 2), xytext=(3.5, 2.5), arrowprops=dict(facecolor='black', arrowstyle='->'))
# # ax.annotate('Real Equilibrium after Intervention', xy=(5, 1), xytext=(4.5, 0.5), arrowprops=dict(facecolor='black', arrowstyle='->'))
# #
# # ax.legend()
# #
# # plt.tight_layout()
# # plt.show()
# import matplotlib.pyplot as plt
#
# # Creating the graphs for the scenario where the Federal Reserve tries to stimulate the economy in an open economy with a fixed exchange rate
#
# fig, ax = plt.subplots()
# ax.set_title('Effect of Expansionary Policy in an Open Economy with Fixed Exchange Rate')
# ax.set_xlabel('Interest Rate')
# ax.set_ylabel('Quantity of Loans')
#
# # Original Loan Demand curve
# ax.plot([5, 4], [1, 2], label='Original Loan Demand (LD1)', color='blue')
# # Attempted Increased Loan Demand curve
# ax.plot([4, 3], [2, 3], label='Attempted Increased Loan Demand (LD2)', linestyle='--', color='red')
# # Real Loan Demand curve after intervention
# ax.plot([5, 4], [1, 2], label='Real Loan Demand (LD1) after intervention', linestyle=':', color='green')
#
# # Loan Supply curve
# ax.plot([5, 3], [1, 3], label='Loan Supply (LS)', color='black')
#
# # Equilibrium points
# ax.plot(5, 1, 'bo', label='Original Equilibrium')  # Original equilibrium
# ax.plot(4, 2, 'ro', label='Attempted New Equilibrium')  # Attempted new equilibrium
# ax.plot(5, 1, 'go', label='Real Equilibrium after Intervention')  # Real equilibrium after intervention
#
# # Adding annotations for clarity
# ax.annotate('Original Equilibrium', xy=(5, 1), xytext=(5.1, 1.2), arrowprops=dict(facecolor='black', arrowstyle='->'))
# ax.annotate('Attempted New Equilibrium', xy=(4, 2), xytext=(3.5, 2.5), arrowprops=dict(facecolor='black', arrowstyle='->'))
# ax.annotate('Real Equilibrium after Intervention', xy=(5, 1), xytext=(4.5, 0.5), arrowprops=dict(facecolor='black', arrowstyle='->'))
#
# ax.legend()
#
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

# Creating the graphs for the scenario where the Federal Reserve tries to stimulate the economy in an open economy with a floating exchange rate

fig, ax = plt.subplots()
ax.set_title('Effect of Expansionary Policy in an Open Economy with Floating Exchange Rate')
ax.set_xlabel('Interest Rate')
ax.set_ylabel('Quantity of Loans')

# Original Loan Demand curve
ax.plot([5, 4], [1, 2], label='Original Loan Demand (LD1)', color='blue')
# Increased Loan Demand curve
ax.plot([4, 3], [2, 3], label='Increased Loan Demand (LD2)', linestyle='--', color='red')
# Effect of currency depreciation
ax.plot([4, 3], [2.5, 3.5], label='Increased Loan Demand with Depreciation (LD3)', linestyle=':', color='green')

# Loan Supply curve
ax.plot([5, 3], [1, 3], label='Loan Supply (LS)', color='black')

# Equilibrium points
ax.plot(5, 1, 'bo', label='Original Equilibrium')  # Original equilibrium
ax.plot(4, 2, 'ro', label='New Equilibrium')  # New equilibrium
ax.plot(3, 3.5, 'go', label='Equilibrium after Depreciation')  # Equilibrium after depreciation

# Adding annotations for clarity
ax.annotate('Original Equilibrium', xy=(5, 1), xytext=(5.1, 1.2), arrowprops=dict(facecolor='black', arrowstyle='->'))
ax.annotate('New Equilibrium', xy=(4, 2), xytext=(4.1, 2.2), arrowprops=dict(facecolor='black', arrowstyle='->'))
ax.annotate('Equilibrium after Depreciation', xy=(3, 3.5), xytext=(2.8, 3.8), arrowprops=dict(facecolor='black', arrowstyle='->'))

ax.legend()

plt.tight_layout()
plt.show()
