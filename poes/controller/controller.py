import xlwings as xw
from poes.model.poes import poes
from poes.model.utils import param_stoiip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns

# Define Sheet names
SUMMARY = "Summary"
RESULTS = "Results"

# Define Column Names
VARIABLES = "Variables"
VALUES = "Values"
DISTRIBUTION = "Distribution"
LOC = "Loc"
SCALE = "Scale"
C = "c"
LIM_MIN = "Lim min"
LIM_MAX = "Lim max"

# Call cells from Ms Excell
DF_POES = "df_poes"
DET_POES = "det_values"
REALIZATIONS = "realizations"
SEED = "seed"

# Write values in Excel from Python
POES_DET = "det_poes"
POES_PROB = "prob_poes"
POES_ARRAY = "poes_array"

# Index of POES Parameters
AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX = 0, 1, 2, 3, 4


def main():
    wb = xw.Book.caller()

    # Define sheet
    sheet = wb.sheets[SUMMARY]

    # Call values from Excel
    params = sheet[DET_POES].options(np.array).value

    # Calculate poes from Python to Excel
    sheet[POES_DET].value = poes(*params)

    # Calculate Stochastic Stoiip
    df_poes = sheet[DF_POES].options(pd.DataFrame, expand="table", index=False).value

    # Call realizations cell
    realizations = int(sheet[REALIZATIONS].value)

    # Call seed cell
    seed = int(sheet[SEED].value)

    # Define random values for STOIIP Parameters
    input_col_names = df_poes[VARIABLES].to_list()

    area_col, h_col, poro_col, swi_col, boi_col = tuple(input_col_names)

    input_idx = [AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX]

    input_dict = dict(zip(input_col_names, input_idx))

    results_dict = {}

    for col, idx, in input_dict.items():
        results_dict[col] = param_stoiip(df_poes, idx, DISTRIBUTION, LOC, SCALE, realizations,
                                         C, LIM_MIN, LIM_MAX, seed)

    # Calculate Stochastic Stoiip into results_dict
    results_dict[POES_PROB] = poes(results_dict[area_col], results_dict[h_col], results_dict[poro_col],
                                   results_dict[swi_col], results_dict[boi_col])

    # Calculate mean, std, P90, P50, P10 from STOIIP
    summary_stoc_results = [results_dict[POES_PROB].mean(), results_dict[POES_PROB].std(),
                            np.percentile(results_dict[POES_PROB], 10),
                            np.percentile(results_dict[POES_PROB], 50),
                            np.percentile(results_dict[POES_PROB], 90)]

    # Send stochastic values to Excel
    sheet[POES_PROB].options(transpose=True).value = summary_stoc_results

    # Call sheet results
    sheet_re = wb.sheets[RESULTS]

    # Create dataframe from results_dict
    df_results = pd.DataFrame(results_dict)

    # Send df_results to Results sheet in Ms. Excel
    sheet_re[POES_ARRAY].options(pd.DataFrame, expand="table", index=False).value = df_results

    # Create Histogram from Stochastic Stoiip
    eng_formatter = ticker.EngFormatter()
    sns.set_style("white")
    fig = plt.figure(figsize=(8, 6))

    ax = sns.histplot(df_results[POES_PROB], color="lightgray", kde=True)

    plt.axvline(
        summary_stoc_results[2],
        ymax=0.85,
        color="darkorange",
        linewidth=1.5,
        linestyle="--",
        label="P90",
    )

    plt.axvline(
        summary_stoc_results[3],
        ymax=0.85,
        color="gold",
        linewidth=1.5,
        linestyle="--",
        label="P50",
    )

    plt.axvline(
        summary_stoc_results[4],
        ymax=0.85,
        color="green",
        linewidth=1.5,
        linestyle="--",
        label="P10",
    )

    ax.xaxis.set_major_formatter(eng_formatter)
    plt.xlabel("STOIIP (STB)")
    plt.suptitle("Stochastic STOOIP")
    plt.legend(loc=0)

    # Send Histogram to Ms. Excel
    sheet.pictures.add(fig, name="Histogram", update=True, left=sheet.range("J2").left)


if __name__ == "__main__":
    xw.Book("stoiip.xlsm").set_mock_caller()
    main()
