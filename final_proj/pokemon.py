import requests

ability_url = 'https://pokeapi.co/api/v2/ability'
poke_url = 'https://pokeapi.co/api/v2/pokemon'
def _fetch(entity_name=None):
    r = requests.get(f'{poke_url}/{entity_name}' if entity_name is not None else f'{url}')
    return r.json()

def _preprocess(pokemon_obj):
    pokemon_final = {}
    abilities = pokemon_obj['abilities']
    preprocessed_abilities = []
    for ability in abilities:
        print(ability)
        p_ab = {}
        a_data = _fetch(ability['ability']['url'])
        p_ab['name'] = ability['ability']['name']
        p_ab['effects'] = [a_data['effect_entries'][i]['effect'] for i in range(len(a_data['effect_entries']))]
        p_ab['generation'] = a_data['generation']['name']
        preprocessed_abilities.append(p_ab)
    pokemon_final['abilities'] = preprocessed_abilities
    pokemon_final['sprites'] = [pokemon_obj['sprites'][key] for key in pokemon_obj['sprites']]
    pokemon_final['types'] = [pokemon_obj['types'][i]['type']['name'] for i in range(len(pokemon_obj['types']))]
    pokemon_final['weight'] = pokemon_obj['weight']
    pokemon_final['name'] = pokemon_obj['name']
    pokemon_final['order'] = pokemon_obj['order']
    pokemon_final['id'] = pokemon_obj['id']
    return pokemon_final

def get_pokemon(pokemon_name):
    pokemon = _fetch(pokemon_name)
    pokemon = _preprocess(pokemon)
    return pokemon