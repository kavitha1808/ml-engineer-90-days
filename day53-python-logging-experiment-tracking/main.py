import logging
from datetime import datetime
import random
import os

# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)

# Log file name with timestamp
log_filename = f"logs/experiment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def run_experiment(learning_rate, epochs, batch_size):
    logger.info("Starting experiment")
    logger.info(f"Parameters -> learning_rate={learning_rate}, epochs={epochs}, batch_size={batch_size}")

    # Simulated training metrics
    train_accuracy = round(random.uniform(0.80, 0.95), 4)
    val_accuracy = round(random.uniform(0.75, train_accuracy), 4)
    train_loss = round(random.uniform(0.10, 0.50), 4)
    val_loss = round(random.uniform(0.15, 0.60), 4)

    logger.info(f"Training completed")
    logger.info(f"Train Accuracy: {train_accuracy}")
    logger.info(f"Validation Accuracy: {val_accuracy}")
    logger.info(f"Train Loss: {train_loss}")
    logger.info(f"Validation Loss: {val_loss}")

    if val_accuracy > 0.85:
        logger.info("Experiment result: Good model performance")
    else:
        logger.warning("Experiment result: Needs tuning")

    return {
        "learning_rate": learning_rate,
        "epochs": epochs,
        "batch_size": batch_size,
        "train_accuracy": train_accuracy,
        "val_accuracy": val_accuracy,
        "train_loss": train_loss,
        "val_loss": val_loss
    }


if __name__ == "__main__":
    logger.info("===== DAY 53: LOGGING + EXPERIMENT TRACKING =====")

    experiments = [
        {"learning_rate": 0.01, "epochs": 10, "batch_size": 32},
        {"learning_rate": 0.001, "epochs": 20, "batch_size": 64},
        {"learning_rate": 0.0005, "epochs": 30, "batch_size": 128}
    ]

    results = []

    for exp in experiments:
        logger.info("-" * 60)
        result = run_experiment(
            learning_rate=exp["learning_rate"],
            epochs=exp["epochs"],
            batch_size=exp["batch_size"]
        )
        results.append(result)

    logger.info("-" * 60)
    best_experiment = max(results, key=lambda x: x["val_accuracy"])

    logger.info("Best Experiment Summary")
    logger.info(f"Best Params -> lr={best_experiment['learning_rate']}, "
                f"epochs={best_experiment['epochs']}, "
                f"batch_size={best_experiment['batch_size']}")
    logger.info(f"Best Validation Accuracy: {best_experiment['val_accuracy']}")
    logger.info("===== END OF DAY 53 =====")
