const httpClient = {
    get: function(url) {
        return new Promise((resolve, reject) => {
            try {
                const h = new XMLHttpRequest();
                h.onreadystatechange = () => {
                    if (h.status == 200 && h.readyState == 4) {
                        try {
                            resolve(JSON.parse(h.responseText));
                        } catch (e) {
                            resolve(h.responseText);
                        }
                    } else if (h.readyState == 4 && h.status !== 200) {
                        const error/*: { code: number, name: string, description: string } */ = JSON.parse(h.response); 
                        reject(`${error.code} ${error.name} - ${error.description}`);
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