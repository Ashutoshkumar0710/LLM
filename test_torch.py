import torch

print("Torch Version:", torch.__version__)

x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

print("x =", x)
print("y =", y)
print("x + y =", x + y)