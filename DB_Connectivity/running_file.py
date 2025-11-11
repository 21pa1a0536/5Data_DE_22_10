from student_db import *

con = create_connection("student_data.db")

create_table(con)

Insert_data(con, 5, "Usopp", "CSBS", 99)

fetch_full_data(con)
fetch_specific_Row(con, 2)

con.close()







