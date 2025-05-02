import hashlib
import datetime
import json

class AuditLogger:
    def __init__(self, log_file="audit_log.json"):
        self.log_file = log_file
        self.log_entries = []
        self._load_log()

    def _load_log(self):
        try:
            with open(self.log_file, "r") as f:
                self.log_entries = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.log_entries = []

    def log_decision(self, decision_data):
        timestamp = datetime.datetime.utcnow().isoformat()
        data_str = json.dumps(decision_data, sort_keys=True)
        entry_hash = hashlib.sha256((data_str + timestamp).encode()).hexdigest()
        entry = {
            "timestamp": timestamp,
            "data": decision_data,
            "hash": entry_hash
        }
        self.log_entries.append(entry)
        self._save_log()

    def _save_log(self):
        with open(self.log_file, "w") as f:
            json.dump(self.log_entries, f, indent=2)

class EthicalGuard:
    def __init__(self, max_lyapunov=1.0):
        self.max_lyapunov = max_lyapunov

    def check_lyapunov(self, lyapunov_exponents):
        if any(le > self.max_lyapunov for le in lyapunov_exponents):
            raise RuntimeError("EthicalGuard: Lyapunov exponent exceeds allowed threshold")

if __name__ == "__main__":
    # Example usage
    logger = AuditLogger()
    guard = EthicalGuard(max_lyapunov=1.0)

    sample_decision = {
        "lyapunov_exponents": [0.9, 0.0, -14.5],
        "model": "Lorenz"
    }

    try:
        guard.check_lyapunov(sample_decision["lyapunov_exponents"])
        logger.log_decision(sample_decision)
        print("Decision logged and ethical check passed.")
    except RuntimeError as e:
        print(str(e))
