// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://infonorm.nl',
  trailingSlash: 'never',
  // The Diensten page is temporarily hidden; send old links to the
  // services overview on the homepage instead.
  redirects: {
    '/diensten': '/#diensten',
  },
});
