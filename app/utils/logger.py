import logging
import os

from config.settings import settings

os.makedirs(settings.logs_path, exist_ok=True)

log_file = os.path.join(settings.logs_path, "pipeline.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("PipelineLogger")