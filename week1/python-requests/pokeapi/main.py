import requests

if __name__ == "__main__":

    # URI of the RESTFUL API Endpoint
    url = "https://pokeapi.co/api/v2/"
    pokemon = "pokemon/bulbasaur/"

    pokemon_uri = url + pokemon

    response = requests.get(
      pokemon_uri, # URI to connect to
      data={}, # Data to be passed to the PokeAPI
      headers={} # Headers to be passed to the PokeAPI
    )

    status_code = response.status_code # Return status of the REST API call
    body = response.json() # Returned content of the REST API call

    print("Status Code", status_code)
    print("Response", body)


    # These are the possbile keys for the endpoint
    # Try retrieving these keys by running the code below
    print("Keys", body.keys())
    # [
    #   'abilities', 
    #   'base_experience', 
    #   'forms', 
    #   'game_indices', 
    #   'height', 
    #   'held_items', 
    #   'id', 
    #   'is_default', 
    #   'location_area_encounters', 
    #   'moves', 
    #   'name', 
    #   'order', 
    #   'species', 
    #   'sprites', 
    #   'stats', 
    #   'types', 
    #   'weight'
    # ]

    # 
    # To get a specific key:
    # body.get("<Specific Key Here>")
    
    print("Abilities", body.get("abilities"))

