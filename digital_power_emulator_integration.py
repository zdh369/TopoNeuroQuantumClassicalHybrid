import torch
from photonic_power_electronics import PhotonicPowerElectronics
from quantum_emulation_core import QuantumEmulationCore
from self_healing_power_channels import SelfHealingPowerChannels

class DigitalPowerEmulatorIntegration:
    """
    Flexible integration framework for the digital power emulator system.
    Allows custom data flow and interaction between photonic power electronics,
    quantum emulation core, and self-healing power channels.
    """

    def __init__(self, device='cpu'):
        self.device = device
        self.photonic_model = PhotonicPowerElectronics().to(device)
        self.quantum_model = QuantumEmulationCore().to(device)
        self.self_healing_model = SelfHealingPowerChannels().to(device)

    def run_step(self, photonic_input, quantum_input, self_healing_input):
        """
        Run one integration step with given inputs.

        Args:
            photonic_input: Tensor input for photonic power electronics model
            quantum_input: Tensor input for quantum emulation core model
            self_healing_input: Tensor input for self-healing power channels model

        Returns:
            dict: Outputs from each module and combined integration results
        """
        photonic_out = self.photonic_model(photonic_input.to(self.device))

        quantum_out = self.quantum_model(quantum_input.to(self.device))

        # For self-healing model, expect sequence input for virtual sensor
        if self_healing_input.dim() == 2:
            # Add sequence dimension with length 1
            seq_input = self_healing_input.unsqueeze(1).to(self.device)
        else:
            seq_input = self_healing_input.to(self.device)

        self_healing_out = self.self_healing_model.forward_virtual_sensor(seq_input)

        # Example integration logic: combine outputs (customize as needed)
        combined_features = photonic_out + quantum_out
        # Optionally incorporate self-healing output (e.g., last time step)
        combined_features = combined_features + self_healing_out[:, -1, :]

        return {
            "photonic_output": photonic_out,
            "quantum_output": quantum_out,
            "self_healing_output": self_healing_out,
            "combined_features": combined_features
        }

    def set_device(self, device):
        """
        Set device for all models (cpu or cuda).
        """
        self.device = device
        self.photonic_model.to(device)
        self.quantum_model.to(device)
        self.self_healing_model.to(device)

if __name__ == "__main__":
    # Example usage
    import torch
    emulator = DigitalPowerEmulatorIntegration(device='cpu')

    photonic_input = torch.randn(5, emulator.photonic_model.input_dim)
    quantum_input = torch.randn(5, emulator.quantum_model.input_dim)
    self_healing_input = torch.randn(5, 10, emulator.self_healing_model.sensor_input_dim)  # sequence length 10

    outputs = emulator.run_step(photonic_input, quantum_input, self_healing_input)

    print("Photonic Output:", outputs["photonic_output"])
    print("Quantum Output:", outputs["quantum_output"])
    print("Self-Healing Output:", outputs["self_healing_output"])
    print("Combined Features:", outputs["combined_features"])
