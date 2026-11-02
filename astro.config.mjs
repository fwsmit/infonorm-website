// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://fwsmit.github.io',
  base: 'https://fwsmit.github.io/infonorm-website',
  trailingSlash: 'never',
  build: {
    format: 'file',
  },
});
