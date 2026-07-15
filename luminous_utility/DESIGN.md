---
name: Luminous Utility
colors:
  surface: '#f7f9ff'
  surface-dim: '#c9dcf3'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#edf4ff'
  surface-container: '#e3efff'
  surface-container-high: '#d9eaff'
  surface-container-highest: '#d1e4fb'
  on-surface: '#091d2e'
  on-surface-variant: '#404850'
  inverse-surface: '#203243'
  inverse-on-surface: '#e8f2ff'
  outline: '#707881'
  outline-variant: '#bfc7d1'
  surface-tint: '#006497'
  primary: '#006497'
  on-primary: '#ffffff'
  primary-container: '#4fa3e1'
  on-primary-container: '#003756'
  inverse-primary: '#92ccff'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fcd664'
  on-secondary-container: '#745c00'
  tertiary: '#476800'
  on-tertiary: '#ffffff'
  tertiary-container: '#81a939'
  on-tertiary-container: '#263a00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cce5ff'
  primary-fixed-dim: '#92ccff'
  on-primary-fixed: '#001e31'
  on-primary-fixed-variant: '#004b73'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e7c353'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#c5f178'
  tertiary-fixed-dim: '#aad55f'
  on-tertiary-fixed: '#131f00'
  on-tertiary-fixed-variant: '#354e00'
  background: '#f7f9ff'
  on-background: '#091d2e'
  surface-variant: '#d1e4fb'
  surface-muted: '#F8FAFC'
  text-body: '#777B93'
  slate-dark: '#2B3152'
typography:
  display-hero:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-hero-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Montserrat
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.6'
    letterSpacing: 0.1em
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  caption:
    fontFamily: Montserrat
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.5'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  section-gap-desktop: 120px
  section-gap-mobile: 64px
  grid-gutter: 30px
  component-padding-sm: 16px
  component-padding-md: 24px
---

## Brand & Style

The design system is engineered for the renewable energy sector, prioritizing a balance between technical expertise and environmental optimism. The brand personality is **authoritative, forward-thinking, and reliable**. It aims to evoke a sense of security and modern innovation, positioning the product not just as a service provider but as a partner in a sustainable future.

The visual style is **Corporate / Modern** with high-contrast functional accents. It utilizes clean lines, a structured grid, and specific typographic "spans" (bolding key words within headlines) to create a proprietary editorial feel. The interface feels expansive yet organized, using ample whitespace to signify clarity of purpose.

## Colors

The palette is rooted in the natural elements of solar energy: the sky and the sun. 

- **Primary (Sky Blue):** Used for primary CTAs, active states, and dominant branding elements. It represents technology and clarity.
- **Secondary (Sun Yellow):** An accent color used sparingly for highlighting critical keywords within headings and specific callouts.
- **Tertiary (Green):** Representing sustainability, used for icon accents and "Green Equipment" categories.
- **Neutral (Dark Slate):** Used for high-level headings and structural text to provide a grounded, professional contrast.
- **Surface Muted:** A very light grey used for alternating background sections to prevent eye fatigue and define content boundaries.

## Typography

This design system utilizes **Montserrat** across all levels to maintain a cohesive, modern geometric feel. 

### Usage Notes:
- **Keyword Emphasis:** Within section headings, use a 900 weight span for the most important word (e.g., Builders of **Future**) to create a proprietary brand rhythm.
- **Pre-Headers:** Always use `label-caps` for section categorizers (e.g., "ABOUT COMPANY") placed above H2 headlines.
- **Readability:** Body text uses a slightly increased line-height (1.6 - 1.7) to handle information-dense descriptions gracefully.

## Layout & Spacing

The system follows a **Fixed Grid** approach for desktop (1200px container) to maintain an editorial, structured feel.

- **Vertical Rhythm:** Sections are separated by generous whitespace (120px) to allow the "breathability" expected of a premium enterprise brand.
- **Grid Models:**
    - **3-Column:** Primary for service cards and offerings.
    - **4-Column:** Used for statistical counters and benefit lists.
    - **2-Column:** Used for split-layout hero sections and contact forms.
- **Component Density:** While section spacing is loose, internal component padding is compact (16-24px) to keep data-heavy cards readable.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layering** and **Subtle Shadows**. 

- **Surface Tiers:** Use `surface-muted` (#F8FAFC) to create a subtle distinction between the global background and specific content blocks like testimonials or feature grids.
- **Shadows:** Use extremely soft, high-diffusion shadows for cards (0px 10px 30px rgba(0,0,0,0.05)).
- **Interactive Layers:** Navigation bars are layered; the top utility bar (contact info) remains static while the primary navigation may use a sticky behavior with a background blur on scroll.

## Shapes

The shape language is **Soft**. 

- **Global Radius:** A 4px - 8px radius is applied to cards, input fields, and buttons. This provides a professional "edge" that isn't overly organic or "bubbly," maintaining the corporate persona.
- **Circular Accents:** Numerical indicators (e.g., benefit steps 01, 02) should use circular containers or heavy stylized underlines to break the geometric rigidity of the grid.

## Components

### Buttons
- **Primary:** Solid `primary-color` with white text. 4px border radius. Heavy uppercase weight for the label.
- **Secondary:** Ghost style with `primary-color` border or `surface-muted` background with slate text.
- **Iconic:** Buttons include a subtle leading or trailing arrow for "Learn More" actions to imply momentum.

### Cards
- **Service Cards:** Center-aligned with a large monochromatic icon, followed by a `headline-md` and `body-md` text.
- **Project Cards:** Full-width image top, followed by a white container with title, metadata (date/author), and a "Learn More" link.

### Navigation
- **Double-Tiered Header:** 
    - *Top Bar:* Dark slate background or white with borders, containing contact numbers and social links.
    - *Main Bar:* Logo left, horizontal menu center, search icon right.

### Input Fields
- Underlined style for high-end "Consultation" forms or fully enclosed boxes with 4px radius for standard data entry. Labels should be small and floating or placed inside as placeholders.

### Lists & Stats
- **Numerical Benefits:** Large, low-opacity numbers (e.g., 01) positioned as background elements or leading accents to list items.
- **Counters:** Bold `headline-lg` numbers with primary-colored icons to highlight company success metrics.