def gate_experts(symbols, emotions, psychology, culture, user_context=None):
    results = {}
    if symbols:
        results['symbols'] = symbols
    if emotions:
        results['emotion'] = emotions
    if psychology:
        results['psychology'] = psychology
    if culture:
        results['culture'] = culture
    if user_context:
        results['user_context'] = user_context
    return results
