#!/usr/bin/env python3
import os
import platform
import psutil
import time

def system_info():
    print(f"System: {platform.system()} {platform.release()}")
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds // 3600
    print(f"Uptime: {uptime_hours:.0f} hours\n")

def cpu_info():
    print("CPU Info:")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%\n")

def memory_info():
    mem = psutil.virtual_memory()
    print("Memory Info:")
    print(f"Total: {mem.total // (1024 * 1024)} MB")
    print(f"Used: {mem.used // (1024 * 1024)} MB")
    print(f"Usage: {mem.percent}%\n")

def disk_info():
    disk = psutil.disk_usage('/')
    print("Disk Info (/ partition):")
    print(f"Total: {disk.total // (1024 * 1024 * 1024)} GB")
    print(f"Used: {disk.used // (1024 * 1024 * 1024)} GB")
    print(f"Usage: {disk.percent}%\n")

if __name__ == "__main__":
    print("===== System Health Check =====\n")
    system_info()
    cpu_info()
    memory_info()
    disk_info()