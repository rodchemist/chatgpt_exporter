# Dare Brand Implementation Guide for React & Electron

This guide covers how to implement the Dare brand styling and logo in your React and Electron applications using the provided stylesheet.

## 📁 Project Setup

### 1. File Structure
```
src/
├── assets/
│   ├── images/
│   │   └── dare-logo.png (or .svg)
│   └── styles/
│       └── dare-brand.css
├── components/
│   ├── Navigation/
│   ├── Layout/
│   └── UI/
└── App.js
```

### 2. Installing the Stylesheet

#### Option A: Direct Import (Recommended)
```jsx
// In your main App.js or index.js
import './assets/styles/dare-brand.css';
```

#### Option B: CSS Modules
```jsx
// Rename to dare-brand.module.css
import styles from './assets/styles/dare-brand.module.css';
```

#### Option C: Styled Components Integration
```jsx
import styled, { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  // Paste the CSS content here
`;
```

## 🎨 Logo Implementation

### 1. Logo Assets Preparation
- **Recommended formats**: SVG (preferred), PNG with transparent background
- **Sizes needed**: 
  - Navigation: 120px × 60px
  - Favicon: 32px × 32px, 16px × 16px
  - App icons: 256px × 256px, 512px × 512px

### 2. Logo Component

```jsx
// components/UI/DareLogo.jsx
import React from 'react';
import dareLogoSrc from '../../assets/images/dare-logo.png';

const DareLogo = ({ 
  size = 'medium', 
  className = '', 
  alt = 'Dare Logo',
  onClick 
}) => {
  const sizeClasses = {
    small: 'h-8 w-auto',     // 32px height
    medium: 'h-12 w-auto',   // 48px height
    large: 'h-16 w-auto',    // 64px height
    xl: 'h-20 w-auto'        // 80px height
  };

  return (
    <img
      src={dareLogoSrc}
      alt={alt}
      className={`${sizeClasses[size]} ${className} cursor-pointer transition-transform hover:scale-105`}
      onClick={onClick}
    />
  );
};

export default DareLogo;
```

### 3. SVG Logo Component (If using SVG)

```jsx
// components/UI/DareLogoSVG.jsx
import React from 'react';

const DareLogoSVG = ({ width = 120, height = 60, className = '' }) => {
  return (
    <svg 
      width={width} 
      height={height} 
      viewBox="0 0 200 100" 
      className={className}
      role="img"
      aria-label="Dare Logo"
    >
      {/* Replace with actual SVG path data */}
      <ellipse cx="100" cy="50" rx="95" ry="45" fill="none" stroke="#E31E24" strokeWidth="4"/>
      <text x="100" y="60" textAnchor="middle" fill="#E31E24" fontSize="32" fontFamily="serif">
        Dare
      </text>
    </svg>
  );
};

