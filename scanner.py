class SSLChecker:
    def __init__(
        self, mass_scan_results_file="mass_scan_results.txt", ips_file="ips.txt"
    ):
        self.mass_scan_results_file = mass_scan_results_file()
        self.ips_file = ips_file()

    def main(self):
        self.check_and_create_files


if __name__ == "__main__":
    ssl_checker = SSLChecker()
