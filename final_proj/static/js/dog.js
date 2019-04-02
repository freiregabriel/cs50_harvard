$(document).ready(function() {

    const breeds = [
        "affenpinscher", "african", "airedale", "akita", "appenzeller", "basenji", "beagle", "bluetick", "borzoi", "bouvier", "boxer", "brabancon", "briard", "bulldog", "bullterrier", "cairn", "cattledog", "chihuahua", "chow", "clumber", "cockapoo", "collie", "coonhound", "corgi", "cotondetulear", "dachshund", "dalmatian", "dane", "deerhound", "dhole", "dingo", "doberman", "elkhound", "entlebucher", "eskimo", "frise", "germanshepherd", "greyhound", "groenendael", "hound", "husky", "keeshond", "kelpie", "komondor", "kuvasz", "labrador", "leonberg", "lhasa", "malamute", "malinois", "maltese", "mastiff", "mastiff", "mastiff", "mexicanhairless", "mix", "mountain", "mountain", "newfoundland", "otterhound", "papillon", "pekinese", "pembroke", "pinscher", "pointer", "pointer", "pomeranian", "poodle", "poodle", "poodle", "pug", "puggle", "pyrenees", "redbone", "retriever", "ridgeback", "rottweiler", "saluki", "samoyed", "schipperke", "schnauzer", "setter", "sheepdog", "shiba", "shihtzu", "spaniel", "springer", "stbernard", "terrier", "vizsla", "weimaraner", "whippet", "wolfhound"
    ];
    const fetch_random_btn = document.querySelector('#dog_fetch_btn');
    const placeholder = document.querySelector('#dog_img_placeholder');
    const random_dog_url = 'https://dog.ceo/api/breeds/image/random';
    const breed_dog_url = (breed) => `https://dog.ceo/api/breed/${breed}/images/random`;

    // add options to select
    let breed_selector = $('#breed_selector').get(0);
    add_select_options(breed_selector, breeds);

    // initialize selector for materialize css
    // P.S.: option elements must be added before this initialization
    $('#breed_selector').formSelect();

    // add events
    fetch_random_btn.onclick = (e) => {
        // fetch server for random dog image
        httpClient.get(random_dog_url).then((res) => {
            if (res.status && res.status == 'success') {
                placeholder.src = res.message;
            } else {
                handleError(res);
            }
            // handle unexpected errors
        }).catch(e => handleError(e))
    }

    breed_selector.onchange = (e) => {
        const breed = e.target.value;
        httpClient.get(breed_dog_url(breed)).then((res) => {
            if (res.status && res.status == 'success') {
                placeholder.src = res.message;
            } else {
                handleError(res);
            }
            // handle unexpected errors
        }).catch(e => handleError(e))
    }

    // add option elements to a given select html element
    function add_select_options(select, opt_arr) {
        let i;
        for (i = 0; i < opt_arr.length; i++) {
            const option = document.createElement('option');
            option.value = opt_arr[i];
            option.textContent = opt_arr[i];
            select.add(option);
        }
    }
})