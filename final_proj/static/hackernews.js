$(document).ready(function() {
    M.toast({ html: 'Loading latest news....' });
    const collection_el = document.querySelector('.collection');
    const hacker_news_url = `${config.api}/api_hacker_news`;
    httpClient.get(hacker_news_url).then((res) => {
        if (!res || !res.length) {
            handleError('No news were found');
            return;
        }
        M.toast({
            html: 'Done!'
        });
        let i;
        for (i = 0; i < res.length; i++) {
            _create_list_link(collection_el, res[i]);
        }
    }).catch(e => handleError(e));

    function _create_list_link(collection_element, data) {
        const a = document.createElement('a');
        a.href = data['url'];
        a.target = '_blank';
        a.className = 'collection-item';
        $(a).html(`
            <h5>
                ${Utils.capitalize(data['type'])} <small>Score:${data['score']}</small>
            </h5>
            <p>${data['title']} - ${data['time']} 
                <br>
                <small>by ${data['by']}</small>
            </p>
        `);
        collection_element.appendChild(a);
    }

})