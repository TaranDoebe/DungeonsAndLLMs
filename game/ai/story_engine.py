import json
from DungeonsAndLLMs.game.ai.llm_generator import generate_monster, clean_llm_output, generate_story_text

def generate_dynamic_story(state, last_action=None):
    story_prompt = f"""
You are the Dungeon Master of an epic fantasy RPG.
Here is the current game state:
{json.dumps(state, indent=2)}

Narrate the next immersive scene, building on the story so far.
Then suggest 2–3 numbered options for what the player can do next.
Avoid meta explanations. Write as if this is part of the unfolding story.

Last action: {last_action if last_action else 'None'}

Format:
<paragraph>

Here are your options:
1. Option one
2. Option two
3. Option three
"""

    raw_response = generate_story_text(story_prompt)
    story_text, options = parse_story_response(raw_response)
    return story_text, options

def parse_story_response(response):
    """
    Splits the LLM output into story text and a list of options.
    Expects format:
    <paragraph>

    Here are your options:
    1. Option one
    2. Option two
    """
    parts = response.strip().split("Here are your options:")
    story = parts[0].strip()
    options = []

    if len(parts) > 1:
        lines = parts[1].strip().split("\n")
        for line in lines:
            line = line.strip()
            if line and line[0] in "123456789" and "." in line:
                options.append(line.split(".", 1)[1].strip())

    return story, options

STORY_TEMPLATE = '''
You are playing a fantasy RPG. The player is currently located at: {location}.
Recent events: {recent_events}
The player's current quest is: {quest}.

Write the next paragraph of the story that continues from the recent events. Then give the player 2–3 options of what they can do next. Format it like this:

"""
<paragraph>

Here are your options:
A) Option 1
B) Option 2
C) Option 3 (optional)
"""

Be vivid, imaginative, and make sure the story feels continuous and fantasy-inspired.
'''

def build_prompt(state):
    location = state.get("location", "a mysterious forest clearing")
    recent_events = state.get("recent_events", ["You woke up in the woods with no memory."])
    quest = state.get("quest", "Find out who you are and what brought you here.")

    return STORY_TEMPLATE.format(
        location=location,
        recent_events=" -> ".join(recent_events[-3:]),
        quest=quest
    )

def advance_story(state):
    player = state.get("player", {})
    name = player.get("name", "The Hero")
    last_action = state.get("last_action", "started")

    # Prompt example (expand later)
    prompt = (
        f"{name} just {last_action}. Generate a short fantasy story event (2-3 sentences) continuing the journey. "
        "The tone should match a dark fantasy RPG. Don't include combat yet."
    )

    story = generate_story_text(prompt)
    return story.strip()

