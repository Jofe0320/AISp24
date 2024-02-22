import torch
from torch.utils import data
from torch import nn
import matplotlib.pyplot as plt


#create noisy data
def generate_data(m, b, num_examples):
    # shape of data features will have num_examples rows by len(m) colums
    dim = (num_examples, len(m))
    # data features
    X = torch.normal(0, 1, dim)
    y = torch.matmul(X, m) + b # equation of the linear regresion
    #now add noise to each observation
    y += torch.normal(0, 0.01, y.shape)

    # pint shapes
    print("X.shape:", X.shape)
    print("y.shape:", y.shape)
    # y is an arrau of values but we need an array of tensors with one element we need to reshape
    # to keep same number of rows but put each element in a tensor
    y = y.reshape((-1, 1))
    print("y.shape:", y.shape)
    return X, y

value_m  = torch.tensor([2, -3.4])
value_c  = 4.2
examples = 1000
X, y = generate_data(value_m, value_c, examples)
# pint shapes
print("X.shape:", X.shape)
print("X[0]: ", X[0])
print("y.shape:", y.shape)
print("y[0]: ", y[0])

def visualize_data(X, y):
    # Optional Step: Visualize data set
    plt.figure()
    plt.xlabel('features')
    plt.ylabel('labels')
    plt.scatter(X[:, (0)].detach().numpy(), y.detach().numpy(), 1)
    plt.show() # uncomment if you want to plot the dataset
    # You need to close the  figure window to resume the code

visualize_data(X, y)

#create a data loader
def load_array(data_arrays, batch_size, is_train=True):

    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)

batch = 10
data_ierator = load_array((X, y), batch)
sample = next(iter(data_ierator))
print("sample batch: ", sample)
print("batch len: ", len(sample))

#define the neural nerwork
class NNModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(NNModel, self).__init__()
        self.fc1 = nn.Linear(input_size, output_size)

    def forward(self, x):
        output = self.fc1(x)
        return output

nnet = NNModel(2, 1)

# Look at strucure
from torchinfo import summary
summary(nnet, input_size=(batch, 2), device='cpu', col_names=['input_size', 'output_size',
                                                              'num_params'])

#setup cost model and optimizer

import torch.optim as optim

criterion = nn.MSELoss()
optimizer = optim.SGD(nnet.parameters(), lr=0.03)
lost_list = []

num_epochs = 5
i=0
for epoch in range(num_epochs):
    for X, y in data_ierator:
        p = nnet(X)
        loss = criterion(y, p)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if i % 100 == 0:
            loss, current = loss.item(), i * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{batch:>5d}]")

print(X[0])
example = X[0]

sample = next(iter(data_ierator))
print(sample[1])
Y = nnet(sample[0])
print(Y)