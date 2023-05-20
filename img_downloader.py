from functools import lru_cache
import re
import os
import json
import requests


# delete the downloaded_links key from config.json to download all images again
CONFIG_FILE = "config.json"  # to store already downloaded images (prevent duplicates)
INPUT_FILENAME = "image_links.json"


def decided_start_number():
    num = 1
    if os.path.exists('images'):
        files = os.listdir('images')
        if len(files) > 0:
            # extract numbers from image names of pattern image-\d.png
            numbers = [int(re.findall(r'\d+', file)[0]) for file in files]
            num = max(numbers) + 1
    print(f"starting from {num}")
    return num


@lru_cache(maxsize=1000)
def is_already_downloaded(img_link):
    return img_link in downloaded_links

def update_config(img_link, key: str):
    if key not in config:
        config[key] = []
    config[key].append(img_link)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as config_writer:
        json.dump(config, config_writer, indent=4)


if __name__ == '__main__':
    if not os.path.exists('images'):
        os.mkdir('images')

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as reader:
            config = json.load(reader)
    except FileNotFoundError:
        config = {}

    downloaded_links = config.get('downloaded_links', [])
    failed_links = config.get('failed_links', [])

    try:
        with open(INPUT_FILENAME, 'r', encoding='utf-8') as reader:
            all_links = json.load(reader)
    except FileNotFoundError:
        print(f"File {INPUT_FILENAME} not found, create a file with name {INPUT_FILENAME} and add all image links in it.")
        exit(1)

    start_number = decided_start_number()
    tot_length = len(all_links) + start_number - 1

    for index, link in enumerate(all_links, start_number):
        print(f"Downloading {index}/{tot_length}...")
        try:
            if is_already_downloaded(link):
                print(f"\tAlready downloaded {index}...")
                continue

            if link in failed_links:
                print(f"\tNot retrying to download, since downloading img {index} failed las time...")
                continue

            resp = requests.get(link, timeout=10)
            with open(f'images/img-{index}.png', 'wb') as writer:
                writer.write(resp.content)
            print(f"\tDownloaded {index}...")

            # to prevent duplicates
            downloaded_links.append(link)
            update_config(link, 'downloaded_links')
        except Exception as e:
            print(f"\tFailed to download {index}...")

            # to prevent retries
            update_config(link, 'failed_links')
            failed_links.append(link)
