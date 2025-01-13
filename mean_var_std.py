import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    reshaped = np.array(list).reshape(3, 3)

    calculations = {
        'mean': calculate_mean(reshaped),
        'variance': calculate_var(reshaped),
        'standard deviation': calculate_std(reshaped),
        'max': calculate_max(reshaped),
        'min': calculate_min(reshaped),
        'sum': calculate_sum(reshaped)
    }

    return calculations

def calculate_mean(arr):
    row_mean = np.mean(arr, axis=0).tolist()
    col_mean = np.mean(arr, axis=1).tolist()
    flat_mean = np.mean(arr.flatten()).tolist()
    return [row_mean, col_mean, flat_mean]

def calculate_var(arr):
    row_var = np.var(arr, axis=0).tolist()
    col_var = np.var(arr, axis=1).tolist()
    flat_var = np.var(arr.flatten()).tolist()
    return [row_var, col_var, flat_var]

def calculate_std(arr):
    row_std = np.std(arr, axis=0).tolist()
    col_std = np.std(arr, axis=1).tolist()
    flat_std = np.std(arr.flatten()).tolist()
    return [row_std, col_std, flat_std]

def calculate_max(arr):
    row_max = np.max(arr, axis=0).tolist()
    col_max = np.max(arr, axis=1).tolist()
    flat_max = np.max(arr.flatten()).tolist()
    return [row_max, col_max, flat_max]

def calculate_min(arr):
    row_min = np.min(arr, axis=0).tolist()
    col_min = np.min(arr, axis=1).tolist()
    flat_min= np.min(arr.flatten()).tolist()
    return [row_min, col_min, flat_min]

def calculate_sum(arr):
    row_sum = np.sum(arr, axis=0).tolist()
    col_sum = np.sum(arr, axis=1).tolist()
    flat_sum = np.sum(arr.flatten()).tolist()
    return [row_sum, col_sum, flat_sum]

