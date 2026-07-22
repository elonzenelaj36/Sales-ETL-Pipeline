import logging
from pathlib import Path

# Krijojmë folderin logs nëse nuk ekziston
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Konfigurimi i logger-it
logging.basicConfig(
    filename=log_dir / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)