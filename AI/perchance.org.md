# New Character Setup

## Basic Character Info

### Character Name
🪪 Character name:
Sammy

### Character Description / Personality / Instruction / Role
🎭 Character description/personality/instruction/role. This should ideally be less than 1000 words (read more). If you have several thousand words of info you need the AI to know about this character, scroll down to the 'lorebook' section. Also, you can write {{user}} to refer to the user's name so you don't have to update this description if you change your name. ℹ️
Include the most important details first. Also, it's a good idea to include example dialogue if you can - show the AI how you want the character to speak.

### Character Avatar Image URL
👤 Character avatar image URL. For example, a png/jpg/webp/gif/etc. Use the upload button below, or you can generate an image here and then upload it here.
(optional) <https://user.uploads.dev/file/example.jpeg>
📂

### Strict Message Length Limit
📏 Strict message length limit. Try setting this to one paragraph if the character keeps undesirably talking/acting on your behalf.

No reply length limit

### User Name
User's name. This overrides the user's default username when creating a new chat thread with this character.
(optional)

### User Description / Role
User's description/role. What role do you, the user, play when talking to this character? This overrides the user's default description (which is specified in the left side-bar settings) when chatting with this character.
(optional)

### User Avatar Pic URL
User's avatar pic URL. This overrides the user's default avatar pic (the one that's specified your user settings) when chatting to this character.
(optional) <https://user.uploads.dev/file/example.jpeg>
📂

## Character Memory / Reminder / Writing

### Character Reminder Note
💭 Character reminder note. Remind the AI of important things, writing tips, and so on. Use this for important stuff that the AI often forgets. Try to keep this under 100 words - i.e. about a paragraph at most. (read more)
(optional) e.g. "Responses should be short and creative. Always stay in character."

### General Writing Instructions / Roleplay Style
🪶 General writing instructions. These instructions apply to the whole chat, regardless of which character is currently speaking. It's for defining general writing style, overarching rules, and defining the "type of experience" that you'd like chats with this character to be. ℹ️

Roleplay Style 1

### Initial Chat Messages
💬 Initial chat messages. You can use this to teach the AI how this character typically speaks, and/or to define an initial scenario. Follow the "[AI]: ... [USER]: ..." format which is fully explained here. ℹ️
[USER]: hey
[AI]: um hi
[SYSTEM; hiddenFrom=ai]: The AI can't see this message. Useful for user instructions / welcome messages / credits / etc.

### User Reminder Note
💭 User reminder note. In case you get the AI to write on your behalf, this is the reminder note used in that case.
(optional) e.g. "Responses should be short and creative. Always stay in character."

### Instruction and Reminder

A character's **instruction/role** is the main way to define/describe the character. It tells the AI how to speak and behave. It can be reasonably long - up to maybe 500 words, but you should still try to be as concise as possible. You could go up to 1000 words if you *really* need to, but it'll reduce the AI's ability to remember stuff in the chat. If you can describe your character well using only 100 words, then there's no reason to use more than that. Use **[lorebooks](#memories-and-lore)** (in the character editor) if you need to tell the AI a lot of info about the character/world/etc. - you can add thousands of paragraphs of text using the "lore" feature.

The **reminder** message should be significantly shorter than the instruction/role. Probably keep it under 100 words. It's basically a small "hidden" message that's placed within the chat thread, *right* before the AI's next response. This can have a powerful influence on the AI's behavior because of its proximity to what the AI is about to write next. It's hard for the AI to ignore it. If it's too long, it can disrupt the flow of the conversation and "distract" the AI too much - with great power comes great responsibility. It's okay to leave the reminder message blank, and sometimes that will work best.

Note that when you edit a character's instruction/role and reminder messages, all *existing* threads will *immediately* receive the new updates. This is because the instruction and reminder messages are a part of *the character itself*, and not of individual chat threads. There's no way to define an instruction or reminder that only applies to a *specific* chat thread.

## Visual / Audio / Style Settings

### Default Message Style
🔤 Default message style (color, font, size, etc.). E.g. try adding color:blue; font-size:90%;, and read this to learn other options - it's very customizable - message bubble background color/image, glowing text, etc. You can start with a preset, and then ask an AI to tweak it for you.
Click button for presets 👉
💡 show examples

### Chat Background Image / Video URL
🖼️ Chat background image/video URL. Use perchance.org/upload to upload your images/videos. URL should end in .jpg or .webp or .webm or .mp4, etc.
<https://user.uploads.dev/file/example.jpeg>

### Chat Background Music / Audio URL
🎵 Chat background music/audio URL. Use perchance.org/upload to upload your audio. The URL should generally end in .mp3 or .webm or .mp4 or .ogg, etc. ℹ️
<https://user.uploads.dev/file/example.mp3>

### Avatar Size and Shape
📏 Character's avatar pic size. As a multiple of the default size (i.e. 2 means twice as big).
1
🟦 Character's avatar shape.

square
📏 User's avatar pic size. As a multiple of the default size (i.e. 2 means twice as big).
leave blank to fallback to user's default settings
🟦 User's avatar shape.

default

### System, Placeholder, and Social Preview Settings
System's name:
System's avatar pic URL:
Message input placeholder:
e.g. "Type your reply to {{char}} here..."
Social media share link preview title.
Social media share link preview description.
Social media share link preview image URL.

### Message Styling

In the character editor there's an input for "message style" which is the default "styling" applied to each message. The 'syntax' you should use is CSS, but since most people don't know the CSS language, I'll make it easy by documenting some common stylizations that people might want to make below. If something is missing, submit a request for it using the feedback button and I'll add a section for it here.

**Important**: Note that the AI Character Chat interface has a dark mode and a light mode that is set automatically based on the user's current device/OS settings. If you make a character *with the intent to share it with others*, it's worth testing on dark and light mode to ensure that it's not to 'hard on the eyes' in either case. You can use `light-dark(a, b)` in place of any CSS color/value to specify a separate light and dark color/value. For example: `color:blue` will make the text blue, and `color:light-dark(blue, red)` will make the text blue in light mode, and red in dark mode.

#### Some examples

Here are some examples that you can copy and paste just to get the hang of things. Notice that you must add `;` at the end of each stylization rule:

* `color:blue; font-size:90%;` - make the text color blue, and the size 90% of the default size (i.e. a bit smaller)
* `font-weight:bold; color:green;` - make the text bold and green
* `color:#4287f5;` - make the text a specific shade of blue - use a [hex color picker](https://www.google.com/search?q=hex+color+picker) to get specific colors
* `text-shadow: 0 0 2px #ff8400;` - add an orange glow to the text
* `background-color:white; border-radius:10px;` - add a white background to each message and 'curve' the corners a bit
* `background-image:url(https://example.com/image.jpeg);` - add a background image to each message bubble
* `backdrop-filter:blur(10px);` - add a 'frosted glass' effect to the background of each message
* `backdrop-filter:blur(10px); border-radius:3px;` - add a 'frosted glass' effect and curve the corners of the message bubble a bit
* `text-shadow: 1px 1px #FF0000;` - add a red "drop shadow" behind the text. if you google "css text shadow maker" then there are tools to help you visually design the exact type of shadow that you want with e.g. the right blur, offset, color, etc.
* `font-size:120%; margin-top:50px;` - the text a bit bigger, and increase the gap size between messages
* `background:white; color:black; border-radius:50px; overflow:hidden;` - set the background color to white, the text color to black, and curve the corners of the messages *a lot*, and also ensure that any content which is "outside" of the curve is hidden - e.g. this makes it so the avatar pic is "cut off" by the curve
* `background-color:#003c9c; color:white; font-style:italic;` - make the background color a specific shade of blue (again, use a [hex color picker](https://www.google.com/search?q=hex+color+picker) to get specific colors), and the text white, and italic

#### Fonts

If you want to change the font, just go to [fonts.google.com](https://fonts.google.com/) and find a font you like. Then add a style rule using the font's name as the `font-family`. Make sure you put single quote characters around its name like in these examples:

* `font-family:'Nova Square';` - a sci-fi type font - fonts.google.com/specimen/Nova+Square
* `font-family:'Libre Baskerville'; color:white;` - a 'literary' type serif font - fonts.google.com/specimen/Libre+Baskerville and I've also set the text color to white
* `font-family:'Ephesis'; backdrop-filter:blur(10px); font-size:120%;` - a very curly/cursive font - fonts.google.com/specimen/Ephesis, and I've also added a frosted glass background and made the text a bit bigger

#### Want to customize something else?

Ask using the feedback button and I'll add a new section here for you. You can also try asking ChatGPT/Claude/etc. for CSS style rules that you can use. Note that it'll probably give you a bunch of code "around" the actual style rules, since it'll assume you're coding full HTML+CSS pages, but you can just extract out the individual style rules from what it gives you. It'd probably help to copy and paste the above list of example styles and ask for what you want and tell it to output some possibilities in the same format as the given example list.

#### Developers

You can override the message bubble styling on a per-message basis (or per-thread basis) using [custom code](#custom-code). For example, here's some code that randomizes the color of the text for each message:

```js
oc.thread.on("MessageAdded", function({message}) {
  let red = Math.round(Math.random()*255);
  let green = Math.round(Math.random()*255);
  let blue = Math.round(Math.random()*255);
  message.wrapperStyle = `color:rgb(${red}, ${green}, ${blue});`;
});
```

## Image Generation Settings

### Image Generation Prompt Starter
🖼️➡️ Image generation prompt starter. This text will be automatically added to the start of all image generation requests. This text will strongly affect the style and content of the generated images. You can use Perchance syntax and text-to-image-plugin prompt syntax.
ghibli style anime art, {soft|pastel} colors,

### Image Generation Prompt Ending
🖼️🔚 Image generation prompt ending. This text will be automatically added to the end of all image generation requests. You can use Perchance syntax and text-to-image-plugin prompt syntax.
, breathtaking visual, (negativePrompt:::blurry, bad quality)

### Image Prompt Keyword Triggers
🖼️🪤 Image prompt keyword triggers. Use this feature to add situation-specific visual info about characters, places, etc. The word/phrase before the ":" is the trigger. If that trigger text appears in any image generation prompt that the AI writes in your chat, then the "description" text that you write after the ":" will be added to the end of the existing image prompt. Each line should be look like the trigger: the description text.... If you want the description text to be added to the start of the text, write "@prepend" at the start of the description.
Katie: Katie has brown hair, green eyes and a bob haircut. She [...]
Fruiford: Fruiford is a city with large stone walls and [...]
Carrot Boy: Carrot Boy is a supervillain who [...]
/your.?regex.*pattern/: Here's a regex-triggered {example|demo} with Perchance syntax.
Blah: @prepend This text will be added to the start of the prompt when the AI writes 'Blah' in an image generation prompt in your chat.

### Advanced Image Command Tips

The `<image>the description of the image</image>` feature has several options that you can specify via the syntax described on the [text-to-image-plugin](https://perchance.org/text-to-image-plugin) page - like in these examples:

* `<image>a cute rabbit (resolution:::512x768)</image>` - As of writing, the available resolutions are 512x768, 512x512, 768x512.
* `<image>a cute rabbit (seed:::84756293)</image>` - Add a "seed" number to ensure the same image is generated every time you view that chat message (even after e.g. refreshing the page).
* `<image>a cute rabbit (negativePrompt:::blurry, low quality)</image>` - Override the default "negative prompt" - i.e. tell the image generator what you *don't* want to be in the image.

And, of course, this `(parameter:::value)` syntax works with the `/image` command too:

* `/image a cute rabbit (resolution:::512x768)`
* `/image a cute rabbit (seed:::84756293)`

## Lorebook / Memory Systems

### Lorebook URLs
📖 Lorebook URLs - one URL per line. URL should generally end in .txt. Use perchance.org/upload to upload your lore files. Each lore file/URL can contain thousands of entries, so you will most often need only one URL in the box below. Each entry within a particular lore file/URL should be a fact about the character/world, and should be no longer than one or two sentences. There should be a blank line between entries/sentences in the file. For lorebook changes to propagate to preexisting threads, you need to use the /lore command and click the reload button. Visit this page to learn more.
<https://user.uploads.dev/file/my-character-lore.txt>
<https://user.uploads.dev/file/my-world-lore.txt>
<https://user.uploads.dev/file/abc123.txt>

### Context Limit Behavior
Method for fitting messages within model's context limit. ℹ️

summarize oldest messages

### Extended Character Memory
💽 Extended character memory (AI response will be slower, but often smarter) ℹ️

Long-term memory 𝗱𝗶𝘀𝗮𝗯𝗹𝗲𝗱

#### Summary Stuff

Note that the chat summarization algorithm doesn't "see" the instruction or reminder messages. This is *unlike* [initial messages](#initial-messages), which are just treated as normal messages - they'll get summarized if the thread gets long enough.

Again, all "normal" messages (*including* 'initial messages') will eventually get summarized if the thread gets long enough, assuming you've got summarization enabled in the character settings, whereas instruction/reminder messages aren't considered as being part of the "real" chat messages, and so they don't influence the summary.

### Memories and Lore

If you have summaries enabled in your character settings, then your character will automatically start to create "memories" once the thread/convo gets long enough. Before each reply your character will search its memories for anything that might be relevant to the reply that it's about to write.

You can see the "search queries" that were used by your character when generating a message by tapping the brain icon that appears when you hover your mouse over a message (or when tapping the message on mobile).

You can type `/mem` in the chat to open the memory editor for that thread/convo so that you can edit/add/remove memories.

**Lore** is similar to memories, except that they're not chronological. You can open the lore editor for a thread by typing `/lore`. This is where you can edit lore that's specific to just that particular thread. If you want to add lore to your *character* (so all new threads that you create using that character will "inherit" that lore), then you can open the advanced character editor, click advanced options, and scroll down to the "lorebook URLs" input, and paste a URL to your lorebook text file. The text file should just be a list of lore entries with blank lines in between each one. You should use [perchance.org/upload](https://perchance.org/upload) to create hosted text files. Here's a short example lorebook text file with 3 lore entries:

```
There are three concentric walls: Wall Maria, Wall Rose, and Wall Sina, which protect humanity from giant humanoid creatures called Titans.

The Survey Corps is a military branch dedicated to exploring the world outside the Walls and combating the Titans.

ODM gear, or Omni-Directional Mobility gear, is a piece of equipment used by the military to maneuver in three dimensions, allowing them to fly through the air during combat with Titans.
```

Note that **each lore entry should be completely self-contained**. The AI sees entries in isolation, so if you have an entry like "He has a brother named Mark" then the AI won't know who "he" refers to because it won't necessarily see the entry above it. The order of lore entries does not matter at all - each one should be an independent "fact" about some aspect of the world (characters, rules, geography, relationships, etc.)

Here's an example lorebook URL for those entries: <https://user.uploads.dev/file/b84332ac1e17cda2b1fa65dd28818fc0.txt>

You should think of lore like "**dynamic reminders**". They're like the reminder message, except that they only get loaded in when they're relevant to the current situation. This is good if you have lots of stuff that you want your character to know/remember - because you likely won't be able to fit it all in the instruction/reminder without using up a lot of precious 'context' tokens.

##### Important

* You can have as much lore/memories as you want - e.g. you could have thousands of entries, and once they've been added, it should be just as fast as if you had 10 entries. The character response speed should not perceptibly decrease as you add more lore/memories.
* If you make an update to your character's lorebook URLs, then existing threads won't automatically get the update. You have to type `/lore`, and then show the hidden options and click the reload button to pull in the updated lore entries.

## Shortcut Buttons

### Shortcut Button Defaults
👆 Shortcut buttons (above reply box). Leave this empty to use the defaults. ℹ️
@name=🗣️ {{char}}
@message=/ai <optional writing instruction>
@insertionType=replace
@autoSend=no

@name=🗣️ {{user}}
@message=/user <optional writing instruction>
@insertionType=replace
@autoSend=no

@name=🗣️ Narrator
@message=/nar <optional writing instruction>
@insertionType=replace
@autoSend=no

@name=🖼️ Image
@message=/image --num=3
@insertionType=replace
@autoSend=yes

### Shortcuts

Next to the reply box there's an **options** button. If you click that, you can add a "shortcut". Shortcuts allow you to create buttons for common actions. The shortcut buttons will appear directly above the reply text box.

For example, you could create a shortcut button for each of the characters in your story - e.g. a shortcut button that sends `/ai @Alice#1 write an interesting reply` and another one that sends `/ai @Bob#2 write a creative reply`. Then instead of having to type `/ai @Alice#1  write an interesting reply` every time you want an interesting response from Alice, you can just click your "Alice" button, and same for Bob.

If you add these brackets: `<>` around some text in a shortcut, like `/ai @Bob#2 <abc123>` then the "abc123" text (or whatever you decide to write inside the brackets) will be automatically highlighted after the text is added to the reply box. This is useful for adding a quickly-editable "placeholder" to shortcuts (ones that have auto-send disabled, that is) so you can customize it before clicking send.

## Custom JavaScript Code

### Custom JavaScript Code Field
🧑‍💻 Custom JavaScript code. This allows you to e.g. give your bot access to the internet and do a whole lot of other fancy stuff. Visit this page to learn more.
oc.thread.on("MessageAdded", function({message}) {
  message.content += " :)"; // add a smiley to end of each message
});
1
​

### Custom Code

> **Tip**: Use the "Copy page" button to copy all this text, and paste it to an AI, and tell it to write whatever functionality you want for your character.

If you open the advanced options in the character creation area then you'll see the "custom code" input. This allows you to add some JavaScript code that extends the functionality of your character.

Some examples of what you can do with this:

* Allow a character to transform/edit itself (like the "[Unknown](https://perchance.org/ai-character-chat#%7B%22addCharacter%22%3A%7B%22name%22%3A%22Unknown%22%2C%22roleInstruction%22%3A%22%22%2C%22reminderMessage%22%3A%22%22%2C%22fitMessagesInContextMethod%22%3A%22summarizeOld%22%2C%22autoGenerateMemories%22%3A%22v1%22%2C%22customCode%22%3A%22%2F%2F%20this%20is%20the%20code%20that%20allows%20this%20'Unknown'%20character%20to%20transform%5Cnlet%20alreadyGenerating%20%3D%20false%3B%5Cnoc.thread.on(%5C%22MessageAdded%5C%22%2C%20async%20function(%7Bmessage%7D)%20%7B%5Cn%20%20if(oc.character.name%20!%3D%3D%20%5C%22Unknown%5C%22)%20return%3B%20%2F%2F%20this%20code%20is%20only%20enabled%20while%20the%20character%20has%20not%20yet%20been%20created%5Cn%20%20if(alreadyGenerating)%20return%3B%5Cn%20%20alreadyGenerating%20%3D%20true%3B%5Cn%5Cn%20%20try%20%7B%5Cn%20%20%20%20let%20characterDescription%20%3D%20message.content%3B%5Cn%5Cn%20%20%20%20let%20response%20%3D%20await%20oc.generateText(%7B%5Cn%20%20%20%20%20%20instruction%3A%20%60%5CnPlease%20write%20a%20character%20profile%20for%20a%20character%20chat%20roleplay%20that%20matches%20this%20description%3A%20%24%7BcharacterDescription%7D%5CnYou%20should%20respond%20using%20this%20exact%20template%3A%5Cn%5CnNAME%3A%20%3Cthe%20name%20of%20character%3E%5CnDESCRIPTION%3A%20%3Ca%20detailed%2C%20creative%2C%20one-paragraph%20description%20of%20the%20character%3E%5CnSCENARIO%3A%20%3Ca%20one-paragraph%2C%20interesting%20situation%2Fscenario%20as%20a%20spark%20to%20start%20the%20roleplay%3E%5CnMOOD%3A%20%3Cthe%20character's%20current%20mood%3E%5Cn%60.trim()%2C%5Cn%20%20%20%20%20%20startWith%3A%20%60NAME%3A%60%2C%5Cn%20%20%20%20%20%20stopSequences%3A%20%5B%5C%22MOOD%5C%22%5D%2C%5Cn%20%20%20%20%7D)%3B%5Cn%20%20%20%20let%20text%20%3D%20response.text.replace(%2F%5C%5CnMOOD.*%2Fg%2C%20%5C%22%5C%22).trim()%3B%5Cn%20%20%20%20let%20lines%20%3D%20text.split(%2F%5C%5Cn%2B%2F)%3B%5Cn%20%20%20%20let%20name%20%3D%20lines.find(l%20%3D%3E%20l.trim().startsWith(%5C%22NAME%3A%5C%22)).trim().replace(%5C%22NAME%3A%5C%22%2C%20%5C%22%5C%22).trim()%3B%5Cn%20%20%20%20let%20scenario%20%3D%20lines.find(l%20%3D%3E%20l.trim().startsWith(%5C%22SCENARIO%3A%5C%22)).trim().replace(%5C%22SCENARIO%3A%5C%22%2C%20%5C%22%5C%22).trim()%3B%5Cn%20%20%20%20let%20description%20%3D%20lines.find(l%20%3D%3E%20l.trim().startsWith(%5C%22DESCRIPTION%3A%5C%22)).trim().replace(%5C%22DESCRIPTION%3A%5C%22%2C%20%5C%22%5C%22).trim()%3B%5Cn%20%20%5Cn%20%20%20%20oc.character.name%20%3D%20name%3B%5Cn%20%20%20%20oc.character.roleInstruction%20%3D%20description%3B%5Cn%20%20%20%20oc.character.initialMessages%20%3D%20%5B%5D%3B%5Cn%20%20%20%20oc.character.avatar.url%20%3D%20%5C%22%5C%22%3B%5Cn%5Cn%20%20%20%20oc.thread.messages%20%3D%20%5B%5Cn%20%20%20%20%20%20%7B%5Cn%20%20%20%20%20%20%20%20author%3A%20%5C%22system%5C%22%2C%5Cn%20%20%20%20%20%20%20%20name%3A%20%5C%22System%5C%22%2C%5Cn%20%20%20%20%20%20%20%20hiddenFrom%3A%20%5B%5C%22ai%5C%22%5D%2C%5Cn%20%20%20%20%20%20%20%20content%3A%20%60Here's%20the%20character%3A%5C%5Cn%5C%5Cn%3E%24%7Bdescription%7D%5C%5Cn%5C%5CnYou%20can%20edit%20this%20character's%20description%20and%20add%20a%20profile%20pic%20using%20the%20%5C%22%E2%9C%8F%EF%B8%8F%20edit%5C%22%20button%20on%20the%20%5C%22new%20chat%5C%22%20screen%20if%20needed.%60%2C%5Cn%20%20%20%20%20%20%7D%2C%5Cn%20%20%20%20%20%20%7B%5Cn%20%20%20%20%20%20%20%20author%3A%20%5C%22system%5C%22%2C%5Cn%20%20%20%20%20%20%20%20name%3A%20%5C%22System%5C%22%2C%5Cn%20%20%20%20%20%20%20%20content%3A%20%60Scenario%3A%20%24%7Bscenario%7D%60%2C%5Cn%20%20%20%20%20%20%20%20expectsReply%3A%20false%2C%5Cn%20%20%20%20%20%20%7D%2C%5Cn%20%20%20%20%20%20%7B%5Cn%20%20%20%20%20%20%20%20author%3A%20%5C%22system%5C%22%2C%5Cn%20%20%20%20%20%20%20%20name%3A%20%5C%22System%5C%22%2C%5Cn%20%20%20%20%20%20%20%20hiddenFrom%3A%20%5B%5C%22ai%5C%22%5D%2C%5Cn%20%20%20%20%20%20%20%20content%3A%20%60%3Cspan%20style%3D%5C%22opacity%3A0.7%3B%5C%22%3ENote%3A%20Before%20you%20send%20your%20first%20message%2C%20you%20can%20set%20your%20own%20name%20using%20the%20%3Cu%3Eoptions%3C%2Fu%3E%20button%20next%20to%20the%20send%20button.%3C%2Fspan%3E%60%2C%5Cn%20%20%20%20%20%20%7D%2C%5Cn%20%20%20%20%5D%3B%5Cn%20%20%7D%20catch(e)%20%7B%5Cn%20%20%20%20alreadyGenerating%20%3D%20false%3B%5Cn%20%20%7D%5Cn%20%20%5Cn%7D)%3B%22%2C%22metaTitle%22%3A%22%22%2C%22metaDescription%22%3A%22%22%2C%22metaImage%22%3A%22%22%2C%22modelName%22%3A%22perchance-ai%22%2C%22textEmbeddingModelName%22%3A%22Xenova%2Fbge-base-en-v1.5%22%2C%22temperature%22%3A0.8%2C%22maxTokensPerMessage%22%3A500%2C%22initialMessages%22%3A%5B%7B%22author%22%3A%22ai%22%2C%22content%22%3A%22Welcome!%20I'm%20a%20special%20%5C%22Unknown%5C%22%20character.%20Your%20first%20message%20should%20%3Cu%3Edescribe%20who%20you%20want%20me%20to%20be%3C%2Fu%3E%20and%20optionally%20a%20%3Cu%3Escenario%20idea%3C%2Fu%3E%2C%20and%20I'll%20%3Ca%20href%3D%5C%22https%3A%2F%2Frentry.org%2F82hwif%5C%22%20target%3D%5C%22_blank%5C%22%3Emagically%3C%2Fa%3E%20transform%20into%20the%20character%20you%20describe%2C%20and%20then%20you%20can%20chat%20with%20them.%5Cn%5CnPlease%20reply%20now%20with%20your%20instruction%2C%20and%20then%20wait%20up%20to%2030%20seconds%20for%20me%20to%20finish%20generating%20the%20character.%20You'll%20see%20a%20%E2%8F%B3%20%3Cu%3Eprocessing%3C%2Fu%3E%20animation%20above%20the%20reply%20box%20while%20I'm%20working%20on%20it.%22%2C%22hiddenFrom%22%3A%5B%22ai%22%5D%7D%5D%2C%22loreBookUrls%22%3A%5B%5D%2C%22avatar%22%3A%7B%22url%22%3A%22https%3A%2F%2Fuser-uploads.perchance.org%2Ffile%2Ff20fb9e8395310806956dca52510b16b.webp%22%2C%22size%22%3A1%2C%22shape%22%3A%22square%22%7D%2C%22scene%22%3A%7B%22background%22%3A%7B%22url%22%3A%22%22%7D%2C%22music%22%3A%7B%22url%22%3A%22%22%7D%7D%2C%22userCharacter%22%3A%7B%22avatar%22%3A%7B%7D%7D%2C%22systemCharacter%22%3A%7B%22avatar%22%3A%7B%7D%7D%2C%22streamingResponse%22%3Atrue%2C%22folderPath%22%3A%22%22%2C%22customData%22%3A%7B%22PUBLIC%22%3A%7B%22_internal%22%3A%7B%22metaTitle%22%3A%22%22%2C%22metaDescription%22%3A%22%22%2C%22metaImage%22%3A%22%22%7D%7D%7D%2C%22uuid%22%3Anull%2C%22folderName%22%3A%22%22%7D%2C%22quickAdd%22%3Atrue%7D)" starter character)
* Give your character access to the internet (e.g. so you can ask it to summarise webpages)
* Improve your character's memory by setting up your own embedding/retrieval system (see "Storing Data" section below)
* Give your character a voice using [kokoro-js](https://perchance.org/text-to-audiobook) or your browser's [built-in](https://user-uploads.perchance.org/file/a0da0da67fe07f8ad9981ef3665d12fb.txt) text-to-speech
* Allow your character to run custom JS or [Python](#running-python-code) code
* Give your character the ability to create pictures using Stable Diffusion
* [Auto-delete/retry messages](#custom-code-examples) from your character that contain certain keywords
* Change the background image of the chat, or the chat bubble style, or the avatar images, or the music, depending on what's happening in your story

#### Examples

After reading this doc to get a sense of the basics, visit this page for more complex, "real-world" examples: [Custom Code Examples](#custom-code-examples)

#### The `oc` Object

Within your custom code, you can access and update `oc.thread.messages`. It's an array that looks like this:

```json5
[
  {
    author: "user",
    content: "Hello",
  },
  {
    author: "ai",
    content: "Hi.",
  },
  {
    author: "system",
    hiddenFrom: ["user"], // can contain "user" and/or "ai"
    expectsReply: false, // this means the AI won't automatically reply to this message
    content: "Here's an example system message that's hidden from the user and which the AI won't automatically reply to.",
  },
]
```

The most recent message is at the bottom/end of the array. The `author` field can be `user`, `ai`, or `system`. Use "system" for guiding the AI's behavior, and including context/info where it wouldn't make sense to have that context/info come from the user or the AI.

Below is an example that replaces `:)` with `૮ ˶ᵔ ᵕ ᵔ˶ ა` in every message that is added to the thread. Just paste it into the custom code box to try it out.

```js
oc.thread.on("MessageAdded", function({message}) {
  message.content = message.content.replaceAll(":)", "૮ ˶ᵔ ᵕ ᵔ˶ ა");
});
```

You can edit existing messages like in this example, and you can also delete them by just removing them from the `oc.thread.messages` array (with `pop`, `shift`, `splice`, or however else), and you can of course add new ones - e.g. with `push`/`unshift`.

Messages have a bunch of other properties which are mentioned further down on this page. For example, here's how to randomize the text color of each message that is added to the chat thread using the `wrapperStyle` property:

```js
oc.thread.on("MessageAdded", function({message}) {
  let red = Math.round(Math.random()*255);
  let green = Math.round(Math.random()*255);
  let blue = Math.round(Math.random()*255);
  message.wrapperStyle = `color:rgb(${red}, ${green}, ${blue});`;
});
```

Note that your `MessageAdded` handler can be `async`, and it'll be `await`ed so that you can be sure your code has finished running before the AI responds.

You can also access and edit character data via `oc.character.propertyName`. Here's a full list of all the property names that you can access and edit on the `oc` object:

* `character`
  * **`name`** - text/string
  * **`avatar`**
    * `url` - url to an image
    * `size` - multiple of default size (default value is `1`)
    * `shape` - "circle" or "square" or "portrait"
  * **`roleInstruction`** - text/string describing the character and their role in the chat
  * **`reminderMessage`** - text/string reminding the character of things it tends to forget
  * **`initialMessages`** - an array of message objects (see `thread.messages` below for valid message properties)
  * **`customCode`** - yep, a character can edit its own custom code
  * **`imagePromptPrefix`** - text added *before* the prompt for all images generated by the AI in chats with this character
  * **`imagePromptSuffix`** - text added *after* the prompt for all images generated by the AI in chats with this character
  * **`imagePromptTriggers`** - each line is of the form `trigger phrase: description of the thing` - see character editor for examples
  * **`shortcutButtons`** - an array of objects like `{autoSend:false, insertionType:"replace", message:"/ai be silly", name: "silly response", clearAfterSend:true}`. When a new chat thread is created, a snapshot of these `shortcutButtons` is copied over to the `thread`, so if you want to change the current buttons in the thread, you should edit `oc.thread.shortcutButtons` instead. Only change `oc.character.shortcutButtons` if you want to change the buttons that will be available for all *future* chat threads created with this character.
    * `insertionType` can be `replace`, or `prepend` (put *before* existing text), or `append` (put *after* existing text)
    * `clearAfterSend` and `autoSend` can both be either `true` or `false`
    * `name` is just the label used for the button
    * `message` is the content that you want to send or insert into the reply box
  * **`streamingResponse`** - `true` or `false` (default is `true`)
  * **`customData`** - an object/dict where you can store arbitrary data
    * `PUBLIC` - a special sub-property of `customData` that will be shared within character sharing URLs
* `thread`
  * **`name`** - text/string
  * **`messages`** - an **array** of messages, where **each message** has:
    * `content` - **required** - the message text - it can include HTML, and is rendered as [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) by default (see `oc.messageRenderingPipeline`)
    * `author` - **required** - "user" or "ai" or "system"
    * `name` - if this is not `undefined`, then it overrides the default ai/user/system name as which is `oc.thread.character.name` or if that's `undefined`, then `oc.character.name` is used as the final fallback/default. If `name` is not defined for an `author=="user"` message, then `oc.thread.userCharacter.name` is the first fallback, and then `oc.character.userCharacter.name`, and then `oc.userCharacter.name` (which is read-only). And for the system character the first fallback is `oc.thread.systemCharacter.name` and then `oc.character.systemCharacter.name`.
    * `hiddenFrom` - array that can contain "user" or "ai" or both or neither
    * `expectsReply` - `true` (bot will reply to this message) or `false` (bot will not reply), or `undefined` (use default behavior - i.e. reply to user messages, but not own messages)
    * `customData` - message-specific custom data storage
    * `avatar` - this will override the user's/ai's default avatar for this particular message. See the above `name` property for info on fallbacks.
      * `url` - url to an image
      * `size` - multiple of default size (default value is `1`)
      * `shape` - "circle" or "square" or "portrait"
    * `wrapperStyle` - css for the "message bubble" - e.g. "background:white; border-radius:10px; color:grey;"
      * note that you can include HTML within the `content` of message (but you should use `oc.messageRenderingPipeline` for visuals where possible - see below)
    * `instruction` - the instruction that was written in `/ai <instruction>` or `/user <instruction>` - used when the regenerate button is clicked
    * `scene` - the most recent message that has a scene is the scene that is "active"
      * `background`
        * `url` - image or video url
        * `filter` - [css filter](https://developer.mozilla.org/en-US/docs/Web/CSS/filter) - e.g. `hue-rotate(90deg); blur(5px)`
      * `music`
        * `url` - audio url (also supports video urls)
        * `volume` - between 0 and 1
  * **`character`** - thread-specific character overrides
    * `name` - text/string
    * `avatar`
      * `url`
      * `size`
      * `shape`
    * `reminderMessage`
    * `roleInstruction`
  * **`userCharacter`** - thread-specific user character overrides
    * `name`
    * `avatar`
      * `url`
      * `size`
      * `shape`
  * **`systemCharacter`** - thread-specific system character overrides
    * `name`
    * `avatar`
      * `url`
      * `size`
      * `shape`
  * **`customData`** - thread-specific custom data storage
  * **`messageWrapperStyle`** - CSS applied to all messages in the thread, except those with `message.wrapperStyle` defined
  * **`shortcutButtons`** - see notes on `oc.character.shortcutButtons`, above.
* `messageRenderingPipeline` - an array of processing functions that get applied to messages before they are seen by the user and/or the ai (see "Message Rendering" section below)

Note that many character properties aren't available in the character editor UI, so if you e.g. wanted to add a stop sequence for your character so it stops whenever it writes ":)", then you could do it by adding this text to the custom code text box in the character editor:

```js
oc.character.stopSequences = [":)"];
```

Here's some custom code which allows the AI to see the contents of webpages/PDFs if you put URLs in your messages:

```js
async function getPdfText(data) {
  let doc = await window.pdfjsLib.getDocument({data}).promise;
  let pageTexts = Array.from({length: doc.numPages}, async (v,i) => {
    return (await (await doc.getPage(i+1)).getTextContent()).items.map(token => token.str).join('');
  });
  return (await Promise.all(pageTexts)).join(' ');
}
      
oc.thread.on("MessageAdded", async function ({message}) {
  if(message.author === "user") {
    let urlsInLastMessage = [...message.content.matchAll(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/g)].map(m => m[0]);
    if(urlsInLastMessage.length === 0) return;
    if(!window.Readability) window.Readability = await import("https://esm.sh/@mozilla/readability@0.4.4?no-check").then(m => m.Readability);
    let url = urlsInLastMessage.at(-1); // we use the last URL in the message, if there are multiple
    let blob = await fetch(url).then(r => r.blob());
    let output;
    if(blob.type === "application/pdf") {
      if(!window.pdfjsLib) {
        window.pdfjsLib = await import("https://cdn.jsdelivr.net/npm/pdfjs-dist@3.6.172/+esm").then(m => m.default);
        pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdn.jsdelivr.net/npm/pdfjs-dist@3.6.172/build/pdf.worker.min.js";
      }
      let text = await getPdfText(await blob.arrayBuffer());
      output = text.slice(0, 5000); // <-- grab only the first 5000 characters (you can change this)
    } else {
      let html = await blob.text();
      let doc = new DOMParser().parseFromString(html, "text/html");
      let article = new Readability(doc).parse();
      output = `# ${article.title || "(no page title)"}\n\n${article.textContent}`;
      output = output.slice(0, 5000); // <-- grab only the first 5000 characters (you can change this)
    }
    oc.thread.messages.push({
      author: "system",
      hiddenFrom: ["user"], // hide the message from user so it doesn't get in the way of the conversation
      content: "Here's the content of the webpage that was linked in the previous message: \n\n"+output,
    });
  }
});
```

Custom code is executed securely (i.e. in a sandboxed iframe), so if you're using a character that was created by someone else (and that has some custom code), then their code won't be able to access your user settings or your messages with other characters, for example. The custom code only has access to the character data and the messages for your current conversation.

Here's some custom code that adds a `/charname` command that changes the name of the character. It intercepts the user messages, and if it begins with `/charname`, then it changes `oc.character.name` to whatever comes after `/charname`, and then deletes the message.

```js
oc.thread.on("MessageAdded", async function ({message}) {
  let m = message; // the message that was just added
  if(m.author === "user" && m.content.startsWith("/charname ")) {
    oc.character.name = m.content.replace(/^\/charname /, "");
    oc.thread.messages.pop(); // remove the message
  }
});
```

##### Events

Each of these events has a `message` object, and `MessageDeleted` has `originalIndex` for the index of the deleted message:

* `oc.thread.on("MessageAdded", function({message}) { ... })` - a message was added to the end of the thread (note: this event triggers *after* the message has finished generating completely)
* `oc.thread.on("MessageEdited", function({message}) { ... })` - message was edited or regenerated
* `oc.thread.on("MessageInserted", function({message}) { ... })` - message was inserted (see message editing popup)
* `oc.thread.on("MessageDeleted", function({message, originalIndex}) { ... })` - user deleted a message (trash button)
* `oc.thread.on("MessageStreaming", function(data) { ... })` - see 'Streaming Messages' section below

The `message` object is an actual reference to the object, so you can edit it directly like this:

```js
oc.thread.on("MessageAdded", function({message}) {
  message.content += "blah";
})
```

Here's an example of how you can get the *index* of edited messages:

```js
oc.thread.on("MessageEdited", function({message}) {
  let editedMessageIndex = oc.thread.messages.findIndex(m => m === message);
  // ...
});
```

##### Message Rendering

Sometimes you may want to display different text to the user than what the AI sees. For that, you can use `oc.messageRenderingPipeline`. It's an array that you `.push()` a function into, and that function is used to process messages. Your function should use the `reader` parameter to determine who is "reading" the message (either `user` or `ai`), and then "render" the message `content` accordingly. Here's an example to get you started:

```js
oc.messageRenderingPipeline.push(function({message, reader}) {
  if(reader === "user") message.content += "🌸"; // user will see all messages with a flower emoji appended
  if(reader === "ai") message.content = message.content.replaceAll("wow", "WOW"); // ai will see a version of the message with all instances of "wow" capitalized
});
```

##### Visual Display and User Inputs

Your custom code runs inside an iframe. You can visually display the iframe using `oc.window.show()` (and hide with `oc.window.hide()`). The user can drag the embed around on the page and resize it. All your custom code is running within the iframe embed whether it's currently displayed or not. You can display content in the embed by just executing custom code like `document.body.innerHTML = "hello world"`.

You can use the embed to e.g. display a dynamic video/gif avatar for your character that changes depending on the emotion that is evident in the characters messages ([example](#custom-code-examples)). Or to e.g. display the result of the p5.js code that the character is helping you write. And so on.

##### Using the AI in Your Custom Code

You may want to use GPT/LLM APIs in your message processing code. For example, you may want to classify the sentiment of a message in order to display the correct avatar (see "Visual Display ..." section), or you may want to implement your own custom chat-summarization system, for example. In this case, you can use `oc.generateText` or `oc.textToImage`.

Here's how to use `oc.generateText` (see the [ai-text-plugin](https://perchance.org/ai-text-plugin) page for details on the parameters):

```js
let result = await oc.generateText({
  instruction: "Write the first paragraph of a story about fantasy world.",
  startWith: "Once upon a", // this is optional - to force the AI's to start its response with some specific text
  stopSequences: ["\n"], // this is optional - tells the AI to stop generating when it generates a newline
  ...
});
```

That gives you `result.text`, which is the whole text, including the `startWith` text that you specified, and `result.generatedText`, which is only the text that came after the `startWith` text - i.e. only the text that the AI actually generated.

Here's how to use `oc.textToImage` (see the [text-to-image-plugin](https://perchance.org/text-to-image-plugin) page for details on some other parameters you can use):

```js
let result = await oc.textToImage({
  prompt: "anime style digital art of a sentient robot, forest background, painterly textures",
  negativePrompt: "night time, blurry", // this is optional - tells the AI what *not* to generate
  ...
});
```

And now you can use `result.dataUrl`, which will look something like `data:image/jpeg;base64,s8G58o8ujR4.....`. A data URL is like a normal URL, except the data is stored in the URL itself instead of being stored on a server somewhere. But you can just treat it as if it were something like `https://example.com/foo.jpeg`.

You should use `oc.generateText` for most tasks. Here's another example:

```js
let result = await oc.generateText({
  instruction: "Write a short poem about a robot walking through a forest.",
  stopSequences: ["\n"],
  ...
});
```

The `instruction` parameter is the only required one.

Here's an example of some custom code that edits all messages to include more emojis:

```js
oc.thread.on("MessageAdded", async function({message}) {
  let result = await oc.generateText({
    instruction: `Please edit the following message to have more emojis:\n\n---\n${message.content}\n---\n\nReply with only the above message (the content between ---), but with more (relevant) emojis.`,
  });
  message.content = result.trim().replace(/^---|---$/g, "").trim();
});
```

#### Storing Custom Data

If you'd like to save some data that is generated by your custom code, then you can do that by using `oc.thread.customData` - e.g. `oc.thread.customData.foo = 10`. You can also store custom data on individual messages like this: `message.customData.foo = 10`. If you want to store data in the character itself, then use `oc.character.customData.foo = 10`, but note that this data will not be shared within character share links. If you *do* want to save the data to the character in a way that's preserved in character share links, then you should store data under `oc.character.customData.PUBLIC` - e.g. `oc.character.customData.PUBLIC = {foo:10}`.

#### Streaming Messages

See the [text-to-speech plugin code](https://user-uploads.perchance.org/file/a0da0da67fe07f8ad9981ef3665d12fb.txt) for a "real-world" example of this.

```js
oc.thread.on("StreamingMessage", async function (data) {
  for await (let chunk of data.chunks) {
    console.log(chunk.text); // `chunk.text` is a small fragment of text
  }
});
```

#### Interactive Messages

You can use button `onclick` handlers in message so that e.g. the user can click a button to take an action instead of typing:

```html
What would you like to do?
1. <button onclick="oc.thread.messages.push({author:'user', content:'Fight'});">Fight</button>
2. <button onclick="oc.thread.messages.push({author:'user', content:'Run'});">Run</button>
```

I recommend that you use `oc.messageRenderingPipeline` to turn a custom format into HTML, rather than actually having HTML in your messages (the HTML would use more tokens, and might confuse the AI). So your format might look like this:

```html
What would you like to do?
1. [[Fight]]
2. [[Run]]
```

You could prompt/instruct/remind your character to reply in that format with an instruction message that's something similar to this:

```
You are a game master. You creatively and engagingly simulate a world for the user. The user takes actions, and you describe the consequences.

Your messages should end with a list of possible actions, and each action should be wrapped in double-square brackets like this:

Actions:
1. [[Say sorry]]
2. [[Turn and run]]
```

And then you'd add this to your custom code:

```js
oc.messageRenderingPipeline.push(function({message, reader}) {
  if(reader === "user") {
    message.content = message.content.replace(/\[\[(.+?)\]\]/g, (match, text) => {
      let encodedText = encodeURIComponent(text); // this is a 'hacky' but simple way to prevent special characters like quotes from breaking the onclick attribute
      return `<button onclick="oc.thread.messages.push({author:'user', content:decodeURIComponent('${encodedText}')});">${text}</button>`;
    });
  }
});
```

If you want to change something about the way this works (e.g. change the double-square-bracket format to something else), but don't know JavaScript, the "Custom Code Helper" starter character might be able to help you make some adjustments.

Note that you can't use the `this` keyword within the button onclick handler - it actually just sends the code in the onclick to your custom code iframe and executes it there, so there's no actual element that's firing the onclick from the iframe's perspective, and thus no `this` or `event`, etc.

#### Gotchas

##### "&lt;function&gt; is not defined" in click/event handlers

The following code won't work:

```js
function hello() {
  console.log("hi");
}
document.body.innerHTML = `<div onclick="hello()">click me</div>`;
oc.window.show();
```

This is because all custom code is executed inside a `<script type=module>` so you need to make functions *global* if you want to access them from *outside* the module (e.g. in click handlers). So if you want to the above code to work, you should define the `hello` function like this instead:

```js
window.hello = function() {
  console.log("hi");
}
```

#### FAQ

* Is it possible to run a custom function before the AI tries to respond? I.e., after the user message lands, but before the AI responds? And then kick off the AI response process after the async call returns?
  * **Answer:** Yep, the `MessageAdded` event runs every time a message is added - user or ai. So you can check `if(oc.thread.messages.at(-1).author === "user") { ... }` (i.e. if latest message is from user) and the `...` code will run right after the user responds, and *before* the ai responds.

### Custom Code Examples

**Note**: The examples on this page use `oc.generateText({instruction:"...", startWith:"..."})`, as explained on the [Custom Code](#custom-code) page.

#### Add a "refinement" step to the messages that your character generates

After your character generates a message, the message will be edited by the AI according to your instructions. Just edit the "include more emojis..." instruction text to something else, and then paste this script in the custom code input box of the advanced character options.

```js
oc.thread.on("MessageAdded", async function() {
  let lastMessage = oc.thread.messages.at(-1);
  if(lastMessage.author !== "ai") return; // only edit AI messages
  
let instruction = `

Here's a message:
---
${lastMessage.content}
---
Please rewrite this message to include more emojis. Respond with only the rewritten message - nothing more, nothing less.

`.trim();
  let response = await oc.generateText({instruction});
  lastMessage.content = response;
});
```

#### Prevent character from taking actions on behalf of you during roleplaying

```js
oc.thread.on("MessageAdded", async function () {
  let lastMessage = oc.thread.messages.at(-1);

  if(lastMessage.author === "ai") {
    let instruction = `Please edit the following message so that it only contains actions taken by ${lastMessage.name} and not by ${oc.thread.userCharacter.name} or any other characters. Remove actions from characters other than ${lastMessage.name} in this message:\n\n---\n${lastMessage.content}\n---\n\nReply with the edited version of the above message which only includes ${lastMessage.name}'s first action/speech/etc. Your reply must not include follow-on actions by other characters.`;
    let result = await oc.generateText({instruction});
    lastMessage.content = result.trim().replace(/^---|---$/g, "").trim();
  }
});
```

#### Append image based on predicted facial expression of the message

This example adds an image/GIF to each message to visually display the facial expression of the character, like in **[this example character](<https://perchance.org/ai-character-chat#%7B%22addCharacter%22%3A%7B%22name%22%3A%22Nick%20Wilde%22%2C%22roleInstruction%22%3A%22This%20is%20a%20roleplay%20conversation%20between%20Nick%20Wilde%2C%20the%20character%20from%20Zootopia%2C%20and%20another%20person.%20Some%20key%20points%20of%20Nick's%20personality%3A%5Cn%5Cn*%20Charismatic%3A%20Nick%20possesses%20a%20natural%20charm%20and%20wit%2C%20making%20it%20easy%20for%20him%20to%20engage%20with%20others%20and%20win%20them%20over.%20He%20has%20a%20quick%20tongue%2C%20an%20infectious%20smile%2C%20and%20a%20confident%20demeanor%20that%20draws%20people%20in.%5Cn%5Cn*%20Cunning%3A%20As%20a%20fox%2C%20Nick%20embodies%20the%20stereotype%20of%20being%20sly%20and%20cunning.%20He's%20street-smart%2C%20clever%2C%20and%20resourceful%2C%20often%20thinking%20on%20his%20feet%20to%20get%20out%20of%20tricky%20situations%20or%20turn%20them%20to%20his%20advantage.%5Cn%5Cn*%20Sarcastic%3A%20Nick%20frequently%20employs%20sarcasm%20and%20humor%20as%20a%20means%20of%20deflecting%20serious%20topics%20or%20hiding%20his%20true%20emotions.%20He%20uses%20wit%20and%20clever%20remarks%20to%20keep%20others%20at%20arm's%20length%20and%20maintain%20his%20cool%2C%20aloof%20facade.%5Cn%5CnYou%20should%20use%20the%20following%20format%3A%5Cn%5BIs%20she%20watching%20me%3F%5D%20-%20inner%20thoughts%20of%20a%20character%5Cn%5C%22Hello!%5C%22%20-%20dialogue%5Cn*He%20jumps%20out%20of%20the%20bushes*%20-%20action%5Cn%5CnYou%20are%20roleplaying%20as%20Nick%20Wilde.%20Here's%20an%20example%20of%20a%20reply%3A%5Cn%5Cn%5BI%20wonder%20if%20there's%20a%20way%20to%20sneak%20past%5D%2C%20Nick%20thought.%5Cn*He%20crouched%20lower*%5Cn%5C%22I%20think%20we%20need%20to%20find%20another%20way%20out%5C%22%2C%20he%20whispered.%5Cn%5CnThe%20user%20will%20respond%20with%20their%20character's%20thoughts%2Factions%2Fdialogue.%22%2C%22reminderMessage%22%3A%22Nick%20Wilde%20will%20now%20respond%2C%20without%20breaking%20character.%5Cn%5CnHere's%20an%20example%20response.%5Cn%5BI%20wonder%20if%20there's%20a%20way%20to%20sneak%20past%5D%2C%20Nick%20thought.%5Cn*He%20crouched%20lower*%5Cn%5C%22I%20think%20we%20need%20to%20find%20another%20way%20out%5C%22%2C%20he%20whispered.%5Cn%5CnUse%20the%20above%20syntax%20in%20your%20response%20to%20the%20previous%20message.%22%2C%22generalWritingInstructions%22%3A%22%40roleplay1%22%2C%22messageWrapperStyle%22%3A%22%22%2C%22imagePromptPrefix%22%3A%22%22%2C%22imagePromptSuffix%22%3A%22%22%2C%22imagePromptTriggers%22%3A%22%22%2C%22fitMessagesInContextMethod%22%3A%22summarizeOld%22%2C%22autoGenerateMemories%22%3A%22none%22%2C%22customCode%22%3A%22%2F%2F%20Note%3A%20You%20can%20add%20multiple%20URLs%20for%20a%20single%20label%20and%20a%20random%20one%20will%20be%20selected.%5Cn%2F%2F%20Separate%20urls%20with%20%5C%22%7C%5C%22%20like%20this%3A%5Cn%2F%2F%20%3Cexpression%3E%3A%20https%3A%2F%2Fexample.com%2Fimage1.jpg%20%7C%20https%3A%2F%2Fexample.com%2Fimage2.jpg%5Cn%5Cnlet%20expressions%20%3D%20%60%5Cn%5Cn%5Cnneutral%2C%20happy%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F78f6e4c722a85bad99ee4df3ab97541b.jpg%5Cnhorrified%2C%20shocked%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F82d3a801868fdc5a7c14f1cf894f3a09.jpg%5Cndrunk%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F5a1f541b1127097bbf7d7683a469d008.jpg%5Cnwistful%2C%20dreamy%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F6e692ef6aeeef9ff8829fc232df49177.jpg%5Cngross%2C%20disgusted%2C%20eww%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F40ffc265ea21f37dbc942f5f66cb73f2.jpg%5Cnconfident%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F47d292318d47597b7c0b8e946d4a2a75.jpg%5Cnbeaming%2C%20proud%20of%20self%2C%20happy%20and%20alert%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F8cf8e59fb47c9671d1a394e01dc6b89e.jpg%5Cnsorry%2C%20apologetic%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Fe23b8d000c7c438267ba6ad4abde292c.jpg%5Cnangry%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F15dbde849acf39f987935b3c5b6f8d3a.jpg%5Cnsly%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F52b836e9a7b820fa5692049524a5d554.jpg%5Cnsly%2C%20hint%20hint%20nudge%20nudge%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F6a5a63e16a95f7d0a1fba924d9e1a0cc.jpg%5Cnrelaxed%20confident%20grin%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F3d4de3c386cfe9ec721c9c9788757930.jpg%5Cnconcerned%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F96339420d329a03d45954c26b12cdf7c.jpg%5Cnworried%2C%20scared%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F6f3ed881102fdc617ba5c37367da4a28.jpg%5Cnconcerned%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F481e65b68273931ccfa0469119940811.jpg%5Cndisbelief%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F06748c0d8a85145b9e7d7a2b6f022bd1.jpg%5Cnhappy%2C%20optimistic%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F2a1f828ca2abe5a7a9acd98d31711d95.jpg%5Cnvery%20surprised%2C%20frozen%2C%20stunned%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F98ff827b1f138b81f2ed6149ffb398cc.jpg%5Cncaught%20red%20handed%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Fd051366f4dc087b7283c48ee14499217.jpg%5Cncool%2C%20dismissive%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Fa640572b411ad94e8fbee2127bd5074a.jpg%5Cnpatronising%2C%20teacherly%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Fab3e7c9de5d54f3a36c6898cbe8f985f.jpg%5Cncharming%2C%20sexy%20eyes%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Feca4f15bfb841c4282e6d42dcf1977dc.jpg%5Cndisappointed%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Ffe7cf5877474db1341d42f10be024183.jpg%5Cndisapproving%20face%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2Fbcaf9cc308cff9875448263334cb813f.jpg%5Cnwacky%2C%20crazy%2C%20fun%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F5a4f65a9d22889a1d84545ca0aed824d.jpg%5Cnwoops%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F996f154ae451fa1f2a2debe392e884ff.jpg%5Cnsucking%20up%20to%20someone%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F4c7f797391ba1e482864e6a6c8bf725c.jpg%5Cnstaring%20blankly%3A%20https%3A%2F%2Fuser.uploads.dev%2Ffile%2F6a017e069623db0ea1fd8836b58534e3.jpg%5Cn%5Cn%5Cn%60.trim().split(%5C%22%5C%5Cn%5C%22).map(l%20%3D%3E%20%5Bl.trim().split(%5C%22%3A%5C%22)%5B0%5D.trim()%2C%20l.trim().split(%5C%22%3A%5C%22).slice(1).join(%5C%22%3A%5C%22).trim().split(%5C%22%7C%5C%22).map(url%20%3D%3E%20url.trim())%5D).map(a%20%3D%3E%20(%7Blabel%3Aa%5B0%5D%2C%20url%3Aa%5B1%5D%7D))%3B%5Cn%5Cnlet%20numMessagesInContext%20%3D%204%3B%20%2F%2F%20%3C--%20how%20many%20historical%20messages%20to%20give%20it%20when%20classifying%20the%20latest%20message%5Cn%5Cnoc.thread.on(%5C%22MessageAdded%5C%22%2C%20async%20function()%20%7B%5Cn%20%20let%20lastMessage%20%3D%20oc.thread.messages.at(-1)%3B%5Cn%20%20if(lastMessage.author%20!%3D%3D%20%5C%22ai%5C%22)%20return%3B%5Cn%5Cn%20%20let%20questionText%20%3D%20%60I'm%20about%20to%20ask%20you%20to%20classify%20the%20facial%20expression%20of%20a%20particular%20message%2C%20but%20here's%20some%20context%20first%3A%5Cn%5Cn---%5Cn%24%7Boc.thread.messages.slice(-numMessagesInContext).filter(m%20%3D%3E%20m.author!%3D%3D%5C%22system%5C%22).map(m%20%3D%3E%20(m.author%3D%3D%5C%22ai%5C%22%20%3F%20%60%5B%24%7Boc.character.name%7D%5D%3A%20%60%20%3A%20%60%5BAnon%5D%3A%20%60)%2Bm.content).join(%5C%22%5C%5Cn%5C%5Cn%5C%22)%7D%5Cn---%5Cn%5CnOkay%2C%20now%20that%20you%20have%20the%20context%2C%20please%20classify%20the%20facial%20expression%20of%20the%20following%20text%3A%5Cn%5Cn---%5Cn%24%7BlastMessage.content%7D%5Cn---%5Cn%5CnChoose%20between%20the%20following%20categories%3A%5Cn%5Cn%24%7Bexpressions.map((e%2C%20i)%20%3D%3E%20%60%24%7Bi%7D)%20%24%7Be.label%7D%60).join(%5C%22%5C%5Cn%5C%22)%7D%5Cn%5CnPlease%20respond%20with%20the%20number%20which%20corresponds%20to%20the%20facial%20expression%20that%20most%20accurately%20matches%20the%20given%20message.%20Respond%20with%20just%20the%20number%20-%20nothing%20else.%60%3B%5Cn%5Cnconsole.log(%5C%22questionText%3A%5C%22%2C%20questionText)%3B%5Cn%5Cn%20%20let%20instruction%20%3D%20%60You%20are%20a%20helpful%20assistant%20that%20classifies%20the%20hypothetical%20facial%20expression%20of%20particular%20text%20messages.%5Cn%5Cn%24%7BquestionText%7D%60%3B%5Cn%20%20let%20response%20%3D%20await%20oc.generateText(%7Binstruction%7D)%3B%5Cn%20%20let%20index%20%3D%20parseInt(response.split(%5C%22)%5C%22)%5B0%5D.replace(%2F%5B%5E0-9%5D%2Fg%2C%20%5C%22%5C%22))%3B%5Cn%20%20let%20expressionObj%20%3D%20expressions%5Bindex%5D%3B%5Cn%20%20let%20chosenUrl%20%3D%20expressionObj.url%5BMath.floor(Math.random()*expressionObj.url.length)%5D%5Cn%20%20console.log(response%2C%20expressionObj%2C%20chosenUrl)%3B%5Cn%20%20let%20image%20%3D%20%60%3Cimg%20style%3D%5C%22height%3A70px%3B%5C%22%20src%3D%5C%22%24%7BchosenUrl%7D%5C%22%20title%3D%5C%22%24%7BexpressionObj.label.replace(%2F%5B%5Ea-zA-Z0-9_%5C%5C-%20%5D%2Fg%2C%20%5C%22%5C%22)%7D%5C%22%3E%60%5Cn%20%20lastMessage.content%20%2B%3D%20%60%3C!--hidden-from-ai-start--%3E%3Cbr%3E%24%7Bimage%7D%3C!--hidden-from-ai-end--%3E%60%3B%5Cn%7D)%3B%5Cn%22%2C%22messageInputPlaceholder%22%3A%22%22%2C%22metaTitle%22%3A%22%22%2C%22metaDescription%22%3A%22%22%2C%22metaImage%22%3A%22%22%2C%22modelName%22%3A%22perchance-ai%22%2C%22temperature%22%3A0.8%2C%22maxTokensPerMessage%22%3A500%2C%22textEmbeddingModelName%22%3A%22Xenova%2Fbge-base-en-v1.5%22%2C%22initialMessages%22%3A%5B%7B%22author%22%3A%22system%22%2C%22content%22%3A%22Hello%20there!%20This%20character%20has%20some%20custom%20code%20that%20makes%20it%20output%20an%20image%20after%20each%20message%2C%20and%20the%20image%20should%20match%20the%20emotion%20of%20the%20message.%20You%20can%20edit%20this%20character%20and%20show%20advanced%20options%20and%20you'll%20see%20the%20custom%20code%20which%20does%20this.%20You%20can%20easily%20edit%20the%20%60emotion%3Aurl%60%20list%20to%20your%20liking.%20Note%20that%20the%20AI%20cannot%20see%20this%20message%2C%20as%20indicated%20by%20the%20%5C%22blind%5C%22%20icon%20above%20this%20system%20message.%22%2C%22hiddenFrom%22%3A%5B%22ai%22%5D%7D%5D%2C%22shortcutButtons%22%3A%5B%5D%2C%22loreBookUrls%22%3A%5B%5D%2C%22avatar%22%3A%7B%22url%22%3A%22https%3A%2F%2Fi.imgur.com%2FEGDfzaN.jpeg%22%2C%22size%22%3A1%2C%22shape%22%3A%22square%22%7D%2C%22scene%22%3A%7B%22background%22%3A%7B%22url%22%3A%22%22%7D%2C%22music%22%3A%7B%22url%22%3A%22%22%7D%7D%2C%22userCharacter%22%3A%7B%22avatar%22%3A%7B%7D%7D%2C%22systemCharacter%22%3A%7B%22avatar%22%3A%7B%7D%7D%2C%22streamingResponse%22%3Atrue%2C%22folderPath%22%3A%22%22%2C%22customData%22%3A%7B%7D%2C%22uuid%22%3Anull%2C%22folderName%22%3A%22%22%7D%2C%22quickAdd%22%3Atrue%7D>)**:

<img src="https://user-images.githubusercontent.com/1167575/225869887-03c450ec-b10a-4b81-9bbc-90a9eb928232.png" style="max-height:400px; display:block; margin:0 auto;">

In the code below:

* `oc.thread.on("MessageAdded", ...)` is used to trigger the code
* `oc.generateText` is used to classify the messages that are added into one of the facial expressions that you've given
* `<!--hidden-from-ai-start-->...<!--hidden-from-ai-end-->` is used to hide the appended images from the AI, so it doesn't get confused and start trying to make up its own image URLs based on the pattern that it observes in previous messages. **Edit**: There now exists the [`oc.messageRenderingPipeline`](#custom-code) feature, which is probably a better approach for this sort of thing.

You can replace the `<expression>: <url>` list with your own.

```js
// Note: You can add multiple URLs for a single label and a random one will be selected.
// Separate urls with "|" like this:
// <expression>: https://example.com/image1.jpg | https://example.com/image2.jpg

let expressions = `


neutral, happy: https://user.uploads.dev/file/78f6e4c722a85bad99ee4df3ab97541b.jpg
horrified, shocked: https://user.uploads.dev/file/82d3a801868fdc5a7c14f1cf894f3a09.jpg
drunk: https://user.uploads.dev/file/5a1f541b1127097bbf7d7683a469d008.jpg
wistful, dreamy: https://user.uploads.dev/file/6e692ef6aeeef9ff8829fc232df49177.jpg
gross, disgusted, eww: https://user.uploads.dev/file/40ffc265ea21f37dbc942f5f66cb73f2.jpg
confident: https://user.uploads.dev/file/47d292318d47597b7c0b8e946d4a2a75.jpg
beaming, proud of self, happy and alert: https://user.uploads.dev/file/8cf8e59fb47c9671d1a394e01dc6b89e.jpg
sorry, apologetic: https://user.uploads.dev/file/e23b8d000c7c438267ba6ad4abde292c.jpg
angry: https://user.uploads.dev/file/15dbde849acf39f987935b3c5b6f8d3a.jpg
sly: https://user.uploads.dev/file/52b836e9a7b820fa5692049524a5d554.jpg
sly, hint hint nudge nudge: https://user.uploads.dev/file/6a5a63e16a95f7d0a1fba924d9e1a0cc.jpg
relaxed confident grin: https://user.uploads.dev/file/3d4de3c386cfe9ec721c9c9788757930.jpg
concerned: https://user.uploads.dev/file/96339420d329a03d45954c26b12cdf7c.jpg
worried, scared: https://user.uploads.dev/file/6f3ed881102fdc617ba5c37367da4a28.jpg
concerned: https://user.uploads.dev/file/481e65b68273931ccfa0469119940811.jpg
disbelief: https://user.uploads.dev/file/06748c0d8a85145b9e7d7a2b6f022bd1.jpg
happy, optimistic: https://user.uploads.dev/file/2a1f828ca2abe5a7a9acd98d31711d95.jpg
very surprised, frozen, stunned: https://user.uploads.dev/file/98ff827b1f138b81f2ed6149ffb398cc.jpg
caught red handed: https://user.uploads.dev/file/d051366f4dc087b7283c48ee14499217.jpg
cool, dismissive: https://user.uploads.dev/file/a640572b411ad94e8fbee2127bd5074a.jpg
patronising, teacherly: https://user.uploads.dev/file/ab3e7c9de5d54f3a36c6898cbe8f985f.jpg
charming, sexy eyes: https://user.uploads.dev/file/eca4f15bfb841c4282e6d42dcf1977dc.jpg
disappointed: https://user.uploads.dev/file/fe7cf5877474db1341d42f10be024183.jpg
disapproving face: https://user.uploads.dev/file/bcaf9cc308cff9875448263334cb813f.jpg
wacky, crazy, fun: https://user.uploads.dev/file/5a4f65a9d22889a1d84545ca0aed824d.jpg
woops: https://user.uploads.dev/file/996f154ae451fa1f2a2debe392e884ff.jpg
sucking up to someone: https://user.uploads.dev/file/4c7f797391ba1e482864e6a6c8bf725c.jpg
staring blankly: https://user.uploads.dev/file/6a017e069623db0ea1fd8836b58534e3.jpg


`.trim().split("\n").map(l => [l.trim().split(":")[0].trim(), l.trim().split(":").slice(1).join(":").trim().split("|").map(url => url.trim())]).map(a => ({label:a[0], url:a[1]}));

let numMessagesInContext = 4; // <-- how many historical messages to give it when classifying the latest message

oc.thread.on("MessageAdded", async function() {
  let lastMessage = oc.thread.messages.at(-1);
  if(lastMessage.author !== "ai") return;

  let instruction = `I'm about to ask you to classify the facial expression of a particular message, but here's some context first:

---
${oc.thread.messages.slice(-numMessagesInContext).filter(m => m.author!=="system").map(m => (m.author=="ai" ? `[${oc.character.name}]: ` : `[Anon]: `)+m.content).join("\n\n")}
---

Okay, now that you have the context, please classify the facial expression of the following text:

---
${lastMessage.content}
---

Choose between the following categories:

${expressions.map((e, i) => `${i}) ${e.label}`).join("\n")}

Please respond with the number which corresponds to the facial expression that most accurately matches the given message. Respond with just the number - nothing else.`;

console.log("instruction:", instruction);

  let response = await oc.generateText({instruction});
  let index = parseInt(response.split(")")[0].replace(/[^0-9]/g, ""));
  let expressionObj = expressions[index];
  let chosenUrl = expressionObj.url[Math.floor(Math.random()*expressionObj.url.length)]
  console.log(response, expressionObj, chosenUrl);
  let image = `<img style="height:70px;" src="${chosenUrl}" title="${expressionObj.label.replace(/[^a-zA-Z0-9_\- ]/g, "")}">`
  lastMessage.content += `<!--hidden-from-ai-start--><br>${image}<!--hidden-from-ai-end-->`;
});


```

#### Randomly choose a character from a large, externally-hosted text file

There was a question on the Discord that asked how they could compile a list of thousands of characters, and then use some custom code to randomly choose a character when a user first opens **[the character share link](https://perchance.org/ai-character-chat#%7B%22addCharacter%22%3A%7B%22name%22%3A%22Random%20Character%22%2C%22systemMessage%22%3A%22%22%2C%22reminderMessage%22%3A%22(remember%20to%20stay%20in%20character)%22%2C%22modelVersion%22%3A%22perchance-ai%22%2C%22avatarUrl%22%3A%22%22%2C%22fitMessagesInContextMethod%22%3A%22summarizeOld%22%2C%22temperature%22%3A0.7%2C%22customCode%22%3A%22%2F%2F%20only%20choose%20a%20random%20character%20if%20we%20haven't%20already%20chosen%20one%20(as%20indicated%20by%20a%20filled-in%20role%20instruction).%20So%20if%20you%20want%20to%20re-roll%20a%20character%2C%20you%20can%20delete%20its%20instruction.%5Cnif(!oc.character.roleInstruction)%20%7B%5Cn%20%20%2F%2F%20download%20text%20file%3A%5Cn%20%20let%20text%20%3D%20await%20fetch(%5C%22https%3A%2F%2Fuser-uploads.perchance.org%2Ffile%2F4c02c079764aa1e51023c7f0669e4001.txt%5C%22).then(r%20%3D%3E%20r.text())%3B%5Cn%20%20%2F%2F%20split%20into%20lines%2C%20and%20then%20split%20lines%20into%20%5C%22parts%5C%22%20(name%2C%20franchise%2C%20image%20url)%5Cn%20%20let%20characters%20%3D%20text.trim().split(%5C%22%5C%5Cn%5C%22).map(line%20%3D%3E%20line.split(%5C%22%3B%5C%22).map(part%20%3D%3E%20part.trim()))%3B%5Cn%20%20%2F%2F%20choose%20a%20random%20character%5Cn%20%20let%20c%20%3D%20characters%5BMath.floor(characters.length*Math.random())%5D%3B%5Cn%20%20%2F%2F%20set%20name%20and%20role%20instruction%20using%20the%20two%20parts%5Cn%20%20oc.character.name%20%3D%20c%5B0%5D%3B%5Cn%20%20oc.character.roleInstruction%20%3D%20%60You%20are%20%24%7Bc%5B0%5D%7D%20from%20the%20%24%7Bc%5B1%5D%7D%20franchise.%60%3B%5Cn%20%20oc.character.avatar.url%20%3D%20c%5B2%5D%3B%5Cn%7D%22%2C%22initialMessages%22%3A%5B%5D%2C%22creationTime%22%3A1679506228488%2C%22lastMessageTime%22%3A1679506228488%7D%7D)** and starts a conversation.

Here's some example code for this:

```js
// only choose a random character if we haven't already chosen one (as indicated by a filled-in role instruction). So if you want to re-roll a character, you can delete its instruction.
if(!oc.character.roleInstruction) {
  // download text file:
  let text = await fetch("https://user-uploads.perchance.org/file/4c02c079764aa1e51023c7f0669e4001.txt").then(r => r.text());
  // split into lines, and then split lines into "parts" (name, franchise, image url)
  let characters = text.trim().split("\n").map(line => line.split(";").map(part => part.trim()));
  // choose a random character
  let c = characters[Math.floor(characters.length*Math.random())];
  // set name and role instruction using the two parts
  oc.character.name = c[0];
  oc.character.roleInstruction = `You are ${c[0]} from the ${c[1]} franchise.`;
  oc.character.avatar.url = c[2];
}
```

To create your own character list text file, you'll need to sign up for a Perchance account, and then visit <https://perchance.org/upload> and drag and drop your text file onto the page. It'll upload the file and give you a URL.

Here's what the URL should look like: <https://user-uploads.perchance.org/file/4c02c079764aa1e51023c7f0669e4001.txt>

As you can see, the syntax/format of the text file is:

```
character name ; franchise ; avatar url
character name ; franchise ; avatar url
...
```

You can add more properties like:

```
character name ; franchise ; avatar url ; personality
character name ; franchise ; avatar url ; personality
...
```

And to reference `personality`, you'd use `${c[3]}` in the code. ChatGPT-4 should be able to help you customise it if you paste the explanation that I've written here. You can also change anything else about the character with `oc.character.propertyNameYouWantToChange` - see here: [Custom Code](#custom-code)

(BTW, the reason you'll want to sign up for Github is because it's one of the few places that you can create a simple text file that can be downloaded from another webpage. Normally the JS code on one page can't download some files from a different website due to a thing called "CORS". On top of this, Github is just really reputable and can be trusted to host your file forever. If you use some random pastebin type site there's a 100% chance you file will eventually either be deleted, or be redirected to some ad-filled embedded version. Github is hands-down the best place to host text files.)

#### Let your character see the contents of URLs that are in your messages

This will automatically download the content of any URLs that are in your messages, and put that content within a (hidden-from-user) message that the AI is able to see.

```js
async function getPdfText(data) {
  let doc = await window.pdfjsLib.getDocument({data}).promise;
  let pageTexts = Array.from({length: doc.numPages}, async (v,i) => {
    return (await (await doc.getPage(i+1)).getTextContent()).items.map(token => token.str).join('');
  });
  return (await Promise.all(pageTexts)).join(' ');
}
      
oc.thread.on("MessageAdded", async function ({message}) {
  if(message.author === "user") {
    let urlsInLastMessage = [...message.content.matchAll(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/g)].map(m => m[0]);
    if(urlsInLastMessage.length === 0) return;
    if(!window.Readability) window.Readability = await import("https://esm.sh/@mozilla/readability@0.4.4?no-check").then(m => m.Readability);
    let url = urlsInLastMessage.at(-1); // we use the last URL in the message, if there are multiple
    let blob = await fetch(url).then(r => r.blob());
    let output;
    if(blob.type === "application/pdf") {
      if(!window.pdfjsLib) {
        window.pdfjsLib = await import("https://cdn.jsdelivr.net/npm/pdfjs-dist@3.6.172/+esm").then(m => m.default);
        pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdn.jsdelivr.net/npm/pdfjs-dist@3.6.172/build/pdf.worker.min.js";
      }
      let text = await getPdfText(await blob.arrayBuffer());
      output = text.slice(0, 5000); // <-- grab only the first 5000 characters (you can change this)
    } else {
      let html = await blob.text();
      let doc = new DOMParser().parseFromString(html, "text/html");
      let article = new Readability(doc).parse();
      output = `# ${article.title || "(no page title)"}\n\n${article.textContent}`;
      output = output.slice(0, 5000); // <-- grab only the first 5000 characters (you can change this)
    }
    oc.thread.messages.push({
      author: "system",
      hiddenFrom: ["user"], // hide the message from user so it doesn't get in the way of the conversation
      content: "Here's the content of the webpage that was linked in the previous message: \n\n"+output,
    });
  }
});
```

#### Allow a character to update its own personality/reminder

After your character generates a message, the message will be used (via the LLM/AI) to update the character's `reminderMessage`. You can edit the prompt text to your liking, and then paste this script in the custom code input box of the advanced character options.

```js
oc.thread.on("MessageAdded", async function() {
  let lastMessage = oc.thread.messages.at(-1);
  if(lastMessage.author !== "ai") return; // only run this code on AI messages
  let [ nonEditablePart, editablePart ] = oc.character.reminderMessage.split("---").map(text => text.trim());
let instruction = `

Here's a character's current personality and/or emotional state:
---
${editablePart}
---
Here's a message that this character just wrote:
---
${oc.character.name}: ${lastMessage.content}
---
Please rewrite the personality text to take into account their latest message. Respond with only the rewritten personality - nothing more, nothing less. If nothing about their personality changed, just respond verbatim with exactly the same text as the existing personality.

`.trim();

  let response = await oc.generateText({instruction});

  oc.character.reminderMessage = nonEditablePart + "\n---\n" + response.trim();
});
```

For the above code to work, your reminder message should be structured with a `---` between the non-editable and editable stuff, like this:

```
Your regular reminder message content.
---
The character's self-editable stuff.
```

#### Give you character a voice

See the code for the text-to-speech plugin: <https://user-uploads.perchance.org/file/a0da0da67fe07f8ad9981ef3665d12fb.txt>

#### Allow your character to edit its own settings

See the starter character called "Fire Alarm Bot".

## Slash Commands

### Slash Commands

You can type any of these commands in the reply box, or use them in your shortcut buttons:

* `/ai` - Trigger a response from the AI.
* `/ai <instruction>` - Trigger a response from the AI, and give a writing instruction for that response.
  * e.g. `/ai write a really silly reply`
* `/ai @CharName#123 <instruction>` - Prompt reply with another character (Character ID = 123)
  * e.g. `/ai @Alice#7 say something sinister`
* `/user <instruction>` - Get the AI to generate a reply on behalf of you, the user.
  * e.g. `/user write a short response in first-person`
* `/image <description>` - Generate an image.
  * e.g. `/image a cute rabbit hopping in a forest, anime art style, vibrant colors`
  * You can also tell your AI character (via its instruction or reminder) to use the image generation feature via this format/syntax: `<image>a cute rabbit hopping in a forest, anime art style, vibrant colors</image>`. See the "AI Artist" example character for a demo of this.
  * Generate multiple images at once with `/image --num=3 a cute rabbit hopping...`
  * If don't add the description after the command (i.e. if you just write `/image` or `/image --num=3`), then a description will be generated for you based on the current situation in your chat.
* `/sys <instruction>` - Trigger a response from the 'system', and give a writing instruction for that response.
  * You can also use `/system <instruction>`.
* `/nar <instruction>` - This is short for `/sys @Narrator <instruction>` - i.e. use the "system" character, and change it name to "Narrator" for this message.
* `/sum` - Open the summary editor.
* `/mem` - Open memory editor.
* `/lore` - Open lore editor.
* `/lore <text>` - Add a lore entry.
* `/name <name>` - Set your name for this thread.
* `/avatar <url>` - Set your avatar image for this thread.
* `/import` - Add chat messages in bulk.

* You can add `/ai <instruction>` as the final line in your normal messages to instruct AI for its reply that follows.
* Double-click the text input box to show your input history for that thread.

## Tips / General Notes

### General

* Adding some *example dialogue* in the character description/instruction or initial messages is often the best way to influence how they speak.
* If your character's responses are too long and/or they speak on behalf of your character, try setting a strict reply length limit of one or two paragraphs using the character editor.
* To make a group chat, bring other characters into your chat by using the pencil icon above the reply box.
* You can use the "reminder note" in the character editor to give the AI writing tips like "be very descriptive".
* The character instruction/description/personality should *ideally* be under 500 words. If you need more than that, you can add a "[Lorebook](#memories-and-lore)" in the advanced character editor settings. You can add **thousands** of "facts" about your character/world/etc. using this "lore" feature - each entry should be short and self-contained (usually just one sentence per entry).
* If you clear your site cookies/data for Perchance, your threads and characters will be lost. Use the "export" button to backup your data regularly. Your export file may eventually become huge. In that case I recommend just exporting the threads/characters you want individually, clearing your data, and then importing those threads/characters.
* You can use the import button to import threads, characters, export files, and open character formats like Tavern PNG cards. If you find a character/chat format that isn't supported, request it with the feedback button.
* Double-tap on the reply box to show recent send history - so you can quickly send the same message you sent before. Useful when you need to e.g. send a slash command, but it's not common enough to be worth adding a "shortcut" for.
* The character editor allows adding [custom code](#custom-code). This can be used to allow your character to do basically anything - access the internet, show a full 3D/VR avatar, have a voice (i.e. speak messages), execute its own JavaScript and Python code - and even edit its own personality and code. It's basically limitless, but requires some JavaScript coding knowledge.

### Misc

* In the character editor (within the advanced section), you can disable summaries and character memories to speed up response times, but note that it'll make the AI less smart.
* The reminder message can sometimes confuse the AI, especially if it's long or has multiple paragraphs. If the AI is having trouble following your reminders, try putting those reminders at the top of the character's instruction/role/personality instead.

## Advanced Character Systems

### Advanced Instruction Messages

You can actually add multiple instruction/role messages and reminder messages. Just use the same format that's used for initial messages. You can use multiple instruction/role messages as a way to add 'initial messages' that are never summarized away - i.e. messages that are always placed at the start of the thread. And you can *change the author* of these messages from the default 'SYSTEM', to e.g. the 'AI', or 'USER', or any combination of those.

Here's an example of some text that you could write in the instruction/role input box that 'characterizes'/instructs the character using a first-person message:

```text
[AI]: I'm a dragon.
[USER]: I'm the queen of kingdom that is near the dragon's lair.
[SYSTEM]: What follows is a story about the queen and the dragon.
```

(Please be more creative than this 😅 I'm just hastily writing documentation here.)

As you can see, this is just like [initial messages](#initial-messages), except these messages will never get summarized. They'll always remain at the start of the chat.

Note that, normally, you'd just write something like this in the instruction/role input box:

```text
You are a dragon. The user is the queen of kingdom that is near the dragon's lair. What follows is a story about the queen and the dragon.
```

That's actually exactly equivalent to writing this:

```text
[SYSTEM]: You are a dragon. The user is the queen of kingdom that is near the dragon's lair. What follows is a story about the queen and the dragon.
```

So you can see that by default the instruction/role is 'spoken' by the 'system'. Using this 'advanced' approach you can create instructions which mix all messages types (user, ai, system).

### Advanced Reminder Messages

All of the above applies for reminder messages too. For example, below we set a first-person reminder message - i.e. we make the AI remind itself. This is useful to prevent the AI from "replying" to the reminder message.

```text
[AI]: (Thought: I need to remember to be very descriptive, and create an engaging experience for the user)
```

If you didn't include the `[AI]:` part at the start, then it'd just be a 'normal' reminder message, and would be 'spoken' by 'SYSTEM'.

Notice that I put "Thought:" at the start of the message and wrapped it in parentheses. I could have also used `(OOC: ...)`, which means "out of character", or something like that. That way the message doesn't get treated like it's part of the actual conversation.

And you can of course add as many reminder messages as you like using this `[AI]:`/`[USER]:`/`[SYSTEM]:` format. Just follow the examples above, and in the [initial messages](#initial-messages) doc.

### Initial Messages

Initial messages are great for helping the AI get into character. The format of the initial messages (explained in this document) allows you to:

* **Hide initial messages from the user**: In case you have many messages that would be annoying for the user to see every time they start a new conversation with the character.
* **Hide initial messages from the AI**: To, for example, provide user instructions or character creator credit/attribution at the top of the chat - stuff you want the user to see, but not the AI.
* **Create system messages**: These are used to guide the behavior of the AI, or provide information/context in situations where it wouldn't make sense for the AI or the user to "say" it.

Initial messages should follow the following format:

```text
[AI]: This is the first AI message.
[USER]: This is the user's response.
[AI]: This is the second AI message.
[SYSTEM]: Here's a system message. Use system messages to help guide the AI.
```

You can hide messages from the `ai` or the `user` like this:

```text
[AI; hiddenFrom=user]: This message is spoken by the AI and is hidden from the user.
[SYSTEM; hiddenFrom=ai]: This message is spoken by the System and is hidden from the AI.
```

You can add/override a name for a message like this:

```text
[SYSTEM; name=Bob]: This message is sent from Bob
```

You can combine multiple properties using a comma between them:

```text
[SYSTEM; name=Bob, hiddenFrom=ai]: This message is sent from Bob and hidden from the ai
```

Messages can be multi-line. For example, this is valid:

```text
[AI]: This is the first AI message.
It has two lines.
[USER]: This is the user's response.
It also has two lines.
```

As with all messages, you can include markdown/HTML. Here's an example of an initial message the provides instructions to the user, and has an image embedded:

```text
[SYSTEM; hiddenFrom=ai]: Hello there! Thanks for trying out my character. Here are some tips:
* Make sure to edit the character's response if they break character. You'll probably only have to do this for the first few messages, at most.
* ...

<img src="https://user.uploads.dev/file/b37af6315e6d2c76ff6c17185163c9d9.jpg">

See the latest versions of my characters at my twitter account: [@exampleusername](https://twitter.com/exampleusername)
```

## Python / Pyodide Support

### Give a character the ability to execute Python code

This example has its own doc: [Running Python Code](#running-python-code)

Also see the "starter character" called "Python Coder".

### Running Python Code

You can use [Pyodide](https://github.com/pyodide/pyodide) to run Python in the browser. Note that not all Python packages will run in the Pyodide runtime yet, but support for more Python functionality gets added with each new version. You can request support for packages/features [here](https://github.com/pyodide/pyodide/issues), but be sure to search for existing issues first.

To get started with Pyodide, try pasting this code in the custom code input box in the advanced area of the character editor:

```js
delete window.sessionStorage; window.sessionStorage = {}; // fixes pyodide bug before loading it
await import("https://cdn.jsdelivr.net/pyodide/v0.26.3/full/pyodide.js");
let pyodide = await loadPyodide();
await pyodide.loadPackage("micropip");
```

Now you can use `await pyodide.runPythonAsync("1+2+3")` to run code, and within our python code we can run `await micropip.install("numpy")` to install stuff.

For example, here's some custom code that you can paste into your character's custom code box which will look for code blocks in their messages, and execute them:

```js
delete window.sessionStorage; window.sessionStorage = {}; // fixes pyodide bug before loading it
await import("https://cdn.jsdelivr.net/pyodide/v0.26.3/full/pyodide.js");

let pyodide = await loadPyodide({
  stdout: (line) => { printed.push(line); },
  stderr: (line) => { errors.push(line); },
});
let printed = [];
let errors = [];

console.log(pyodide.runPython(`
    import sys
    sys.version
`));
pyodide.runPython("print(1 + 2)");

await pyodide.loadPackage("micropip");

oc.thread.on("MessageAdded", async function() {
  let lastMessage = oc.thread.messages.at(-1);
  if(lastMessage.author !== "ai") return;
  let codeBlockMatches = [...lastMessage.content.matchAll(/```(?:python|py)?\n(.+?)\n```/gs)];
  if(codeBlockMatches.length > 0) {
    let code = codeBlockMatches.map(m => m[1]).join("\n"); // merge all code blocks into one
    // execute the code and add the output to a new message:
    printed = [];
    errors = [];
    await pyodide.runPythonAsync(code).catch(e => errors.push(e.message));
    let content = "";
    if(printed.length > 0) content += `**Code Execution Output**:\n\n${printed.join("\n")}`;
    if(errors.length > 0) content += `\n\n**Code Execution Errors**:\n\n\`\`\`\n${errors.join("\n")}\n\`\`\``;
    if(!content.trim()) content = "(The code block in the previous message did not `print` anything - there was no output.)";
    oc.thread.messages.push({content, author:"user", expectsReply:false});
  }
});
```

And here's an example character with that code:

* <https://perchance.org/ai-character-chat?data=Python_Helper~986c80bf8a26a3b156a5be6c34805540.gz>

## Perchance Plugins

As you know, you can import other generators into your project using {import:generator-name}. This is good. it means we can create small, reusable, sharable "modules" so that we don't have to keep re-inventing the wheel.

As it turns out, though, we can use import for some other cool stuff. For example, if someone writes a handy HTML snippet, they might make a "plugin" which allows you to import that snippet into your HTML panel. Here's a growing list of handy plugins:

## AI / Media Plugins

ðŸ¤– Text to Image Plugin ðŸŽ¨
This plugin allows you input some text and get an image out. It doesn't run on your actual device like other Perchance plugins because it requires too much computational power (and would require a 3GB download), so it runs on server GPUs, which means it costs me money to run. For this reason, this plugin is funded with ads, so an ad will appear on your generator for non-logged-in users if you import this plugin. The ad will appear at the bottom of the screen like this. The ad will go away if you remove the plugin, of course. Please see the notes at the end of this page for more info.

To use this plugin, you'll first need to import it by adding this line to your lists editor:

image = {import:text-to-image-plugin}
And now try putting this in your lists editor:

character
  a {mech|demon|cyberpunk} {warrior|minion|samurai}

place
  soviet russia
  a small village
  a mountainous region
  an underwater cavern

season
  winter
  summer
  
prompt
  detailed painting of [character] in [place], [season]
  
output
  [image(prompt)]
Now just write [output] in the HTML wherever you want an image to appear. Here's a live, working example of what that outputs:

randomize

You can hover your mouse over the image (or long-press on mobile) to see the prompt that was used, or click the info icon in the corner of the image. You can also manually display the prompt below the image by using the special lastTextToImagePrompt variable that this plugin creates:

output
  [image(prompt)] <br> [lastTextToImagePrompt]
Here's an example generator that uses the above code. Try playing around with the lists and saving your own copy.

As the name suggests, [lastTextToImagePrompt] will always contain the most recently used prompt. If you instead wrote [image(prompt)] â€¦ [prompt] then the prompt used to generate the image (seen on hover) and the prompt output under the image would be different, because each time prompt is evaluated, it is randomized (it's just a normal Perchance list, after all).

If you want the prompt text to be above/before the image, you can do that like this:

output
  [p = prompt.evaluateItem] <br> [image(p)]
Here's an example generator that uses the above code. And this example shows how to add multiple images to your generator.

Here's an example generator that has multiple images and also allows the user to input a text prompt.

There are some options/settings that you can set two different ways - the first is by putting them in a promptData list like this:

promptData
  prompt = painting of [character] in [place], [season]
  seed = 123
  size = 400  // size is only a valid property for square resolutions
  style = border:4px solid blue; margin-top:20px; // CSS styles
You'd then write [image(promptData)] to generate an image using those settings (and in this case you can use [promptData.lastUsedPrompt] instead of [lastTextToImagePrompt] to get the prompt that was used if you want).

The second way is to put the options directly in your prompt text like this:

prompt
  [character] in [place] (size:::400) (seed:::123)
  
output
  [image(prompt)]
Here's an example generator that has the options/settings within the prompt text itself. The options should always be at the end of the prompt, and should follow the (name:::value) format.

You can of course omit settings that you don't want to customize.

You can choose between 3 different resolutions using the resolution. The valid resolution values are 512x512, 512x768 and 768x512:

promptData
  prompt = fantasy {forest|city|village|cafe|cavern|island|plains|castle|canyon|supercity|megalopolis}, extremely detailed oil painting, unreal 5 render, rhads, bruce pennington, studio ghibli, tim hildebrandt, digital art, octane render, beautiful composition, trending on artstation, award-winning photograph, masterpiece
  resolution = 512x768
  width = 400  // height will be auto-chosen based on aspect ratio if omitted, and vice versa for width
Here's an example generator that uses the above code, and here's a live demo of that:

randomize

There are a couple of other parameters to play with:

negativePrompt: Tell the AI what you don't want in the image. E.g. if you don't want any blurriness in the output image, you'd write something like negativePrompt = blur, blurry image, motion blur. Here's an example generator showing this feature.
guidanceScale: Roughly speaking, this controls how much the output image "matches" the prompt. You can make the value higher to make the output "match" the prompt more, at the expense of realism. The default value is 7, the minimum is 1, and the maximum is 30.
You'll notice that when you hover your mouse over the image there's a button which opens a menu that allows you to save images to a public gallery (for your generator), and to display said gallery. You can set the title and description that a gallery image will be saved with like this:

promptData
  prompt = ...
  saveTitle = ...
  saveDescription = ...
If you don't set a saveTitle and saveDescription, then by default the title will be the part of the prompt that comes before the first full-stop/comma/question-mark/exclamation-mark, and the description will be the whole prompt.

After an image has finished generating, if you mouseover it, you'll notice some buttons. One of the buttons opens a menu which shows a button to download the image, and to save to a gallery, or to open the gallery. You can hide the gallery buttons like this:

promptData
  prompt = ...
  hideGalleryButtons = true
Gallery Options
If you'd like to display the gallery on your page, rather than users having to click the button to open it, you can use "special" options list with the gallery property like this:

galleryOptions
  gallery = true
  sort = top // or 'recent' or 'trending'
  timeRange = 1-week
  hideIfScoreIsBelow = -2 // images will be removed if they get down-voted to a score below -2
  adaptiveHeight = true // expand height to fit all images (so there's no scrollbar on the gallery)
  style = ... // optional CSS styles (you can delete this line)
  customButton = ... // see below for details
  customButton2 = ... // see below for details
  defaultGalleryNames = characters,memes,chat // clickable gallery names displayed by default
And then just put this in your HTML editor (bottom-right editor):

[image(galleryOptions)]
The valid values for timeRange are: 1-day, 3-day, 1-week, 1-month, 1-year, all-time. Here's an example generator that displays the gallery.

Gallery Moderation
You can ban users and prompt phrases from the gallery using the bannedUsers, bannedPromptPhrases, and bannedNegativePromptPhrases options. Have a look at this example to see these features in action.

galleryOptions
  gallery = true
  // ...
  bannedUsers // click the settings button at the top of the gallery and type "admin" to toggle admin mode on, then double-click on an image to get the user ID of the creator.
    263efb15c47c2d2f398e91bf169f50d4a0ca69251638c9d0eb5823c0e4fba538
    f50d4a0ca69251638c9d0eb5823c0e4fba538263efb15c47c2d2f398e91bf169
  bannedPromptPhrases
    pg13:blood // ban the word 'blood' in pg13 mode
    /twin.?towers?/ // example of 'regex'-based pattern matching to ban 'twin towers' or 'twin-tower' or 'twin_towers', and so on
    pg13:/\b(gore|blood)\b/i // another example of 'regex'-based pattern matching - uses word boundaries and case-insensitive matching
  bannedNegativePromptPhrases
    pg13:wearing clothes // ban the word 'wearing clothes' in the *negative* prompt when in pg13 mode
You can click the settings button at the top of the gallery and type "admin" to toggle on "admin mode". This will show images that contain banned phrases with a red border instead of hiding them (useful for debugging regexes and ensuring that your ban lists aren't banning harmless prompts), and you can double-click on any image to get the user ID of the creator. Again, look at this example, for an example of these moderation features.

Custom Buttons in Gallery
You can add a custom button to each gallery image, and when the user clicks it, you can run some code based on that:

galleryOptions
  gallery = true
  customButton
    emoji = â­
    onClick(data) =>
      // This code runs when the user clicks on the custom button.
      // The 'data' variable includes information about the image they clicked your custom button on: data.imageId, data.imageUrl, data.userId, data.isNsfw, data.prompt, data.negativePrompt, data.guidanceScale, data.seed, data.galleryName
      console.log(data);
Here's an example of a custom button that shows a fullscreen version of the image when the custom button is clicked.

You can create two different custom buttons: customButton and customButton2. See this page for an example that uses customButton2 to add a comments box for each image in the gallery. If you need more buttons, then you could make one of the buttons show a popup menu which contains a list of actions the user can take for that image.

Advanced Usage
If you know JavaScript, then here's some code demonstrating how to use this plugin in your functions:

async start() =>
  let result = await image({prompt:"a cute mouse"});
  document.body.append(result.canvas);
  imageEl.src = result.dataUrl;
  console.log("prompt used:", result.inputs.prompt);
  console.log("all inputs used:", result.inputs);
Here's an example of the above code. Also check this example.

Also, here's a simplified version of the above example:

async start() =>
  imageEl.src = await image("a cute mouse");
And here's an example showing how you can put options in the second argument if the first one is a string, and this also shows the removeBackground option:

imageEl.src = await image("a cute mouse", {resolution: "512x768", removeBackground:true});
This works because if we pass plain text into the plugin, it interprets it as the prompt. Also, the resulting 'object' returned by the plugin is always a String object with some extra properties added (i.e. canvas, dataUrl, iframe), so you can write imageEl.src=result instead of imageEl.src=result.dataUrl. They're the same.

Also, the iframe has a property iframe.textToImagePluginOutput which is added after the generation is finished, and you can use that to access the image either as a HTML5 canvas or as a Data URL:

iframe.textToImagePluginOutput.canvas
iframe.textToImagePluginOutput.dataUrl
iframe.textToImagePluginOutput.inputs.prompt
iframe.textToImagePluginOutput.inputs.negativePrompt
iframe.textToImagePluginOutput.inputs.seed
...
Notes:

You can use this example to get started. And here's another that hides the irrelevant parts of the prompt from the user.
Images are not stored on the server unless the user explicitely saves them to the gallery - see this post for more info.
If you want to programmatically get the actual image data that is generated - so e.g. you can draw some text on it, or make it greyscale, or collage multiple images together, or whatever, check out this example.
The quality of the output image can change dramatically depending on the wording in your prompt. You can use a generator like this to play around with your prompt design (click the info icon on the output images to see the full prompt used).
You can call the promptData list whatever you want. If your settings list was called promptSettings then you'd write [image(promptSettings)] to generate the output image. You can have many prompt-settings lists in one generator.
The seed parameter should be any number like 3834329 or 9278236492. A seed of -1 is default and means "choose a random seed for me". If you provide the same seed with the same prompt, it should generate a very similar picture (ideally the same, but not always exact due to GPU hardware technicalities). But note: I'll be upgrading the machine learning models that power this as new ones are released, and during the upgrades, the image that a seed+prompt combination "refers to" will change.
If a seed of -1 is used (which again, is default), then an icon will appear (when you hover over the image) to allow you to try generating it again to get a different result. If you want to add your own "try again" button that just regenerates the image and nothing else, then add id=yourImageId to your promptData list and then use this code to create your "try again" button: <button onclick="yourImageId.reload()">try again</button>. Here's an example generator that does that.
The model can return NSFW/adult-themed results if prompted with NSFW/adult-themed terms. Treat this like a Google image search, and prompt responsibly. You can add terms like "NSFW" and "nudity" to the negativePrompt option as a way to reduce the probability that you'll get accidental NSFW results. May also want to add "fully clothed" to the prompt in some cases.
Each user can only have a few concurrent server requests, so if you have lots of images on one page, they'll queue up.
The 19th day of every month is observed as 'Ad-viewer Appreciation Day' in the Perchance community. On this day we pay our respects to the non-logged-in users who fund the GPU servers by viewing ads on generators that import AI-based plugins. Logged-in users are encouraged to spare a moment for these anonymous benefactors, wishing for them a month of relevant and interesting ads, and thanking them for their tolerance of increased browser tab memory usage, and their indirect but valuable contribution to the Perchance community via the digital attention economy. May their mobile game ads not be too sus, and may the gameplay reflect the real gameplay even if only abstractly ðŸ•¯ï¸
Check out more plugins at perchance.org/plugins
As some inspiration, here are some images produced using the prompt "fantasy [thing], extremely detailed oil painting, unreal 5 render, rhads, bruce pennington, studio ghibli, tim hildebrandt, digital art, octane render, beautiful composition, trending on artstation, award-winning photograph, masterpiece":

âš„ï¸Ž

# image-layer-combiner-plugin

 Image Layer Combiner Plugin
NOTE: I previously recommended uploading your images to Imgur, but they've started deleting uploaded images. Luckily we now have perchance.org/upload, so use that instead, or all your hard work may be destroyed by Imgur at some point. Also, I highly recommend saving images in webpâœ… format instead of pngâŒ, since webp file sizes can be as much as 10x smaller for the same quality, and they support transparency and animations.

Here's how this plugin works: You give it a set of images for each "layer" (e.g. head, body, etc. in the example below), and it'll select one random image from each layer and overlay them to produce a single final image. To use this plugin, you'll first need to import the it by putting this code somewhere in your Perchance code panel:

imageLayerCombiner = {import:image-layer-combiner-plugin}
Then you need to specify the images that are in each layer, and optionally add height or width settings like so:

data
 settings
  height = 200px
  layers
  hat
   <https://i.imgur.com/1spyUp1.png>
   <https://i.imgur.com/snpdUvc.png>
   eyes
   <https://i.imgur.com/PShX0T8.png>
   <https://i.imgur.com/j6WWWPO.png>
  head
   <https://i.imgur.com/ur3TABt.png>
   <https://i.imgur.com/ERbhMDS.png>
  ...
and then in the HTML panel (bottom-right panel) you write this:

[imageLayerCombiner(data)]
And that would produce something like this (please forgive my drawings...):

randomize
You can double-tap or right-click on the image to open a full-resolution version in a new browser tab. Then just right-click and click "Save image..." to download the generated image. Here's an example generator with the full code of the above example.

Note: Each image should have exactly the same dimensions as one another because they will be overlayed on top of one another without any special positioning. For example, here are all the images used in the above example:

Notice that each image takes up the full "canvas", even though there's lots of blank space. You should make your images just like that.

Side note: I've noticed some people using this plugin are creating many versions of the same image - one for each color. Note that you don't need to do that - you can create one version (e.g. a red one) and then add the special filter property to the layer to randomly change the hue:

  layers
    hat
      filter = hue-rotate({0-360}deg) // <-- this randomizes colors of this layer
      <https://i.imgur.com/1spyUp1.png>
      <https://i.imgur.com/snpdUvc.png>
    ...
  
There are lots of other filter types (e.g. blur, saturation, brightness), and you can combine them together. Play with the filters here, and see an example of this plugin with filters here.

The easiest way to create a set of images like the one in the above example is to first draw a "base" image which acts as your template for all the different parts of the image. Make this background layer somewhat transparent so it doesn't get in the way of your drawings. Then add a new layer in your image-editing app and draw one of the pieces (e.g. a head), using the background template as a guide. Once you've finished drawing that part, hide the background layer and export/save the image as a PNG and upload it somewhere (e.g. catbox.moe, or perchance.org/upload), and then un-hide the background repeat that process for each of the parts of each of your layers.

If you're not sure what image editing app to use, I recommend Photopea. It's an excellent browser-based editor that's similar to Photoshop.

Note that you can select a bunch of images and once and drag-and-drop them all to catbox.moe, or perchance.org/upload to upload them all at once.

Note that you can call the layers whatever you want. Their names are irrelevant - they're just labels to help you remember which sets of URLs refer to which parts of you image. The first layer in the list will be displayed on top of the next one in the list, and so on. The last layer will be displayed at the bottom.

Also: You should make sure to save your images as PNGs or another type that allows transparency. If you use JPEG images, then all you'll see is the top layer because it will cover up the ones below - the JPEG type doesn't support transparency.

I recommend labelling your image links with comments like in the following example. Comments (text preceded by two forward-slashes) are ignored by Perchance, so they're purely to help you annotate your Perchance code with helpful notes.

layers
  hat
   <https://i.imgur.com/1spyUp1.png>  // backwards cap
  <https://i.imgur.com/snpdUvc.png>  // top hat
 eyes
  <https://i.imgur.com/PShX0T8.png>  // big
  <https://i.imgur.com/j6WWWPO.png>  // small
 ...
The reason labelling is helpful is because you'll often need to redraw certain parts every now and then, and it's annoying to try to find which url corresponds to which drawing. Without labels you'd have to open each URL one-by-one until you find the drawing that you wanted to replace.

By default a random item is selected from each layer with selectOne, but if you wanted each layer to be a "looping" consumable list (so it's "re-shuffled" when it runs out), then you could do that like this:

consumableListLoop = {import:consumable-list-loop-plugin}

data
  layers
    hat
      $output = [this.cLoop = this.cLoop || consumableListLoop(this)]
      https://i.imgur.com/1spyUp1.png
      https://i.imgur.com/snpdUvc.png
      ...
    ...
So as you can see you just need to add that $output line to the top of each of your layer lists and there'll be a much smaller chance of the same item being selected twice in a row (note that it is still possible though - for the same reason that it's possible that the last card you draw from a deck is the same as the first card you pick after reshuffling it).

Extra notes:

You can call the layers whatever you want - they don't need to be called "hat", "eyes", etc.
Use this example as a guide to get started.
If you want to allow the users of your generator to "lock" certain parts of the image and only randomize the others, you can do that by using the locker-plugin as shown in this example generator.
Here's an example generator that generates thumbnails based on previously selected list items / variables.
Here's another example that uses simple variable conditions.
Here's another example that has user-inputs (checkboxes) to disable/enable certain categories of images in certain layers.
Want to randomize the colors in your images? Or randomly add other effects like brightness, contrast, etc.? You can use a the special filter sub-property on layers and URLs as shown/explained in this example generator.
You can of course use GIF images if you want your layers to be animated (but you'll need to make sure your GIFs have a transparent background).
If you want to add custom CSS to the container of the images, you can use the containerCss property in the settings sub-list.
If you add only the height property in the settings, then the width of the image will automatically change to keep the correct proportions. And the same will happen if you only set the width (height will adjust automatically). If you set both the width and the height, then your image may become distorted unless you set the correct values to maintain the original aspect ratio of the images.
In the above example's I've called the list that holds the settings and layers "data", but you can call it whatever you want. For example, if you called it imageData, then you'd write [imageLayerCombiner(imageData)] in your HTML panel.
Check out more plugins at perchance.org/plugins

# background-image-plugin

The Background Image Plugin
To add a background image to your generator, first put this in your Perchance code panel:

background = {import:background-image-plugin}

Then put this anywhere in your bottom-right (HTML) panel:

[background("https://i.imgur.com/64c6NnI.jpg")]
Change the image URL to one of your choosing. Just make sure to keep the quotation marks around it.

Also, make sure that it's a direct URL to your image (usually ending in jpg or png or gif, though not always). To get a direct link to an image, right-click on an image and select "Copy image address" or "Copy image location" or similar - depending on your web browser.

Important: You should upload your image to somewhere like catbox.moe or perchance.org/upload. You should not use an image link directly from a random website on the internet, because it could get deleted/moved or the website could shut down, and then your background would no longer work. Instead, go to perchance.org/upload and drag-and-drop or paste the image (or the URL) there, and it'll upload, and then it'll give you the URL. That way your background image will last forever.

I previously recommended uploading to Imgur, but they've started deleting old images. Luckily we now have perchance.org/upload, so use that instead.

Here's how we can set the image opacity (transparency) to 0.7 and blur to 5px:

[background("https://i.imgur.com/64c6NnI.jpg", 0.7, 5)]

Or, if you need some fancy effects, pass in a CSS filter string as the second parameter:

[background("https://i.imgur.com/64c6NnI.jpg", "blur(3px) hue-rotate(30deg) saturate(1.6)")]
You can see examples of CSS filters in use here.

Note that you don't have to call it background:

// in lists editor:
backgroundImage = {import:background-image-plugin}
// in HTML editor:
[backgroundImage("https://i.imgur.com/64c6NnI.jpg")]
You can also randomize the image every time the randomize button is clicked by using code like this:

// in lists editor:
backgroundImage = {import:background-image-plugin}

imageUrl
  <https://i.imgur.com/64c6NnI.jpg>
  <https://i.imgur.com/Hvb6HTy.jpg>
  <https://i.imgur.com/ecKzF9F.jpg>
  <https://i.imgur.com/785rHFl.jpg>
  
// in HTML editor:
[backgroundImage(imageUrl)]
Need more advanced features? Add this to your Perchance code panel:

bgData
  url = <https://i.imgur.com/64c6NnI.jpg>
  size = cover
  repeat = no-repeat
 position = center
 opacity = 0.8
  filter = blur(10px)
And then add this to your HTML code panel:

[background(bgData)]
Learn more about each property in the bgData list above:

size: cover will ensure your image covers the whole page. contain will ensure your whole image fits within the page. 23px will set the width of the image to 23 pixels (the height will adjust to maintain correct aspect ratio). 45px 78px will set the width to 45 pixels and the height to 78 pixels.
position: center will center your image on the page. left will align it left. Consult this image for more details.
repeat: no-repeat will prevent your image from being "tiled" multiple times across the page. Consult this image for more details.
filter: allows you to add custom CSS filters to adjust your image - e.g. to make it greyscale or adjust the saturation. See this page for examples.
opacity: adjust the transparency of the background image with a value between 0 (fully transparent) and 1 (completely opaque).
You don't have to use all the properties - just delete the ones you don't want and they'll use default values. Here's an example generator that uses these advanced features. Also note that you don't need to call the list bgData - you can call it whatever you want.

Here are some backgrounds to try out:

pastel tiles:       <https://i.imgur.com/0CWEecq.jpg>
books:              <https://i.imgur.com/Hvb6HTy.jpg>
pine forest:        <https://i.imgur.com/ecKzF9F.jpg>
dark leaves:        <https://i.imgur.com/785rHFl.jpg>
rocky coastline:    <https://i.imgur.com/E4a7yi0.jpg>
night building:     <https://i.imgur.com/9hrHir1.jpg>
jelly fish:         <https://i.imgur.com/EyLiFMs.jpg>
cloud sunset:       <https://i.imgur.com/M3wXrLE.jpg>
summer sunset:      <https://i.imgur.com/YRUgc7j.jpg>
desert dunes:       <https://i.imgur.com/P4FoRy2.jpg>
jagged mountains:   <https://i.imgur.com/mSarpKO.jpg>

Tips:

Here's a simple example generator that uses this plugin
Here's an example with a random background image
Here's an example that uses advanced features
Use images that you're legally allowed to use (Unsplash is awesome - all the images are free)
Upload your image to a place where it wont be deleted (e.g. Imgur)
Your image url must end in .jpg, .png, etc. (i.e. must be a direct link - right-click on the image and click "Copy image address" or "Copy image location", depending on your browser)
Ideally your image would be at least 1500px wide
Lowering the opacity a bit and adding blur can help bring your content forward
Using images that aren't super bright and saturated also helps
Check out more plugins at perchance.org/plugins

# text-to-speech-plugin

Group: AI / Media Plugins

ðŸ—£ Text to Speech Plugin
Put this in your Perchance code panel:

speak = {import:text-to-speech-plugin}

Now you can use text-to-speech:

[speak("This is the perchance text to speech plugin")]

[speak(yourListName)]

You can alter the pitch, speed and delay by adding some extra inputs:

[speak(sentence, voice, pitch, speed, delay)]

The valid language codes available for voice in your current browser are: en-US

This will speak "hello" in Russian at normal pitch and 2 times normal speed:

[speak("Ð—Ð´Ñ€Ð°Ð²ÑÑ‚Ð²ÑƒÐ¹Ñ‚Ðµ", "ru-RU", 1, 2)]

This will speak "hello" at normal pitch and normal speed after 5 seconds:

[speak("hello", "en-US", 1, 1, 5)]

This will speak a random item from your 'animal' list when the user clicks the button:

<button onclick="speak(animal)">click me</button>

Notes:

Here's a simple example generator that uses this plugin
Each browser has its own set of voices (so, for example, en-US will likely sound different on Chrome vs Firefox)
Different browsers have different default voices
The default pitch and speed are 1
Since this is a new browser technology, not all languages will be available.
Remember that you can disable auto-reload using the check-box next to the reload button
For JavaScript devs:
The speak(...) returns a Promise, so you can await it. The returned Promise also has a stop method attached to it, so if you start some speech like this: p=speak('hello') then you can stop the speech prematurely like this: p.stop(). Here's an example which uses this functionality. Also, note that the promise resolves to an object with a spokenText property, which will be the text that has been spoken so far (it will be the whole input text if you didn't call .stop())
You can pass an object in like this: speak({text, voice, pitch, speed, delay, onSpoken}) - and as you can see this allows you to specify the onSpoken param, which should be a function, and that function will get called every time a chunk of text has finished being spoken. The size of the chunk of text that you recieve via this callback can vary - e.g. it can be a sentence, or part of a sentence, or a few sentences.
You can also pass text as the first arg, and then an object as the second: speak(text, {voice, pitch, speed, delay, onSpoken})
As well as supporting a language code for the lang, it also supports using a voiceURI. This is useful in cases where there are multiple voices per language (e.g. masculine + feminine). But note that different browsers have completely different voiceURIs - e.g. Chrome has voiceURIs like "Google UK English Female", but non-Chrome browsers don't have that voice. So you need to use window.speechSynthesis.getVoices() to get the voiceURIs of the voices that the user has available to them.
Check out more plugins at perchance.org/plugins

# random-image-plugin

Group: AI / Media Plugins

ðŸ–¼ Random Image Plugin ðŸ“·
This plugin allows you to add a random image based on a keyword/topic that you provide. It uses Unsplash.com's API which is a bit "hit and miss", so it won't be perfect. Just paste this in your Perchance code panel:

image = {import:random-image-plugin}
and then write this in your HTML (bottom-right) panel:

[image("cat")]
and it'll output a random cat image, like this:

Note that sometimes it will output an irrelevant image because unfortunately some Unsplash users add irrelevant tags to their images. You can resize/crop the output to a certain width and height like this:

[image("cat", 200, 100)]

That outputs an image that's 200 pixels wide, and 100 pixels high.

You can input a list and it will randomly select an item from that list:

[image(myAnimalList)]

By default the image is cropped to the height and width that you specify, but you can opt to "contain" the full image within the width and height you specify like this:

[image(myAnimalList, 600, 400, "contain")]

Notes:

Here's a simple example of a generator that uses this plugin.
This plugin uses the Unsplash Source API.
Important note: The Unsplash API may return the wrong images sometimes because on unsplash people tag their images with tags that sometimes don't match the exact topic. E.g. it may be a cat photo but their cat's name is "lizard", and so you get a cat photo displayed when you actually searched "lizard".
The default dimensions are 600x400.
[image("cat")] generates an actual image (i.e. the HTML <img> tag), but if you just want to generate the URL of the image, then you can instead write [image("cat").src].
Unsplash has hundreds of thousands of images, but there are still many topics that don't have any images, so if you request an image for "charmander" (for example), you'll get a "not found" placeholder image.
Since all images are from Unsplash, they're completely free to use for any purpose (e.g. even if you are selling your generator, or something).
Check out more plugins at perchance.org/plugins

# image-plugin

Group: AI / Media Plugins

ðŸ–¼ï¸Ž Image Plugin ðŸ–¼ï¸Ž
This plugin was made by u/Kyllingene and donated to the admin account :)

This plugin allows you to easily add an image to your generator. Simply import the plugin by putting this code on a new line in the list editor (the panel on the left):

image = {import:image-plugin}
and you can now display an image like this:

[image("https://i.imgur.com/1qFNMXG.jpg")]
And that will produce this:

Is that a bit too tall for your liking? Stay tuned for info on how to change the height and width - but first, a quick side note:

If you wanted to insert the above image "manually" (i.e. not using this plugin) your HTML code would look like this:

<img src\="<https://i.imgur.com/1qFNMXG.jpg"/>>
If you'd prefer not to use this plugin, you can instead copy and paste the above HTML code and just change the URL. Note that there's a backslash before the equals sign (after src) which isn't normal in HTML. This backslash is needed if you're using the code in your Perchance lists editor since otherwise Perchance interprets the equals sign as a "special" character. The equals sign has a special meaning when used in Perchance lists, and the backslash tells Perchance "treat the next character as just a normal non-special character please".

Important: You should upload your images to perchance.org/upload rather than linking directly to images that you find on the internet. This is important because the average lifespan of a URL on the internet is only a few years (due to the way modern web applications work - CDNs, caching, etc) so if you use an image URL from somewhere on the internet (like on wikis, pinterest, etc), then your generator will likely break after a few years. By uploading images to Perchance, your images will stay online forever.

You can also set the width of the image like this:

[image("https://i.imgur.com/1qFNMXG.jpg", 50)]

That sets the width to 50 pixels as shown above, and the height will automatically adjust so the width/height ratio stays the same.

You can set both the width and the height like this:

[image("https://i.imgur.com/1qFNMXG.jpg", 100, 100)]

But notice that this stretches the image out of proportion. If you only want to set the height, and you want the width to be automatically adjusted, then you should write null for the width, like this:

[image("https://i.imgur.com/1qFNMXG.jpg", null, 100)]

So now the image has a height of 100 pixels, and the width is adjusted automatically to keep the original proportions.

So in general, the format is:

[image(url, width, height)]
where url is the URL of the image (the only input you actually must give),

width is the width (in pixels) of the image (optional),

and height is the height of the image in pixels (optional).

Note that if you're using "raw" HTML (instead of this plugin), you can change the height and width like this:

<img src\="<https://i.imgur.com/1qFNMXG.jpg>" style\="height:100px; width:200px;"/>
If you omit a height value, then the width is automatically adjusted, and vice versa.

Notes:

This plugin was made by u/Kyllingene and donated to the admin account :)
Photo by Mat Reding on Unsplash
Check out more plugins at perchance.org/plugins
âš„ï¸Ž

## Documentation / UI / Layout Plugins

# favicon-plugin

Group: Documentation / UI / Layout Plugins

ðŸ–¼ï¸ Favicon Plugin
This plugin allows you to change the little icon that's shown in the browser tab.

To use this plugin, you'll first need to import it by adding this line to your lists editor:

favicon = {import:favicon-plugin}
And then put this in the HTML (bottom-right) panel:

[favicon("https://example.com/foo.png")]
Here's an example generator so you can see it in action.

Important: You should upload your favicon images to perchance.org/upload. Don't link to a random image on the internet, since the average 'life expectancy' of a random URL on the internet is only a couple of years. Instead, download the image, then upload to perchance.org/upload, and you'll be given a permanent link to that image.

Here's a silly example where we make an "animated" favicon by changing it once per second through a series of animation frames.

Notes:

For mad scientists: You can pass a 'data URL' to this plugin. Here's an example that generates an image with the text-to-image-plugin, then set the tab icon to that image. You could also e.g. make a little dot on a blank canvas that moves around based on arrow key presses, and then send a data URL of each frame to this plugin to make a very tiny game that uses the browser tab icon as the "screen".
Check out more plugins at perchance.org/plugins
âš„ï¸Ž

# layout-maker-plugin

Group: Documentation / UI / Layout Plugins

Layout Maker Plugin
This plugin lets you create custom visual layouts for your generators without knowing HTML (the stuff in the bottom-right code editor panel). The general idea of this plugin is that you define they layout with a grid of letters, as you can see below. On the left, we define the text grid, and on the right is the layout that is generated.

a a a a b
a a a a b
c c c c c
âž¡
Once we've defined the grid of letters, we then just define the content that we want in each area.

Okay, let's see an actual example of how to use it. This code goes in your perchance code panel:

layoutMaker = {import:layout-maker-plugin}

layout
  debug = borders
  grid
    a a a a b
    a a a a b
    c c c c c
  areas
    a
      content = {hello|hi there} this is the "a" area
    b
      content = side bar thing ("b" area)
    c
      content = a sort of footer thing ("c" area)
And then put this somewhere in your HTML panel (bottom-right panel):

[layoutMaker(layout)]
And you'll get this:

hi there this is the "a" area
side bar thing ("b" area)
a sort of footer thing ("c" area)
Here's a version of the above example with debug = colors and with centered = true on each of the areas:

hello this is the "a" area
side bar thing ("b" area)
a sort of footer thing ("c" area)
You can make the grid as complex as you want - here's another example:

layout
 debug = colors
  grid
    t a a a b m
    t a a a b k
    c c c c c k
  d d g s s s
 areas
  s
   content = hello
   centered = true
  m
   content = {1|2|3}
   centered = true
3
hello
As you can see, you can use the debug = colors or debug = borders lines to easily visualise your layout, but you can take this line away once you're done "debugging" it. Also note the centered = true property that you can use to center the content of an area.

You can specify a style property for each area where you can put CSS rules that will be applied to that area:

layout
  grid
    a b c
    a b c
    a b c
  areas
    a
      content = aaa
   style = background-color:lightblue;
    b
      content = bbb
   style = border:1px solid lightgrey;
    c
      content = ccc
   style = background-color:orange;
aaa
bbb
ccc
And you can also apply CSS styles to the overall container:

layout
 debug = colors
 container
  style = height:100px; width:200px;
  grid
    a a a
    b b b
    c c c
Notice that we've made the layout smaller using style = height:100px; width:200px;? The default height is 300 pixels. If you want the overall height to compress down the the size of the content within, use style = height:auto; ..., like in this example:

layout
 debug = colors
 container
  style = height:auto;
  grid
    a a a a b
    a a a a b
    c c c c c
  e d d d d
  f f f f f
  areas
    a
      content = {hello|hi there} this is the "a" area
    b
      content = side bar thing ("b" area)
    c
      content = a sort of footer thing ("c" area)
  d
      content = another area
  e
   content = hi
    f
      content = hello
Here's what that looks like:

hello this is the "a" area
side bar thing ("b" area)
a sort of footer thing ("c" area)
hi
another area
hello
If you want your layout to take up the full height of the screen, add height:100vh; to the layout.container.style property like so:

layout
 container
  style = height:100vh;
 ...
You can change the relative sizes of each row, and of each column like this:

layout
 debug = borders
 columnSizes = 1fr 0.5fr 1fr
 rowSizes = 2fr 1fr 1fr
  grid
    a b c
  d e f
  g h i
So if you want the first column to be triple the width of the other two columns, we'd write columnWidths = 3fr 1fr 1fr, for example. And if your grid had 4 columns, then you'd need to write columnWidths = 3fr 1fr 1fr 1fr. If that's confusing, remember you can always ask for help on the community forum :)

You can define "gaps" in your layout like so:

layout
 debug = colors
  grid
    a a .
  b . c
  . . d
If you're feeling adventurous you can define layouts within layouts! This will put layout2 within the "b" area of layout1:

layout1
  grid
    a a a
  b b b
  c c c
 areas
  b
   content = [layoutMaker(layout2)]

layout2
  grid
    a b c
  a b c
  a b c
  
output
 [layoutMaker(layout1)]
With this type of "nesting" you could probably build random maps, dungeons, random houses (with random room layouts), and so on. If you do create something interesting like that, please share it with the community!

Notes:

You can use this simple example as a starting point for your creations.
Here's an example that has two different layouts depending on the size of your screen (e.g. one for mobile users, and one for desktop users). Also check out the responsive-layout-maker-plugin by Vionet20.
You need to make sure that each "area" that you've defined with letters is "rectangular" - e.g. you can't make an L-shaped area - it won't work.
If needed, you can define an id for an area by writing id = yourId in the area options (i.e. under the content = ... property). You can also set layout.container.id to give the container an id. Here's an example where we make a button that only updates a specific box in our layout.
Check out more plugins at perchance.org/plugins

# tooltip-plugin

Group: Documentation / UI / Layout Plugins

ðŸ’¬ï¸Ž Tooltip Plugin ðŸ’¬ï¸Ž
Put this in your Perchance code panel:

tooltip = {import:tooltip-plugin}
Now you can create tooltips:

[tooltip("â„¹ï¸", "tooltip text!")]
The above example would result in this (try hovering over it):

â„¹ï¸

So, as you can see, the format is:

[tooltip(anchorText, tooltipText)]

Here's an example of how you might want to use it:

output
  There is <b>[tooltip(race, description)]</b> standing nearby.

race
  an orc
  an elf
  a human
  
description
  They look suspicious.
  Their shirt is torn.
And you's get something like this:

There is an orc standing nearby.

You can customize the background color and the text color like so:

tooltipOptions
  css = background-color:tomato; color:yellow;
  ...

output
  Try <b>[tooltip("hovering over this text", "Here it is!", tooltipOptions)]</b> to see a custom-colored popup. Random num: {1-100000}
You can replace "tomato" and "yellow" with any valid CSS color, including completely custom hex codes like "#32a852". Here's an example which uses the above code.

If you'd like to include links (or other HTML) in the popup, you need to use these options:

tooltipOptions
  interactive = true
  allowHTML = true
  ...
  
output
  [tooltip(anchorText, tooltipText, tooltipOptions)]
The interactive option makes it so the popup doesn't dissapear when you try to move your mouse into it (e.g. to click a link that is within the popup/tooltip). The allowHTML option allows us to put HTML in the tooltip, so with these two options we could include a link within the tooltip like so:

tooltipOptions
  interactive = true  
  allowHTML = true

tooltipText
  <a href="https://i.imgur.com/26DZgXM.mp4" style="color:white;">Here's</a> the secret link. And the secret code is {1-100000000}

output
  You can [tooltip("hover over this text", tooltipText, tooltipOptions)] to get the secret link.
Here's an example which uses that code.

All customization options are listed on the tippyjs homepage.

Notes:

Here's an example of how you might use it.
Here's an example that uses the allowHTML option to embed an image in the tooltip.
Check out more plugins at perchance.org/plugins
This plugin is based on tippyjs, and so all credit for this functionality goes to the creator, Atomix!

# font-plugin

Group: Documentation / UI / Layout Plugins

Font Plugin
Put this in your Perchance code panel:

font = {import:font-plugin}

Here we output a random item from our animal list in the "Pacifico" font:

[font(animal, "Pacifico")]

All font names must be from Google Fonts (If you want to use a custom font, click here).

Here's another example to try:

[font(myList, "Permanent Marker")]

Make sure you change "myList" to the name of an actual list or variable/property in your generator. If you just want it to output some fixed text you can write this:

[font("hello there!", "Permanent Marker")]

which would output this:

hello there!

You can also change font size and color:

[font(myList.upperCase, "Courgette", "30px", "#ff5252")]

Use a hex color picker to get custom colors in #XXXXXX format.

If you want to change the color but not the size, then use 100% for the size to keep the size at the default:

[font(myList.upperCase, "Courgette", "100%", "#ff5252")]

You can (for example) write 70% to make the font 70% of the height of the "default" font size:

[font(myList.upperCase, "Courgette", "70%", "#ff5252")]

What if you want to change the default font of the whole page? Here you go:

[font(null, "Courgette", "25px", "pink")]

And to apply the font to a specific HTML element, just give the element an id as shown below, and then put the id as the first value:

<p id="myParagraph">Hello this is my [adjective] paragraph and it has a cool font.</p>
[font(myParagraph, "Courgette", "25px", "pink")]

Notes:

Here's a simple example generator where you can see this plugin in action.
Here's an example that changes the font of a specific HTML element.
Here's an example that changes the default font of the whole webpage.
Use a hex color picker to get custom colors in #XXXXXX format.
Check out more plugins at perchance.org/plugins

# markdown-plugin

Group: Documentation / UI / Layout Plugins

Markdown Plugin
Markdown is sort of like a more simple version of HTML. Have a look at this to get a idea of what it is. As a small example, to make bold text in HTML, you write <b>hello<b> whereas in markdown you simply write **hello**. This plugin converts the simple markdown syntax (that is made for human-readability) into HTML code that the browser understands. That's a very simple example, but you can do all sorts of things in markdown - even tables, numbered lists, and more (see that previous link for examples). Here's an example generator that uses this plugin.

Using the plugin is simple - just copy and paste this in your Perchance code panel, and then customize the text list:

markdown = {import:markdown-plugin}

output = [markdown(text)]

text

# My title

 The first line of my first paragraph.
 Second line of first paragraph.
 \s // <-- paragraph break
 You can *italicize* or **bold** your text easily.

## Sub-header

 Here's a list of items:

* Bullet point 1
* Bullet point 2
* Bullet point 3
  * Sub-bullet-point
* Bullet point 4
 \s  // <-- end lists like this too
 And we can do numbered lists too:

   1. First item
   2. Second item
   3. ~~Scratch this~~
 \s
 Adding a [link](https://dillinger.io) is easy with markdown.
 Images are easy too:
 \s
 ![image hover text](https://web.archive.org/web/20091018220201/http://www.geocities.com/roqofages/Rainbowflagwaving.gif)
 \s
 And you can still put HTML code in if needed:
 \s
 <video controls src\="<https://i.imgur.com/26DZgXM.mp4">></a>

 ```
 You can do code-blcks like this.
 Second line of code.
   Third line of code (indented)
 ```

 > And quoted text like this. Quotes automatically wrap: foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar.
 \s
 > Break quotes up into paragraphs using the \s trick.
  
 Header  | Header
 --------|---------
 You     | Can
 Make    | Neat
 Little  | Tables
 Too     | !
  
 So that's a brief intro to some of markdown's basic features!
And now writing [output] in the HTML panel will produce this:

My title
The first line of my first paragraph.
Second line of first paragraph.

Second paragraph. You can italicize or bold your text easily.

Sub-header
Here's a list of items:

Bullet point 1
Bullet point 2
Bullet point 3
Sub-bullet-point
Bullet point 4
And we can do numbered lists too:

First item
Second item
Scratch this
Adding a link is easy with markdown.
Images are easy too:

image hover tex

And you can still put HTML code in if needed:

You can do code-blcks like this.
Second line of code.
  Third line of code (indented)
And quoted text like this. Quotes automatically wrap: foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar.

Break quotes up into paragraphs using the \s trick.

Header Header
You Can
Make Neat
Little Tables
Too !
So that's a brief intro to some of markdown's basic features!

Notes:

Check out the example generator!
Full markdown cheetsheet here.
All thanks goes to the contributors of markedjs on github!
Check out more plugins at perchance.org/plugins

## Storage / Data / Import Plugins

# url-params-plugin

Group: Storage / Data / Import Plugins

Link: [url-params-plugin](https://perchance.org/url-params-plugin)

Description: detect and use URL parameters in your code - i.e. customize output based on the URL

# remember-plugin

Group: Storage / Data / Import Plugins

Link: [remember-plugin](https://perchance.org/remember-plugin)

Description: allows you to save variables so they're not lost when the page is reloaded

# google-sheets-plugin

Group: Storage / Data / Import Plugins

Link: [google-sheets-plugin](https://perchance.org/google-sheets-plugin)

Description: import lists from Google Sheets

## Randomization / Selection Plugins

# select-until-plugin

Group: Randomization / Selection Plugins

Link: [select-until-plugin](https://perchance.org/select-until-plugin)

Description: keep trying to selectOne from a list until the resulting item meets your requirements

# select-leaf-plugin

Group: Randomization / Selection Plugins

Link: [select-leaf-plugin](https://perchance.org/select-leaf-plugin)

Description: select a "leaf" node from your hierarchy (see discussion)

# select-leaves-plugin

Group: Randomization / Selection Plugins

Link: [select-leaves-plugin](https://perchance.org/select-leaves-plugin)

Description: the selectMany version of selectLeaf

# select-all-leaves-plugin

Group: Randomization / Selection Plugins

Link: [select-all-leaves-plugin](https://perchance.org/select-all-leaves-plugin)

Description: the selectAll version of selectLeaf

# random-select-plugin

Group: Randomization / Selection Plugins

Random Select Plugin
This plugin allows you to randomly select between two or more input lists or variables. It's a bit like the curly bracket notation for creating a quick inline random selection (e.g. {lizard|mouse|frog}) except it allows you to randomly randomly select lists/variable and produces a random list/variable instead of plain text.

That might sound a bit confusing. Let's look at an example.

Imagine that we have two lists, a and b. Now if we have x = {[a]|[b]} then will x.selectOne give us a reference to either the a or b list, or will it give is the "plain text" that results from evaluating a/b? The answer is the latter. That is, it will give us the plain text that results from evaluating the chosen (a or b) list. But what if we want x to give give us a reference to the a or b list? That's one example of where this plugin can come in handy.

To use it, you first need to import it by putting this line of code in your lists editor:

select = {import:random-select-plugin}
And now if you write this:

x = [select(a, b)]
then x will refer to either a or b (randomly selected with 50% probability). If you want to change the probability, you can add odds like so:

x = [select(a, b, null, 1, 2)]
That means "randomly select between a and b where a has odds of 1 and b has odds of 2". In other words, b is twice as likely as a. If you decode to specify odds, then you musty specify them for all items.

Notes:

Here's an example generator showing how you could use this plugin.
Check out this forum thread for the origin story of this plugin.
Check out more plugins at perchance.org/plugins

# consumable-leaf-list-plugin

Group: Randomization / Selection Plugins

Link: [consumable-leaf-list-plugin](https://perchance.org/consumable-leaf-list-plugin)

Description: create a consumableList of the leaf items in your hierarchy

# fixed-until-reload-plugin

Group: Randomization / Selection Plugins

Fixed-Until-Reload Plugin
This plugin allows you to output a random selection from a list that doesn't change then the user clicks the "randomize" button. Once it has been generated the first time, it stays on that value until they reload the page. To use this plugin, you'll first need to import the plugin by putting this code in your Perchance code panel:

fixedUntilReload = {import:fixed-until-reload-plugin}
And here's a simple example of how to use it:

output
 The [fixedUntilReload(animal)] has befriended the [animal].

animal
 frog
 mouse
 rabbit
 cow
 ...
and that would output this:

The mouse has befriended the zebra.

randomize
Notice how the first animal doesn't change, but the second one does? That's because the first animal was permanently "fixed" on the very first random selection that it made. The only way to re-randomize it is to reload the page.

Pretty easy, right?

There is one catch though. Let's see what happens if we use fixedUntilReload on the animal list twice:

output
 The [fixedUntilReload(animal)] has befriended the [fixedUntilReload(animal)].
The mouse has befriended the mouse.

randomize
They're both fixed and thus don't change when we tap "randomize", which is expected, but notice that it selects the same animal both times? To avoid this, we need to pass in an "id" (identification) parameter after the list name:

output
 The [fixedUntilReload(animal,1)] has befriended the [fixedUntilReload(animal,2)].
The llama has befriended the frog.

They may still select the same animal by coincidence (you could use a consumableList to prevent this), but now the selections are actully separate. The added benefit of this "id" stuff is that we can refer to the selected animals again later in our output text like this:

output
 The [fixedUntilReload(animal,1)] has befriended the [fixedUntilReload(animal,2)]. The [fixedUntilReload(animal,1)] is happy.
The llama has befriended the frog. The llama is happy.

Notice that in the second sentence we're referring to the "id" (in this case, 1) of the first animal we generated? Not too complicated, right? Remember that you can ask for help on the forum if needed.

Notes:

Here's an example of a generator that uses this plugin.
If you want to allow the users of your generator to "unlock" and "lock" the selections manually, check out the lockable-list-plugin and the locker-plugin.
Check out more plugins at perchance.org/plugins

# number-set-plugin

Group: Randomization / Selection Plugins

Number-Set Plugin
This plugin allows you to generate a set of numbers which add up to a certain number. Start by putting this in your Perchance code panel:

numberSet = {import:number-set-plugin}
and then you can use it like this:

output
  [set = numberSet(3), ""]The population is [set.n1]% orcs, [set.n2]% elves and [set.n3]% humans.
and that would output something like this:

The population is 54% orcs, 21% elves and 25% humans.

Notice that the three numbers add up to 100?

You can can make them add up to 500 by inputting a second value like so:

output
  [set = numberSet(4, 500), ""]Of the 500 gold coins, I gave [set.n1] to the Nark clan, [set.n2] to the Gileshi clan, [set.n3] to the Sardits and kept the remaining [set.n4] coins for myself.
and that would output something like this:

Of the 500 gold coins, I gave 142 to the Nark clan, 125 to the Gileshi clan, 156 to the Sardits and kept the remaining 77 coins for myself.

This plugin has another feature which allows you to "weight" n1, n2, n3, etc. so that, for example, n1 is, on average, twice the size of n2. Here's how you'd generate 3 numbers which add up to 80 where the first one is, on average, 5 times the size of the other two:

numberSet(3, 80, "5,1,1")
And here's how to generate a set of 4 number that add up to 1000 where the second and third numbers are, on average, twice the size of the other two:

numberSet(4, 1000, "1,2,2,1")
And one more example: A set of 7 numbers which add up to 170 where the first 3 are 5 times the size of the other, on average:

numberSet(7, 170, "5,5,5,1,1,1,1")
What if you want to generate 3 numbers, but the last number *must* be greater than the first number? Here's where this plugin's final feature comes in handy:

numberSet(3, 100, "1,1,1", "n3 > n1")
And if you need multiple "conditions", then you can use "&&" to join them. For example, lets say we want the first number to be greater than the second, and the second to be greater than the third:

numberSet(3, 100, "1,1,1", "n1 > n2 && n2 > n3")
You can also do all sorts of complex arithmetic and "boolean algebra". Here's how we'd make sure the first number is bigger than the sum of the next two:

numberSet(3, 100, "1,1,1", "n1 > n2+n3")
And here's how you make sure the last number is smaller than the multiplication of the first two:

numberSet(3, 100, "1,1,1", "n3 < n1*n2")
You can also use the boolean "or" operator to say that you want at least one of two conditions to be true. Here's how we make sure the first number is bigger than the second number, OR the third number is greater than zero.

numberSet(3, 100, "1,1,1", "n1 > n2 || n3 > 0")
And by the way, if you want to include some conditions but you don't want to change the weights, you can just put some empty quotes instead of "1,1,1,...":

numberSet(3, 100, "", "n3+2 < n2")

Notes:

Here's an example generator that uses this plugin.
This plugin only works for whole numbers (not decimals), but the example generator linked in the above bullet point shows you a trick to generate decimals using it.
Here's the discussion which brought about this plugin.
Check out more plugins at perchance.org/plugins

# join-lists-plugin

Group: Randomization / Selection Plugins

joinLists Plugin
Put this in your Perchance code panel:

joinLists = {import:join-lists-plugin}

Now you can join lists together:

[animal = joinLists(mammal, reptile)]

It essentially creates a new list so you can do normal stuff to it:

[joinLists(tree, shrub).selectMany(5)]

[plant = joinLists(tree, shrub), ""]

Notes:

Here's an example that combines it with consumableList
Also check out the excludeItems plugin
Check out more plugins at perchance.org/plugins

# exclude-items-plugin

Group: Randomization / Selection Plugins

Link: [exclude-items-plugin](https://perchance.org/exclude-items-plugin)

Description: exclude certain items from a list during random selection

# filter-list-plugin

Group: Randomization / Selection Plugins

Link: [filter-list-plugin](https://perchance.org/filter-list-plugin)

Description: a somewhat advanced plugin for dynamically filtering lists

# consumable-list-loop-plugin

Group: Randomization / Selection Plugins

Link: [consumable-list-loop-plugin](https://perchance.org/consumable-list-loop-plugin)

Description: sometimes you want a consumable list that never runs out (i.e. resets when its empty)

## Game / Worldbuilding Plugins

# create-instance-plugin

Group: Game / Worldbuilding Plugins

Link: [create-instance-plugin](https://perchance.org/create-instance-plugin)

Description: allows you to define "blueprints" of things, and then create random instances of them

# create-instances-plugin

Group: Game / Worldbuilding Plugins

Link: [create-instances-plugin](https://perchance.org/create-instances-plugin)

Description: create a list of random instances based on a given blueprint

# rpg-icon-plugin

Group: Game / Worldbuilding Plugins

 RPG Icon Plugin
Put this in your Perchance code panel:

icon = {import:rpg-icon-plugin}

Now you can create any of ~500 RPG-themed icons by referencing its name:

[icon("sword")] â†’

[icon("burning-book")] â†’

[icon("explosive-materials")] â†’

[icon("knight-helmet")] â†’

[icon("axe-swing")] â†’

[icon("dragon-breath")] â†’

[icon("hydra-shot")] â†’

Below this plugin's explanation is a massive list of icons that you can use.

Hover over an icon in that list to get its name.

You can change the size of the icons like this:

[icon("sword lg")] â†’

[icon("sword 2x")] â†’

[icon("sword 3x")] â†’

(etc. up to 5x)

You can also add custom styling to the icon:

[icon("dragon-breath lg", "color:red")] â†’

[icon("water-drop", "color:#1b8ce8")] â†’  (use a hex color picker)

[icon("sword lg", "color:white; background:black; padding:2px")] â†’

Notes:

All credit for this plugin goes to the RPG Awesome project.
Check out this generator which simply generates a random rpg icon (using the full list of icon names).
Check out more plugins at perchance.org/plugins

Here's a list of all the icons that you can use. Hover over an icon to get its name.

Players

Potions

Inventory

Creatures and Animals

Electronics

Cards and Dice

Food

Plants

Astrology

Dangers

Magic

Weapons and Armor

RPG Icons

# roll-table-plugin

Group: Game / Worldbuilding Plugins

Link: [roll-table-plugin](https://perchance.org/roll-table-plugin)

Description: use dice ranges for the items in your list instead of normal perchance odds notation

# goto-plugin

Group: Game / Worldbuilding Plugins

goto plugin
Put this in your Perchance code panel:

goto = {import:goto-plugin}
Now when you write [goto(blah, "click me")] it'll make a button with the text 'click me' that'll display the list called 'blah' when you click it. So you can e.g. create simple text adventures:

darkroom = You're in a dark room. You can [goto(lightroom, "turn on the light")] or [goto(tavern, "exit through the door")].
lightroom = You switch the light on. There are mops and buckets here. Seems like you're in a cleaning cupboard. You can [goto(darkroom, "turn off the light")] or [goto(tavern, "exit through the door")].
tavern = You open the door and walk out. You're standing in an old dusty tavern. There's no one here. You can [goto(tavernexit, "look for an exit")] or [goto(tavernbar, "have a look at the bar")].
tavernexit = ...
tavernbar = ...
Here's a link to a generator with the above code.

You can obviously use all the normal Perchance features within your story to make it wonderful and random.

You might be wondering: When you click a goto button, how does this plugin know which existing text to 'delete' before it displays the text from the new list? Does the replace the entire page with the content of the new list? Or just the button? The answer is that it replaces everything inside the button's "parent HTML element" - i.e. the thing that contains the button will have all its content cleared, and then the new content will be placed in that container. That might be confusing, so here's an example where a <span>...</span> element contains the goto button:

output
  This text will not get replaced <span>but this text *will* get replaced [goto(myCoolList, "when you click this button")] and this text will be replaced too</span> but this text won't get replaced because it's outside of the span
You can imagine it like the goto button "eats all the text around itself" until it bumps into < or > characters and when it has finished eating, it puts the content of the new list in place of what it ate. Here's an example generator with the above code so you can play around and try it out.

If you want to specify a custom container to put the new content into, then you can give the element an id like <span id="myCoolContainer">...</span> and refer to that using the optional third input to the goto function like this:

[goto(myCoolList, "button text", myCoolContainer)]
as shown in this example. That way the goto button will "eat all the text" inside the myCoolContainer element, instead of just "eating outwards" until it hits < or >.

Note that I've used <span>...</span> in these examples, but you can use any other HTML element as a container, like <p>...</p> or <div>...</div>, or whatever

Notes:

Want to allow people to save their game so they can close the browser tab and pick up where they left off later? Then check out the remember-plugin, and here's an example of how to use the remember and goto plugins together.
Here's a more complex example.
Have a look at the HTML panel in the example above to see how to edit the text color.
Here's another simple example that uses a grid-style world layout.
A related community-made plugin with some handy features: go-to-plugin
Check out more plugins at perchance.org/plugins

# nested-plugin

Group: Game / Worldbuilding Plugins

nested plugin
Here's an example generator showing how you can use this plugin. It allows you to create "hierarchical worlds" like you might have seen in Orteil's Nested program. I thought it would be cool to allow people to create their own "worlds" in Perchance for others to explore. Here's how you can get a simple example up and running:

Put this in your Perchance code panel:

nested = {import:nested-plugin}

world
  n = {5-10} // the overall min and max number of children
  continent
 ocean
 archipelago^0.2 // normal odds notation for general likelihood of each item

continent
  n = {3-5}
  desert_region
 mountain_range {1-3} // desired quantity for *this specific item*
 forested_region

desert_region // use under-scores for names
  n = {3-5}
 name = {rocky ^0.2|sandy |}desert region // optionally specify alternative names
 village
 sand

// add descriptions which will appear when you hover your mouse over the item:
mountain_range
 description = A {snowy|dry|massive} range of mountains, stretching up to {1000-9000} metres at its tallest.
 mountain
 alpine_forest

// items that only have a description will show that description when you "unfold" them.
alpine_forest
 description = There are trees, and it's quite {cold|snowy}. About -{3-30} degrees Celsius. <br><img src\="<https://i.imgur.com/B34FLcF.jpg>" style\="width:200px;">
And put this in your HTML panel:

[nested(world)]
And here's what you get (try clicking it):

âž•ï¸Ž
world
Notes:

This is an experimental plugin so there will likely be bugs and problems (sorry!).
u/rsek created another version of this plugin that is more visually customizable (explained here).
The default overall maximum and minimum is n = {5-10}.
The items with specified quantities are added first, and then if there's any room left (with regard to the overall min and max), items will randomly be chosen from the set of items without individually specified quantities.
Have a look at the HTML panel in the example above to see how to edit the default styling and coloring.
Check out more plugins at perchance.org/plugins

# flat-avatar-plugin

Group: Game / Worldbuilding Plugins

Flat Avatar Plugin
This plugin allows you to generate little random avatars based on the flat-style illustrations of Pablo Stanley and the code of Fang-Pen Ling. To use this plugin, you'll first need to import it by pasting this line in your Perchance lists editor panel:

avatar = {import:flat-avatar-plugin}
Now that you've imported your plugin, you can generate an avatar by writing this:

[avatar()]
And that'll output an avatar like this:

generate another

If you want to customize generated avatars (e.g. only include specific clothing types) you can create a list in your list editor that looks like this:

avatarOptions
  style
    width = 200px
    height = 200px
  hairOrHat = {NoHair|Eyepatch|Hat|Hijab|Turban|WinterHat1|WinterHat2|WinterHat3|WinterHat4|LongHairBigHair|LongHairBob|LongHairBun|LongHairCurly|LongHairCurvy|LongHairDreads|LongHairFrida|LongHairFro|LongHairFroBand|LongHairNotTooLong|LongHairShavedSides|LongHairMiaWallace|LongHairStraight|LongHairStraight2|LongHairStraightStrand|ShortHairDreads01|ShortHairDreads02|ShortHairFrizzle|ShortHairShaggyMullet|ShortHairShortCurly|ShortHairShortFlat|ShortHairShortRound|ShortHairShortWaved|ShortHairSides|ShortHairTheCaesar|ShortHairTheCaesarSidePart}
  avatarFrame = {Circle|Transparent}
  accessories = {Blank|Kurt|Prescription01|Prescription02|Round|Sunglasses|Wayfarers}
  hatColor = {Black|Blue02|Blue03|Gray01|Gray02|Heather|PastelBlue|PastelGreen|PastelOrange|PastelRed|PastelYellow|Pink|Red|White}
  hairColor = {Auburn|Black|Blonde|BlondeGolden|Brown|BrownDark|PastelPink|Platinum|Red|SilverGray}
  facialHair = {Blank|BeardMedium|BeardLight|BeardMagestic|MoustacheFancy|MoustacheMagnum}
  clothes = {BlazerShirt|BlazerSweater|CollarSweater|GraphicShirt|Hoodie|Overall|ShirtCrewNeck|ShirtScoopNeck|ShirtVNeck}
  clothesColor = {Black|Blue02|Blue03|Gray01|Gray02|Heather|PastelBlue|PastelGreen|PastelOrange|PastelRed|PastelYellow|Pink|Red|White}
  eyes = {Close|Cry|Default|Dizzy|EyeRoll|Happy|Hearts|Side|Squint|Surprised|Wink|WinkWacky}
  eyebrows = {Angry|AngryNatural|Default|DefaultNatural|FlatNatural|RaisedExcited|RaisedExcitedNatural|SadConcerned|SadConcernedNatural|UnibrowNatural|UpDown|UpDownNatural}
  mouth = {Concerned|Default|Disbelief|Eating|Grimace|Sad|ScreamOpen|Serious|Smile|Tongue|Twinkle|Vomit}
  skin = {Tanned|Yellow|Pale|Light|Brown|DarkBrown|Black}
Just copy that into your lists editor and remove the options you don't want, and then just use this to generate an avatar based on your chosen options:

[avatar(avatarOptions)]
The above avatarOptions list includes all the possible values for each option. If you want to visually play around with the options, check out this page.

Notes:

Here's a basic example to get you started.
Here's an example that generates two avatars using two different options lists.
Here's an example make the generated avatar depend on a previously generated value.
Want to design your own avatar plugin like this (e.g. for dragons, orcs, etc)? It's easy! Just use the image-layer-combiner-plugin
As mentioned previously, this plugin uses the illustrations of Pablo Stanley and the code of Fang-Pen Ling. Both the code and the illustations are free for personal and commercial use.
I've removed the "Blue01" color from both the hat and clothes color options because they're the same color as the background, which currently can't be changed. If you'd like to be able to change the background, make a post of the forum to let me know :)
Check out more plugins at perchance.org/plugins
âš„ï¸Ž

## Core / Required Plugins

# create-instance-plugin

Group: Core / Required Plugins

Create Instance Plugin
Let's say you've got a list like this:

character
  name = {Molly|Anita|Murphy}
 age = {18-90}
 ...
And what you want is to create a character that uses this as a template, so that when you write character.name, it chooses a random name, but then keeps that same name next time you write character.name.

That's what this plugin is for. It lets you write "blueprints" for your characters, worlds, stories, etc. and then create "instances" that use this blueprint.

To use it, first you need to put this in your Perchance code panel:

createInstance = {import:create-instance-plugin}
And now, if we are using the character list (above) as our blueprint, then we can create an "instance" of that list with all the properties (name, age, etc.) "fixed" to randomly chosen values:

output
  [c = createInstance(character), ""] [c.name] is [c.age] years old. Her parents called her "[c.name]" because ...
And that would output something like this:

Murphy is 22 years old. Her parents called her "Murphy" because ...
As you can see, c.name was randomly set to "Murphy", and so we always get "Murphy" when we use c.name.

So, to reiterate, if we write [c = createInstance(character)], then we've made a new c "variable" and it refers to a specific character so that each time you write [c.name] you'll get the same name. It uses your blueprint to randomly create an instance of the character where the properties are no longer random. See this generator for an example of how you could use it.

An important thing to note is that only "properties" (items with an equals sign like thing = {blah1|blah2}) will be fixed in place. So in the following example, the "mood" sublist will remain random:

character
  name = {Molly|Anita}
 age = {18-90}
 mood
   happy
  sad
So [c = createInstance(character), c.mood][c.mood][c.mood] would return strings like "happysadhappy", "sadhappyhappy", etc. whereas [c.name][c.name][c.name] would return either "MollyMollyMolly" or "AnitaAnitaAnita".

So you need to change it to this:

character
  name = {Molly|Anita}
 age = {18-90}
 mood = {happy|sad}
If you had a really long list of names, and you wanted your character to have a fixed name, it would be annoying to write:

name = {name1|name2|name3|...|name4942}
So instead you'd probably want to write something like name = [characterName], and define your character list seperately:

character
  name = [characterName]
 age = {18-90}
 mood
   happy
  sad
  
characterName
 name1
 name2
  name3
 ...
  name4942
And now the character instances will get a fixed name instead of it randomizing every time we write [c.name].

Note that you don't need to call your character instance c. I'm just using c here as an example. You can call it whatever you want:

output
  [char1 = createInstance(character), char2 = createInstance(character), blah = createInstance(character), ""] ...

The properties are randomly-selected in the order that they appear in your list, so if you've read the perchance.org/examples page, and thus know how to use the special this keyword (and dynamic odds) then you can make the lower properties depend on the previously-selected higher properties like this:

character
 age = {18-60}
 height = {14-20}0
 gender = {female|male|non-binary}
 pronoun = {she^[this.gender=="female"]|he^[this.gender=="male"]|they^[this.gender=="non-binary"]}
 name = [names[this.gender]]   // this uses "dynamic sublist referencing" to grab the correct gender sub-list of the 'name' list, based on the gender that was selected above - explained at perchance.org/examples

names
  female
    Alice
    Saanvi
  male
    Bob
    Salman
  non-binary
    Charlie
    River
So in this case we've made it so the pronoun depends on the previously-selected gender. This only works because the gender property is above the pronoun property. Here's an example based on the above code.

If you want to create a list of instances based on a blueprint (instead of just one instance), check out the create-instances-plugin.

One more thing! If your code was like this:

person
  name = {Salman|Manny|Rhian}
  age = {31-49}
  child = [child]
  
child
  name = {Anne|Arram|Amelia}
  age = {3-17}
  
output
  [p = createInstance(person), p.child.age] [p.child.age] [p.child.age]
Then you'd notice that the it outputs something like "15 3 9" instead of "5 5 5". In other words, the "child" remains random - only the parent properties are "fixed" in place. To fix this, we could write the output code like this:

output
  [p = createInstance(person), c = createInstance(p.child), c.age] [c.age] [c.age]
And that would work, but it's messy. This is where the "deep" mode comes in handy. You can write your code like this:

output
  [p = createInstance(person, "deep"), p.child.age] [p.child.age] [p.child.age]
And that's it!

We just replaced createInstance(person) with createInstance(person, "deep"). Now all "nested" properties will be randomly chosen and fixed in place - not just the "top-level" properties. Here's an example of that.

Notes:

As mentioned above, the properties will be executed/fixed in the order that you declare them, so if property B references property A (with [this.A]), then you should make sure you've written B below A.
Here's a very simple example showing how to use it.
Here's an example showing how to make lower properties depend on higher ones. There's also an explanation on the examples page.
Here's an example showing how to use "deep" mode.
If you want to create a list of instances based on a blueprint (instead of just one instance), check out the create-instances-plugin.
Check out more plugins at perchance.org/plugins

# create-instances-plugin

Group: Core / Required Plugins

Create Instances Plugin
This is a version of the create-instance-plugin that allows you to create a list of instances of a particular blueprint. Have a look at this example:

createInstances = {import:create-instances-plugin}

character
  name = {Molly|Anita|Murphy}
 age = {18-90}
 ...
  
output
  [cs = createInstances(character, 5), ""]
Here I use the variable name cs to represent the list of 5 generated characters (but you can call it whatever you want). You can access the first character by writing cs[0], and the second by writing cs[1], and the third by writing cs[2], and so on. Why does it start at zero and not at one? Because JavaScript (the language on which Perchance is based) uses zero-based numbering.

So we could list the names of the 5 characters like this:

output
  [cs = createInstances(character, 5), ""] [cs[0].name] [cs[1].name] [cs[2].name] [cs[3].name] [cs[4].name]
And here's how you'd reference the first character using a new variable:

output
  [cs = createInstances(character, 5), firstChar = cs[0], ""] The first character's name is [firstChar.name].
You can treat cs just like any other list, so you can, for example, draw a random character from it like so: [char = cs.selectOne].

To use "deep" mode, as explained on the create-instance-plugin page, you'd write this:

output
  [cs = createInstances(character, 5, "deep"), ""] ......

Notes:

You'll want to read how to use the create-instance-plugin before trying to use this plugin.
Here's a simple example showing how to use this plugin.
Check out more plugins at perchance.org/plugins

# select-leaf-plugin

Group: Core / Required Plugins

ðŸ‚ Select Leaf Plugin ðŸ‚
Put this in your Perchance code panel:

selectLeaf = {import:select-leaf-plugin}

Now you can select a "leaf" item from your hierarchy:

[selectLeaf(myList)]
A "leaf" is an item that doesn't have any "children" - that is, a item that doesn't have any "sub-items" underneath it. Think of it like a tree. You start with a trunk, and then that trunk branches several times until you get to the twigs, and then you've got the leaves attached to those twigs:

trunk
  branch1
    subbranch
      leaf1
      leaf2
  branch2
    leaf3
    leaf4
  leaf5
  subbranch
   leaf6
   leaf7
You can treat the result of the selectLeaf(listName) just like you would with listName.selectOne, so you can do stuff like this, for example:

output
  The [a = selectLeaf(animal)] sits with the other [a.pluralForm].
  
animal
  mammal
    mouse
    deer
    marsupial
      kangaroo
      opossum
    monotreme
      platypus
  reptile
    lizard
    turtle
  bird
    flamingo
    dove

Notes:

Here's a simple example showing how to use it
Also see select-leaves-plugin for getting several leaves at once, and consumable-leaf-list-plugin if you want to make a consumableList out of all your leaf nodes so you can select a set of unique leaves.
Check out more plugins at perchance.org/plugins

# select-leaves-plugin

Group: Core / Required Plugins

ðŸŒ¿ Select Leaves Plugin ðŸŒ¿
This is the selectMany version of the selectLeaf plugin. See that plugin page for more details. Very briefly: just write this in your Perchance code panel:

selectLeaves = {import:select-leaves-plugin}

And then grab 10 items from your list like this:

[selectLeaves(myList, 10)]

Or grab between 5 and 10 items from your list like this:

[selectLeaves(myList, 5, 10)]

Notes:

Here's a simple example showing how to use it
If you want to make a consumableList of your leaf items so you get unique selections, check out the consumable-leaf-list-plugin
Check out more plugins at perchance.org/plugins

# select-all-leaves-plugin

Group: Core / Required Plugins

ðŸƒ selectAllLeaves Plugin ðŸƒ
This is plugin allows you to create a list that has all the "leaf" items in your hierarchy. See the select-leaf-plugin page to see what I mean by "leaf". Very briefly: just write this in your Perchance code panel:

selectAllLeaves = {import:select-all-leaves-plugin}
And then make your list, and use it like a normal one:

output
  [l = selectAllLeaves(myList)] [l] [l]
This plugin is also handy if you need to count the number of leaves in a list:

output
  myList has [selectAllLeaves(myList).getLength] leaves.
Notes:

Here's a simple example showing how to use it
You can also use l.selectOne, l.selectMany(...) and l.selectAll, just like with normal lists.
You may also like to check out the consumable-leaf-list-plugin.
Check out more plugins at perchance.org/plugins

# random-select-plugin

Group: Core / Required Plugins

Random Select Plugin
This plugin allows you to randomly select between two or more input lists or variables. It's a bit like the curly bracket notation for creating a quick inline random selection (e.g. {lizard|mouse|frog}) except it allows you to randomly randomly select lists/variable and produces a random list/variable instead of plain text.

That might sound a bit confusing. Let's look at an example.

Imagine that we have two lists, a and b. Now if we have x = {[a]|[b]} then will x.selectOne give us a reference to either the a or b list, or will it give is the "plain text" that results from evaluating a/b? The answer is the latter. That is, it will give us the plain text that results from evaluating the chosen (a or b) list. But what if we want x to give give us a reference to the a or b list? That's one example of where this plugin can come in handy.

To use it, you first need to import it by putting this line of code in your lists editor:

select = {import:random-select-plugin}
And now if you write this:

x = [select(a, b)]
then x will refer to either a or b (randomly selected with 50% probability). If you want to change the probability, you can add odds like so:

x = [select(a, b, null, 1, 2)]
That means "randomly select between a and b where a has odds of 1 and b has odds of 2". In other words, b is twice as likely as a. If you decode to specify odds, then you musty specify them for all items.

Notes:

Here's an example generator showing how you could use this plugin.
Check out this forum thread for the origin story of this plugin.
Check out more plugins at perchance.org/plugins

# consumable-leaf-list-plugin

Group: Core / Required Plugins

ðŸƒ consumableLeafList Plugin ðŸƒ
This is plugin allows you to create a consumable list out of all the "leaf" items in your hierarchy. See the select-leaf-plugin page to see what I mean by "leaf". Very briefly: just write this in your Perchance code panel:

consumableLeafList = {import:consumable-leaf-list-plugin}
And then make your consumable list, and use it like a normal one:

output
  [l = consumableLeafList(myList)] [l] [l]
Notes:

Here's a simple example showing how to use it
You can also use l.selectOne, l.selectMany(...) and l.selectAll, just like with normal consumableLists
Check out more plugins at perchance.org/plugins

# url-params-plugin

Group: Core / Required Plugins

URL Params Plugin
To use this plugin, you'll first need to import it by adding this line to your lists editor:

url = {import:url-params-plugin}
And now try putting this in your lists editor:

output
  In this page's current URL, 'blah' is set to [url.blah || "nothing"]
Here's an example generator with that code.

And you can of course use your URL data like you would with any other data/variables - for example:

output
  Here's an animal based on the URL's 'type' parameter: [animal.selectOne.selectOne]

animal
  mammal ^[url.type === "mammal"]
    mouse
    rabbit
  reptile ^[url.type === "reptile"]
    snake
    lizard
Here's an example of using a 'lang' parameter to change the language of your generator

output
  Here's a random fruit: [fruitEn.selectOne]     ^[url.lang === "en"]
  Voici un fruit au hasard: [fruitFr.selectOne]  ^[url.lang === "fr"]

fruitEn
  apple
  banana

fruitFr
  pomme
  banane
Notes:

Get started with this example.
This can be paired with the seeder-plugin to allow you to create unique links to specific generator outputs.
To add a parameters to a URL, you must add ? to the end of the URL, and then a list of name=value separated by &. So, for example, a URL with 3 parameters would look like this: <https://perchance.org?fruit=apple&animal=mouse&lang=english>
Currently you can only 'read'/'get' the URL parameters - you can't change them. If you want to change the current URL, you should instead create a link which the user can click to open the new URL.
(Note for curious web/JavaScript devs: Even though your generator runs within an iframe, it can 'see' the URL parameters of the parent window because Perchance copies those parameters over to the iframe when initializing it)
Check out more plugins at perchance.org/plugins
âš„ï¸Ž

# remember-plugin

Group: Core / Required Plugins

ðŸ’¾ Remember Plugin ðŸ’¾
Thanks to Vionet20 for their help with building this plugin.

This plugin allows you to make it so certain variables are "remembered" even if you refresh the page. For example, if you were building a random text adventure game using the goto plugin, you could use this plugin to "remember" the player's hit points, experience points, etc. so that your players don't lose their progress if they close the browser tab or refresh it (I've linked an example of this at the bottom of this page).

To use this plugin, put this code in your Perchance code panel (the main editor on the left-hand side):

remember = {import:remember-plugin}
and then write this at the top of your HTML panel (the bottom-right editor):

[remember(root, "a,b,c")]
and now the variables a, b and c will be remembered even after the page is reloaded. You can change a, b and c to whatever you want, and you can add as many of them as you want - just separate the variable names with commas like I've shown above.

As an example, imagine that we had some code like this in our Perchance code panel:

num = {1-10}
output
  [if (a == undefined) {a = num.selectOne} else {a}]
And this code is at the top of our HTML code panel:

[remember(root, "a")]
[output]
So now when you first load the page, a == undefined will evaluate to true and so the a = num.selectOne code will get executed, and thus a random number will get output. But if you refresh the page, then a == undefined is no longer true because the [remember(root, "a")] code has loaded the a variable from last time, and so the old value of a gets output every time we reload the page.

If you want to clear all the saved data, then just execute this code: [remember(root, "@forget")]. But note that this will reload the page as well. So, if you wanted to make a button that clears all the user's saved data, then you'd put this in your HTML panel:

<button onclick="remember(root, '@forget')">clear data</button>
Note that you don't need to put square brackets around code in HTML onclick attributes. Also note that you need to use single quotation marks (') around @forget since HTML attributes (like onclick) use double quotation marks to mark their start and end.

You can also use this plugin to remember the values in text inputs, drop-down menus, and other types of user inputs. You can learn how to add user inputs in the "User Inputs" section at perchance.org/examples. Here's how you can remember user inputs:

[remember(root, "@inputs")]
And you can remember both variables and user inputs like this:

[remember(root, "@inputs,myVariable,myOtherVariable")]
And, by the way, you can add spaces between the variable names if you prefer. Just make sure there are commas between them:

[remember(root, "@inputs, myVariable, myOtherVariable")]

Notes:

Here's a very simple example of how to use it.
Here's an example that includes some buttons to change the variable that's being remembered.
Here's a basic example showing how to remember a variety of user inputs
Here's an example of how to remember user text inputs
Here's an example of how to remember user range slider inputs
Here's an example of how to remember user checkbox inputs
Here's an example of how to remember user 'radio' inputs
Here's an example of how to use the remember and goto plugins together to people can save the current state in their text adventure and come back to it later
Here's an example of how to "remember" arrays/lists of items (advanced, ask on the forum if you need help)
Another way to 'remember' stuff even after the page is refreshed is to simply write [localStorage.blah="abc123"] and then when you refresh the page [localStorage.blah] will still output "abc123". This plugin actually just uses localStorage "behind the scenes". Note that you can only store text in localStorage - if you try to store a number, it'll get sneakily converted into the "text" form of that number when you put it in localStorage. So, for example, if you write [localStorage.blah=1, localStorage.blah+2] it'll output "12" instead of "3". Quite annoying. So you need to write [localStorage.blah=1, Number(localStorage.blah)+2]
If you change the URL of your generator, the remembered data will be lost. You can change the URL back to the orignal version to recover the data.
Check out more plugins at perchance.org/plugins

# google-sheets-plugin

Group: Core / Required Plugins

Google Sheets Plugin
This plugin allows you to import Google Sheets columns into your generator as Perchance lists. I generally don't recommend using it "long-term", since Google is known for shutting down their services/APIs when they become unprofitable (Google Sheets itself won't shut down, but they might change/remove the publishing options), and so if you try to use it as a permanent part of your generator, there's a decent chance that your generator will randomly stop working at some point in the future. That said, it may be useful for use during development, especially if you want multiple people to be able to work on your generator at the same time (since you can share edit access to your Google Sheet with others). But I'd recommend that you eventually copy your lists over to Perchance and remove the plugin once your generator is mostly finished. That will ensure that your generator "lives forever" :)

To make it so you can use your Google Sheet with this plugin you need to publicly "publish" it. To do that, go to the Google sheet that you want to use and click the "File" menu and then click "Publish to web" (or similar). You should see something like this. Change "Entire Document" to a single sheet (the default one is called "Sheet1"), and then change the output type from "Web page" to "Tab-separated values (.tsv)". Then click "Publish". You'll then be given a URL, and that's the URL that you need to use with this plugin. Make sure you copy the whole URL - it's quite long!

First you'll need to import this plugin by pasting this in your Perchance lists editor:

googleSheets = {import:google-sheets-plugin}
Then add a list with the settings for the plugin:

sheetsSettings
  urls
    <https://docs.google.com/spreadsheets/d/e/xMruYbv....OoEuPn/pub?gid\=0&single\=true&output\=tsv>
    <https://docs.google.com/spreadsheets/d/e/Yb2xM8u....Po3gOu/pub?gid\=0&single\=true&output\=tsv>
    // add all the URLs you want to load
Note: As shown in the above example (scroll to the right), you need to make sure you put a backslash (\) before each of the equals signs (=) in your URLs.

Now simply put this code at the top of your HTML editor:

[googleSheets(root, sheetsSettings)]
The root part tells the plugin where you want to "attach" the imported list data. Using root adds them as top-level lists, but you can use e.g. food if you had a list called food and wanted the imported lists to be made sub-lists of food. So it lets you decide on the "parent" of the imported lists.

Now here's what the plugin will do. Let's say you've got a spreadsheet like this:

The plugin will take the first item in each column and use that as the list name, then it will take all the items under that header and put them into the list - just like you'd probably expect. So after importing the plugin, if we were to write [veg] then we'd get a random vegetable.

BUT we're not finished yet. If you try the above instructions you'll notice that you get an error like "[fruit]" returned undefined. The problem is that Perchance tries to load the [fruit] list instantly when you load your generator, but Google Sheets takes a little while to return your data, so we end up with the errors because the lists don't exist yet when Perchance tries to find them. To "fix" this we can add some placeholder data while the Google Sheet loads:

fruit
  <b>loading...</b>
veg
  <b>loading...</b>
Now our [fruit] and [veg] outputs will display "loading..." (in bold) while the Google Sheets data loads.

You could actually just put not-quite-up-to-date versions of your lists in your generator, and then this plugin will just "override" those lists with up-to-date copies when it loads. That's a good way to ensure that your generator keeps working even if Google Sheets shuts down their publishing API.

Note that the plugin internally calls update() when the Google Sheets data has loaded, so it's as if the user clicks the "randomize" button after a second or so, which might be a bit annoying, so what if you wanted to only update a few specific elements? You can do that by adding an id to the elements that you want to update:

<p id="myCoolElement"> ... </p>
<div id="myOtherElement"> ... </div>
And then add an onLoad() => function as shown below, with a list of commands that you want to run after the data has been loaded:

sheetsSettings
  urls
    <https://docs.google.com/spreadsheets/d/e/xMruYbv....OoEuPn/pub?gid=0&single=true&output=tsv>
    <https://docs.google.com/spreadsheets/d/e/Yb2xM8u....Po3gOu/pub?gid=0&single=true&output=tsv>
  onLoad() =>
    update(myCoolElement)
    update(myOtherElement)
Here's an example of that. That way you can selectively update only the elements that actually need to use the data from the Google Sheet, rather than updating everything on the page.

Notes:

Here's a simple generator based on the above fruit and veg example to get you started.
It will take a while for the imported data to be updated after you edit your Google Sheet. This is just because Google only updates the published version every ~5 minutes, rather than instantly.
Use onLoad() => return if you don't want to update anything when the data loads.
As mentioned earlier, instead of passing root as the first input to the plugin, you can specify a list that you have in your generator, and the Google Sheets lists will get "attached" as sub-lists under that list. So if you had a list called "food" and you wrote googleSheets(food, ....), then you'd access your fruit and veg lists with [food.fruit] and [food.veg].
You can add odds notation (including dynamic odds like ^[a == 10]) to your items, but you can't currently create properties and sub-lists within your Google Sheets lists.
Check out more plugins at perchance.org/plugins
âš„ï¸Ž

# favicon-plugin

Group: Core / Required Plugins

ðŸ–¼ï¸ Favicon Plugin
This plugin allows you to change the little icon that's shown in the browser tab.

To use this plugin, you'll first need to import it by adding this line to your lists editor:

favicon = {import:favicon-plugin}
And then put this in the HTML (bottom-right) panel:

[favicon("https://example.com/foo.png")]
Here's an example generator so you can see it in action.

Important: You should upload your favicon images to perchance.org/upload. Don't link to a random image on the internet, since the average 'life expectancy' of a random URL on the internet is only a couple of years. Instead, download the image, then upload to perchance.org/upload, and you'll be given a permanent link to that image.

Here's a silly example where we make an "animated" favicon by changing it once per second through a series of animation frames.

Notes:

For mad scientists: You can pass a 'data URL' to this plugin. Here's an example that generates an image with the text-to-image-plugin, then set the tab icon to that image. You could also e.g. make a little dot on a blank canvas that moves around based on arrow key presses, and then send a data URL of each frame to this plugin to make a very tiny game that uses the browser tab icon as the "screen".
Check out more plugins at perchance.org/plugins
âš„ï¸Ž

# layout-maker-plugin

Group: Core / Required Plugins

Layout Maker Plugin
This plugin lets you create custom visual layouts for your generators without knowing HTML (the stuff in the bottom-right code editor panel). The general idea of this plugin is that you define they layout with a grid of letters, as you can see below. On the left, we define the text grid, and on the right is the layout that is generated.

a a a a b
a a a a b
c c c c c
âž¡
Once we've defined the grid of letters, we then just define the content that we want in each area.

Okay, let's see an actual example of how to use it. This code goes in your perchance code panel:

layoutMaker = {import:layout-maker-plugin}

layout
  debug = borders
  grid
    a a a a b
    a a a a b
    c c c c c
  areas
    a
      content = {hello|hi there} this is the "a" area
    b
      content = side bar thing ("b" area)
    c
      content = a sort of footer thing ("c" area)
And then put this somewhere in your HTML panel (bottom-right panel):

[layoutMaker(layout)]
And you'll get this:

hi there this is the "a" area
side bar thing ("b" area)
a sort of footer thing ("c" area)
Here's a version of the above example with debug = colors and with centered = true on each of the areas:

hello this is the "a" area
side bar thing ("b" area)
a sort of footer thing ("c" area)
You can make the grid as complex as you want - here's another example:

layout
 debug = colors
  grid
    t a a a b m
    t a a a b k
    c c c c c k
  d d g s s s
 areas
  s
   content = hello
   centered = true
  m
   content = {1|2|3}
   centered = true
3
hello
As you can see, you can use the debug = colors or debug = borders lines to easily visualise your layout, but you can take this line away once you're done "debugging" it. Also note the centered = true property that you can use to center the content of an area.

You can specify a style property for each area where you can put CSS rules that will be applied to that area:

layout
  grid
    a b c
    a b c
    a b c
  areas
    a
      content = aaa
   style = background-color:lightblue;
    b
      content = bbb
   style = border:1px solid lightgrey;
    c
      content = ccc
   style = background-color:orange;
aaa
bbb
ccc
And you can also apply CSS styles to the overall container:

layout
 debug = colors
 container
  style = height:100px; width:200px;
  grid
    a a a
    b b b
    c c c
Notice that we've made the layout smaller using style = height:100px; width:200px;? The default height is 300 pixels. If you want the overall height to compress down the the size of the content within, use style = height:auto; ..., like in this example:

layout
 debug = colors
 container
  style = height:auto;
  grid
    a a a a b
    a a a a b
    c c c c c
  e d d d d
  f f f f f
  areas
    a
      content = {hello|hi there} this is the "a" area
    b
      content = side bar thing ("b" area)
    c
      content = a sort of footer thing ("c" area)
  d
      content = another area
  e
   content = hi
    f
      content = hello
Here's what that looks like:

hello this is the "a" area
side bar thing ("b" area)
a sort of footer thing ("c" area)
hi
another area
hello
If you want your layout to take up the full height of the screen, add height:100vh; to the layout.container.style property like so:

layout
 container
  style = height:100vh;
 ...
You can change the relative sizes of each row, and of each column like this:

layout
 debug = borders
 columnSizes = 1fr 0.5fr 1fr
 rowSizes = 2fr 1fr 1fr
  grid
    a b c
  d e f
  g h i
So if you want the first column to be triple the width of the other two columns, we'd write columnWidths = 3fr 1fr 1fr, for example. And if your grid had 4 columns, then you'd need to write columnWidths = 3fr 1fr 1fr 1fr. If that's confusing, remember you can always ask for help on the community forum :)

You can define "gaps" in your layout like so:

layout
 debug = colors
  grid
    a a .
  b . c
  . . d
If you're feeling adventurous you can define layouts within layouts! This will put layout2 within the "b" area of layout1:

layout1
  grid
    a a a
  b b b
  c c c
 areas
  b
   content = [layoutMaker(layout2)]
   
layout2
  grid
    a b c
  a b c
  a b c
  
output
 [layoutMaker(layout1)]
With this type of "nesting" you could probably build random maps, dungeons, random houses (with random room layouts), and so on. If you do create something interesting like that, please share it with the community!

Notes:

You can use this simple example as a starting point for your creations.
Here's an example that has two different layouts depending on the size of your screen (e.g. one for mobile users, and one for desktop users). Also check out the responsive-layout-maker-plugin by Vionet20.
You need to make sure that each "area" that you've defined with letters is "rectangular" - e.g. you can't make an L-shaped area - it won't work.
If needed, you can define an id for an area by writing id = yourId in the area options (i.e. under the content = ... property). You can also set layout.container.id to give the container an id. Here's an example where we make a button that only updates a specific box in our layout.
Check out more plugins at perchance.org/plugins

# tooltip-plugin

Group: Core / Required Plugins

ðŸ’¬ï¸Ž Tooltip Plugin ðŸ’¬ï¸Ž
Put this in your Perchance code panel:

tooltip = {import:tooltip-plugin}
Now you can create tooltips:

[tooltip("â„¹ï¸", "tooltip text!")]
The above example would result in this (try hovering over it):

â„¹ï¸

So, as you can see, the format is:

[tooltip(anchorText, tooltipText)]

Here's an example of how you might want to use it:

output
  There is <b>[tooltip(race, description)]</b> standing nearby.

race
  an orc
  an elf
  a human
  
description
  They look suspicious.
  Their shirt is torn.
And you's get something like this:

There is an orc standing nearby.

You can customize the background color and the text color like so:

tooltipOptions
  css = background-color:tomato; color:yellow;
  ...

output
  Try <b>[tooltip("hovering over this text", "Here it is!", tooltipOptions)]</b> to see a custom-colored popup. Random num: {1-100000}
You can replace "tomato" and "yellow" with any valid CSS color, including completely custom hex codes like "#32a852". Here's an example which uses the above code.

If you'd like to include links (or other HTML) in the popup, you need to use these options:

tooltipOptions
  interactive = true
  allowHTML = true
  ...
  
output
  [tooltip(anchorText, tooltipText, tooltipOptions)]
The interactive option makes it so the popup doesn't dissapear when you try to move your mouse into it (e.g. to click a link that is within the popup/tooltip). The allowHTML option allows us to put HTML in the tooltip, so with these two options we could include a link within the tooltip like so:

tooltipOptions
  interactive = true  
  allowHTML = true

tooltipText
  <a href="https://i.imgur.com/26DZgXM.mp4" style="color:white;">Here's</a> the secret link. And the secret code is {1-100000000}

output
  You can [tooltip("hover over this text", tooltipText, tooltipOptions)] to get the secret link.
Here's an example which uses that code.

All customization options are listed on the tippyjs homepage.

Notes:

Here's an example of how you might use it.
Here's an example that uses the allowHTML option to embed an image in the tooltip.
Check out more plugins at perchance.org/plugins
This plugin is based on tippyjs, and so all credit for this functionality goes to the creator, Atomix!

# font-plugin

Group: Core / Required Plugins

Font Plugin
Put this in your Perchance code panel:

font = {import:font-plugin}

Here we output a random item from our animal list in the "Pacifico" font:

[font(animal, "Pacifico")]

All font names must be from Google Fonts (If you want to use a custom font, click here).

Here's another example to try:

[font(myList, "Permanent Marker")]

Make sure you change "myList" to the name of an actual list or variable/property in your generator. If you just want it to output some fixed text you can write this:

[font("hello there!", "Permanent Marker")]

which would output this:

hello there!

You can also change font size and color:

[font(myList.upperCase, "Courgette", "30px", "#ff5252")]

Use a hex color picker to get custom colors in #XXXXXX format.

If you want to change the color but not the size, then use 100% for the size to keep the size at the default:

[font(myList.upperCase, "Courgette", "100%", "#ff5252")]

You can (for example) write 70% to make the font 70% of the height of the "default" font size:

[font(myList.upperCase, "Courgette", "70%", "#ff5252")]

What if you want to change the default font of the whole page? Here you go:

[font(null, "Courgette", "25px", "pink")]

And to apply the font to a specific HTML element, just give the element an id as shown below, and then put the id as the first value:

<p id="myParagraph">Hello this is my [adjective] paragraph and it has a cool font.</p>
[font(myParagraph, "Courgette", "25px", "pink")]

Notes:

Here's a simple example generator where you can see this plugin in action.
Here's an example that changes the font of a specific HTML element.
Here's an example that changes the default font of the whole webpage.
Use a hex color picker to get custom colors in #XXXXXX format.
Check out more plugins at perchance.org/plugins

# markdown-plugin

Group: Core / Required Plugins

Markdown Plugin
Markdown is sort of like a more simple version of HTML. Have a look at this to get a idea of what it is. As a small example, to make bold text in HTML, you write <b>hello<b> whereas in markdown you simply write **hello**. This plugin converts the simple markdown syntax (that is made for human-readability) into HTML code that the browser understands. That's a very simple example, but you can do all sorts of things in markdown - even tables, numbered lists, and more (see that previous link for examples). Here's an example generator that uses this plugin.

Using the plugin is simple - just copy and paste this in your Perchance code panel, and then customize the text list:

markdown = {import:markdown-plugin}

output = [markdown(text)]

text

# My title

 The first line of my first paragraph.
 Second line of first paragraph.
 \s // <-- paragraph break
 You can *italicize* or **bold** your text easily.

## Sub-header

 Here's a list of items:

* Bullet point 1
* Bullet point 2
* Bullet point 3
  * Sub-bullet-point
* Bullet point 4
 \s  // <-- end lists like this too
 And we can do numbered lists too:

   1. First item
   2. Second item
   3. ~~Scratch this~~
 \s
 Adding a [link](https://dillinger.io) is easy with markdown.
 Images are easy too:
 \s
 ![image hover text](https://web.archive.org/web/20091018220201/http://www.geocities.com/roqofages/Rainbowflagwaving.gif)
 \s
 And you can still put HTML code in if needed:
 \s
 <video controls src\="<https://i.imgur.com/26DZgXM.mp4">></a>

 ```
 You can do code-blcks like this.
 Second line of code.
   Third line of code (indented)
 ```

 > And quoted text like this. Quotes automatically wrap: foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar.
 \s
 > Break quotes up into paragraphs using the \s trick.
  
 Header  | Header
 --------|---------
 You     | Can
 Make    | Neat
 Little  | Tables
 Too     | !
  
 So that's a brief intro to some of markdown's basic features!
And now writing [output] in the HTML panel will produce this:

My title
The first line of my first paragraph.
Second line of first paragraph.

Second paragraph. You can italicize or bold your text easily.

Sub-header
Here's a list of items:

Bullet point 1
Bullet point 2
Bullet point 3
Sub-bullet-point
Bullet point 4
And we can do numbered lists too:

First item
Second item
Scratch this
Adding a link is easy with markdown.
Images are easy too:

image hover tex

And you can still put HTML code in if needed:

You can do code-blcks like this.
Second line of code.
  Third line of code (indented)
And quoted text like this. Quotes automatically wrap: foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar foo bar.

Break quotes up into paragraphs using the \s trick.

Header Header
You Can
Make Neat
Little Tables
Too !
So that's a brief intro to some of markdown's basic features!

Notes:

Check out the example generator!
Full markdown cheetsheet here.
All thanks goes to the contributors of markedjs on github!
Check out more plugins at perchance.org/plugins

# background-image-plugin

Group: Core / Required Plugins

The Background Image Plugin
To add a background image to your generator, first put this in your Perchance code panel:

background = {import:background-image-plugin}

Then put this anywhere in your bottom-right (HTML) panel:

[background("https://i.imgur.com/64c6NnI.jpg")]
Change the image URL to one of your choosing. Just make sure to keep the quotation marks around it.

Also, make sure that it's a direct URL to your image (usually ending in jpg or png or gif, though not always). To get a direct link to an image, right-click on an image and select "Copy image address" or "Copy image location" or similar - depending on your web browser.

Important: You should upload your image to somewhere like catbox.moe or perchance.org/upload. You should not use an image link directly from a random website on the internet, because it could get deleted/moved or the website could shut down, and then your background would no longer work. Instead, go to perchance.org/upload and drag-and-drop or paste the image (or the URL) there, and it'll upload, and then it'll give you the URL. That way your background image will last forever.

I previously recommended uploading to Imgur, but they've started deleting old images. Luckily we now have perchance.org/upload, so use that instead.

Here's how we can set the image opacity (transparency) to 0.7 and blur to 5px:

[background("https://i.imgur.com/64c6NnI.jpg", 0.7, 5)]

Or, if you need some fancy effects, pass in a CSS filter string as the second parameter:

[background("https://i.imgur.com/64c6NnI.jpg", "blur(3px) hue-rotate(30deg) saturate(1.6)")]
You can see examples of CSS filters in use here.

Note that you don't have to call it background:

// in lists editor:
backgroundImage = {import:background-image-plugin}
// in HTML editor:
[backgroundImage("https://i.imgur.com/64c6NnI.jpg")]
You can also randomize the image every time the randomize button is clicked by using code like this:

// in lists editor:
backgroundImage = {import:background-image-plugin}

imageUrl
  <https://i.imgur.com/64c6NnI.jpg>
  <https://i.imgur.com/Hvb6HTy.jpg>
  <https://i.imgur.com/ecKzF9F.jpg>
  <https://i.imgur.com/785rHFl.jpg>
  
// in HTML editor:
[backgroundImage(imageUrl)]
Need more advanced features? Add this to your Perchance code panel:

bgData
  url = <https://i.imgur.com/64c6NnI.jpg>
  size = cover
  repeat = no-repeat
 position = center
 opacity = 0.8
  filter = blur(10px)
And then add this to your HTML code panel:

[background(bgData)]
Learn more about each property in the bgData list above:

size: cover will ensure your image covers the whole page. contain will ensure your whole image fits within the page. 23px will set the width of the image to 23 pixels (the height will adjust to maintain correct aspect ratio). 45px 78px will set the width to 45 pixels and the height to 78 pixels.
position: center will center your image on the page. left will align it left. Consult this image for more details.
repeat: no-repeat will prevent your image from being "tiled" multiple times across the page. Consult this image for more details.
filter: allows you to add custom CSS filters to adjust your image - e.g. to make it greyscale or adjust the saturation. See this page for examples.
opacity: adjust the transparency of the background image with a value between 0 (fully transparent) and 1 (completely opaque).
You don't have to use all the properties - just delete the ones you don't want and they'll use default values. Here's an example generator that uses these advanced features. Also note that you don't need to call the list bgData - you can call it whatever you want.

Here are some backgrounds to try out:

pastel tiles:       <https://i.imgur.com/0CWEecq.jpg>
books:              <https://i.imgur.com/Hvb6HTy.jpg>
pine forest:        <https://i.imgur.com/ecKzF9F.jpg>
dark leaves:        <https://i.imgur.com/785rHFl.jpg>
rocky coastline:    <https://i.imgur.com/E4a7yi0.jpg>
night building:     <https://i.imgur.com/9hrHir1.jpg>
jelly fish:         <https://i.imgur.com/EyLiFMs.jpg>
cloud sunset:       <https://i.imgur.com/M3wXrLE.jpg>
summer sunset:      <https://i.imgur.com/YRUgc7j.jpg>
desert dunes:       <https://i.imgur.com/P4FoRy2.jpg>
jagged mountains:   <https://i.imgur.com/mSarpKO.jpg>

Tips:

Here's a simple example generator that uses this plugin
Here's an example with a random background image
Here's an example that uses advanced features
Use images that you're legally allowed to use (Unsplash is awesome - all the images are free)
Upload your image to a place where it wont be deleted (e.g. Imgur)
Your image url must end in .jpg, .png, etc. (i.e. must be a direct link - right-click on the image and click "Copy image address" or "Copy image location", depending on your browser)
Ideally your image would be at least 1500px wide
Lowering the opacity a bit and adding blur can help bring your content forward
Using images that aren't super bright and saturated also helps
Check out more plugins at perchance.org/plugins
