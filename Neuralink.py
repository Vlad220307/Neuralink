import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptik_weight = 2 * np.random.random((3,1)) - 1

print("Случайные инициализирующие веса:")
print(synaptik_weight)

#Метод обратного распространения 

for i in range(20000):
    input_layer = training_inputs
    outpuyts = sigmoid( np.dot( input_layer, synaptik_weight ) )

    errors = training_outputs - outpuyts
    adjustments = np.dot( input_layer.T, errors * ( outpuyts * ( 1 - outpuyts ) ) )

    synaptik_weight += adjustments

print("Веса после обучения:")
print(synaptik_weight)

print("Результат:")
print(outpuyts)

# Test

new_inputs = np.array([1,1,0])
output = sigmoid( np.dot( new_inputs, synaptik_weight ) )

print( "Новая ситуация:" )
print(output)
