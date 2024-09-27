# Configuration file for lab.
import os

c = get_config()  #noqa

c.ServerApp.ResourceUseDisplay.show_host_usage=True

c.ServerApp.ResourceUseDisplay.track_cpu_percent=True

c.ServerApp.ResourceUseDisplay.track_disk_usage=True

c.ServerApp.ResourceUseDisplay.mem_limit=int(os.environ['MEM_LIMIT'])
