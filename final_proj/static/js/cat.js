$(document).ready(function() {
    const fetch_random_btn = document.querySelector('#cat_fetch_btn');
    const placeholder = document.querySelector('#cat_img_placeholder');
    const random_cat_url = 'https://aws.random.cat/meow';

    // add events
    fetch_random_btn.onclick = (e) => {
        httpClient.get(random_cat_url).then((res) => {
            if (res.file) {
                placeholder.src = res.file;
            } else {
                handleError(res);
            }
        }).catch(e => handleError(e))
    }
})