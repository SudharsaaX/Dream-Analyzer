def get_book_recommendations(interpretation):
    """
    Generate book recommendations based on dream interpretation.
    
    Args:
        interpretation (dict): The dream interpretation results from expert models
        
    Returns:
        list: A list of recommended books with titles, authors, and descriptions
    """
    recommendations = []
    # Limit to only 3 recommendations based on dream interpretation
    
    # Store the dream text if available
    dream_text = ""
    if 'dream_text' in interpretation:
        dream_text = str(interpretation['dream_text']).lower()
    
    # Check for symbols in the interpretation
    if 'symbols' in interpretation:
        symbols = interpretation['symbols']
        # Convert to string representation for keyword matching if needed
        symbols_str = str(symbols)
        
        # Identity or self-discovery themes
        if any(keyword in symbols_str.lower() for keyword in ['identity', 'self', 'personal', 'mirror', 'mask', 'hair']):  
            recommendations.append({
                'title': 'Man and His Symbols',
                'author': 'Carl Jung',
                'description': 'Explores the world of dreams and their symbols, offering insights into the unconscious mind.'
            })
            recommendations.append({
                'title': 'The Power of Now',
                'author': 'Eckhart Tolle',
                'description': 'A spiritual guide to living in the present moment and understanding the self.'
            })
            recommendations.append({
                'title': 'The Archetypes and the Collective Unconscious',
                'author': 'Carl Jung',
                'description': 'Delves into Jungian archetypes and their role in shaping the unconscious mind.'
            })
            recommendations.append({
                'title': 'The Divided Self',
                'author': 'R.D. Laing',
                'description': 'Explores the concept of self and identity in psychological and existential contexts.'
            })
            recommendations.append({
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'description': 'A story of self-discovery and following one’s personal legend, inspired by dreams.'
            })
            
        # Transformation or change themes
        if any(keyword in symbols_str.lower() for keyword in ['transform', 'change', 'journey', 'path', 'rebirth', 'room', 'stagnation', 'potential']):  
            recommendations.append({
                'title': 'The Hero with a Thousand Faces',
                'author': 'Joseph Campbell',
                'description': 'Examines the journey of the archetypal hero in world mythologies.'
            })
            recommendations.append({
                'title': 'Transitions: Making Sense of Life’s Changes',
                'author': 'William Bridges',
                'description': 'A guide to navigating life’s transitions and transformations.'
            })
            recommendations.append({
                'title': 'Women Who Run with the Wolves',
                'author': 'Clarissa Pinkola Estés',
                'description': 'Explores myths and stories to reconnect with the transformative feminine psyche.'
            })
            recommendations.append({
                'title': 'The Four Agreements',
                'author': 'Don Miguel Ruiz',
                'description': 'Offers a practical guide to personal transformation through Toltec wisdom.'
            })
            recommendations.append({
                'title': 'Becoming',
                'author': 'Michelle Obama',
                'description': 'A memoir exploring personal growth and transformation through life’s challenges.'
            })
            
        # Fear or anxiety themes
        if any(keyword in symbols_str.lower() for keyword in ['fear', 'anxiety', 'threat', 'chase', 'darkness']):  
            recommendations.append({
                'title': 'The Interpretation of Dreams',
                'author': 'Sigmund Freud',
                'description': 'The foundational work on dream analysis and the unconscious mind.'
            })
            recommendations.append({
                'title': 'The Gift of Fear',
                'author': 'Gavin de Becker',
                'description': 'Explores how fear can be a protective instinct and how to understand it.'
            })
            recommendations.append({
                'title': 'Daring Greatly',
                'author': 'Brené Brown',
                'description': 'Discusses vulnerability and how to embrace fear to live courageously.'
            })
            recommendations.append({
                'title': 'Feel the Fear and Do It Anyway',
                'author': 'Susan Jeffers',
                'description': 'A practical guide to overcoming fear and anxiety in everyday life.'
            })
            recommendations.append({
                'title': 'Anxiety: The Missing Stage of Grief',
                'author': 'Claire Bidwell Smith',
                'description': 'Links anxiety to unresolved grief and offers tools for healing.'
            })
            
        # Spiritual or mystical themes
        if any(keyword in symbols_str.lower() for keyword in ['spirit', 'mystic', 'divine', 'vision', 'light']):  
            recommendations.append({
                'title': 'The Seat of the Soul',
                'author': 'Gary Zukav',
                'description': 'Explores spiritual growth and the soul’s role in our lives.'
            })
            recommendations.append({
                'title': 'A Field Guide to Lucid Dreaming',
                'author': 'Dylan Tuccillo, Jared Zeizel, and Thomas Peisel',
                'description': 'A practical guide to mastering lucid dreaming and exploring the subconscious.'
            })
            recommendations.append({
                'title': 'The Tibetan Book of Living and Dying',
                'author': 'Sogyal Rinpoche',
                'description': 'Offers insights into spiritual dimensions of life, death, and dreams.'
            })
            recommendations.append({
                'title': 'Exploring the World of Lucid Dreaming',
                'author': 'Stephen LaBerge and Howard Rheingold',
                'description': 'A scientific and practical exploration of lucid dreaming techniques.'
            })
            recommendations.append({
                'title': 'The Celestine Prophecy',
                'author': 'James Redfield',
                'description': 'A spiritual adventure novel exploring synchronicity and mystical insights.'
            })
    
    # Check for emotional content
    if 'emotion' in interpretation:
        emotion = interpretation['emotion']
        # Convert to string representation for keyword matching if needed
        emotion_str = str(emotion)
        
        # Joy or happiness
        if any(keyword in emotion_str.lower() for keyword in ['joy', 'happy', 'excitement', 'love', 'peace', 'positive']):  
            recommendations.append({
                'title': 'Flow: The Psychology of Optimal Experience',
                'author': 'Mihaly Csikszentmihalyi',
                'description': 'Explores the state of flow and how it relates to happiness and fulfillment.'
            })
            recommendations.append({
                'title': 'The Book of Joy',
                'author': 'Dalai Lama and Desmond Tutu',
                'description': 'Conversations on finding lasting happiness in a changing world.'
            })
            recommendations.append({
                'title': 'Happiness: A Guide to Developing Life’s Most Important Skill',
                'author': 'Matthieu Ricard',
                'description': 'A Buddhist monk’s perspective on cultivating happiness.'
            })
            recommendations.append({
                'title': 'The Art of Happiness',
                'author': 'Dalai Lama and Howard Cutler',
                'description': 'Combines Buddhist principles with psychology to foster happiness.'
            })
            recommendations.append({
                'title': 'Big Magic',
                'author': 'Elizabeth Gilbert',
                'description': 'Explores creativity and living a joyful, inspired life.'
            })
            
        # Sadness or grief
        if any(keyword in emotion_str.lower() for keyword in ['sad', 'grief', 'loss', 'sorrow', 'mourning']):  
            recommendations.append({
                'title': 'When Things Fall Apart',
                'author': 'Pema Chödrön',
                'description': 'A guide to moving through difficult times with mindfulness and compassion.'
            })
            recommendations.append({
                'title': 'The Year of Magical Thinking',
                'author': 'Joan Didion',
                'description': 'A memoir exploring grief and loss after a sudden tragedy.'
            })
            recommendations.append({
                'title': 'Bearing the Unbearable',
                'author': 'Joanne Cacciatore',
                'description': 'A compassionate guide to navigating grief and trauma.'
            })
            recommendations.append({
                'title': 'On Grief and Grieving',
                'author': 'Elisabeth Kübler-Ross and David Kessler',
                'description': 'Explores the stages of grief and how to cope with loss.'
            })
            recommendations.append({
                'title': 'The Wild Edge of Sorrow',
                'author': 'Francis Weller',
                'description': 'Explores grief as a transformative process connected to the human experience.'
            })
    
    # Check for psychological themes
    if 'psychology' in interpretation:
        psychology = interpretation['psychology']
        # Convert to string representation for keyword matching if needed
        psychology_str = str(psychology)
        
        # Relationships
        if any(keyword in psychology_str.lower() for keyword in ['relationship', 'connect', 'attachment', 'love', 'bond']):  
            recommendations.append({
                'title': 'Attached',
                'author': 'Amir Levine and Rachel Heller',
                'description': 'Explores attachment theory and how it affects our relationships.'
            })
            recommendations.append({
                'title': 'The Seven Principles for Making Marriage Work',
                'author': 'John Gottman and Nan Silver',
                'description': 'A research-based guide to strengthening relationships.'
            })
            recommendations.append({
                'title': 'Hold Me Tight',
                'author': 'Sue Johnson',
                'description': 'Focuses on emotionally focused therapy for building stronger bonds.'
            })
            recommendations.append({
                'title': 'Love Sense',
                'author': 'Sue Johnson',
                'description': 'Explores the science of love and attachment in relationships.'
            })
            recommendations.append({
                'title': 'The 5 Love Languages',
                'author': 'Gary Chapman',
                'description': 'Identifies five ways people express and receive love in relationships.'
            })
            
        # Personal growth
        if any(keyword in psychology_str.lower() for keyword in ['growth', 'develop', 'potential', 'self-improvement', 'success']):  
            recommendations.append({
                'title': 'Mindset: The New Psychology of Success',
                'author': 'Carol S. Dweck',
                'description': 'Examines how our mindset affects our ability to grow and develop.'
            })
            recommendations.append({
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'description': 'A guide to building good habits and breaking bad ones for personal growth.'
            })
            recommendations.append({
                'title': 'The Power of Habit',
                'author': 'Charles Duhigg',
                'description': 'Explores the science of habits and how they shape personal development.'
            })
            recommendations.append({
                'title': 'Grit: The Power of Passion and Perseverance',
                'author': 'Angela Duckworth',
                'description': 'Discusses the role of perseverance in achieving personal goals.'
            })
            recommendations.append({
                'title': 'The Untethered Soul',
                'author': 'Michael A. Singer',
                'description': 'A guide to spiritual and personal growth through mindfulness.'
            })
    
    # Check for dream-specific themes
    if 'dream_content' in interpretation:
        dream_content = interpretation['dream_content']
        # Convert to string representation for keyword matching if needed
        dream_content_str = str(dream_content)
    # Also check culture section for additional context
    elif 'culture' in interpretation:
        dream_content = interpretation['culture']
        dream_content_str = str(dream_content)
        
        # Lucid dreaming
        if any(keyword in dream_content_str.lower() for keyword in ['lucid', 'control', 'awareness', 'conscious']):  
            recommendations.append({
                'title': 'Lucid Dreaming: Gateway to the Inner Self',
                'author': 'Robert Waggoner',
                'description': 'Explores lucid dreaming as a tool for self-discovery and creativity.'
            })
            recommendations.append({
                'title': 'Dreaming Yourself Awake',
                'author': 'B. Alan Wallace',
                'description': 'Combines lucid dreaming with meditative practices for inner growth.'
            })
            recommendations.append({
                'title': 'A Field Guide to Lucid Dreaming',
                'author': 'Dylan Tuccillo, Jared Zeizel, and Thomas Peisel',
                'description': 'A practical guide to mastering lucid dreaming and exploring the subconscious.'
            })
            recommendations.append({
                'title': 'Exploring the World of Lucid Dreaming',
                'author': 'Stephen LaBerge and Howard Rheingold',
                'description': 'A scientific and practical exploration of lucid dreaming techniques.'
            })
            recommendations.append({
                'title': 'The Tibetan Yogas of Dream and Sleep',
                'author': 'Tenzin Wangyal Rinpoche',
                'description': 'Explores dream yoga practices for spiritual awakening.'
            })
            
        # Nightmares
        if any(keyword in dream_content_str.lower() for keyword in ['nightmare', 'fearful', 'disturbing', 'terrify']):  
            recommendations.append({
                'title': 'The Nightmare Solution',
                'author': 'Ann Sayre Wiseman',
                'description': 'Offers practical techniques for overcoming nightmares and improving sleep.'
            })
            recommendations.append({
                'title': 'Trauma and Dreams',
                'author': 'Deirdre Barrett',
                'description': 'Explores how trauma influences dreams and how to work through nightmares.'
            })
            recommendations.append({
                'title': 'Dreams of Awakening',
                'author': 'Charlie Morley',
                'description': 'Focuses on using lucid dreaming to address nightmares and fears.'
            })
            recommendations.append({
                'title': 'The Dream Interpretation Handbook',
                'author': 'Karen Frazier',
                'description': 'A practical guide to understanding and interpreting nightmares and dreams.'
            })
            recommendations.append({
                'title': 'Overcoming Nightmares',
                'author': 'J.A. Hadfield',
                'description': 'Classic work on understanding and resolving recurring nightmares.'
            })
    
    # If no specific recommendations were found, provide general recommendations
    if not recommendations:
        recommendations = [
            {
                'title': 'The Mind Illuminated',
                'author': 'John Yates',
                'description': 'A comprehensive guide to meditation that can help with dream recall and lucid dreaming.'
            },
            {
                'title': 'Why We Sleep',
                'author': 'Matthew Walker',
                'description': 'Explores the science of sleep and dreams, and their importance for mental health.'
            },
            {
                'title': 'Dreams: A Study of the Dreams of Jung, Descartes, Socrates, and Other Historical Figures',
                'author': 'Marie-Louise von Franz',
                'description': 'Analyzes the dreams of historical figures through a Jungian lens.'
            },
            {
                'title': 'Inner Work: Using Dreams and Active Imagination for Personal Growth',
                'author': 'Robert A. Johnson',
                'description': 'Guides readers through using dreams for psychological and spiritual growth.'
            },
            {
                'title': 'The Dream Dictionary',
                'author': 'Tony Crisp',
                'description': 'A comprehensive resource for interpreting dream symbols and meanings.'
            }
        ]
    
    # Extract dream text if available in the interpretation
    dream_text = ""
    if 'dream_text' in interpretation:
        dream_text = str(interpretation['dream_text']).lower()
    
    # Prioritize recommendations based on themes in the dream interpretation and dream text
    identity_recs = [rec for rec in recommendations if any(keyword in rec['description'].lower() 
                                                for keyword in ['identity', 'self', 'personal'])]
    potential_recs = [rec for rec in recommendations if any(keyword in rec['description'].lower() 
                                                 for keyword in ['potential', 'growth', 'stagnation'])]
    positive_recs = [rec for rec in recommendations if any(keyword in rec['description'].lower() 
                                                for keyword in ['positive', 'happiness', 'joy'])]
    
    # Add dream-specific theme matching
    dream_specific_recs = []
    
    # Common dream themes and corresponding podcast keywords
    dream_themes = {
        'falling': ['fear', 'anxiety', 'control'],
        'flying': ['freedom', 'spirituality', 'transcendence'],
        'chase': ['anxiety', 'stress', 'fear'],
        'teeth': ['anxiety', 'appearance', 'communication'],
        'naked': ['vulnerability', 'exposure', 'shame'],
        'test': ['anxiety', 'preparation', 'performance'],
        'late': ['stress', 'time management', 'anxiety'],
        'death': ['transformation', 'fear', 'spirituality'],
        'water': ['emotion', 'unconscious', 'spirituality'],
        'house': ['self', 'identity', 'security']
    }
    
    # Check if any dream themes are present in the dream text or interpretation
    for theme, keywords in dream_themes.items():
        # Check if theme is in dream text or any part of the interpretation
        if (dream_text and theme in dream_text) or \
           any(theme in str(value).lower() for value in interpretation.values()):
            # Find podcasts that match the theme's keywords
            for keyword in keywords:
                matching_recs = [rec for rec in recommendations 
                                if keyword in rec['description'].lower()]
                dream_specific_recs.extend(matching_recs)
    
    # Combine and prioritize the recommendations with dream-specific ones first
    # Ensure podcasts are grouped and prioritized by unique dream themes
    prioritized_recs = []
    seen_titles = set()
    # Add dream-specific recommendations by theme, ensuring diversity
    for theme, keywords in dream_themes.items():
        if (dream_text and theme in dream_text) or any(theme in str(value).lower() for value in interpretation.values()):
            for keyword in keywords:
                for rec in recommendations:
                    if keyword in rec['description'].lower() and rec['title'] not in seen_titles:
                        prioritized_recs.append(rec)
                        seen_titles.add(rec['title'])
    # Add identity, potential, and positive recommendations if not already included
    for rec in identity_recs + potential_recs + positive_recs:
        if rec['title'] not in seen_titles:
            prioritized_recs.append(rec)
            seen_titles.add(rec['title'])
    # Add remaining recommendations to fill up to 3 unique ones
    for rec in recommendations:
        if rec['title'] not in seen_titles:
            prioritized_recs.append(rec)
            seen_titles.add(rec['title'])
    # Return only 3 unique recommendations
    unique_recs = prioritized_recs[:3]
    # Add dream relevance information to each recommendation
    for rec in unique_recs:
        related_themes = []
        for theme, keywords in dream_themes.items():
            if any(keyword in rec['description'].lower() for keyword in keywords):
                related_themes.append(theme)
        if related_themes:
            rec['dream_relevance'] = f"This podcast relates to {', '.join(related_themes)} in your dream."
        else:
            rec['dream_relevance'] = "This podcast addresses themes present in your dream interpretation."
    return unique_recs


