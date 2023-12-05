import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup


OK_TEXT = "\033[92mOK\033[0m"
CHANGED_TEXT = "\033[93mCHANGED\033[0m"
ERROR_TEXT = "\033[91mERROR\033[0m"
SEPARATOR_TEXT = '-' * 30 + '\n'


def get_parsed_webpage(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def log(level, msg):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    level = level.lower()
    if level == 'ok':
        print(f"{now} - [{OK_TEXT}] - {msg}")
    elif level == 'changed':
        print(f"{now} - [{CHANGED_TEXT}] - {msg}")
    elif level == 'error':
        print(f"{now} - [{ERROR_TEXT}] - {msg}")


def monitoring_loop(urls, cooldown):
    try:
        # First check
        print("\nPierwsze sprawdzenie...\n")
        last_content = {}
        webpage_responses = {}
        for url in urls:
            # Add url entry to responses dict
            webpage_responses[url] = {'ok': 0, 'changed': 0, 'error': 0}

            # Fetch webpage
            try: 
                last_content[url] = get_parsed_webpage(url)

            # Error
            except:
                urls.remove(url)
                log('error', url)
                webpage_responses[url]['error'] += 1
                continue

            # Ok
            log('ok', url)
            webpage_responses[url]['ok'] += 1
        print(SEPARATOR_TEXT)
        time.sleep(cooldown)

        # Monitoring loop
        turn = 1
        while True:
            print(f"Tura: {turn}\n")
            for url in urls:
                # Fetch webpage
                try:
                    soup = get_parsed_webpage(url)

                # Error
                except:
                    log('error', url)
                    webpage_responses[url]['error'] += 1
                    continue

                # Changed
                if soup != last_content[url]:
                    log('changed', url)
                    webpage_responses[url]['changed'] += 1
                    diff = [i.strip() for i in soup if i not in last_content[url]]
                    for i in diff:
                        print(i)

                # Ok
                else:
                    log('ok', url)
                    webpage_responses[url]['ok'] += 1

                # Update last content
                last_content[url] = soup
            print(SEPARATOR_TEXT)
            turn += 1
            time.sleep(cooldown)

    # Print summary on exit
    except KeyboardInterrupt:
        print("\n\nMonitoring zakończony. Podsumowanie:\n")
        for url in webpage_responses:
            print(f"{url} - {OK_TEXT}: {webpage_responses[url]['ok']}, {CHANGED_TEXT}: {webpage_responses[url]['changed']}, {ERROR_TEXT}: {webpage_responses[url]['error']}")
        print()


def main():
    # Set cooldown
    cooldown = input('Podaj cooldown monitoringu w sekundach (60): ')
    if cooldown == '':
        cooldown = 60
    else:
        cooldown = int(cooldown)
    

    # Get urls from file
    with open('urls.txt', 'r') as f:
        urls = [line.strip() for line in f]

    # Run monitoring
    monitoring_loop(urls, cooldown)


if __name__ == '__main__':
    main()
