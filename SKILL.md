---
name: quit-slop
description: Design and copy rules that strip AI slop from websites and UIs and make them feel crafted for one specific product. Covers design direction, hard rules, writing the actual copy (headlines, buttons, empty states, errors), UX decisions, and a scripted check for common tells. Make sure to use this skill whenever the user is designing, creating, redesigning, restyling, polishing, writing copy for, or reviewing any website, landing page, web app, dashboard, component, or UI, even if they never say "slop" or "design system". Also use it for animation, motion, micro-interaction, typography, microcopy, or glass effect requests.
---

# Quit slop

The goal is a design that looks like someone with taste made it for this one product. Removing slop is the floor, not the goal. A site can pass every rule below and still be generic, so the order matters.

Run in this order: direction, hard rules, copy, UX decisions, craft pass, verify.

## 1. Pick a direction before touching any style

Settle three things first (in your head, not in the output):

- Who uses this, and what are they trying to do in the next 30 seconds
- The feel in three words, plus one real reference (a magazine, a tool, a shop, a printed manual)
- The one thing someone should remember about the design

Then derive type, colour, layout and motion from that direction. These six are starting points, not a menu you must pick from. Blend or invent when the product calls for it.

| Direction | Type | Colour | Layout | Motion |
|---|---|---|---|---|
| Editorial | Serif display, clean sans body | Paper neutrals, ink, one muted accent | Asymmetric columns, big type, wide margins | Slow fades, no bounce |
| Tool | One grotesque sans, mono for data | Cool neutrals, one saturated accent | Dense grid, tables, keyboard first | Almost none |
| Warm craft | Soft serif or humanist sans | Cream, clay, deep green | Loose grid, real photography | Gentle springs |
| Technical | Mono forward | Near black or off white, one signal colour | Strict grid, code as the hero | Instant, snappy |
| Playful | Chunky display face | Flat bold colours, two accents | Oversized shapes, tilted pieces | Expressive but short |
| Quiet luxury | High contrast serif or light wide-tracked sans in sentence case | Stone, bone, black | Few elements, lots of empty space | Slow ease-out reveals |

Variation rules:

- A default is not a decision. If you picked a font, colour, or layout because it is what you always pick, pick again.
- Do not reuse the same font pair, accent hue and layout skeleton as the previous build in this conversation.
- If the user gave brand guidelines, an existing design system, or screenshots, those win over everything here, including the hard rules.

## 2. Hard rules

These apply to every build unless the user's brand says otherwise.

1. No em dashes anywhere in copy. Use a comma, colon, period, or hyphen.
2. No all caps text (RECENT, PRODUCTS, NEW). Sentence case everywhere, including when `text-transform: uppercase` would do it for you.
3. No purple gradients. Pick one accent colour that fits the product.
4. No eyebrows (the tiny label above a headline).
5. No unnecessary text. If a label repeats what the UI already says, delete it.
6. Keep spacing clean and on one scale. Group related things with space, not boxes.
7. No unnecessary dots (status dots, bullet dots, decorative dots).
8. No unnecessary badges, pills, or chips.
9. No fake content. No lorem ipsum, "John Doe", invented testimonials, invented logos, or invented statistics. Use clearly marked placeholders or ask for real content.

## 3. Copy

Generic writing is the loudest slop signal and the rules above barely touch it. Write the words before you design around them.

- The headline says what the product does, for whom, in plain words. "Deploy your bot from GitHub in one push" beats "Ship faster with confidence".
- Use concrete nouns and verbs. Replace adjectives with numbers, names, or examples.
- Buttons are verb plus object: "Create project", "Send invite". Never "Submit", "Click here", "Get started" on its own.
- Errors say what happened and what to do next. Empty states say what goes here and how to add the first one.
- No filler openers or stock phrases: "Welcome to", "In today's fast-paced world", "Say goodbye to", "Unlock", "Supercharge", "Elevate", "Seamless", "Revolutionize", "Empower", "All-in-one", "Next-generation", "Take X to the next level".
- No reflex triads ("fast, simple, and secure") and no "It's not just X, it's Y" constructions.
- One voice per product. Match it to the direction: an editorial site can be wry, a tool should be terse.
- Cut every sentence that would survive a find-and-replace of the product name. That is the swap test.

## 4. UX decisions

Answer these before laying anything out:

1. What is the one primary action in this view? Make it obvious, make everything else quieter.
2. What can be removed without hurting the task? Remove it.
3. Design every state, not just the happy path: empty, loading, error, success, partial. Use shimmer skeletons instead of spinners for loading.
4. Mobile first: reachable with a thumb, 44px minimum touch targets, respect `env(safe-area-inset-*)`.
5. Accessibility floor: text contrast 4.5:1 (3:1 for large text), visible focus on every interactive element, real `<button>` and `<a>` elements, labels on inputs, never colour alone for meaning, honour `prefers-reduced-motion`.
6. Forms: labels above fields, ask for less, validate after blur, accept messy input (spacing, casing, formats), put the error next to the field.
7. Navigation: about seven top-level items at most, the current location is obvious, follow conventions people already know.

When a situation matches, reach for the law:

| Situation | Law | Do this |
|---|---|---|
| Primary action is small or far | Fitts | Make it bigger and closer, pad the hit area |
| Too many equal choices | Hick | Cut options or add one recommended default |
| A long flat list of info | Miller | Chunk into groups of about seven or fewer |
| Something takes time | Doherty | Respond under 400ms or show progress |
| Unusual pattern for a common task | Jakob | Use the convention users already know |
| Frequent action | Frequency of use | Lighter or no animation |
| Input formats vary | Postel | Accept liberally, output strictly |
| Dense settings or detail | Progressive disclosure | Basics first, detail on demand |

More principles, timings and terms live in `references/motion.md`. Read it when the task involves animation, micro-interactions, or typography details.

## 5. Craft pass

Apply once the structure and copy are settled.

Remove
1. Delete filler badges
2. Drop redundant labels
3. Remove embellishments (extra borders, glows, shadows, dividers)

Structure
4. Group with space
5. Show the actual product, not abstract illustration
6. Enlarge the main feature
7. Emphasize the CTA, one primary action per view
8. Use a design system (tokens for colour, type, spacing, radius)
9. Add one accent colour

Type
10. Un-italicize random words
11. Use mono only where it is needed (numbers, code, passwords)
12. Wrap headlines properly (`text-wrap: balance`, no widows)
13. Use tabular numbers (`font-variant-numeric: tabular-nums`)
14. Tighten tracking on large headlines, keep body line height near 1.5 and line length 45 to 75 characters

Detail
15. Keep icons consistent (one set, one stroke weight, one size grid)
16. Inner radius = outer radius minus padding
17. Align by eye, not pixels (optical alignment for icons, play buttons, text)

Motion
18. Add loading states
19. Animate useful feedback only

Backgrounds, and recipes for password screens, chat screens, and liquid glass, are in `references/recipes.md`. Treat them as starting points to adapt to the direction, not templates to copy.

## 6. Verify

1. Run the scripted check on everything you wrote:

   `python scripts/slop_check.py <file-or-folder>`

   Fix every error. Read each warning and either fix it or have a reason to keep it.
2. Swap test: would the headline and body copy still work with a competitor's name in it? If yes, rewrite.
3. Squint test: blur your eyes at the layout. Is there one clear focal point and an obvious order to read in? If not, fix the hierarchy.
4. State test: did you design empty, loading and error, or only the happy path?
5. Variation test: if you built something earlier in this conversation, is this one visibly different in type, colour and layout?

When you present the result, say in one or two lines what direction you chose and the main decisions. Do not recite the rules or narrate the checks.
