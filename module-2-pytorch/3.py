import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

x = torch.tensor([[1,2],[3,4],[5,6],[7,8]])
y = torch.tensor([0,1,0,1])

dataset = TensorDataset(x, y)


loader = DataLoader(dataset, batch_size=4, shuffle=True)

for batch_x, batch_y in loader:
    print(batch_x, batch_y)

