import pandas as pd
import plotly.express as pe

data = pd.read_csv("data.csv")

Mean = data.groupby(["student_id","level"],as_index = False)["attempt"].mean()

Graph = pe.scatter(
    Mean,x = "student_id",y = "level",color = "attempt",size = "attempt"
)

Graph.show()