from flask import Flask, jsonify, request
import random
import json
import os

app = Flask(__name__)

# Cargar wallpapers desde JSON
def load_wallpapers():
    with open('wallpapers.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Rutas de la API
@app.route('/api/wallpapers', methods=['GET'])
def get_wallpapers():
    data = load_wallpapers()

    # Filtrar por categoría si se especifica
    category = request.args.get('category')
    if category:
        wallpapers = [w for w in data['wallpapers'] if w['category'].lower() == category.lower()]
    else:
        wallpapers = data['wallpapers']

    return jsonify({
        "count": len(wallpapers),
        "wallpapers": wallpapers
    })

@app.route('/api/wallpapers/random', methods=['GET'])
def get_random_wallpaper():
    data = load_wallpapers()

    category = request.args.get('category')
    if category:
        wallpapers = [w for w in data['wallpapers'] if w['category'].lower() == category.lower()]
    else:
        wallpapers = data['wallpapers']

    if not wallpapers:
        return jsonify({"error": "No se encontraron wallpapers"}), 404

    random_wallpaper = random.choice(wallpapers)
    return jsonify(random_wallpaper)

@app.route('/api/categories', methods=['GET'])
def get_categories():
    data = load_wallpapers()
    return jsonify({
        "categories": data['categories']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
