import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from model import CNN

device = "cuda" if torch.cuda.is_available() else "cpu"

transform = transforms.ToTensor()

test_data = datasets.MNIST(root="./data", train=False, download=True, transform=transform)

test_loader = DataLoader(test_data, batch_size=64, shuffle=False)

model = CNN().to(device)
model.load_state_dict(torch.load("model.pth", map_location=device))
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)

        preds = model(images)
        _, predicted = torch.max(preds, 1)

        correct += (predicted == labels).sum().item()
        total += labels.size(0)

print("Accuracy:", correct / total)