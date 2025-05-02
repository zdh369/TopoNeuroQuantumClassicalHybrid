import torch
from torch.utils.data import DataLoader, TensorDataset
from quantum_emulation_core import QuantumEmulationCore
import numpy as np

def generate_synthetic_data(num_samples=1000, input_dim=100):
    # Generate synthetic input data for training
    X = np.random.rand(num_samples, input_dim).astype(np.float32)
    # Targets are noisy versions of inputs for simulation
    y = X + 0.05 * np.random.randn(num_samples, input_dim).astype(np.float32)
    return X, y

def main():
    input_dim = 100
    model = QuantumEmulationCore(input_dim=input_dim)
    optimizer_sim = torch.optim.Adam(model.simulation_model.parameters(), lr=1e-3)
    optimizer_disc = torch.optim.Adam(model.discriminator.parameters(), lr=1e-3)

    X, y = generate_synthetic_data(num_samples=2000, input_dim=input_dim)
    dataset = TensorDataset(torch.tensor(X), torch.tensor(y))
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    model.train()
    for epoch in range(20):
        total_sim_loss = 0.0
        total_disc_loss = 0.0
        for inputs, targets in dataloader:
            sim_loss, disc_loss = model.train_step(targets, optimizer_sim, optimizer_disc)
            total_sim_loss += sim_loss
            total_disc_loss += disc_loss
        print(f"Epoch {epoch+1}/20, Simulation Loss: {total_sim_loss/len(dataloader):.6f}, Discriminator Loss: {total_disc_loss/len(dataloader):.6f}")

if __name__ == "__main__":
    main()
