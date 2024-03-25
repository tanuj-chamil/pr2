import pandas as pd
import numpy as np
import re
import io

pd.options.plotting.backend = "plotly"


def read_data(path):
    return pd.read_csv(path)


def plot_data(data):
    return data.plot(x="x", y="y")


def read_dsc(path):
    with open(
        path,
        encoding="utf-16-le",
    ) as file:
        raw = file.read()
        raw = raw.split("StartOfData")
        metadata = raw[0].split("\n")
        data = raw[1]

    for i, m in enumerate(metadata):
        if re.match(r"Nsig\t\d", m):
            nsig = int(m.split("\t")[-1])
            nsig_loc = i
            break

    signal_names = metadata[nsig_loc + 1 : nsig_loc + nsig + 1]
    signals_names = [s.split("\t")[-1] for s in signal_names]
    signals = pd.read_csv(
        io.StringIO(data), delimiter="\t", names=[f"sig{i}" for i in range(1, nsig + 1)]
    )
    return signals


if __name__ == "__main__":
    print(read_dsc("dsc_data\\empty_pans"))
