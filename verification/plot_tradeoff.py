#!/usr/bin/env python3
"""Plot committed high-precision samples against the analytic limiting law.

Run verify_driven_qubit.py --json to regenerate the input data. This script
only renders those calculations; it performs no numerical optimization.
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    root = Path(__file__).resolve().parents[1]
    report = json.loads((root / "verification/outputs/driven-qubit.json").read_text())
    samples = report["finite_ratio_samples"]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "svg.fonttype": "none", "svg.hashsalt": "delay-tradeoff"})
    fig, ax = plt.subplots(figsize=(7.7, 4.8), constrained_layout=True)
    k = np.linspace(0, 2.5, 501)
    ax.plot(k, np.maximum(0, k-k*k/2), color="#202833", lw=2,
            label=r"Limit: $[k-k^2/2]_+$")
    for time, color, marker in [(10, "#007F86", "o"), (20, "#D27630", "s"),
                                (40, "#7868A8", "+")]:
        rows = [row for row in samples if float(row["time"]) == time]
        ax.plot([float(r["k"]) for r in rows],
                [float(r["scaled_concurrence"]) for r in rows],
                linestyle="none", marker=marker, markersize=6,
                markerfacecolor="none", markeredgewidth=1.3, color=color,
                label=rf"$\gamma\tau={time}$, resonant source")
    ax.axvline(1, color="#758493", lw=.9, ls=":", zorder=0)
    ax.set(xlabel=r"Scaled stationary mixedness  $k=s/e^{-\gamma\tau/2}$",
           ylabel=r"Scaled concurrence  $C(\sigma_\tau)/e^{-\gamma\tau}$",
           xlim=(-.04, 2.55), ylim=(-.015, .58))
    ax.set_title("Stationary entanglement balances source mixedness and delay",
                 loc="left", fontsize=12, pad=15)
    ax.grid(axis="y", color="#e1e5e9", lw=.7)
    ax.legend(frameon=False, loc="upper right", fontsize=9)
    out = root / "figures"
    out.mkdir(exist_ok=True)
    fig.savefig(out / "stationary-tradeoff.svg", metadata={"Date": None})
    svg = out / "stationary-tradeoff.svg"
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
    fig.savefig(out / "stationary-tradeoff.png", dpi=180,
                metadata={"Software": "Matplotlib"})
    print("Wrote figures/stationary-tradeoff.svg and .png from committed samples.")


if __name__ == "__main__":
    main()
