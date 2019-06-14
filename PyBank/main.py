import os, csv

bank_input = "PyBank_data.csv"

t_m = []
t_p = []
m_p_c =[]
#Write up open pathway and csvreader then indicate variable as listed above
with open(bank_input) as finance:

    csvreader = csv.reader(finance, delimiter = ",")

    header = next(csvreader)

    for row in csvreader:

        t_m.append(row[0])
        t_p.append(int(row[1]))

    for i in range(len(t_p)-1):

        m_p_c.append(t_p[i +1]-t_p[i])

#indicate max and min from each month in the list to the proper month
i_value = max(m_p_c)
d_value = min(m_p_c)

m_i_m = m_p_c.index(max(m_p_c)) + 1
m_d_m = m_p_c.index(min(m_p_c)) + 1

#Print

print("Financial Anaylsis")
print("------------------------")
print(f"Total Months: {len(t_m)}")
print(f"Total: ${sum(t_p)}")
print(f"Average change: {round(sum(m_p_c)/len(m_p_c),2)}")
print(f"Greatest Increase in Profits: {t_m[i_value]} (${(i_value)})")
print(f"Greatest Decrease in Profits: {t_m[d_value]} (${(d_value)})")

#file command Financial_Anaylsis_Summary

with open("PyBank_data.csv", "w") as file:

    file.write("Financial Anaylsis")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(t_m)}")
    file.write("\n")
    file.write(f"Total: ${sum(t_p)}")
    file.write("\n")
    file.write(f"Average change: {round(sum(m_p_c)/len(m_p_c),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {t_m[m_i_m]} (${(str(i_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {t_m[m_d_m]} (${(str(d_value))})")






