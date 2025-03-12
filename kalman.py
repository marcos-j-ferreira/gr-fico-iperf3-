import numpy as np
import matplotlib.pyplot as plt 
from pykalman import KalmanFilter
import random 

bandwidth_data = [round(random.uniform(5,25), 2)for _ in range(500)]

time = np.arange(len(bandwidth_data))

kf = KalmanFilter(initial_state_mean=bandwidth_data[0], n_dim_obs=1)

filtered_state_means, _ = kf.filter(bandwidth_data)

plt.figure(figsize=(12, 5))
plt.plot(time, filtered_state_means, label="Filtered Data", color='green', linewidth=2)

plt.plot(time, [bw if bw < 15 else np.nan for bw in bandwidth_data], 'ro', label="Value < 15 Mbits/sec")

plt.title('Bandwidth com Filtro de Kalman e Valores Abaixo de 15 Mbits/sec', fontsize=14)
plt.xlabel('Tempo (minutos)', fontsize=12)
plt.ylabel('Bandwidth (Mbits/sec)', fontsize=12)

plt.legend()

plt.grid(True)
plt.show()

