# Configuration file for lab.
import os

c = get_config()  # noqa

# jupyter-resource-usage extension

if 'MEM_LIMIT' in os.environ:
    # Display memory limit
    c.ServerApp.ResourceUseDisplay.mem_limit = int(os.environ['MEM_LIMIT'])

# Flash the warning to the user when they are within 10% of the memory limit
c.ServerApp.ResourceUseDisplay.mem_warning_threshold = 0.1

# Display host information from the Kernel Usage sidebar
c.ServerApp.ResourceUseDisplay.show_host_usage = True

# Enable CPU usage tracking
c.ServerApp.ResourceUseDisplay.track_cpu_percent = True

# Enable disk usage tracking
c.ServerApp.ResourceUseDisplay.track_disk_usage = True

# When to flag disk usage warning
c.ServerApp.ResourceUseDisplay.disk_warning_threshold = 0.1