#!/usr/bin/env python3
import os

# Create a .env file in the src directory
env_file_path = os.path.join('src', '.env')
with open(env_file_path, 'w') as env_file:
    # Ask the user for the port number
    port = input("Entrez le numéro de port: ")
    # Write the port number to the .env file
    env_file.write(f"PORT={port}\n")
    
print(f"Fichier .env créé avec succès dans le dossier 'src' avec le port {port}")
