import csv
import pandas as pd
import numpy as np

ls=list()
ls.append(company_name)
ls.append(company_add)
ls.append(contact_name)
ls.append(company_web)
ls.append(company_ali)
ls.append(business_type)
ls.append(location)
ls.append(main_products)
ls.append(total_employees)
ls.append(total_annual_revenue)
ls.append(year_established)
ls.append(top_3_markets)
ls.append(response_time)
ls.append(response_rate)
ls.append(certification)
ls.append(product_certification)
ls.append(market)
ls.append(export)
ls.append(trade_employees)
df=pd.DataFrame(ls)
df=df.T
df.to_csv("ali_test_all.csv",index=False)