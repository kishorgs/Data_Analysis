import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(lst).reshape(3, 3)
    
    result = {
        'mean': [
            np.mean(arr, axis=1).tolist(),  
            np.mean(arr, axis=0).tolist(),  
            float(np.mean(arr))             
        ],
        'variance': [
            np.var(arr, axis=1).tolist(),  
            np.var(arr, axis=0).tolist(),   
            float(np.var(arr))            
        ],
        'standard deviation': [
            np.std(arr, axis=1).tolist(),  
            np.std(arr, axis=0).tolist(),  
            float(np.std(arr))             
        ],
        'max': [
            np.max(arr, axis=1).tolist(),   
            np.max(arr, axis=0).tolist(),
            int(np.max(arr))              
        ],
        'min': [
            np.min(arr, axis=1).tolist(),  
            np.min(arr, axis=0).tolist(),  
            int(np.min(arr))               
        ],
        'sum': [
            np.sum(arr, axis=1).tolist(),  
            np.sum(arr, axis=0).tolist(),  
            int(np.sum(arr))              
        ]
    }
    
    return result


result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)