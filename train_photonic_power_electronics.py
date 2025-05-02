import torch
from torch.utils.data import DataLoader, TensorDataset
from photonic_power_electronics import PhotonicPowerElectronics
import numpy as np

def generate_synthetic_data(num_samples=1000, input_dim=100):
    # Generate synthetic input features and targets for training
    X = np.random.rand(num_samples, input_dim).astype(np.float32)
    # Simulate target with some nonlinear function plus noise
    y = np.sin(X.sum(axis=1))[:, None] + 0.1 * np.random.randn(num_samples, 1).astype(np.float32)
    return X, y

def main():
    input_dim = 100
    model = PhotonicPowerElectronics(input_dim=input_dim)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    X, y = generate_synthetic_data(num_samples=2000, input_dim=input_dim)
    dataset = TensorDataset(torch.tensor(X), torch.tensor(y))
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    model.train_model(dataloader, epochs=20, lr=1e-3)

if __name__ == "__main__":
    main()
