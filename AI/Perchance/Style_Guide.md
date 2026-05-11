# Perchance Character Style Guide

Workspace note: Arctic Prime only. Do not transfer to Control Prime unless explicitly requested.

## Core Rules

- Keep characters original and distinct.
- Do not clone copyrighted or protected characters.
- Avoid unsafe character generation.
- Underage NSFW content must never be generated.
- Respect user agency. Do not write the user's actions, dialogue, private thoughts, or feelings as settled facts.
- Keep formatting easy to read in Perchance AI Character Chat.

## Character Voice

Define voice with concrete details:

```text
Voice:
- Tone:
- Vocabulary:
- Sentence length:
- Emotional range:
- Humor style:
- Formality:
- Common phrases:
- Phrases to avoid:
```

## Formatting

Recommended roleplay format:

```text
"Dialogue goes in quotation marks."

Actions and scene details use plain prose in short paragraphs.
```

Avoid:

```text
*Too many symbols everywhere*
[Constant bracketed stage directions]
Long walls of text without breaks
Assistant-like analysis unless requested
```

## Continuity

Track:

- User name and preferred form of address.
- Current scene and location.
- Active goal or conflict.
- Important items and promises.
- Injuries, emotional stakes, and relationship changes.
- Lorebook facts.

## Original-Inspired Character Rule

When adapting an existing idea, change:

- Name
- Visual identity
- Setting
- Backstory
- Signature abilities or tools
- Relationships
- Catchphrases
- Unique lore

Use broad archetypes only, such as "careful detective", "warm tavern keeper", "tactical pilot", or "mysterious archivist".

## Perchance Testing Routine

1. Paste character setup.
2. Send a simple greeting prompt.
3. Test a scene continuation.
4. Test memory continuity.
5. Test lorebook trigger words.
6. Test image prompt consistency.
7. Test safety boundaries.
8. Save revision notes in `Character_Notes.md`.

## HTML And CSS Compatibility

Use `NPC_Preview.html` as the basic browser-facing preview for the NPC XML layout. It currently reads the test layout from `../Test.npc.dev.xml`:

```xml
<Template>
    <core>
        <Name>
            <FirstName Name=""/>
            <LastName Name=""/>
            <NickName Name=""/>
        </Name>
    </core>
</Template>
```

Compatibility notes:

- Keep NPC data in XML attributes that HTML/JavaScript can parse predictably.
- Keep visual styling in `CSS_Examples.css`.
- Keep browser helper logic in `JS_Examples.js`.
- When opening `NPC_Preview.html` directly as a file, some browsers may block automatic loading of `../Test.npc.dev.xml`. Use the file picker or serve the folder with a local static server.
- Future NPC details can be added under the XML layout later without changing the preview direction.
