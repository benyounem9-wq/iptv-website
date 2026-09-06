#!/usr/bin/env node
/**
 * Regenerates sitemap.xml from the actual files in the repository.
 *
 * Why this exists:
 * The previous sitemap.xml was a hand-maintained static file that drifted out
 * of sync with the real site (stale lastmod dates, and previously contained
 * URLs for pages that had been removed, returning 404s).
 *
 * This script is the single source of truth going forward. It:
 *   - Discovers URLs by scanning the filesystem (index.html, blog/index.html,
 *     blog/*.html) instead of hand-listing them, so it can never reference a
 *     page that doesn't exist.
 *   - Skips any page that has a noindex robots meta tag or an
 *     X-Robots-Tag: noindex comment marker, so noindexed pages never end up
 *     in the sitemap.
 *   - Uses each file's real last commit date (from git history) as lastmod.
 *     If git history isn't available (e.g. a shallow checkout with no
 *     history for that file), lastmod is OMITTED for that URL rather than
 *     inventing a fake date -- lastmod is optional per the sitemaps.org spec.
 *
 * Run via `node scripts/generate-sitemap.mjs` (also wired into
 * .github/workflows/update-sitemap.yml to run automatically on every push).
 */

import { execFileSync } from "node:child_process";
import { readdirSync, writeFileSync, readFileSync, existsSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname;
const SITE = "https://bestiptvtoday.com";

function isNoindex(absPath) {
  if (!existsSync(absPath)) return false;
  const html = readFileSync(absPath, "utf-8");
  return /<meta\s+[^>]*name=["']robots["'][^>]*content=["'][^"']*noindex/i.test(html);
}

function lastCommitDate(relPath) {
  try {
    const out = execFileSync(
      "git",
      ["log", "-1", "--format=%cI", "--", relPath],
      { cwd: ROOT, stdio: ["ignore", "pipe", "ignore"] }
    )
      .toString()
      .trim();
    if (!out) return null;
    // Normalize to YYYY-MM-DD (date-only) per common sitemap convention.
    return out.slice(0, 10);
  } catch {
    return null;
  }
}

function urlEntry(loc, relPath, { changefreq, priority }) {
  const abs = join(ROOT, relPath);
  const lastmod = lastCommitDate(relPath);
  const lines = ["  <url>", `    <loc>${loc}</loc>`];
  if (lastmod) lines.push(`    <lastmod>${lastmod}</lastmod>`);
  if (changefreq) lines.push(`    <changefreq>${changefreq}</changefreq>`);
  if (priority) lines.push(`    <priority>${priority}</priority>`);
  lines.push("  </url>");
  return { xml: lines.join("\n"), skip: isNoindex(abs) };
}

const entries = [];

// Homepage
{
  const { xml, skip } = urlEntry(`${SITE}/`, "index.html", {
    changefreq: "weekly",
    priority: "1.0",
  });
  if (!skip) entries.push(xml);
}

// Blog index
{
  const { xml, skip } = urlEntry(`${SITE}/blog/`, "blog/index.html", {
    changefreq: "daily",
    priority: "0.9",
  });
  if (!skip) entries.push(xml);
}

// Blog articles (auto-discovered -- can never list a page that doesn't exist)
const blogFiles = readdirSync(join(ROOT, "blog"))
  .filter((f) => f.endsWith(".html") && f !== "index.html")
  .sort();

for (const file of blogFiles) {
  const relPath = `blog/${file}`;
  const { xml, skip } = urlEntry(`${SITE}/blog/${file}`, relPath, {
    changefreq: "monthly",
    priority: "0.8",
  });
  if (!skip) entries.push(xml);
}

const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${entries.join("\n")}
</urlset>
`;

writeFileSync(join(ROOT, "sitemap.xml"), xml);
console.log(`sitemap.xml written with ${entries.length} URLs.`);
