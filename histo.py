import numpy as np
import matplotlib.pyplot as plt

n = 10
results = []
mus = []
for i in range(1,10000):
    muestras_uniformes = np.random.uniform(low=-0.5,high=0.5, size= n)
    results.append(sum(muestras_uniformes))

    # if i % 100 == 0:
    #     mus.append(sum(results)/100)
standardized_values = [(x - n * np.mean(results)) / (np.var(results) * np.sqrt(n)) for x in results]
print(np.mean(mus))
print(np.std(mus))

plt.hist(mus, bins=30, density=True, alpha=0.7, color='blue')
plt.xlabel('Mean of Experiments')
plt.ylabel('Probability Density')
plt.title('Histogram of Means for Every 100 Iterations')
plt.grid(True)
plt.show()

plt.hist(standardized_values, bins=30, density=True, alpha=0.7, color='blue')
plt.xlabel('Standardized Values')
plt.ylabel('Probability Density')
plt.title('Histogram of Standardized Values')
plt.grid(True)
plt.show()

plt.hist(results, bins=30, density=True, alpha=0.7, color='blue')
plt.xlabel('Sum of 10 Uniform Random Variables')
plt.ylabel('Probability Density')
plt.title('Histogram of the Sum of 10 Uniform Random Variables')
plt.grid(True)
plt.show()


def ej4():
    results = []
    for n in range(1, 10001):
        muestras_uniformes = np.random.uniform(low=-0.5, high=0.5, size=n)
        results.append(sum(muestras_uniformes)/n)

        plt.hist(results, bins=30, density=True, alpha=0.7, color='blue')
        plt.xlabel('Sum of 10 Uniform Random Variables')
        plt.ylabel('Probability Density')
        plt.title('Histogram of the Sum of 10 Uniform Random Variables')
        plt.grid(True)
        plt.show()
# ej4()

def ej5():
    results = []
    for _ in range(1, 10001):
        muestras_uniformes = np.random.uniform(low=0, high=1, size=1)
        x = -(np.log(1-muestras_uniformes)/2)

    plt.hist(results, bins=30, density=True, alpha=0.7, color='blue')
    plt.xlabel('Sum of 10 Uniform Random Variables')
    plt.ylabel('Probability Density')
    plt.title('Histogram of the Sum of 10 Uniform Random Variables')
    plt.grid(True)
    plt.show()
ej5()
