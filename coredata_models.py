from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any, List
from datetime import datetime
import uuid

class DataStream(BaseModel):
    """Base model for real-time data streams"""
    stream_id: str = Field(default_factory=lambda: f"stream_{uuid.uuid4().hex[:8]}")
    source_type: str  # e.g., "sensor", "api", "log", "transaction"
    source_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    payload: Dict[str, Any]
    metadata: Dict[str, Any] = Field(default_factory=dict)
    confidence_score: float = Field(ge=0.0, le=1.0, default=1.0)
    
    @validator('source_type')
    def validate_source_type(cls, v):
        valid_types = {"sensor", "api", "log", "transaction", "social", "iot"}
        if v not in valid_types:
            raise ValueError(f"source_type must be one of {valid_types}")
        return v

class EdgeProcessedData(DataStream):
    """Data after edge processing"""
    edge_node_id: str
    processing_time_ms: float
    features_extracted: List[str] = Field(default_factory=list)
    anomaly_score: Optional[float] = None
    compression_ratio: Optional[float] = None

class FusedData(BaseModel):
    """Fused data from multiple sources"""
    fusion_id: str = Field(default_factory=lambda: f"fusion_{uuid.uuid4().hex[:8]}")
    source_streams: List[str]  # List of stream_ids
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    fused_payload: Dict[str, Any]
    fusion_confidence: float = Field(ge=0.0, le=1.0)
    decision