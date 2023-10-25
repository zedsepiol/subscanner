from __init__ import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A CLI tool for scanning and discovering subdomains of a target domain.",
        prefix_chars="-",
    )

    parser.add_argument(
        "-d", "--domain", 
        type=str, 
        help="Enter the main domain to scan for its associated subdomains, facilitating a thorough web service scan."
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="txt",
        help="Specify the name and path of the output file for the retrieved data."
    )

    parser.add_argument(
        "-s", "--sort",
        action="store_true",
        help="Method of sorting specified data."
    )

    args = parser.parse_args()
    
    assert args.domain, "Domain address cannot be empty!"
    
    urlValidate = URLValidator()
    httpValidate = HTTPValidator()


    print(f"{Fore.RED}[*] {Fore.RESET}-> {Fore.GREEN}Checking the URL address...{Fore.RESET}")
    urlValidate = urlValidate.is_valid_url(args.domain)
    
    print(f"{Fore.RED}[*] {Fore.RESET}-> {Fore.GREEN}Sending request to WEB address!{Fore.RESET}")
    httpValidate = httpValidate.is_valid_http_status(args.domain)

    assert httpValidate, "HTTP address could not be verified!"
    assert urlValidate, "Failed URL verification!"

    print(f"{Fore.RED}[*] {Fore.RESET}-> {Fore.GREEN}Subdomain addresses are being identified...{Fore.RESET}")
    fetcher = DataFetcher().fetch_data(args.domain)
    assert fetcher, "Data could not be analyzed!"


    datas = TXTConverter(fetcher).convert_data()
    if args.sort:
        datas = datas.splitlines()
        datas.sort()
        print(f"\n".join(f"{Fore.BLUE}[!]{Fore.RESET} -> {Fore.GREEN}{data}{Fore.RESET}" for data in datas))
    else:
        print(f"\n".join(f"{Fore.BLUE}[!]{Fore.RESET} -> {Fore.GREEN}{data}{Fore.RESET}" for data in datas.split()))


    if args.output == "txt":
        with open("output/domains.txt", "w") as f:
            f.write("\n".join(data for data in datas))