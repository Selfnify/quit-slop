# Recipes

Starting points, not templates. Adapt colour, type and layout to the direction chosen in the main skill so these do not become the same look on every site.

## Backgrounds that fix flat designs

Pick one per design, only if the design feels flat without it. Keep it subtle, keep text contrast intact. A plain surface is a valid choice.

1. Felt texture: fine noise grain over a flat tone (SVG `feTurbulence` or a tiled noise PNG at 3 to 6% opacity)
2. Fluted glass: vertical ridges refracting a soft gradient behind them
3. Thermal gradients: heat-map style blends of warm and cool tones, blurred, slowly drifting
4. Water ripples: concentric distortion shader or displacement, slow and low contrast

## Password screen recipe

1. Cut the red rule checklist and the confirm field
2. Enforce strict rules silently and block common passwords
3. Recommend a secure generated password so choosing feels effortless
4. Make the input outline the strength meter (the border fills and shifts colour as strength grows)
5. Use monospace characters so dots morph into letters smoothly with no width jump

## Chat screen recipe

1. Drop the ugly purple
2. Background: pick one that fits the direction (a soft two-colour shader, a cream base near `#F4F1EA`, a cool neutral for a tool). Do not default to the same one every time
3. Add suggested text prompts
4. Show each step the assistant takes and cite every claim
5. Lay out each paragraph block before it streams so text never jumps
6. Make the plan interactive and pre-empt the next action so it feels proactive

## Liquid glass recipe

Chromium only for `backdrop-filter: url(#filter)`. Always ship a fallback.

Structure:

```html
<div class="liquidglass" id="glass">
  <svg class="glass-surface__filter" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <filter id="glass-filter" color-interpolation-filters="sRGB" x="0%" y="0%" width="100%" height="100%">
        <feImage id="glass-map" x="0" y="0" width="100%" height="100%" preserveAspectRatio="none" result="map"/>
        <feDisplacementMap in="SourceGraphic" in2="map" scale="-20" xChannelSelector="R" yChannelSelector="G" result="dispRed"/>
        <feColorMatrix in="dispRed" type="matrix" values="1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0" result="red"/>
        <feDisplacementMap in="SourceGraphic" in2="map" scale="-24" xChannelSelector="R" yChannelSelector="G" result="dispGreen"/>
        <feColorMatrix in="dispGreen" type="matrix" values="0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0" result="green"/>
        <feDisplacementMap in="SourceGraphic" in2="map" scale="-28" xChannelSelector="R" yChannelSelector="G" result="dispBlue"/>
        <feColorMatrix in="dispBlue" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0" result="blue"/>
        <feBlend in="red" in2="green" mode="screen" result="rg"/>
        <feBlend in="rg" in2="blue" mode="screen" result="output"/>
        <feGaussianBlur in="output" stdDeviation="3"/>
      </filter>
    </defs>
  </svg>
  <div class="glass-content">Content</div>
</div>
```

CSS:

```css
:root {
  --glass-frost: 0.1;
  --glass-saturation: 1.2;
  --filter-id: url(#glass-filter);
}

.liquidglass {
  position: relative;
  width: min(340px, 90vw);
  min-height: 140px;
  border-radius: 9999px;
  background: hsl(0 0% 0% / var(--glass-frost, 0));
  -webkit-backdrop-filter: blur(12px) saturate(var(--glass-saturation, 1));
  backdrop-filter: blur(12px) saturate(var(--glass-saturation, 1));
  box-shadow:
    inset 0 0 2px 1px #ffffff59,
    inset 0 0 10px 4px #ffffff26,
    inset 0 4px 16px #11111a0d,
    inset 0 8px 24px #11111a0d,
    inset 0 6px 56px #11111a0d;
}

@supports (backdrop-filter: url(#x)) {
  .liquidglass {
    -webkit-backdrop-filter: var(--filter-id) saturate(var(--glass-saturation, 1));
    backdrop-filter: var(--filter-id) saturate(var(--glass-saturation, 1));
  }
}

.glass-surface__filter {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  z-index: -1;
  pointer-events: none;
}

.glass-content {
  position: relative;
  padding: clamp(16px, 4vw, 28px);
}
```

Displacement map (rebuild on resize so it stays responsive, no giant base64 blob):

```js
function glassMap(w, h, r, border = 0.07, blur = 11, brightness = 50, opacity = 0.93) {
  const edge = Math.min(w, h) * (border * 0.5);
  const svg = `<svg viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="r" x1="100%" y1="0%" x2="0%" y2="0%"><stop offset="0%" stop-color="#0000"/><stop offset="100%" stop-color="red"/></linearGradient><linearGradient id="b" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#0000"/><stop offset="100%" stop-color="blue"/></linearGradient></defs><rect width="${w}" height="${h}" fill="black"/><rect width="${w}" height="${h}" rx="${r}" fill="url(#r)"/><rect width="${w}" height="${h}" rx="${r}" fill="url(#b)" style="mix-blend-mode:difference"/><rect x="${edge}" y="${edge}" width="${w - edge * 2}" height="${h - edge * 2}" rx="${r}" fill="hsl(0 0% ${brightness}% / ${opacity})" style="filter:blur(${blur}px)"/></svg>`;
  return `data:image/svg+xml,${encodeURIComponent(svg)}`;
}

const glass = document.getElementById("glass");
const map = document.getElementById("glass-map");
const update = () => {
  const { width, height } = glass.getBoundingClientRect();
  const r = parseFloat(getComputedStyle(glass).borderTopLeftRadius) || 0;
  map.setAttribute("href", glassMap(Math.round(width), Math.round(height), Math.min(r, height / 2)));
};
new ResizeObserver(update).observe(glass);
update();
```

Notes:

1. Give each glass instance a unique filter id if there are several on one page
2. The glass needs a rich, colourful background behind it or the effect is invisible
3. Keep `pointer-events: none` only on the filter svg, not on interactive content
4. Fixed centred glass: use `left: 50%; top: 50%; transform: translate(-50%, -50%)`
5. Safari and Firefox get the plain blur fallback, which is fine
