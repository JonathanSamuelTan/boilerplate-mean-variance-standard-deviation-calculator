import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        input = np.array(list).reshape(3,3)
        mean = [np.mean(input, axis=0).tolist(), np.mean(input, axis=1).tolist(), np.mean(input)]
        variance = [np.var(input, axis=0).tolist(), np.var(input, axis=1).tolist(), np.var(input)]
        st_dev = [np.std(input, axis=0).tolist(), np.std(input, axis=1).tolist(), np.std(input)]
        max = [np.max(input, axis=0).tolist(), np.max(input, axis=1).tolist(), np.max(input)]
        min = [np.min(input, axis=0).tolist(), np.min(input, axis=1).tolist(), np.min(input)]
        sum = [np.sum(input, axis=0).tolist(), np.sum(input, axis=1).tolist(), np.sum(input)]
        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': st_dev,
            'max': max,
            'min': min,
            'sum': sum
        }
    return calculations