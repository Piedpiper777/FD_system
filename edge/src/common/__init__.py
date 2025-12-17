"""
通用功能模块
"""

from .routes import file_upload_bp, connection_bp, health_bp, training_bp
from .services import CloudCommunicationService

__all__ = [
    'file_upload_bp',
    'connection_bp',
    'health_bp',
    'training_bp',
    'CloudCommunicationService'
]
