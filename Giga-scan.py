import os
import subprocess
import re
import asyncio
import aiohttp

class SSLChecker:
    def __init__(self, mass_scan_results_file="masscanResults.txt", ips_file="ips.txt", masscan_rate=10000, chunkSize=2000, timeout=2):
        self.mass_scan_results_file = mass_scan_results_file,
        self.ips_file = ips_file,
        self.masscan_rate = masscan_rate,
        self.timeout=timout
        slef.chunkSize=chunkSize

    def start_vpn(self):
        try:
            # Connect to ExpressVPN using the default location or a specified location
            command = "expressvpn connect"  # Or use "expressvpn connect LOCATION" to specify
            subprocess.run(command, shell=True, check=True)
            print("VPN connected successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error while connecting to VPN: {e}")

    def stop_vpn(self):
        try:
            # Disconnect from ExpressVPN
            command = "expressvpn disconnect"
            subprocess.run(command, shell=True, check=True)
            print("VPN disconnected successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error while disconnecting from VPN: {e}")

    def run_massScan(self):
        try:
            command = f"sudo masscan -p80,443 --rate {self.masscan_rate} --wait 0 -iL {self.ips_file} -oL {self.mass_scan_results_file}"
            subprocess.run(command,shell=True, check=True)
       
        except subprocess.CalledProcessError as e:
           print(f"Error while running masscan: {e}")

        except FileNotFoundError:
            print("Masscan exec not found")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def check_and_create_files(self, *file_paths):
        for file_path in file_paths:
            if not os.path.exists(file_path):
                # If the file doesn't exist,create it
                with open(file_path, "w") as file:
                    pass
                print(f'File "{file_path}" has been created')

    async def extract_domains():
        try:
            with open(self.mass_scan_results_file, "r") as file:
                content=file.read()

            ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            ip_addresses=re.findall(ip_pattern,content)
            
            for i in range(0,len(ip_addresses), self.chunkSize):
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.MAX_CONCURRENT,ssl=False)) as session:
                
            

    def main(self):
        self.check_and_create_files(self.mass_scan_results_file, self.ips_file)
        self.start_vpn()
        self.run_massScan()
        await self.extract_domains()
        self.stop_vpn()

if __name__ == "__main__":
    ssl_checker = SSLChecker()
    ssl_checker.main()