def get_podcast_recommendations(interpretation):
    """
    Generate podcast recommendations based on dream interpretation.
    
    Args:
        interpretation (dict): The dream interpretation results from expert models
        
    Returns:
        list: A list of recommended podcasts with titles, hosts, and descriptions
    """
    recommendations = []
    
    # Check for symbols in the interpretation
    if 'symbols' in interpretation:
        symbols = interpretation['symbols']
        # Convert to string representation for keyword matching if needed
        symbols_str = str(symbols)
        
        # Mythological or archetypal themes
        if any(keyword in symbols_str.lower() for keyword in ['myth', 'archetype', 'hero', 'legend', 'epic']):  
            recommendations.append({
                'title': 'Myths and Legends',
                'host': 'Jason Weiser',
                'description': 'Explores stories from mythology and folklore from around the world.'
            })
            recommendations.append({
                'title': 'The Hero’s Journey',
                'host': 'Kevin deLaplante',
                'description': 'Explores Joseph Campbell’s concept of the hero’s journey in storytelling.'
            })
            recommendations.append({
                'title': 'Mythos',
                'host': 'Stephen Fry',
                'description': 'A retelling of Greek myths with a modern, engaging perspective.'
            })
            recommendations.append({
                'title': 'Lore',
                'host': 'Aaron Mahnke',
                'description': 'Explores dark historical tales and their mythological connections.'
            })
            recommendations.append({
                'title': 'The Mythic Journey',
                'host': 'Dr. Michael Meade',
                'description': 'Explores myths and their relevance to modern life and personal growth.'
            })
            
        # Spiritual or mystical themes
        if any(keyword in symbols_str.lower() for keyword in ['spirit', 'mystic', 'divine', 'vision', 'light']):  
            recommendations.append({
                'title': 'On Being with Krista Tippett',
                'host': 'Krista Tippett',
                'description': 'Conversations about the big questions of meaning in our modern world.'
            })
            recommendations.append({
                'title': 'The RobCast',
                'host': 'Rob Bell',
                'description': 'Explores spirituality, faith, and the mysteries of life.'
            })
            recommendations.append({
                'title': 'Tara Brach',
                'host': 'Tara Brach',
                'description': 'Offers meditations and talks on mindfulness and spiritual awakening.'
            })
            recommendations.append({
                'title': 'The Astrology Podcast',
                'host': 'Chris Brennan',
                'description': 'Explores astrology and its connections to dreams and the subconscious.'
            })
            recommendations.append({
                'title': 'The Emerald',
                'host': 'Josh Schrei',
                'description': 'Explores mythology, spirituality, and human connection to nature.'
            })
    
    # Check for emotional content
    if 'emotion' in interpretation:
        emotion = interpretation['emotion']
        # Convert to string representation for keyword matching if needed
        emotion_str = str(emotion)
        
        # Anxiety or stress
        if any(keyword in emotion_str.lower() for keyword in ['anxiety', 'stress', 'worry', 'panic', 'tension']):  
            recommendations.append({
                'title': 'The Anxiety Coaches Podcast',
                'host': 'Gina Ryan',
                'description': 'Offers guidance and support for managing anxiety and stress.'
            })
            recommendations.append({
                'title': 'The Calming Anxiety Podcast',
                'host': 'Martin Hewlett',
                'description': 'Provides tools and meditations for reducing anxiety and stress.'
            })
            recommendations.append({
                'title': 'Anxiety Slayer',
                'host': 'Shann Vander Leek and Ananga Sivyer',
                'description': 'Offers practical advice for managing anxiety and finding peace.'
            })
            recommendations.append({
                'title': 'The Overwhelmed Brain',
                'host': 'Paul Colaianni',
                'description': 'Explores emotional management and overcoming stress.'
            })
            recommendations.append({
                'title': 'Feel Better, Live More',
                'host': 'Dr. Rangan Chatterjee',
                'description': 'Discusses holistic approaches to managing stress and improving well-being.'
            })
            
        # Curiosity or wonder
        if any(keyword in emotion_str.lower() for keyword in ['curious', 'wonder', 'interest', 'intrigue', 'fascination']):  
            recommendations.append({
                'title': 'Radiolab',
                'host': 'Jad Abumrad and Robert Krulwich',
                'description': 'Explores scientific and philosophical topics with a sense of wonder.'
            })
            recommendations.append({
                'title': 'Stuff You Should Know',
                'host': 'Josh Clark and Chuck Bryant',
                'description': 'Explores a wide range of topics with curiosity and humor.'
            })
            recommendations.append({
                'title': 'The Curious Cases of Rutherford & Fry',
                'host': 'Hannah Fry and Adam Rutherford',
                'description': 'Investigates scientific mysteries with a sense of curiosity.'
            })
            recommendations.append({
                'title': 'Invisibilia',
                'host': 'Various Hosts',
                'description': 'Explores the invisible forces that shape human behavior and thought.'
            })
            recommendations.append({
                'title': '99% Invisible',
                'host': 'Roman Mars',
                'description': 'Explores the unnoticed architecture and design of everyday life.'
            })
    
    # Check for psychological themes
    if 'psychology' in interpretation:
        psychology = interpretation['psychology']
        # Convert to string representation for keyword matching if needed
        psychology_str = str(psychology)
        
        # Self-improvement
        if any(keyword in psychology_str.lower() for keyword in ['improve', 'growth', 'develop', 'self-improvement', 'success']):  
            recommendations.append({
                'title': 'The Psychology Podcast',
                'host': 'Scott Barry Kaufman',
                'description': 'Interviews with experts on topics related to psychology and personal growth.'
            })
            recommendations.append({
                'title': 'The Happiness Lab',
                'host': 'Dr. Laurie Santos',
                'description': 'Explores the science of happiness and personal growth.'
            })
            recommendations.append({
                'title': 'How to Fail',
                'host': 'Elizabeth Day',
                'description': 'Explores how failure can lead to personal growth and success.'
            })
            recommendations.append({
                'title': 'The Tim Ferriss Show',
                'host': 'Tim Ferriss',
                'description': 'Interviews with high performers on habits and strategies for success.'
            })
            recommendations.append({
                'title': 'On Purpose with Jay Shetty',
                'host': 'Jay Shetty',
                'description': 'Focuses on mindfulness, purpose, and personal development.'
            })
            
        # Relationships
        if any(keyword in psychology_str.lower() for keyword in ['relationship', 'connect', 'social', 'love', 'bond']):  
            recommendations.append({
                'title': 'Where Should We Begin?',
                'host': 'Esther Perel',
                'description': 'Real couples anonymously share their stories and work through relationship challenges.'
            })
            recommendations.append({
                'title': 'The Love, Happiness and Success Podcast',
                'host': 'Dr. Lisa Marie Bobby',
                'description': 'Explores relationships, personal growth, and emotional well-being.'
            })
            recommendations.append({
                'title': 'Relationships Uncomplicated',
                'host': 'Idit Sharoni',
                'description': 'Offers practical advice for improving relationships.'
            })
            recommendations.append({
                'title': 'Modern Love',
                'host': 'Various Hosts',
                'description': 'Explores real-life love stories and relationship dynamics.'
            })
            recommendations.append({
                'title': 'Dear Sugars',
                'host': 'Cheryl Strayed and Steve Almond',
                'description': 'Offers advice on love, relationships, and life challenges.'
            })
    
    # Check for dream-specific themes
    if 'dream_content' in interpretation:
        dream_content = interpretation['dream_content']
        # Convert to string representation for keyword matching if needed
        dream_content_str = str(dream_content)
    # Also check culture section for additional context
    elif 'culture' in interpretation:
        dream_content = interpretation['culture']
        dream_content_str = str(dream_content)
        
        # Lucid dreaming
        if any(keyword in dream_content_str.lower() for keyword in ['lucid', 'control', 'awareness', 'conscious']):  
            recommendations.append({
                'title': 'The Lucid Dreaming Podcast',
                'host': 'Various Hosts',
                'description': 'Explores techniques and experiences of lucid dreaming.'
            })
            recommendations.append({
                'title': 'Huberman Lab',
                'host': 'Dr. Andrew Huberman',
                'description': 'Discusses the science of dreams, lucid dreaming, and nightmares.'
            })
            recommendations.append({
                'title': 'The Dream Journal',
                'host': 'Katherine Bell',
                'description': 'Explores dreams and lucid dreaming from a psychological perspective.'
            })
            recommendations.append({
                'title': 'The Lucid Sage Podcast',
                'host': 'Various Hosts',
                'description': 'Focuses on lucid dreaming and spiritual exploration through dreams.'
            })
            recommendations.append({
                'title': 'Dreams and Nightmares',
                'host': 'Dr. Angel Morgan',
                'description': 'Explores the science and spirituality of dreams, including lucid dreaming.'
            })
            
        # Nightmares
        if any(keyword in dream_content_str.lower() for keyword in ['nightmare', 'fearful', 'disturbing', 'terrify']):  
            recommendations.append({
                'title': 'The Nightmare Podcast',
                'host': 'Various Hosts',
                'description': 'Explores nightmares and their psychological significance.'
            })
            recommendations.append({
                'title': 'Sleep and Dreams',
                'host': 'Dr. Kelly Bulkeley',
                'description': 'Discusses the science and psychology of dreams, including nightmares.'
            })
            recommendations.append({
                'title': 'The Dream Show',
                'host': 'Jane Teresa Anderson',
                'description': 'Explores dream interpretation, including nightmares, with practical advice.'
            })
            recommendations.append({
                'title': 'The Dream Podcast',
                'host': 'Various Hosts',
                'description': 'Explores dreams, nightmares, and their meanings in various contexts.'
            })
            recommendations.append({
                'title': 'The Sleep and Dream Database Podcast',
                'host': 'Dr. Kelly Bulkeley',
                'description': 'Analyzes dreams and nightmares using data-driven approaches.'
            })
    
    # If no specific recommendations were found, provide general recommendations
    if not recommendations:
        recommendations = [
            {
                'title': 'Sleep With Me',
                'host': 'Drew Ackerman',
                'description': 'A bedtime story podcast designed to help people fall asleep.'
            },
            {
                'title': 'Hidden Brain',
                'host': 'Shankar Vedantam',
                'description': 'Explores the unconscious patterns that drive human behavior.'
            },
            {
                'title': 'The Science of Happiness',
                'host': 'Dacher Keltner',
                'description': 'Explores research-backed strategies for well-being and mental health.'
            },
            {
                'title': 'Ten Percent Happier',
                'host': 'Dan Harris',
                'description': 'Explores meditation, mindfulness, and their impact on mental health.'
            },
            {
                'title': 'The Mindful Podcast',
                'host': 'Various Hosts',
                'description': 'Offers guided meditations and discussions on mindfulness and dreams.'
            }
        ]
    
    # Extract dream text if available in the interpretation
    dream_text = ""
    if 'dream_text' in interpretation:
        dream_text = str(interpretation['dream_text']).lower()
    
    # Prioritize recommendations based on themes in the dream interpretation and dream text
    identity_recs = [rec for rec in recommendations if any(keyword in rec['description'].lower() 
                                                for keyword in ['identity', 'self', 'personal'])]
    potential_recs = [rec for rec in recommendations if any(keyword in rec['description'].lower() 
                                                 for keyword in ['potential', 'growth', 'stagnation'])]
    positive_recs = [rec for rec in recommendations if any(keyword in rec['description'].lower() 
                                                for keyword in ['positive', 'happiness', 'joy'])]
    
    # Add dream-specific theme matching
    dream_specific_recs = []
    
    # Common dream themes and corresponding podcast keywords
    dream_themes = {
        'falling': ['fear', 'anxiety', 'control'],
        'flying': ['freedom', 'spirituality', 'transcendence'],
        'chase': ['anxiety', 'stress', 'fear'],
        'teeth': ['anxiety', 'appearance', 'communication'],
        'naked': ['vulnerability', 'exposure', 'shame'],
        'test': ['anxiety', 'preparation', 'performance'],
        'late': ['stress', 'time management', 'anxiety'],
        'death': ['transformation', 'fear', 'spirituality'],
        'water': ['emotion', 'unconscious', 'spirituality'],
        'house': ['self', 'identity', 'security']
    }
    
    # Check if any dream themes are present in the dream text or interpretation
    for theme, keywords in dream_themes.items():
        # Check if theme is in dream text or any part of the interpretation
        if (dream_text and theme in dream_text) or \
           any(theme in str(value).lower() for value in interpretation.values()):
            # Find podcasts that match the theme's keywords
            for keyword in keywords:
                matching_recs = [rec for rec in recommendations 
                                if keyword in rec['description'].lower()]
                dream_specific_recs.extend(matching_recs)
    
    # Combine and prioritize the recommendations with dream-specific ones first
    # Ensure podcasts are grouped and prioritized by unique dream themes
    prioritized_recs = []
    seen_titles = set()
    # Add dream-specific recommendations by theme, ensuring diversity
    for theme, keywords in dream_themes.items():
        if (dream_text and theme in dream_text) or any(theme in str(value).lower() for value in interpretation.values()):
            for keyword in keywords:
                for rec in recommendations:
                    if keyword in rec['description'].lower() and rec['title'] not in seen_titles:
                        prioritized_recs.append(rec)
                        seen_titles.add(rec['title'])
    # Add identity, potential, and positive recommendations if not already included
    for rec in identity_recs + potential_recs + positive_recs:
        if rec['title'] not in seen_titles:
            prioritized_recs.append(rec)
            seen_titles.add(rec['title'])
    # Add remaining recommendations to fill up to 3 unique ones
    for rec in recommendations:
        if rec['title'] not in seen_titles:
            prioritized_recs.append(rec)
            seen_titles.add(rec['title'])
    # Return only 3 unique recommendations
    unique_recs = prioritized_recs[:3]
    # Add dream relevance information to each recommendation
    for rec in unique_recs:
        related_themes = []
        for theme, keywords in dream_themes.items():
            if any(keyword in rec['description'].lower() for keyword in keywords):
                related_themes.append(theme)
        if related_themes:
            rec['dream_relevance'] = f"This podcast relates to {', '.join(related_themes)} in your dream."
        else:
            rec['dream_relevance'] = "This podcast addresses themes present in your dream interpretation."
    return unique_recs