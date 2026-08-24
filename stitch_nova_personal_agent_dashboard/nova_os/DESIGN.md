---
name: Nova OS
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c2c6d6'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8c909f'
  outline-variant: '#424754'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e6a'
  primary-container: '#4d8eff'
  on-primary-container: '#00285d'
  inverse-primary: '#005ac2'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#b7c8e1'
  on-tertiary: '#213145'
  tertiary-container: '#8292aa'
  on-tertiary-container: '#1a2b3e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style
The design system embodies the persona of a high-intelligence personal PC agent—silent, efficient, and sophisticated. The aesthetic is a hybrid of **Minimalism** and **Glassmorphism**, creating a digital environment that feels like a premium workspace rather than a cluttered tool.

The UI should evoke a sense of focused calm through deep obsidian surfaces and light-refracting layers. It targets power users, developers, and creative professionals who require an AI assistant that feels integrated into the hardware. Visuals rely on high-quality strokes, precise alignment, and translucent materials to imply depth and technical mastery.

## Colors
The palette is rooted in a "Deep Space" philosophy. The base layer is `#0A0A0A`, providing absolute black levels for OLED screens and high-contrast legibility. 

- **Primary (Cyber Blue):** Reserved for active intent, primary calls to action, and the "pulse" of the AI agent.
- **Secondary (Emerald Green):** Specifically used for "Online," "Success," and "Ready" states, signifying health and connectivity.
- **Surface Strategy:** Use `#121212` for elevated containers. All borders should use a subtle 10% white stroke to define boundaries without adding visual weight.
- **Subtle Slate:** Used for inactive icons, secondary text, and utility elements.

## Typography
This design system utilizes a dual-font approach to balance human-centric design with technical precision.

- **Inter** serves as the primary typeface for all UI elements, navigation, and body copy. It is chosen for its exceptional legibility in dark mode and its neutral, modern character.
- **JetBrains Mono** is used for system logs, data readouts, and metadata labels. This distinguishes "Agent-generated data" from "User Interface elements."
- **Scale:** Use tight tracking on larger headlines to emphasize the "Futuristic" feel. Use generous line height for body text to ensure comfort during long reading sessions of AI-generated content.

## Layout & Spacing
The system follows a **Fluid Grid** model with a base-4 rhythm. 

- **Desktop (1440px+):** 12-column grid with 24px gutters. Use wide margins (48px) to create a centered, focused "cockpit" feel.
- **Tablet (768px - 1439px):** 8-column grid with 20px gutters.
- **Mobile (Up to 767px):** 4-column grid with 16px gutters and margins.

Spacing should be generous between functional groups to maintain the "Minimalist" aesthetic. Use `xl` spacing to separate major content sections, while `sm` is used for internal card padding.

## Elevation & Depth
Elevation is expressed through **Glassmorphism** and **Tonal Layering** rather than traditional heavy shadows.

1.  **Base (Level 0):** `#0A0A0A` - The deep background.
2.  **Surface (Level 1):** `#121212` - Used for primary layout containers.
3.  **Floating (Level 2):** Semi-transparent surfaces with `backdrop-filter: blur(20px)`. These elements should have a 1px solid white stroke at 10% opacity.
4.  **Shadows:** When necessary, use extremely diffused shadows (40px blur) with a 20% opacity black tint to create a soft "lift" effect without appearing muddy on the dark background.

## Shapes
The shape language is "Soft-Modern." Elements use a standard 0.5rem (8px) radius, while larger cards and containers utilize 1rem (16px) or 1.5rem (24px) for a more approachable, premium feel.

Interactive elements like buttons and chips should feel substantial but never fully circular unless they are icon-only buttons. The consistent use of `rounded-lg` across main containers creates a cohesive, hardware-integrated look.

## Components
- **Buttons:** Primary buttons use a solid Cyber Blue fill with white text. Secondary buttons use a ghost style (1px border, no fill) or a glass effect (blur background).
- **Cards:** Defined by a 16px radius, a 1px white/10% border, and a subtle glass effect. Content inside cards should follow the 8px internal grid.
- **Inputs:** Darker than the surface color (`#000000`), with a 1px border that glows Cyber Blue on focus. Use JetBrains Mono for the input text.
- **Chips:** Small, highly rounded (pill-shaped) elements for tags or status. Use secondary green for "Active" and slate for "Idle."
- **Progress Bars:** Thin (4px) lines. Use a Cyber Blue gradient for the fill to simulate movement and data flow.
- **AI Pulse:** A custom component representing the agent's state. It should be a 24px circle with a multi-layered glow using the primary color.
- **Lists:** Clean, border-less rows separated by subtle 8px vertical gaps. Hover states should trigger a light-gray glass highlight.