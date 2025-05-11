def interpret_psychology(tokens, user_context=None):
    themes = {
        "chased": "Avoiding a situation or fear of confrontation.",
        "attacked": "Feeling vulnerable or threatened.",
        "repeating": "Unresolved issues or persistent effort.",
        "frozen": "Fear or inability to act in a situation.",
        "eating": "Nourishment, indulgence, or emotional fulfillment.",
        "late": "Anxiety about missing opportunities or deadlines.",
        "swimming": "Navigating emotions or challenging situations.",
        "locked": "Feeling trapped or restricted in life.",
        "snakes": "Fear, transformation, or hidden threats.",
        "money": "Self-worth, financial concerns, or desire for security.",
        "flying": "Freedom, escape, or ambition.",
        "falling": "Loss of control, insecurity, or fear of failure.",
        "dressed": "Concerns about self-image or social perception.",
        "nude": "Vulnerability, honesty, or fear of exposure.",
        "tied": "Feeling restricted or helpless.",
        "knowledge": "Seeking wisdom or feeling intellectually empowered.",
        "creatures": "Facing the unknown or complex identities.",
        "teeth": "Anxiety about appearance or communication.",
        "mirror": "Self-reflection or identity concerns.",
        "magical": "Desire for control or escape from reality.",
        "floods": "Overwhelmed by emotions or situations.",
        "tornadoes": "Chaos or uncontrollable life events.",
        "earthquakes": "Instability or sudden life changes.",
        "insects": "Annoyance, small stressors, or fear.",
        "opposite": "Exploring different aspects of identity.",
        "object": "Feeling inanimate or disconnected from self.",
        "killed": "Fear of loss or significant change.",
        "dead": "Endings, transformation, or unresolved grief.",
        "presence": "Sensing the unknown or spiritual connection.",
        "toilet": "Embarrassment or need for privacy.",
        "school": "Feelings of inadequacy or performance anxiety.",
        "sexual": "Desire, intimacy, or personal connection.",
        "vehicle": "Lack of control over life’s direction.",
        "fire": "Anger, passion, or destruction.",
        "beasts": "Untamed emotions or powerlessness.",
        "movie": "Feeling like an observer in life.",
        "killing": "Suppressed anger or desire to eliminate issues.",
        "insane": "Fear of losing control or rationality."
    }
    found = {}
    for token in tokens:
        if token in themes:
            found[token] = themes[token]
    if user_context:
        found['user_context'] = user_context
    return found