## ANY-IMG-DOWNLOADER

### A simple python script to download images from any website.

---

## How to use:

1.  Clone the repository

    ```bash
    git clone https://github.com/Tuhin-thinks/any-img-downloader.git
    ```

2.  Install the requirements

    ```bash
    pip install requests
    ```

3.  Copy paste and Run the [JS script](./imgLinksGetter.js) & Download the image_links.json file

    ```js
    // This script will get all the image links from the current page and download it as a json file.
    function downloadFile(blob_data) {
        var link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob_data);
        link.style.display = null;
        link.download = 'image_links.json';
        link.click();
        window.URL.revokeObjectURL(link.href);
        link.remove();
    }

    // play with the selector a lil bit.
    var css_selector = 'img[class*=tile--img]';
    imgSrcLinks = Array.from(document.querySelectorAll(css_selector)).map(
        (node) => node.src
    );
    blob = new Blob([JSON.stringify(imgSrcLinks, null, 2)], {
        type: 'application/json',
    });

    // function call to download all image links as a json file.
    downloadFile(blob);
    ```

4.  Run the [python script](./img_downloader.py)

    ```bash
    python img_downloader.py
    ```

After the above steps, you will have all the images downloaded in the `./images` folder.

---

## FAQ:

-   Q. How to download only relevant images from any site?

    Ans.: You have to change the CSS-Selector in the [JS script](./imgLinksGetter.js) to get the relevant images. Learn more about CSS-Selectors [here](https://www.w3schools.com/cssref/css_selectors.asp).

-   Q. How to download images from multiple pages?

    Ans.: Download from multiple pages at once isn't supported yet. But you can download images from multiple pages by running the [JS script](./imgLinksGetter.js) on each page and then running the [python script](./img_downloader.py) on the downloaded json files.

-   Q. I deleted all downloaded images, retrying download doesn't work?

    Ans.: The script checks if the image is already downloaded or not. If it is already downloaded, it skips the download. So, if you want to download the images again, you have to delete the images' links from the `config.json` file.
    \
    `"downloaded_images"` key in the `config.json` file contains all the downloaded images' links.

-   How is it different from any scrapper written in Python?

    Ans.: This script is written in Python and JavaScript. The JavaScript script is used to get all the image links from the current page and download it as a json file. The Python script is used to download the images from the json file. This script is useful when you want to download images from multiple pages at once. You can run the JavaScript script on each page and then run the Python script on the downloaded json files.

    The advantage of this script is that you can download images from any website without writing any code. You just have to change the CSS-Selector in the [JS script](./imgLinksGetter.js) to get the relevant images. (Scrappers generally need to be updated when the website changes its HTML structure. But the downloader script doesn't need to be updated.)

-   Q. How to download other files like pdf, doc, etc.?

    Ans.: Also you can download any files other than images by changing the CSS-Selector in the [JS script](./imgLinksGetter.js) and the file extension in the [python script](./img_downloader.py). As long as the file is downloadable from the browser, you can download it using this script.
