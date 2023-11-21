import pandas as pd
import networkx as kx
df = pd.read_csv("data\\sunday_times_panama_data.zip",
                 encoding="utf8",sep=",",encoding_errors="ignore")
print(df.head(5))

"""
company_url          OpenCorporates URL for the company.
company_name         Company name as stated in the Panama companies registry.
officer_position_es  Officer's position in the company, as stated in Spanish in the Panama companies registry.
officer_position_en  Officer's position in the company, translated into English by the Sunday Times Data Team.
officer_name         Officer's name, as stated in the Panama companies registry. Note that this can be the name of a person or another company. Sometimes more than one person is listed in one record.
inc_date             Incorporation date of the company.
dissolved_date       Dissolution date of the company, or 0000-00-00 if the company is current.
updated_date         Time and date given by the Panama companies registry when OpenCorporates retrieved the record.
company_type         Company type as stated in the Panama companies registry in Spanish.
mf_link              Indicator denoting officers we have linked to Mossack Fonseca. Please note that our search has not been exhaustive - there are likely many more associates of Mossack Fonseca in this data who we have not yet discovered. 0 = not linked, 1 = linked.
"""

g=kx.DiGraph()
for ind, row in df.iterrows():
    company_attr = row[["company_url","company_name","inc_date","dissolved_date","company_type"]]
    officer_attr = row[["officer_name", "mf_link"]]
    rel_attr = row[["officer_position_en"]]
    g.add_nodes_from([(row["company_name"], company_attr.to_dict())])
    g.add_nodes_from([(row["officer_name"], officer_attr.to_dict())])
    edge = g.add_edge(row["officer_name"],row["company_name"],**rel_attr.to_dict())

print(g)