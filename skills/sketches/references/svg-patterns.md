# SVG Sketch Patterns Reference

Load this file when building sketches, wireframes, or diagrams. It contains reusable SVG snippet patterns, hand-drawn style techniques, color palettes, and layout grids.

## Table of Contents

1. [Hand-Drawn Style Techniques](#hand-drawn-style-techniques)
2. [Sketch Primitives](#sketch-primitives)
3. [Arrows and Connectors](#arrows-and-connectors)
4. [Text Labels and Annotations](#text-labels-and-annotations)
5. [Icons and Symbols](#icons-and-symbols)
6. [Color Palettes](#color-palettes)
7. [Wireframe Layout Grids](#wireframe-layout-grids)
8. [Complete Examples](#complete-examples)

---

## Hand-Drawn Style Techniques

### Jittered Paths (Core Technique)

Replace straight `<rect>` and `<line>` elements with `<path>` elements that add slight randomness to each point. This is the single most important technique for the sketchy aesthetic.

**Straight line to sketchy line:**

```xml
<!-- Clean (avoid) -->
<line x1="50" y1="50" x2="250" y2="50"/>

<!-- Sketchy (use this) -->
<path d="M 50,51 C 90,48 130,53 170,49 C 210,52 240,48 250,51"
      stroke="#333" stroke-width="2" fill="none"
      stroke-linecap="round"/>
```

**Formula for jitter:** For each control point, offset x by random(-2, 2) and y by random(-2, 2). Use cubic beziers (C) for smooth wobble, or quadratic (Q) for sharper wobble.

### Sketchy Rectangle

Replace `<rect>` with a 4-segment path. Each corner gets 1-3px of random offset.

```xml
<!-- Sketchy box: 200x100 at position (50, 50) -->
<path d="M 51,52 C 90,49 160,53 248,51
         C 251,75 249,110 251,149
         C 200,152 100,148 52,151
         C 49,120 51,80 49,52"
      stroke="#333" stroke-width="2" fill="#fef9e7"
      stroke-linecap="round" stroke-linejoin="round"/>
```

**Algorithm to generate sketchy rect(x, y, w, h):**

```
jitter = () => random(-2, 2)
top-left:     (x + jitter(), y + jitter())
top-right:    (x + w + jitter(), y + jitter())
bottom-right: (x + w + jitter(), y + h + jitter())
bottom-left:  (x + jitter(), y + h + jitter())
```

Connect with cubic beziers. Add 1-2 midpoint control points per edge with jitter applied.

### Sketchy Circle / Ellipse

Draw a circle as a slightly imperfect closed path using bezier curves. Overshoot the closure slightly.

```xml
<!-- Sketchy circle at (150, 150) radius ~40 -->
<path d="M 150,110 C 175,108 192,128 191,150
         C 193,172 174,192 150,191
         C 126,193 108,173 109,150
         C 107,127 126,109 152,110"
      stroke="#333" stroke-width="2" fill="none"
      stroke-linecap="round"/>
```

### Double-Stroke Effect

Draw the same shape twice with slight offset for a "drawn twice" look common in whiteboard sketches.

```xml
<g opacity="0.9">
  <path d="M 50,50 C 100,48 200,52 250,50" stroke="#333" stroke-width="1.5" fill="none"/>
  <path d="M 51,52 C 100,50 200,54 249,51" stroke="#333" stroke-width="1.5" fill="none" opacity="0.4"/>
</g>
```

### Slight Rotation

Apply small rotation transforms (0.5-2 degrees) to groups for a casual, placed-by-hand feel.

```xml
<g transform="rotate(-1.2, 150, 100)">
  <!-- box content here -->
</g>
```

### Cross-Hatch Fill

For shaded areas, use a pattern of diagonal lines instead of solid fill.

```xml
<defs>
  <pattern id="hatch" width="8" height="8" patternTransform="rotate(45)"
           patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="0" y2="8" stroke="#999" stroke-width="0.8" opacity="0.3"/>
  </pattern>
</defs>
<!-- Usage -->
<rect x="50" y="50" width="200" height="100" fill="url(#hatch)" stroke="#333" stroke-width="2"/>
```

---

## Sketch Primitives

### Box with Label (Wireframe Component)

```xml
<g transform="rotate(-0.5, 175, 100)">
  <!-- Sketchy box -->
  <path d="M 52,51 C 120,48 230,53 298,50
           C 301,80 299,130 301,149
           C 230,152 120,148 52,151
           C 49,130 51,70 49,51"
        stroke="#333" stroke-width="2" fill="#fef9e7"
        stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Label -->
  <text x="175" y="105" text-anchor="middle"
        font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="16" fill="#333">Header</text>
</g>
```

### Placeholder Image Box

The classic X-through-a-box for image placeholders in wireframes.

```xml
<g>
  <rect x="50" y="50" width="200" height="120" fill="#e8e8e8" stroke="#999" stroke-width="1.5"
        stroke-dasharray="none" rx="2"/>
  <line x1="50" y1="50" x2="250" y2="170" stroke="#bbb" stroke-width="1"/>
  <line x1="250" y1="50" x2="50" y2="170" stroke="#bbb" stroke-width="1"/>
  <text x="150" y="115" text-anchor="middle"
        font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="12" fill="#999">image</text>
</g>
```

### Button

```xml
<g transform="rotate(0.8, 150, 40)">
  <path d="M 101,22 C 130,20 170,23 199,21
           C 202,32 200,48 201,58
           C 170,60 130,57 101,59
           C 99,48 101,32 99,22"
        stroke="#555" stroke-width="2" fill="#d4e6f1"
        stroke-linecap="round" stroke-linejoin="round"/>
  <text x="150" y="45" text-anchor="middle"
        font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="14" fill="#333">Click Me</text>
</g>
```

### Text Line Placeholder (Squiggly Lines)

Represent text content with wavy horizontal lines.

```xml
<g>
  <path d="M 50,80 C 80,78 120,82 180,79 C 220,81 260,78 300,80"
        stroke="#bbb" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M 50,100 C 80,98 120,102 180,99 C 220,101 260,98 300,100"
        stroke="#bbb" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M 50,120 C 80,118 120,122 160,119"
        stroke="#bbb" stroke-width="2" fill="none" stroke-linecap="round"/>
</g>
```

### Input Field

```xml
<g>
  <path d="M 51,31 C 120,29 230,33 299,30
           C 301,40 299,50 301,59
           C 230,61 120,58 51,61
           C 49,50 51,40 49,31"
        stroke="#888" stroke-width="1.5" fill="#fff"
        stroke-linecap="round"/>
  <text x="65" y="50" font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="13" fill="#aaa">Type here...</text>
</g>
```

### Toggle / Checkbox

```xml
<!-- Unchecked -->
<rect x="50" y="50" width="20" height="20" fill="none" stroke="#555" stroke-width="2" rx="3"/>

<!-- Checked -->
<g>
  <rect x="50" y="50" width="20" height="20" fill="none" stroke="#555" stroke-width="2" rx="3"/>
  <path d="M 54,60 L 58,66 L 67,54" stroke="#333" stroke-width="2.5" fill="none"
        stroke-linecap="round" stroke-linejoin="round"/>
</g>
```

---

## Arrows and Connectors

### Simple Arrow

```xml
<g>
  <!-- Sketchy line -->
  <path d="M 50,100 C 100,98 200,103 280,100"
        stroke="#555" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Arrowhead -->
  <path d="M 270,93 L 282,100 L 270,107" stroke="#555" stroke-width="2"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
```

### Curved Arrow (Down-Right)

```xml
<g>
  <path d="M 100,50 C 100,120 100,140 200,150"
        stroke="#555" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M 190,143 L 202,150 L 192,158" stroke="#555" stroke-width="2"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
```

### Bidirectional Arrow

```xml
<g>
  <path d="M 70,100 C 120,97 220,103 280,100"
        stroke="#555" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Left arrowhead -->
  <path d="M 80,93 L 68,100 L 80,107" stroke="#555" stroke-width="2"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Right arrowhead -->
  <path d="M 270,93 L 282,100 L 270,107" stroke="#555" stroke-width="2"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
```

### Dashed Connector

```xml
<path d="M 100,50 C 100,80 200,80 200,110"
      stroke="#888" stroke-width="1.5" fill="none"
      stroke-dasharray="6 4" stroke-linecap="round"/>
```

### Right-Angle Connector (Elbow)

```xml
<path d="M 100,60 L 100,120 L 250,120"
      stroke="#555" stroke-width="2" fill="none"
      stroke-linecap="round" stroke-linejoin="round"/>
<path d="M 240,113 L 252,120 L 240,127" stroke="#555" stroke-width="2"
      fill="none" stroke-linecap="round" stroke-linejoin="round"/>
```

---

## Text Labels and Annotations

### Handwritten Label

```xml
<text x="100" y="50"
      font-family="'Segoe Print', 'Comic Sans MS', cursive"
      font-size="16" fill="#333"
      transform="rotate(-2, 100, 50)">
  User Dashboard
</text>
```

### Annotation with Callout Line

```xml
<g>
  <path d="M 300,80 C 280,70 240,55 220,50"
        stroke="#e74c3c" stroke-width="1.5" fill="none" stroke-linecap="round"/>
  <circle cx="220" cy="50" r="3" fill="#e74c3c"/>
  <text x="305" y="85" font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="12" fill="#e74c3c"
        transform="rotate(-3, 305, 85)">fix this!</text>
</g>
```

### Numbered Callout

```xml
<g>
  <circle cx="30" cy="30" r="14" fill="#e74c3c" stroke="none"/>
  <text x="30" y="35" text-anchor="middle"
        font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="14" fill="white" font-weight="bold">1</text>
</g>
```

### Section Title with Underline

```xml
<g>
  <text x="50" y="40" font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="20" fill="#333" font-weight="bold">Navigation</text>
  <path d="M 48,46 C 80,48 140,44 210,47" stroke="#333" stroke-width="2"
        fill="none" stroke-linecap="round"/>
</g>
```

---

## Icons and Symbols

### User / Person

```xml
<g transform="translate(0,0)">
  <circle cx="20" cy="12" r="8" fill="none" stroke="#555" stroke-width="2"/>
  <path d="M 4,38 C 4,24 12,20 20,20 C 28,20 36,24 36,38"
        fill="none" stroke="#555" stroke-width="2" stroke-linecap="round"/>
</g>
```

### Gear / Settings

```xml
<circle cx="20" cy="20" r="10" fill="none" stroke="#555" stroke-width="2"/>
<circle cx="20" cy="20" r="4" fill="#555"/>
```

### Cloud

```xml
<path d="M 25,40 C 10,40 5,30 10,22 C 8,12 18,5 28,10
         C 32,2 48,2 50,12 C 60,8 68,18 62,28
         C 70,35 62,42 50,40 Z"
      fill="none" stroke="#555" stroke-width="2" stroke-linecap="round"/>
```

### Database (Cylinder)

```xml
<g>
  <ellipse cx="25" cy="12" rx="20" ry="8" fill="none" stroke="#555" stroke-width="2"/>
  <line x1="5" y1="12" x2="5" y2="38" stroke="#555" stroke-width="2"/>
  <line x1="45" y1="12" x2="45" y2="38" stroke="#555" stroke-width="2"/>
  <ellipse cx="25" cy="38" rx="20" ry="8" fill="none" stroke="#555" stroke-width="2"/>
</g>
```

### Star / Favorite

```xml
<path d="M 20,2 L 25,15 L 38,15 L 27,23 L 31,36 L 20,28 L 9,36 L 13,23 L 2,15 L 15,15 Z"
      fill="none" stroke="#f39c12" stroke-width="2" stroke-linejoin="round"/>
```

### Hamburger Menu

```xml
<g>
  <path d="M 5,8 C 10,7 25,9 35,8" stroke="#555" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 5,18 C 10,17 25,19 35,18" stroke="#555" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 5,28 C 10,27 25,29 35,28" stroke="#555" stroke-width="2.5" stroke-linecap="round"/>
</g>
```

### Search / Magnifying Glass

```xml
<g>
  <circle cx="18" cy="18" r="12" fill="none" stroke="#555" stroke-width="2"/>
  <path d="M 27,27 L 38,38" stroke="#555" stroke-width="2.5" stroke-linecap="round"/>
</g>
```

---

## Color Palettes

### Whiteboard Palette (Default)

Best for general sketches. Mimics dry-erase markers on a whiteboard.

| Role | Color | Hex |
|------|-------|-----|
| Background | Off-white | `#fafafa` |
| Stroke | Dark gray | `#333333` |
| Light stroke | Medium gray | `#888888` |
| Placeholder | Light gray | `#cccccc` |
| Primary fill | Soft yellow | `#fef9e7` |
| Secondary fill | Soft blue | `#d4e6f1` |
| Accent fill | Soft green | `#d5f5e3` |
| Warning fill | Soft pink | `#fadbd8` |
| Highlight | Red marker | `#e74c3c` |
| Link / action | Blue marker | `#3498db` |

### Blueprint Palette

For technical diagrams and architecture sketches.

| Role | Color | Hex |
|------|-------|-----|
| Background | Dark blue | `#1a2744` |
| Stroke | Light blue | `#8ec6e6` |
| Grid | Faint blue | `#2a3f5f` |
| Fill | Translucent | `rgba(142,198,230,0.1)` |
| Accent | Bright cyan | `#00d4ff` |
| Text | White | `#e0e8f0` |

### Notebook Palette

Lined-paper feel, good for concept sketches and brainstorming.

| Role | Color | Hex |
|------|-------|-----|
| Background | Cream | `#fdf6e3` |
| Stroke | Pencil gray | `#444444` |
| Lines | Faint blue | `#c5d9e8` |
| Margin | Faint red | `#e8b4b4` |
| Highlight | Pencil yellow | `#f7dc6f` |
| Accent | Pen blue | `#2e86c1` |

### Pastel Palette

For friendly, approachable wireframes and concept art.

| Role | Color | Hex |
|------|-------|-----|
| Background | White | `#ffffff` |
| Stroke | Charcoal | `#4a4a4a` |
| Box 1 | Pastel blue | `#a8d8ea` |
| Box 2 | Pastel pink | `#f3c1c6` |
| Box 3 | Pastel green | `#b5ead7` |
| Box 4 | Pastel yellow | `#ffeaa7` |
| Box 5 | Pastel purple | `#c7b8ea` |

---

## Wireframe Layout Grids

### Mobile (375px width)

```xml
<svg viewBox="0 0 375 812" xmlns="http://www.w3.org/2000/svg">
  <!-- Phone frame -->
  <rect x="0" y="0" width="375" height="812" rx="20" fill="#fafafa"
        stroke="#ccc" stroke-width="2"/>
  <!-- Status bar -->
  <rect x="0" y="0" width="375" height="44" fill="#f0f0f0" rx="20"/>
  <!-- Content area: y=44 to y=734 (690px tall) -->
  <!-- Bottom nav: y=734 to y=812 (78px tall) -->
  <line x1="0" y1="734" x2="375" y2="734" stroke="#ddd" stroke-width="1"/>
</svg>
```

Columns: 1-column layout, 16px side margins, content width = 343px.

### Tablet (768px width)

```xml
<svg viewBox="0 0 768 1024" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="768" height="1024" rx="12" fill="#fafafa"
        stroke="#ccc" stroke-width="2"/>
  <!-- Nav bar: 64px tall -->
  <!-- Content: 24px side margins, 720px usable width -->
  <!-- 2-column grid: each column 348px with 24px gap -->
</svg>
```

### Desktop (1200px width)

```xml
<svg viewBox="0 0 1200 800" xmlns="http://www.w3.org/2000/svg">
  <!-- Browser chrome -->
  <rect x="0" y="0" width="1200" height="800" rx="8" fill="#fafafa"
        stroke="#ccc" stroke-width="2"/>
  <rect x="0" y="0" width="1200" height="36" rx="8" fill="#e8e8e8"/>
  <!-- Traffic lights -->
  <circle cx="16" cy="18" r="5" fill="#ff5f57"/>
  <circle cx="32" cy="18" r="5" fill="#febc2e"/>
  <circle cx="48" cy="18" r="5" fill="#28c840"/>
  <!-- Content: starts at y=36 -->
  <!-- 12-column grid: 80px margins, 1040px usable, columns ~73px with 16px gaps -->
</svg>
```

### Flowchart Grid

For flow diagrams, use a loose grid with consistent spacing.

```
Node width:  140-200px
Node height: 60-80px
Horizontal gap: 60-80px
Vertical gap: 60-80px
Arrow length: fills the gap
```

### Architecture Diagram Grid

For system/architecture diagrams, use a layered vertical layout.

```
Layer width:  full viewBox width minus 40px margins
Layer height: 60-80px
Layer gap:    40-60px (room for arrows + labels)
viewBox:      calculate from layer count
```

---

## Complete Examples

### Minimal Wireframe (Login Page)

```xml
<svg viewBox="0 0 400 500" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="500" fill="#fafafa"/>

  <!-- Title -->
  <text x="200" y="80" text-anchor="middle"
        font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="24" fill="#333">Login</text>

  <!-- Email field -->
  <g transform="rotate(-0.5, 200, 160)">
    <path d="M 72,141 C 150,139 280,143 328,140
             C 330,155 328,170 330,179
             C 280,181 150,178 72,181
             C 70,170 72,155 70,141"
          stroke="#888" stroke-width="1.5" fill="#fff" stroke-linecap="round"/>
    <text x="85" y="165" font-family="'Segoe Print', 'Comic Sans MS', cursive"
          font-size="13" fill="#aaa">email</text>
  </g>

  <!-- Password field -->
  <g transform="rotate(0.8, 200, 230)">
    <path d="M 72,211 C 150,209 280,213 328,210
             C 330,225 328,240 330,249
             C 280,251 150,248 72,251
             C 70,240 72,225 70,211"
          stroke="#888" stroke-width="1.5" fill="#fff" stroke-linecap="round"/>
    <text x="85" y="235" font-family="'Segoe Print', 'Comic Sans MS', cursive"
          font-size="13" fill="#aaa">password</text>
  </g>

  <!-- Login button -->
  <g transform="rotate(-0.3, 200, 310)">
    <path d="M 122,292 C 160,290 240,293 278,291
             C 280,305 278,320 280,329
             C 240,331 160,328 122,331
             C 120,320 122,305 120,292"
          stroke="#555" stroke-width="2" fill="#d4e6f1" stroke-linecap="round"/>
    <text x="200" y="316" text-anchor="middle"
          font-family="'Segoe Print', 'Comic Sans MS', cursive"
          font-size="16" fill="#333">Log In</text>
  </g>

  <!-- Forgot password link -->
  <text x="200" y="380" text-anchor="middle"
        font-family="'Segoe Print', 'Comic Sans MS', cursive"
        font-size="12" fill="#3498db">forgot password?</text>
</svg>
```

### Minimal Flowchart (3 Steps)

```xml
<svg viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
  <rect width="500" height="400" fill="#fafafa"/>

  <!-- Step 1 -->
  <g transform="rotate(-1, 250, 60)">
    <path d="M 152,32 C 200,30 300,33 348,31
             C 350,55 348,75 350,89
             C 300,91 200,88 152,91
             C 150,75 152,55 150,32"
          stroke="#333" stroke-width="2" fill="#d5f5e3" stroke-linecap="round"/>
    <text x="250" y="67" text-anchor="middle"
          font-family="'Segoe Print', 'Comic Sans MS', cursive"
          font-size="16" fill="#333">Start</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 250,92 C 252,110 248,130 250,148"
        stroke="#555" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M 243,140 L 250,152 L 257,140" stroke="#555" stroke-width="2"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Step 2 -->
  <g transform="rotate(0.8, 250, 190)">
    <path d="M 152,162 C 200,160 300,163 348,161
             C 350,185 348,205 350,219
             C 300,221 200,218 152,221
             C 150,205 152,185 150,162"
          stroke="#333" stroke-width="2" fill="#fef9e7" stroke-linecap="round"/>
    <text x="250" y="197" text-anchor="middle"
          font-family="'Segoe Print', 'Comic Sans MS', cursive"
          font-size="16" fill="#333">Process</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 250,222 C 252,240 248,260 250,278"
        stroke="#555" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M 243,270 L 250,282 L 257,270" stroke="#555" stroke-width="2"
        fill="none" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Step 3 -->
  <g transform="rotate(-0.5, 250, 320)">
    <path d="M 152,292 C 200,290 300,293 348,291
             C 350,315 348,335 350,349
             C 300,351 200,348 152,351
             C 150,335 152,315 150,292"
          stroke="#333" stroke-width="2" fill="#d4e6f1" stroke-linecap="round"/>
    <text x="250" y="327" text-anchor="middle"
          font-family="'Segoe Print', 'Comic Sans MS', cursive"
          font-size="16" fill="#333">Done!</text>
  </g>
</svg>
```
