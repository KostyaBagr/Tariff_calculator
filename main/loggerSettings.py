
import json
from datetime import datetime


class CustomLogger:
    """Custom settings for logger."""
    def _serialize_value(self, value):
        """
        Convert value to str
        """
        if isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, bytes):
            return value.decode('utf-8', 'replace')
        return str(value)
    
    def json_data(self, data):
        """
        Convert data to json format.
        """
        data_dict = {key: self._serialize_value(value) for key, value in 
                     data.validated_data.items()}
        return json.dumps(data_dict, indent=4)