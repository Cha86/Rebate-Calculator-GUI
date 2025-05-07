
import tkinter as tk
from tkinter import ttk, messagebox

# Front-end margin targets by category (editable)
CATEGORY_MARGIN = {
    "GRAPHIC CARD": 0.04,
    "MOTHERBOARD": 0.06,
    "MONITOR": 0.10,
    "NOTEBOOK": 0.06,
    "DESKTOP PC": 0.06,
    "SSD": 0.04,
    "MEMORY": 0.04,
    "POWER SUPPLY": 0.10,
    "COOLER": 0.10,
    "CHASSIS": 0.20,
    "PERIPHERAL": 0.10,
}

class RebateApp(tk.Tk):
    """A minimal desktop window to calculate rebate for a single promotional event and show margin impact."""

    def __init__(self):
        super().__init__()
        self.title("Rebate & Margin Impact Calculator")
        self.geometry("500x500")
        self.resizable(False, False)
        self._build()

    def _build(self):
        pad = {"padx": 10, "pady": 6}

        # Category selector
        ttk.Label(self, text="Category:").grid(row=0, column=0, sticky="w", **pad)
        self.category_var = tk.StringVar()
        ttk.Combobox(
            self,
            textvariable=self.category_var,
            values=list(CATEGORY_MARGIN.keys()),
            state="readonly",
        ).grid(row=0, column=1, **pad)

        # Numeric input fields
        fields = [
            ("MSRP", "msrp"),
            ("Cost", "cost"),
            ("Promo price", "promo"),
            ("Event qty", "qty"),
        ]
        self.entries = {}
        for i, (label, key) in enumerate(fields, start=1):
            ttk.Label(self, text=f"{label}:").grid(row=i, column=0, sticky="w", **pad)
            var = tk.DoubleVar()
            self.entries[key] = var
            ttk.Entry(self, textvariable=var).grid(row=i, column=1, **pad)

        # Calculate button
        ttk.Button(self, text="Calculate rebate", command=self._calculate).grid(
            row=6, column=0, columnspan=2, pady=15
        )

        # Result display
        self.result = tk.Text(self, width=45, height=10, borderwidth=0)
        self.result.grid(row=7, column=0, columnspan=2, padx=10)
        self.result.config(state="disabled")

    def _calculate(self):
        cat = self.category_var.get()
        if not cat:
            messagebox.showerror("Input error", "Please choose a category.")
            return
        try:
            msrp = self.entries["msrp"].get()
            cost = self.entries["cost"].get()
            promo = self.entries["promo"].get()
            qty = self.entries["qty"].get()
        except tk.TclError:
            messagebox.showerror("Input error", "All numeric fields must be filled.")
            return

        # Target margin for this category
        target_margin = CATEGORY_MARGIN[cat]
        # Calculate required per-unit rebate to hit target margin
        rebate = cost - (1 - target_margin) * promo
        cost_after_ir = cost - rebate
        # Profit and ROI
        profit_per_unit = promo - cost_after_ir
        total_profit = profit_per_unit * qty
        event_budget = rebate * qty
        roi = total_profit / event_budget if event_budget else float("nan")

        # Margin impact analysis
        baseline_margin_pct = (promo - cost) / promo if promo else 0
        actual_margin_pct = profit_per_unit / promo if promo else 0
        margin_delta = actual_margin_pct - baseline_margin_pct

        # Prepare output text
        output = (
            f"Category target margin: {target_margin:.2%}\n"
            f"Required rebate per unit: ${rebate:,.2f}\n"
            f"Cost after IR: ${cost_after_ir:,.2f}\n"
            f"Total event budget: ${event_budget:,.2f}\n"
            f"Expected ROI: {roi:.2f}\n"
            "\n"
            f"Baseline margin (no rebate): {baseline_margin_pct:.2%}\n"
            f"Actual margin (after rebate): {actual_margin_pct:.2%}\n"
            f"Margin impact: {margin_delta:.2%} change"
        )

        # Display in text widget
        self.result.config(state="normal")
        self.result.delete("1.0", tk.END)
        self.result.insert(tk.END, output)
        self.result.config(state="disabled")

if __name__ == "__main__":
    RebateApp().mainloop()
