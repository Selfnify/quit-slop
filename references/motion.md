# Motion, UX principles and design terms

Reference for the quit-slop skill. Apply the ones that fit the task and the chosen direction. Do not force all of them into one screen.

Quick defaults when unsure: entrances ease-out, moves ease-in-out, UI motion under 300ms, exits about 20% shorter than entrances, no bounce on everyday UI, always honour `prefers-reduced-motion`.

## Principles of UX and animation

Apply the ones that fit. Do not force all of them into one screen.

1. Squash and stretch: elements deform slightly with motion to feel physical
2. Anticipation: a small wind-up before a big move (button dips before launching a modal)
3. Staging: direct focus to one thing at a time, dim or blur the rest
4. Pose to pose: define start and end states first, let easing fill between
5. Follow through: parts settle after the main body stops
6. Slow in and slow out: ease curves, never linear for movement
7. Arcs: natural motion curves, not straight lines
8. Secondary actions: small supporting motion that sells the main one
9. Snappy timing: fast feels responsive, UI motion mostly under 300ms
10. Exaggerated feedback: make confirmation clear, but not cartoonish
11. Solid drawing: respect depth, light, and shadow consistency
12. Appeal: the whole thing should feel intentional and pleasant
13. Fitts's law: big, close targets are faster to hit
14. Bigger hit areas: at least 44px touch targets, pad the click area beyond the visual
15. Hick's law: fewer choices, faster decisions
16. Miller's law: chunk info into groups of about 7 or fewer
17. Doherty threshold: respond under 400ms or show progress
18. Postel's law: be liberal in what you accept (formats, spacing, casing), strict in what you output
19. Jakob's law: users expect your site to work like the ones they know
20. Frequency of use: the more often an action happens, the lighter its animation should be

## 20 design terms to apply deliberately

1. Kerning: adjust space between specific letter pairs in large display text
2. Optical centre: centre by eye, play icons sit slightly right, shapes slightly up
3. Tabular numbers: `font-variant-numeric: tabular-nums` for prices, timers, tables
4. Layout shift: reserve space for images, fonts, and async content
5. Tracking: letter spacing, tighten large headlines, loosen small text slightly
6. Optimistic update: show the result instantly, reconcile with the server after
7. X-height: pick fonts with a generous x-height for UI text
8. Touch target: 44px minimum
9. Leading: line height, about 1.5 for body, 1.1 to 1.2 for headlines
10. Origin-aware animation: scale and slide from where the trigger is
11. OKLCH: define colours in `oklch()` for even lightness across hues
12. Widow: avoid a single word alone on the last line
13. Safe area: respect `env(safe-area-inset-*)` on phones
14. Stagger: offset sequential items slightly
15. Line length: 45 to 75 characters for reading text
16. Affordance: things should look like what they do
17. Combobox: searchable select instead of a giant dropdown
18. Interruptible animation: a new input can cancel or reverse a running animation smoothly
19. Progressive disclosure: show the basics first, reveal detail on demand
20. Shared element transition: an element morphs between screens instead of cutting

## 20 ways to make beautiful animations

1. Ease-out for entrances
2. Dropdowns at 150 to 250ms
3. Stagger list rows by 30ms
4. Scale to 0.97 on press
5. Stretch moving knobs by 12%
6. Stagger as details settle
7. Arcs for object movement
8. Pulse to confirm success
9. Ease-in-out for moves between positions
10. Start popovers at scale 0.95
11. Enter from the trigger
12. Exit to the trigger
13. No bounce on everyday UI
14. Do not tween while the user is holding or dragging, track the pointer directly
15. Make exits about 20% shorter than entrances
16. Overlap old and new states during a swap
17. Use masks for reveals and colour changes
18. Crossfade icons with a small blur
19. Rubber band past scroll or drag bounds
20. Reuse the same `layoutId` for shared element morphs

Always honour `prefers-reduced-motion`.
