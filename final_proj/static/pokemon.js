$(document).ready(function() {
    // store instances
    let pokemon_input = document.querySelector('#pokemon_input');
    let fetch_random_btn = document.querySelector('#pokemon_fetch_btn');
    let sprites_placeholder = document.querySelector('#sprites_placeholder');
    let name_sec = document.querySelector('#name_sec');
    let ability_sec = document.querySelector('#ability_sec');
    const pokemon_url = `${config.api}/pokemon`;

    // Handle fetch click
    fetch_random_btn.onclick = (e) => {
        // clear output element
        _clear();

        // validate input value
        let name = pokemon_input.value;
        if (!name) {
            // handle no pokemon name value
            handleError("No pokemon name");
            $(sprites_placeholder).html('<strong style="color:red;">No pokemon name</strong>')
            return;
        }
        // transform pokemon nameto lowercase
        name = name.toLowerCase();
        
        M.toast({ html: 'Loading...' });
        // make http request to the server
        http.get(`${pokemon_url}?name=${name}`).then((res) => {
            // validate request
            if (!res || res.error) {
                // handle invalid pokemon name error
                handleError(res.error || 'Invalid pokemon name');
                $(sprites_placeholder).html('<strong style="color:red;">Invalid pokemon name</strong>')
                return;
            }

            // notify user that all went fine
            M.toast({ html: 'Success!' })

            // create UI elements
            let sprites = res['sprites'];
            _create_sprites_elements(sprites);
            _create_name_sec(res, name_sec);
            _create_ability_sec(res, ability_sec);
            // catch unexpected errors
        }).catch(e => handleError(e))
    }

    // function to create sprites UI elements
    function _create_sprites_elements(sprites) {
        for (let i = 0; i < sprites.length; i++) {
            if (!sprites[i]) { continue; }
            _create_image(sprites[i]);
        }
    }

    // function to create and <img> HTML element with src attr
    function _create_image(src) {
        let div = document.createElement('div');
        div.className = 'col s3';
        let img = document.createElement('img');
        img.src = src;
        div.appendChild(img);
        sprites_placeholder.appendChild(div);
    }

    // below are functions to create different info and abilities section

    // information UI section
    function _create_name_sec(res, section) {
        let { name, id, order, weight } = res;
        section.appendChild(_make_h5(`${name}`));
        section.appendChild(_make_p(`${_make_strong_str('Id: ')}${id}`));
        section.appendChild(_make_p(`${_make_strong_str('Order: ')}${order}`));
        section.appendChild(_make_p(`${_make_strong_str('Weight: ')}${weight}`));

    }

    // abilities UI section
    function _create_ability_sec(res, section) {
        section.appendChild(_make_h5(`Abilities`));
        let abilities = res['abilities'];
        for (let i = 0; i < abilities.length; i++) {
            let { name, effects, generation } = abilities[i];
            section.appendChild(_make_p(`${_make_strong_str('Name: ')}${name}`));
            section.appendChild(_make_p(`${_make_strong_str('Effect: ')}${effects}`));
            section.appendChild(_make_p(`${_make_strong_str('Generation: ')}${generation}`));
            section.appendChild(_make_divider());
        }
    }

    // end UI sections functions

    // below are some utility functions for HTML elements like h5, p, strong and divs
    function _make_h5(text) {
        let h5 = document.createElement('h5');
        h5.textContent = text;
        return h5;
    }

    function _make_p(html, cls = 'text-left') {
        let p = document.createElement('p');
        p.className = cls + ' flow-text';
        p.style.margin = '10px';
        $(p).html(html);
        return p;
    }

    function _make_divider() {
        let div = document.createElement('div');
        div.className = 'divider';
        return div;
    }

    function _make_strong_str(text) {
        return `<strong>${text}</strong>`;
    }

    // clear output UI
    function _clear() {
        sprites_placeholder.innerHTML = "";
        name_sec.innerHTML = "";
        ability_sec.innerHTML = "";
    }

    // initialize materialize tabs
    $('.tabs').tabs();
})