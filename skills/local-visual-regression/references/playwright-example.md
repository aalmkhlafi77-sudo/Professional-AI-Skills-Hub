# Example: adapt to existing Playwright test project

This is a **template**, not executable code in the skill repository. Requires a locally installed and version-pinned `@playwright/test` and browser binary in the consuming project.

```ts
import { test, expect } from '@playwright/test';

const viewports = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'mobile', width: 390, height: 844 },
  { name: 'tablet', width: 768, height: 1024 },
] as const;

for (const viewport of viewports) {
  test(`homepage ${viewport.name} is visually stable`, async ({ page }) => {
    await page.setViewportSize({ width: viewport.width, height: viewport.height });
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.goto('http://127.0.0.1:4173/', { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await expect(page.locator('body')).toBeVisible();
    const overflow = await page.evaluate(() =>
      document.documentElement.scrollWidth - document.documentElement.clientWidth);
    expect(overflow).toBeLessThanOrEqual(1);
    await expect(page).toHaveScreenshot(`home-${viewport.name}.png`, {
      animations: 'disabled',
      caret: 'hide',
      maxDiffPixelRatio: 0.001, // Project-specific; review every difference.
    });
  });
}

test('keyboard focus is visible', async ({ page }) => {
  await page.goto('http://127.0.0.1:4173/');
  await page.keyboard.press('Tab');
  const active = page.locator(':focus-visible');
  await expect(active).toHaveCount(1);
});

test('RTL does not overflow', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('http://127.0.0.1:4173/');
  await page.locator('html').evaluate(el => el.setAttribute('dir', 'rtl'));
  const overflow = await page.evaluate(() =>
    document.documentElement.scrollWidth - document.documentElement.clientWidth);
  expect(overflow).toBeLessThanOrEqual(1);
});
```

**Important:** Forced RTL is a structural smoke test only. For real RTL screenshots use the application's supported Arabic locale and authentic text. For scroll-triggered animation, set actual scroll positions and verify no clipping, hidden content or trapped scroll. For reduced motion, confirm intended accessible fallback rather than assuming animation disabled means the design works. The sample does not run in this repository; adapt and execute in a disposable app.
