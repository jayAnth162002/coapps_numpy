#Task 3 => Implement the function to calculate the cosine similarity between two vectors using NumPy.
import numpy as np

def cosine_similarity(vector1,vector2):
    
    dot_product = np.dot(vector1,vector2)
    
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    
    cosine_sim =dot_product/(magnitude1 * magnitude2)
    
    return cosine_sim

vector1 = np.array([1,3,5])
vector2 = np.array([2,4,6])
cosine_sim = cosine_similarity(vector1,vector2)

print("Cosine Similarity:",cosine_sim) 
    