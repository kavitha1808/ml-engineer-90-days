# Day 53 - Logging in Python + Experiment Tracking Mindset

## Overview
This project demonstrates how to use Python logging for better visibility into program execution and introduces the experiment tracking mindset used in machine learning workflows.

Instead of relying only on print statements, logging helps record:
- Experiment start and end
- Hyperparameters used
- Training metrics
- Validation metrics
- Warnings for poor performance
- Best experiment summary

This is a beginner-friendly simulation of how ML engineers track experiments.

## Concepts Covered
- Python `logging` module
- Logging levels: `INFO`, `WARNING`
- Logging to both console and file
- Timestamped log files
- Tracking hyperparameters
- Recording experiment results
- Comparing multiple experiments
- Selecting the best experiment based on validation accuracy

## Features
- Creates a `logs/` folder automatically
- Generates a new log file for each run
- Logs experiment parameters
- Simulates training and validation metrics
- Warns when model performance is weak
- Finds and logs the best experiment

## Example Output
```bash
2026-03-27 10:00:00,123 | INFO | ===== DAY 53: LOGGING + EXPERIMENT TRACKING =====
2026-03-27 10:00:00,124 | INFO | ------------------------------------------------------------
2026-03-27 10:00:00,124 | INFO | Starting experiment
2026-03-27 10:00:00,124 | INFO | Parameters -> learning_rate=0.01, epochs=10, batch_size=32
2026-03-27 10:00:00,124 | INFO | Training completed
2026-03-27 10:00:00,124 | INFO | Train Accuracy: 0.9123
2026-03-27 10:00:00,124 | INFO | Validation Accuracy: 0.8612
2026-03-27 10:00:00,124 | INFO | Train Loss: 0.2145
2026-03-27 10:00:00,124 | INFO | Validation Loss: 0.2987
2026-03-27 10:00:00,124 | INFO | Experiment result: Good model performance
...
2026-03-27 10:00:00,130 | INFO | Best Experiment Summary
2026-03-27 10:00:00,130 | INFO | Best Params -> lr=0.001, epochs=20, batch_size=64
2026-03-27 10:00:00,130 | INFO | Best Validation Accuracy: 0.8934
2026-03-27 10:00:00,130 | INFO | ===== END OF DAY 53 =====
```
## Learning Outcome
- By completing this project, you will understand:
- Why logging is better than print statements in real projects
- How to keep experiment records for reproducibility
- How ML engineers compare multiple runs systematically
- How experiment tracking helps in debugging and model improvement
