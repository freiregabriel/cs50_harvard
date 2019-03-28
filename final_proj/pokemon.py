import requests
from typing import Any, Optional, List, Dict
from .exceptions import InvalidPokemonNameError, InvalidUsage

class Pokemon:
    """
        Pokemon class to make API request and preprocess results

    """
    def __init__(self):
        self.pokemon_api_url: str = 'https://pokeapi.co/api/v2/pokemon'

        self.abilities: Optional[ List[ dict ] ] = None
        self.sprites: Optional[List[str]] = None
        self.types: Optional[List[str]] = None
        self.weight: Optional[int] = None
        self.name: Optional[str] = None
        self.order: Optional[int] = None
        self.id: Optional[int] = None

        self.obj_to_parse = None

    def preprocess(self, pokemon_json: dict) -> dict:
        """
            Filter only the useful information of the object returned from @request_pokemon_or_url
        """
        abilities = pokemon_json['abilities']
        preprocessed_abilities = []
        for ability in abilities:
            print(ability)
            p_ab = {}
            a_data = self.request_pokemon_or_url(url=ability['ability']['url'])
            if a_data:
                p_ab['name'] = ability['ability']['name']
                p_ab['effects'] = [a_data['effect_entries'][i]['effect'] for i in range(len(a_data['effect_entries']))]
                p_ab['generation'] = a_data['generation']['name']
                preprocessed_abilities.append(p_ab)
                
        self.abilities = preprocessed_abilities
        self.sprites = [pokemon_json['sprites'][key] for key in pokemon_json['sprites']]
        self.types = [pokemon_json['types'][i]['type']['name'] for i in range(len(pokemon_json['types']))]
        self.weight = pokemon_json['weight']
        self.name = pokemon_json['name']
        self.order = pokemon_json['order']
        self.id = pokemon_json['id']
        return self.__dict__
 
    def request_pokemon_or_url(self, name: Optional[str]=None, url: Optional[str]=None) -> Optional[dict]:
        """
            Make request using pokemon name or api url
        """
        r = requests.get(f'{self.pokemon_api_url}/{name}' if name is not None else f'{url}')
        if r.status_code == 200:
            return r.json()
        return None

def get_pokemon(pokemon_name: Optional[str]) -> dict:
    pokemon: Pokemon = Pokemon()
    try:
        pokemon_json: Optional[dict] = pokemon.request_pokemon_or_url(name=pokemon_name)
        if not pokemon_json:
            raise InvalidUsage("There are no pokemons with this name", 404)

        return pokemon.preprocess(pokemon_json)
    except InvalidPokemonNameError as e:
        raise e