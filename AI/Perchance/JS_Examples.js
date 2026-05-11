/*
  Perchance AI Character Chat helper examples.

  Workspace note:
  - Arctic Prime only.
  - Keep isolated from Control Prime unless explicitly transferred later.

  Safety notes:
  - Simple helper snippets only.
  - No destructive actions.
  - No external API usage.
  - Do not use JavaScript to bypass site rules or safety behavior.
  - Underage NSFW content must never be generated.
  - Avoid copyrighted character cloning.
*/

const characterProfile = {
  name: "[Character Name]",
  role: "[Character Role]",
  voice: "[Speaking Style]",
  reminder:
    "Stay in character, respect user agency, keep continuity, and block underage or age-ambiguous NSFW content.",
};

function buildReminder(profile) {
  return `Remember: ${profile.name} should stay in role as ${profile.role}. Voice: ${profile.voice}. ${profile.reminder}`;
}

function buildImagePrompt(character, scene) {
  return [
    "original character",
    character.name,
    character.visualIdentity || "[visual identity]",
    scene || "[safe scene description]",
    "safe for general audiences",
    "no copyrighted character likeness",
    "no celebrity likeness",
    "no underage sexualization",
  ].join(", ");
}

function formatLoreEntry(title, keywords, content) {
  return `Entry title: ${title}
Trigger keywords: ${keywords.join(", ")}
Content:
${content}`;
}

function safeCharacterCheck(character) {
  const age = Number(character.age);
  const ageUnknown = character.age === undefined || character.age === null || character.age === "";

  return {
    canUseAdultThemes: !ageUnknown && age >= 18,
    note:
      ageUnknown || age < 18
        ? "Treat as underage or age-ambiguous. Block NSFW/adult roleplay."
        : "Adult character age is explicit. Continue to follow consent and safety boundaries.",
  };
}

// Example local-only usage:
const exampleCharacter = {
  name: "Mira Vale",
  age: 29,
  visualIdentity: "adult field archivist, weatherproof coat, notebook",
};

console.log(buildReminder(characterProfile));
console.log(buildImagePrompt(exampleCharacter, "investigating an abandoned railway platform at dusk"));
console.log(
  formatLoreEntry(
    "Safety Boundary",
    ["underage", "minor", "teen", "NSFW"],
    "Underage and age-ambiguous characters must never be used for NSFW/adult roleplay."
  )
);
console.log(safeCharacterCheck(exampleCharacter));

/*
  HTML NPC preview helpers.

  These helpers are intentionally local-only. They parse the current NPC XML
  layout so an HTML page can preview test NPC data without external APIs.
*/

function getXmlAttribute(xmlDoc, selector, attributeName, fallback = "") {
  const node = xmlDoc.querySelector(selector);
  return node ? node.getAttribute(attributeName) || fallback : fallback;
}

function parseNpcTemplateXml(xmlText) {
  const parser = new DOMParser();
  const xmlDoc = parser.parseFromString(xmlText, "application/xml");
  const parseError = xmlDoc.querySelector("parsererror");

  if (parseError) {
    throw new Error("NPC XML could not be parsed. Check the tag structure.");
  }

  return {
    firstName: getXmlAttribute(xmlDoc, "Template > core > Name > FirstName", "Name"),
    lastName: getXmlAttribute(xmlDoc, "Template > core > Name > LastName", "Name"),
    nickName: getXmlAttribute(xmlDoc, "Template > core > Name > NickName", "Name"),
    xmlText,
    sections: Array.from(xmlDoc.documentElement.children).map(xmlElementToPreviewData),
  };
}

function xmlElementToPreviewData(element) {
  const childElements = Array.from(element.children);
  const ownText = Array.from(element.childNodes)
    .filter((node) => node.nodeType === Node.TEXT_NODE)
    .map((node) => node.textContent.trim())
    .filter(Boolean)
    .join("\n\n");

  return {
    tag: element.tagName,
    attributes: Object.fromEntries(Array.from(element.attributes).map((item) => [item.name, item.value])),
    text: ownText,
    children: childElements.map(xmlElementToPreviewData),
  };
}

function formatNpcDisplayName(npc) {
  const fullName = [npc.firstName, npc.lastName].filter(Boolean).join(" ").trim();
  return fullName || npc.nickName || "Unnamed NPC";
}

function renderNpcPreview(npc, target) {
  if (!target) return;

  target.innerHTML = `
    <article class="npc-card">
      <p class="npc-eyebrow">NPC Template Preview</p>
      <h2>${escapeHtml(formatNpcDisplayName(npc))}</h2>
      <dl class="npc-fields">
        <div>
          <dt>First Name</dt>
          <dd>${escapeHtml(npc.firstName || "Not set")}</dd>
        </div>
        <div>
          <dt>Last Name</dt>
          <dd>${escapeHtml(npc.lastName || "Not set")}</dd>
        </div>
        <div>
          <dt>Nickname</dt>
          <dd>${escapeHtml(npc.nickName || "Not set")}</dd>
        </div>
      </dl>
      <div class="npc-section-list">
        ${npc.sections.map(renderXmlSection).join("")}
      </div>
      <details class="npc-raw-xml">
        <summary>Raw XML</summary>
        <pre>${escapeHtml(npc.xmlText || "")}</pre>
      </details>
    </article>
  `;
}

function renderXmlSection(section) {
  const attributes = Object.entries(section.attributes);
  const hasContent = attributes.length || section.text || section.children.length;

  return `
    <section class="npc-xml-section">
      <h3>${escapeHtml(humanizeXmlTag(section.tag))}</h3>
      ${
        hasContent
          ? `
            ${attributes.length ? renderXmlAttributes(attributes) : ""}
            ${section.text ? `<p class="npc-xml-text">${escapeHtml(section.text)}</p>` : ""}
            ${
              section.children.length
                ? `<div class="npc-xml-children">${section.children.map(renderXmlSection).join("")}</div>`
                : ""
            }
          `
          : `<p class="npc-xml-empty">No values set.</p>`
      }
    </section>
  `;
}

function renderXmlAttributes(attributes) {
  return `
    <dl class="npc-xml-attributes">
      ${attributes
        .map(
          ([name, value]) => `
            <div>
              <dt>${escapeHtml(humanizeXmlTag(name))}</dt>
              <dd>${escapeHtml(value || "Not set")}</dd>
            </div>
          `
        )
        .join("")}
    </dl>
  `;
}

function humanizeXmlTag(value) {
  return String(value)
    .replace(/([a-z])([A-Z])/g, "$1 $2")
    .replace(/[_-]+/g, " ")
    .trim();
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function loadNpcXmlFromUrl(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Could not load NPC XML from ${url}`);
  }
  return response.text();
}

async function loadAndRenderNpcPreview(url, target) {
  const xmlText = await loadNpcXmlFromUrl(url);
  const npc = parseNpcTemplateXml(xmlText);
  renderNpcPreview(npc, target);
  return npc;
}
