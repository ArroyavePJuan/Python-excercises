import pandas as pd
import matplotlib.pyplot as mpl

data_frame = pd.DataFrame({
    "Cliente": ["Antonio", "Juan", "Amelia", "Marisa", "Violeta", "Carmen"],
    "Fecha Llegada": ["25/06/2002", "20/06/2002", "14/05/2002", "05/06/2002", "14/06/2002", "07/07/2002"],
    "Días de estancia": [2, 5, 4, 7, 14, 10]
})

data_frame["Precio"] = data_frame["Días de estancia"] * 53.49
data_frame["I.V.A"] = data_frame["Precio"] * 0.16
data_frame["TOTAL"] = data_frame["Precio"] + data_frame["I.V.A"]

mpl.pie(data_frame["TOTAL"], labels=data_frame["Cliente"])

mpl.show()
print(data_frame)

