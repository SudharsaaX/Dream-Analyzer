def cultural_context(tokens, user_context=None):
    culture_map = {
        # Chinese Culture (50 symbols)
        "sun": "happiness and success in Chinese culture",
        "moon": "happiness and success in Chinese culture",
        "stars": "happiness and success in Chinese culture",
        "clouds": "bright clouds symbolize happiness in Chinese culture",
        "mountains": "triumph when climbing in Chinese culture",
        "water": "clear water symbolizes wealth in Chinese culture",
        "trees": "beautiful trees symbolize blessings in Chinese culture",
        "dogs": "good signs in Chinese culture",
        "snakes": "lucky under certain conditions in Chinese culture",
        "spiders": "generally not good in Chinese culture",
        "horses": "auspicious in Chinese culture",
        "bears": "trouble in Chinese culture",
        "lions": "success in Chinese culture",
        "tigers": "pressure in Chinese culture",
        "eyes": "success if shining in Chinese culture",
        "teeth": "falling out is unfortunate in Chinese culture",
        "blood": "wealth in Chinese culture",
        "limbs": "auspicious if growing in Chinese culture",
        "pregnancy": "wealth and happy life in Chinese culture",
        "food": "good food is auspicious in Chinese culture",
        "deities": "blessing if worshipped in Chinese culture",
        "ghosts": "lucky in certain conditions in Chinese culture",
        "death": "longevity and wealth in Chinese culture",
        "killing": "wealth and blessing in Chinese culture",
        "reading": "auspicious in Chinese culture",
        "writing": "auspicious in Chinese culture",
        "exams": "auspicious in Chinese culture",
        "weddings": "auspicious in Chinese culture",
        "house": "building a new house is auspicious in Chinese culture",
        "traveling": "auspicious in Chinese culture",
        "crying": "auspicious in Chinese culture",
        "anger": "auspicious in Chinese culture",
        "music": "auspicious in Chinese culture",
        "firecrackers": "auspicious in Chinese culture",
        "harvesting": "auspicious in Chinese culture",
        "jewelry": "receiving jewelry is auspicious in Chinese culture",
        "wind": "lucky omen in Chinese culture",
        "cow": "sacred in Indian culture",
        "dragon": "power in Chinese culture",
        "snake": "evil or danger in Western, wisdom in Eastern cultures"
    }
    found = {}
    for token in tokens:
        if token in culture_map:
            found[token] = culture_map[token]
    if user_context:
        found['user_context'] = user_context
    return found