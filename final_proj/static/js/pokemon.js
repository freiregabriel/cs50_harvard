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

        // clear output
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
        httpClient.get(`${pokemon_url}?name=${name}`).then((res) => {
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
        section.appendChild(Utils.make_h5(`${name}`));
        section.appendChild(Utils.make_p(`${Utils.make_strong_string('Id: ')}${id}`));
        section.appendChild(Utils.make_p(`${Utils.make_strong_string('Order: ')}${order}`));
        section.appendChild(Utils.make_p(`${Utils.make_strong_string('Weight: ')}${weight}`));

    }

    // abilities UI section
    function _create_ability_sec(res, section) {
        section.appendChild(Utils.make_h5(`Abilities`));
        let abilities = res['abilities'];
        for (let i = 0; i < abilities.length; i++) {
            let { name, effects, generation } = abilities[i];
            section.appendChild(Utils.make_p(`${Utils.make_strong_string('Name: ')}${name}`));
            section.appendChild(Utils.make_p(`${Utils.make_strong_string('Effect: ')}${effects}`));
            section.appendChild(Utils.make_p(`${Utils.make_strong_string('Generation: ')}${generation}`));
            section.appendChild(Utils.make_divider());
        }
    }

    // end UI sections functions

    // clear output UI
    function _clear() {
        Utils.removeChildren(sprites_placeholder);
        Utils.removeChildren(name_sec);
        Utils.removeChildren(ability_sec);
    }

    // initialize materialize tabs
    $('.tabs').tabs();
})