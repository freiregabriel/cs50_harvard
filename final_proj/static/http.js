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
                //XHR binary charset opt by Marcus Granado 2006 [http://mgran.blogspot.com]
                h.overrideMimeType('text\/plain; charset=x-user-defined');
                h.send();
            } catch (e) {
                reject(e);
            }
        })
    }
}