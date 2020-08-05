import numpy as np




def weighted_sum(training_data, weights, bias):

    # weighted_sum = np.dot(np.concatenate([Perceptron.weights,Perceptron.bias]),  training_data)
     weighted_sum = np.dot(np.concatenate([weights,bias]) , training_data)
     return weighted_sum

def step_function(x):
  if x<0:
    return 0
  elif x>=0:
    return 1



training_data= np.array([[1,1, 1], [ 0, 0, 1 ], [1, 0, 1], [0, 1, 1]])
test_data= np.array([1, 1, 0, 0])
learning_rate = 0.2

lmao =2
bias = np.random.rand(1)
weights = np.random.rand(2)

for x in range(lmao):
  random_xi = np.random.randint(len(training_data))
  point_x = training_data[random_xi]
  point_y = test_data[random_xi]
  sum_weighted= weighted_sum(point_x, weights, bias)
  _sum_ = step_function(sum_weighted)
  error = learning_rate*(point_y-_sum_ )
  print('weights before:')
  print(weights)
  print(bias)
  bias[0] +=  error
  weights[0] +=  error * point_x[0]
  weights[1] +=  error * point_x[1]
  print('weights after')
  print(weights)
  print(bias)



def predict(x1, x2):
  parameters = np.array([x1, x2, 1])

  result = np.dot(np.concatenate([weights,bias]),  parameters)
  if (result>=0.0):
   print("The result is : 1")
  elif(result<0):
   print("The result is 0")






predict(0, 1)
predict(0, 0)
predict(1, 1)
predict(1, 0)



































