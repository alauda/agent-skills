/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        acp: {
          // Backgrounds - Light Mode
          'bg-main': '#ffffff',
          'bg-primary': '#f4f6f8',
          'bg-panel': '#eef4ff',
          'bg-secondary': '#fafafa',

          // Info - Light Mode
          'info-bg': '#e3f2fd',
          'info-border': '#90caf9',
          'info-dark': '#1e3a8a',

          // Success - Light Mode
          'success-bg': '#d7f5e9',
          'success-border': '#4caf50',
          'success-dark': '#064e3b',

          // Process - Light Mode
          'process-bg': '#e8f2ff',
          'process-border': '#2196f3',
          'process-dark': '#1e40af',

          // Teal - Light Mode
          'teal-bg': '#e0f2f1',
          'teal-border': '#4db6ac',
          'teal-dark': '#134e4a',

          // Borders
          'border-primary': '#cbd7e0',
          'border-secondary': '#cbd5e1',
          'border-light': '#e2e8f0',

          // Text - Light Mode
          'text-primary': '#1a202c',
          'text-secondary': '#4a5568',
          'text-tertiary': '#718096',
          'text-disabled': '#cbd5e0',

          // Dark mode variants
          'dark-bg-main': '#1a1a1a',
          'dark-bg-primary': '#2d3748',
          'dark-bg-panel': '#1e3a5f',
          'dark-bg-secondary': '#2d3748',
          'dark-info-bg': '#1e3a8a',
          'dark-info-border': '#60a5fa',
          'dark-success-bg': '#064e3b',
          'dark-success-border': '#10b981',
          'dark-process-bg': '#1e40af',
          'dark-process-border': '#3b82f6',
          'dark-teal-bg': '#134e4a',
          'dark-teal-border': '#14b8a6',
          'dark-border-primary': '#4b5563',
          'dark-border-secondary': '#555d6f',
          'dark-border-light': '#374151',
          'dark-text-primary': '#f3f4f6',
          'dark-text-secondary': '#e5e7eb',
          'dark-text-tertiary': '#d1d5db',
          'dark-text-disabled': '#9ca3af',
        },
      },
      spacing: {
        '0': '0',
        '1': '0.25rem',
        '2': '0.5rem',
        '4': '1rem',
        '6': '1.5rem',
        '8': '2rem',
        '12': '3rem',
        '16': '4rem',
        '20': '5rem',
        '24': '6rem',
        '32': '8rem',
        '48': '12rem',
        '64': '16rem',
      },
      fontSize: {
        xs: ['0.75rem', { lineHeight: '1rem' }],
        sm: ['0.875rem', { lineHeight: '1.25rem' }],
        base: ['1rem', { lineHeight: '1.5rem' }],
        lg: ['1.125rem', { lineHeight: '1.75rem' }],
        xl: ['1.25rem', { lineHeight: '1.75rem' }],
        '2xl': ['1.5rem', { lineHeight: '2rem' }],
        '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
        '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
      },
      fontFamily: {
        sans: [
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          'sans-serif',
        ],
      },
      boxShadow: {
        none: 'none',
        subtle: '0 1px 2px rgba(0, 0, 0, 0.05)',
        medium: '0 4px 6px rgba(0, 0, 0, 0.1)',
        strong: '0 10px 15px rgba(0, 0, 0, 0.15)',
      },
      borderRadius: {
        sm: '4px',
        md: '8px',
        lg: '12px',
        xl: '16px',
      },
      transitionDuration: {
        fast: '200ms',
        standard: '300ms',
        slow: '500ms',
      },
    },
  },
  plugins: [],
  darkMode: ['class', 'media'],
  corePlugins: {
    darkMode: true,
  },
};
