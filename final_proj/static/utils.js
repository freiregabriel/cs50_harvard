const download = (binary) => {
    // It is necessary to create a new blob object with mime-type explicitly set
    // otherwise only Chrome works like it should
    // decode base64 string, remove space for IE compatibility
    //   var binary = atob(blob.replace(/\s/g, ''));
    // var len = binary.length;
    // var buffer = new ArrayBuffer(len);
    // var view = new Uint8Array(buffer);
    // for (var i = 0; i < len; i++) {
    //     view[i] = binary.charCodeAt(i);
    // }

    // create the blob object with content-type "application/pdf"
    var mimeType = 'application/octet-stream';
    var newBlob = new Blob([binary], { type: mimeType });
    // IE doesn't allow using a blob object directly as link href
    // instead it is necessary to use msSaveOrOpenBlob
    if (window.navigator && window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(newBlob);
        return;
    }

    // For other browsers: 
    // Create a link pointing to the ObjectURL containing the blob.
    const data = window.URL.createObjectURL(newBlob);
    var link = document.createElement('a');
    link.href = data;
    link.download = 'youtube-video.mp4';
    link.click();
    setTimeout(function() {
        // For Firefox it is necessary to delay revoking the ObjectURL
        window.URL.revokeObjectURL(data);
    }, 100);
}