export default DareLogoSVG;
```

## 🧭 Navigation Component

```jsx
// components/Navigation/Navbar.jsx
import React, { useState } from 'react';
import DareLogo from '../UI/DareLogo';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navItems = [
    { label: 'Our Products', href: '/products', hasDropdown: true },
    { label: 'Our Promise', href: '/promise', hasDropdown: true },
    { label: 'Our Story', href: '/story', hasDropdown: true },
    { label: 'Recipes', href: '/recipes', hasDropdown: true },
    { label: 'Contact', href: '/contact', hasDropdown: true },
    { label: 'Where to Buy', href: '/where-to-buy' }
  ];

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo */}
        <a href="/" className="navbar-brand">
          <DareLogo size="medium" />
        </a>

        {/* Desktop Navigation */}
        <ul className="navbar-nav d-none d-md-flex">
          {navItems.map((item, index) => (
            <li key={index} className="nav-item">
              <a 
                href={item.href} 
                className={`nav-link ${item.hasDropdown ? 'dropdown' : ''}`}
              >
                {item.label}
              </a>
            </li>
          ))}
        </ul>

        {/* Mobile Menu Button */}
        <button 
          className="d-md-none btn btn-outline text-white"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
        >
          ☰
        </button>
      </div>

      {/* Mobile Menu */}
      {isMenuOpen && (
        <div className="mobile-menu d-md-none">
          <ul className="navbar-nav">
            {navItems.map((item, index) => (
              <li key={index} className="nav-item">
                <a href={item.href} className="nav-link">
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
```

## 🏗️ Layout Components

### 1. Main Layout Component

```jsx
// components/Layout/Layout.jsx
import React from 'react';
import Navbar from '../Navigation/Navbar';
import Footer from './Footer';

const Layout = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-1">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;
```

### 2. Hero Section Component

```jsx
// components/Layout/HeroSection.jsx
import React from 'react';

const HeroSection = ({ 
  title, 
  description, 
  backgroundImage,
  ctaButton 
}) => {
  return (
    <section 
      className="featured-section"
      style={backgroundImage ? { 
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center'
      } : {}}
    >
      <div className="container">
        <h1 className="featured-title">{title}</h1>
        <p className="featured-description">{description}</p>
        {ctaButton && (
          <div className="mt-4">
            {ctaButton}
          </div>
        )}
      </div>
    </section>
  );
};

export default HeroSection;
```

## 🎛️ UI Components

### 1. Button Components

```jsx
// components/UI/Button.jsx
import React from 'react';

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  onClick, 
  disabled = false,
  type = 'button',
  className = ''
}) => {
  const baseClass = 'btn';
  const variantClass = `btn-${variant}`;
  const sizeClass = size !== 'md' ? `btn-${size}` : '';
  
  return (
    <button
      type={type}
      className={`${baseClass} ${variantClass} ${sizeClass} ${className}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};

export default Button;
```

### 2. Card Component

```jsx
// components/UI/Card.jsx
import React from 'react';

const Card = ({ 
  children, 
  header, 
  footer, 
  className = '',
  hover = true 
}) => {
  return (
    <div className={`card ${className} ${!hover ? 'no-hover' : ''}`}>
      {header && (
        <div className="card-header">
          {header}
        </div>
      )}
      <div className="card-body">
        {children}
      </div>
      {footer && (
        <div className="card-footer">
          {footer}
        </div>
      )}
    </div>
  );
};

export default Card;
```

## ⚛️ React Implementation Examples

### 1. App Component

```jsx
// App.js
import React from 'react';
import Layout from './components/Layout/Layout';
import HeroSection from './components/Layout/HeroSection';
import Button from './components/UI/Button';
import Card from './components/UI/Card';
import './assets/styles/dare-brand.css';

function App() {
  return (
    <Layout>
      <HeroSection
        title="Featured Brands"
        description="Whether your family is rushing out the door in the morning or relaxing together after a long day, tempt your tastebuds with some of our all-time favourite snacks and treats!"
        ctaButton={
          <Button variant="primary" size="lg">
            Explore Products
          </Button>
        }
      />
      
      <section className="section">
        <div className="container">
          <div className="row">
            <div className="col-4">
              <Card 
                header={<h3>Premium Quality</h3>}
                footer={<Button variant="secondary">Learn More</Button>}
              >
                <p>Discover our commitment to quality ingredients and exceptional taste.</p>
              </Card>
            </div>
            <div className="col-4">
              <Card 
                header={<h3>Family Favorites</h3>}
                footer={<Button variant="secondary">View Products</Button>}
              >
                <p>Time-tested recipes that bring families together around delicious moments.</p>
              </Card>
            </div>
            <div className="col-4">
              <Card 
                header={<h3>Where to Buy</h3>}
                footer={<Button variant="secondary">Find Stores</Button>}
              >
                <p>Locate Dare products at stores near you across Canada and beyond.</p>
              </Card>
            </div>
          </div>
        </div>
      </section>
    </Layout>
  );
}

export default App;
```

## 🖥️ Electron-Specific Implementation

### 1. Main Process (main.js)

```javascript
const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    icon: path.join(__dirname, 'assets/icon.png'), // Dare logo as app icon
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    },
    titleBarStyle: 'hidden', // For custom title bar
    frame: false // If you want a completely custom frame
  });

  mainWindow.loadFile('build/index.html');
}

app.whenReady().then(createWindow);
```

### 2. Custom Title Bar Component

```jsx
// components/Electron/TitleBar.jsx
import React from 'react';
import DareLogo from '../UI/DareLogo';

const TitleBar = ({ title = 'Dare App' }) => {
  const handleMinimize = () => {
    window.electronAPI?.minimize();
  };

  const handleMaximize = () => {
    window.electronAPI?.maximize();
  };

  const handleClose = () => {
    window.electronAPI?.close();
  };

  return (
    <div className="electron-titlebar d-flex justify-content-between align-items-center px-3">
      <div className="d-flex align-items-center">
        <DareLogo size="small" />
        <span className="text-white ml-2 font-weight-medium">{title}</span>
      </div>
      
      <div className="d-flex">
        <button className="titlebar-btn" onClick={handleMinimize}>−</button>
        <button className="titlebar-btn" onClick={handleMaximize}>□</button>
        <button className="titlebar-btn close" onClick={handleClose}>×</button>
      </div>
    </div>
  );
};

export default TitleBar;
```

### 3. Electron App Component

```jsx
// ElectronApp.jsx
import React from 'react';
import TitleBar from './components/Electron/TitleBar';
import Layout from './components/Layout/Layout';

const ElectronApp = () => {
  return (
    <div className="electron-app">
      <TitleBar title="Dare Brand App" />
      <div className="electron-content">
        <Layout>
          {/* Your app content */}
        </Layout>
      </div>
    </div>
  );
};

export default ElectronApp;
```

## 🎨 Brand Guidelines

### Logo Usage Rules
1. **Minimum Size**: Never display the logo smaller than 40px in height
2. **Clear Space**: Maintain clear space equal to the height of the "D" around the logo
3. **Background**: Logo works best on white backgrounds; ensure sufficient contrast
4. **Modifications**: Never stretch, skew, or modify the logo proportions

### Color Usage
- **Primary Red**: `#E31E24` - Use for primary actions, navigation, and brand elements
- **Hover States**: `#C71C21` - Slightly darker red for interactive elements
- **Text**: Use the defined text colors for optimal readability
- **Backgrounds**: Prefer white or light gray backgrounds to maintain brand consistency

### Typography
- **Headings**: Use the system font stack for consistency across platforms
- **Body Text**: Maintain readable line heights (1.6) and appropriate font sizes
- **Hierarchy**: Follow the established heading sizes (h1-h6) for proper content structure

## 🔧 Development Tips

### 1. CSS Custom Properties
Use the CSS variables for consistent theming:
```css
/* Easy theme customization */
:root {
  --dare-red: #E31E24;
  --dare-red-hover: #C71C21;
}
```

### 2. Responsive Design
Test on multiple screen sizes:
```jsx
// Use the provided responsive classes
<div className="col-12 col-md-6 col-lg-4">
  {/* Content adapts to screen size */}
</div>
```

### 3. Performance Optimization
- Use appropriate image formats (WebP for web, PNG for Electron)
- Implement lazy loading for images
- Consider using React.memo for expensive components

### 4. Accessibility
- Always include proper alt text for the logo
- Ensure color contrast meets WCAG guidelines
- Use semantic HTML elements
- Test with screen readers

## 📱 Mobile Considerations

```jsx
// Example responsive navigation
const MobileNavigation = () => {
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <div className="d-md-none">
      <button 
        className="btn btn-outline text-white"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle navigation"
      >
        <DareLogo size="small" />
      </button>
      {/* Mobile menu content */}
    </div>
  );
};
```

## 🚀 Deployment Checklist

### React Web App
- [ ] Optimize images and assets
- [ ] Test responsive design on multiple devices
- [ ] Verify logo displays correctly on all pages
- [ ] Check color contrast ratios
- [ ] Test navigation functionality

### Electron App
- [ ] Set proper app icons for all platforms
- [ ] Test custom title bar functionality
- [ ] Verify native menu integration
- [ ] Test window controls (minimize, maximize, close)
- [ ] Package with proper branding assets

This guide provides a complete foundation for implementing the Dare brand consistently across your React and Electron applications while maintaining the professional, food-industry aesthetic of the original brand.