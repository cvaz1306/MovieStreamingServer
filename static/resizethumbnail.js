function resizeThumbnail() {
    const input = document.getElementById('id_thumbnail');
    const file = input.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const img = new Image();
        img.src = e.target.result;

        img.onload = function() {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            // Calculate the new width and height to resize the image
            const maxWidth = 200; // Set your desired maximum width
            const maxHeight = 200; // Set your desired maximum height
            let width = img.width;
            let height = img.height;

            if (width > height) {
                if (width > maxWidth) {
                    height *= maxWidth / width;
                    width = maxWidth;
                }
            } else {
                if (height > maxHeight) {
                    width *= maxHeight / height;
                    height = maxHeight;
                }
            }

            // Resize the image
            canvas.width = width;
            canvas.height = height;
            ctx.drawImage(img, 0, 0, width, height);

            // Convert the resized image to data URL
            const resizedDataURL = canvas.toDataURL('image/jpeg');

            // Replace the original input file with the resized image
            input.files[0] = dataURLtoFile(resizedDataURL, file.name);
        };
    };

    reader.readAsDataURL(file);
}

function dataURLtoFile(dataURL, filename) {
    const arr = dataURL.split(',');
    const mime = arr[0].match(/:(.*?);/)[1];
    const bstr = atob(arr[1]);
    let n = bstr.length;
    const u8arr = new Uint8Array(n);

    while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
    }

    return new File([u8arr], filename, { type: mime });
}