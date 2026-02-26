import os
from dataclasses import dataclass
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass
class FirebaseConfig:
    """Firebase configuration with validation"""
    project_id: str = os.getenv("FIREBASE_PROJECT_ID", "")
    private_key_id: str = os.getenv("FIREBASE_PRIVATE_KEY_ID", "")
    private_key: str = os.getenv("FIREBASE_PRIVATE_KEY", "").replace("\\n", "\n")
    client_email: str = os.getenv("FIREBASE_CLIENT_EMAIL", "")
    client_id: str = os.getenv("FIREBASE_CLIENT_ID", "")
    
    def validate(self) -> bool:
        """Validate Firebase configuration"""
        required_fields = [self.project_id, self.private_key, self.client_email]
        return all(required_fields)

@dataclass
class EdgeConfig:
    """Edge node configuration"""
    node_id: str = os.getenv("EDGE_NODE_ID", "edge_01")
    max_processing_time: int = int(os.getenv("MAX_PROCESSING_TIME", "5"))
    batch_size: int = int(os.getenv("BATCH_SIZE", "100"))
    health_check_interval: int = int(os.getenv("HEALTH_CHECK_INTERVAL", "60"))

@dataclass
class RLConfig:
    """Reinforcement Learning configuration"""
    learning_rate: float = float(os.getenv("RL_LEARNING_RATE", "0.001"))
    discount_factor: float = float(os.getenv("RL_DISCOUNT_FACTOR", "0.95"))
    exploration_rate: float = float(os.getenv("RL_EXPLORATION_RATE", "0.1"))
    memory_capacity: int = int(os.getenv("RL_MEMORY_CAPACITY", "10000"))

# Global configuration instances
firebase_config = FirebaseConfig()
edge_config = EdgeConfig()
rl_config = RLConfig()

# Validate critical configuration
if not firebase_config.validate():
    raise ValueError("Firebase configuration incomplete. Check environment variables.")