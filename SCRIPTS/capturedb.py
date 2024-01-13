
import mysql.connector as mysql
from datetime import datetime
# Connect to the Database
db = mysql.connect(
    host = "197.26.19.254",
    port = "1406",
    user = "root",
    passwd = "root",
    database = "FlowDatabase"
)
print(db)
cursor = db.cursor()
from nfstream import NFStreamer
my_streamer = NFStreamer(source="ens160", #  Live capture
                         decode_tunnels=True,
                         bpf_filter=None,
                         promiscuous_mode=True,
                         snapshot_length=1536,
                         idle_timeout=1,
                         active_timeout=1800,
                         accounting_mode=0,
                         udps=None,
                         n_dissections=20,
                         statistical_analysis=False,
                         splt_analysis=0,
                         n_meters=0,
                         performance_report=0,
                         system_visibility_mode=0,
                         system_visibility_poll_ms=100,
                         system_visibility_extension_port=28314)


for flow in my_streamer:
    print(flow.bidirectional_bytes)
    result=cursor.execute("INSERT INTO NETWORK_FLOW(application_name, application_category_name,bidirectional_bytes,time) VALUES (%s,%s,%s,%s)", (flow.application_name, flow.application_category_name, flow.bidirectional_bytes, datetime.now()))  # Send a query
    print(result)
    db.commit()
# Close connection
db.close()
