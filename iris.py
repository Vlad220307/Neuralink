import numpy as np

input_dim = 4
out_dim = 3
h_dim = 10

x = np.random.randn(input_dim)

w1 = np.random.randn(input_dim, h_dim)
b1 = np.random.randn(h_dim)
w2 = np.random.randn(h_dim, out_dim)
b2 = np.random.randn(out_dim)

def relu(t):
    return np.maximum(t, 0)

def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)

def predict(x):
    t1 = x @ w1 + b1
    h1 = relu(t1)

    t2 = h1 @ w2 + b2
    z = softmax(t2)
    return z

probs = predict(x)
pred_class = np.argmax(probs)
class_names = ["Setosa", "Versocolor", "Verginica"]
print("Predicsted class", class_names[pred_class])
