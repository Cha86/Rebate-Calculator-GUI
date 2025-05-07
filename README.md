Rebate & Margin Impact Calculator

A lightweight Python desktop application to help pricing and sales teams quickly calculate promotional rebates and understand their impact on profit margins and ROI.

Features

Front-end margin targets per product category (editable in code).

Required rebate calculation to hit a chosen margin target.

Cost after internal rebate (IR), profit per unit, total event budget, and expected ROI.

Margin impact analysis comparing baseline margin (no rebate) vs. actual margin (after rebate).

Simple Tkinter GUI—no command‑line flags or configuration files.

Prerequisites

Python 3.7+

Tkinter (bundled with most Python installations)

Installation

Clone the repository

git clone https://github.com/yourorg/rebate-calculator.git
cd rebate-calculator

(Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows

Install dependencies

# No external packages required beyond standard library

Usage

Run the GUI:

python rebate_optimizer.py

Select the product category from the dropdown.

Enter:

MSRP (Manufacturer’s Suggested Retail Price)

Cost (unit cost before rebate)

Promo price (selling price during promotion)

Event quantity (forecasted units sold)

Click Calculate rebate.

Review the results in the bottom pane:

Required rebate per unit

Cost after IR

Total event budget

Expected ROI

Baseline margin (no rebate) vs. actual margin

Margin impact (difference in percentage points)

Configuration

Front-end margin targets are defined in the CATEGORY_MARGIN dictionary at the top of rebate_optimizer.py. Adjust values or add new categories as needed.

Contributing

Fork the repo.

Create a feature branch: git checkout -b feature/your-feature

Commit your changes: git commit -m "Add awesome feature"

Push to your branch: git push origin feature/your-feature

Open a pull request.
