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
