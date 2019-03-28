// below are some utility functions for HTML elements like h5, p, strong and divs
const Utils = {
    make_h5: function (text) {
        let h5 = document.createElement('h5');
        h5.textContent = text;
        return h5;
    },
    make_p: function (html, cls = 'text-left') {
        let p = document.createElement('p');
        p.className = cls + ' flow-text';
        p.style.margin = '10px';
        $(p).html(html);
        return p;
    },
    make_divider: function () {
        let div = document.createElement('div');
        div.className = 'divider';
        return div;
    },
    make_strong_string: function(text) {
        return `<strong>${text}</strong>`;
    },
    capitalize: function (str) {
        return str[0].toUpperCase() + str.slice(1);
    },
    removeChildren: function(element){
        while (element.firstChild) {
            element.removeChild(element.firstChild)
        }
    }
}