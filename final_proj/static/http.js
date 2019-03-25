window['http'] = {
    get: function(url) {
        return new Promise((resolve, reject) => {
            try {
                let h = new XMLHttpRequest();
                h.onreadystatechange = () => {
                    if (h.status == 200 && h.readyState == 4) {
                        try {
                            resolve(JSON.parse(h.responseText));
                        } catch (e) {
                            resolve(h.responseText);
                        }
                    }
                }
                h.open('GET', url);
                h.send();
            } catch (e) {
                reject(e);
            }
        })
    }
}