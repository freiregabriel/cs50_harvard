$(document).ready(function() {
    M.toast({ html: 'Loading latest news....' });
    let collection_el = document.querySelector('.collection');
    let hacker_news_url = `${config.api}/api_hacker_news`;
    http.get(hacker_news_url).then((res) => {
        if (!res || !res.length) {
            handleError('No news were found');
            return;
        }
        M.toast({
            html: 'Done!'
        });
        for (let i = 0; i < res.length; i++) {
            _create_list_link(collection_el, res[i]);
        }
    }).catch(e => handleError(e))

    function _create_list_link(collection_element, data) {
        let a = document.createElement('a');
        a.href = data['url'];
        a.target = '_blank';
        a.className = 'collection-item';
        $(a).html(`
            <p><strong>${data['type']} (${data['score']})</strong></p><p>${data['title']} - ${data['time']} <small>by ${data['by']}</small></p>
        `)
        collection_element.appendChild(a);
    }
})