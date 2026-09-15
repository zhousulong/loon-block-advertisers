import urllib.request
import re
import sys

URL = "https://kelee.one/Tool/Loon/Lpx/BlockAdvertisers.lpx"
HEADERS = {
    "User-Agent": "Loon/338 CFNetwork/1498.700.2 Darwin/23.6.0"
}

# Domains/keywords to exclude (Google and Yandex)
EXCLUDE_KEYWORDS = [
    "doubleclick",
    "googlesyndication",
    "googleapis.com",
    "google.com",
    "app-analytics-services.com",
    "app-ads-services.com",
    "yandex",
    "appmetrica",
]

def should_exclude(line: str) -> bool:
    line_lower = line.strip().lower()
    # Check if line contains any excluded keywords in the domain portion
    for kw in EXCLUDE_KEYWORDS:
        if kw in line_lower:
            return True
    return False

def main():
    print(f"Fetching latest rules from {URL} ...")
    req = urllib.request.Request(URL, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
    except Exception as e:
        print(f"Failed to fetch: {e}")
        sys.exit(1)

    lines = content.splitlines()
    filtered_lines = []
    removed_count = 0

    for line in lines:
        stripped = line.strip()
        # Handle metadata line
        if stripped.startswith("#!desc="):
            # Remove "Google、" from description if present
            line = line.replace("Google、", "").replace("Google,", "")
            filtered_lines.append(line)
            continue

        if stripped.startswith("DOMAIN") or stripped.startswith("IP-CIDR") or stripped.startswith("AND"):
            if should_exclude(stripped):
                print(f"[-] Removed rule: {stripped}")
                removed_count += 1
                continue

        filtered_lines.append(line)

    # Clean up excess consecutive blank lines
    output_text = "\n".join(filtered_lines).rstrip() + "\n"
    output_text = re.sub(r"\n{3,}", "\n\n", output_text)

    output_file = "BlockAdvertisers.lpx"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"\nSuccessfully updated {output_file}!")
    print(f"Total lines: {len(filtered_lines)}, Removed {removed_count} Google/Yandex rules.")

if __name__ == "__main__":
    main()
