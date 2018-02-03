import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("household_power_consumption.txt",sep = ";")
#nan_idx = np.where(df.Voltage == "?")[0]

firstDay_idx = np.where(df.Date == df.Date[0])[0][-1] + 1
lastDay_idx = np.where(df.Date == df.Date[len(df.Date)-1])[0][0]

def show_plot(arr):
    voltage_data = np.array(arr[firstDay_idx:lastDay_idx])
    voltage_data[voltage_data == "?"] = 0.#1e-5
    voltage_data = voltage_data.astype(np.float)
    voltage_c = np.array([np.sum(voltage_data[i:i+1440]) for i in range(int(len(voltage_data)/1440))])
    plt.plot(range(voltage_c.shape[0]),voltage_c)
    plt.show()
    
show_plot(df.Global_intensity)
show_plot(df.Global_reactive_power)
show_plot(df.Sub_metering_3)

