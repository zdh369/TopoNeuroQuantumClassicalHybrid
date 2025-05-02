import torch
from torch.utils.data import DataLoader, TensorDataset
from self_healing_power_channels import SelfHealingPowerChannels
import numpy as np

def generate_synthetic_sensor_data(num_samples=1000, seq_len=10, sensor_input_dim=50):
    # Generate synthetic sensor input sequences
    X = np.random.rand(num_samples, seq_len, sensor_input_dim).astype(np.float32)
    # Targets are next-step sensor states (shifted sequences)
    y = np.roll(X, shift=-1, axis=1)
    return X, y

def main():
    sensor_input_dim = 50
    model = SelfHealingPowerChannels(sensor_input_dim=sensor_input_dim)
    optimizer = torch.optim.Adam(list(model.virtual_sensor.parameters()) + list(model.sensor_output.parameters()), lr=1e-3)

    X, y = generate_synthetic_sensor_data(num_samples=2000, seq_len=10, sensor_input_dim=sensor_input_dim)
    dataset = TensorDataset(torch.tensor(X), torch.tensor(y))
    dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

    model.train_virtual_sensor(dataloader, epochs=20, lr=1e-3)

if __name__ == "__main__":
    main()
