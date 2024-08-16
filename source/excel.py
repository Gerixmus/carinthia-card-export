import pandas as pd
from timing import timeit

#TO-DO switch to openpyxl
@timeit
def get_excel(excursion_destinations):
    colums = ["Name", "Description", "Contact"]
    data = [['=HYPERLINK("%s", "%s")' % (dest.url, dest.name.replace("\"", "'")), dest.description, str.join(", ", dest.contact_info)] for dest in excursion_destinations]
    df = pd.DataFrame(data=data, columns=colums)
    df.to_excel('destinations.xlsx', index=False)