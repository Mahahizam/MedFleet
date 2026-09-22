# MedFleet 

A medical device maintenance prioritization tool that calculates a transparent risk score and generates a prioritized list of devices to check.

## Project Overview

Medical equipment maintenance can become reactive or inefficient when hospitals have many devices with different usage levels, error histories, maintenance dates, and clinical importance.

**MedFleet** aims to support maintenance teams by identifying which medical devices should receive attention first.

The project starts with a simple, transparent rule-based approach for the MVP. Machine learning can be explored later as an upgrade once the core workflow is working.

## MVP

The MVP will:

1. Store the required medical-device data.
2. Calculate a maintenance risk score for each device.
3. Rank devices by their risk score.
4. Generate a prioritized list of devices to check each week.

### MVP Risk Factors

The initial risk score is based on three factors:

* **Error history** — recent device errors increase risk.
* **Time since last maintenance** — devices that have not been maintained for longer receive a higher score.
* **Clinical criticality** — devices that are more clinically critical receive a higher priority.

The weights used for these factors are **project assumptions for the MVP** and may be revised after testing.

## Example Risk Score

The MVP uses a weighted formula:

```text
Risk Score =
    Error Score × Error Weight
  + Maintenance Score × Maintenance Weight
  + Criticality Score × Criticality Weight
```

The purpose of this approach is to make the prioritization easy to understand and inspect before introducing more complex prediction methods.

## Data

The MVP requires information such as:

* Device ID
* Device type
* Department
* Clinical criticality
* Usage information
* Error/failure history
* Last maintenance date
* Next maintenance or inspection due date

A public dataset will be preferred where suitable. If a suitable dataset is not available, synthetic data may be used for development and testing.

## Project Status

🚧 **In development**

Current focus:

* [ ] Define data requirements
* [ ] Define risk-score formula
* [ ] Prepare dataset
* [ ] Implement risk-score calculation
* [ ] Generate prioritized maintenance list
* [ ] Test the scoring logic
* [ ] Build a simple interface

## Project Structure

```text
MedFleet/
│
├── data/
│   └── sample_devices.csv
│
├── src/
│   └── risk_score.py
│
├── tests/
│   └── test_risk_score.py
│
├── app.py
├── requirements.txt
└── README.md
```

## Technology

The project is being developed with:

* Python
* Pandas
* Streamlit
* Git & GitHub

Additional technologies may be added only when they support the MVP or a clearly defined later improvement.

## Future Improvements

After the MVP is complete, possible extensions include:

* Machine-learning-based risk prediction
* Anomaly detection
* Remaining useful life prediction
* Comparison between rule-based and ML approaches
* Additional maintenance and regulatory data

These features are **not required for the current MVP**.

## Project Goal

The goal of MedFleet is to create a practical and understandable maintenance-prioritization workflow that can help answer one simple question:Which medical devices should we check first this week?

> **Which medical devices should we check first this week?**
