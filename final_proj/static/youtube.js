$(document).ready(function() {
    let youtube_download_btn = document.querySelector('#youtube_download_btn');
    let youtube_form = document.querySelector('#youtube_form');

    // // add events
    youtube_form.onsubmit = (e) => {
        M.toast({
            html: 'Success!'
        });
    }
    youtube_download_btn.onmousedown = (e) => {
        M.toast({
            html: 'Please wait...'
        });
    }
})