/**
 * Brand Voice Dash Cleaner
 * Version: 1.2.0
 * Purpose: Auto-correct improper dash and em-dash usage
 *
 * Modes:
 *   Hook mode (default): Reads JSON from stdin (PostToolUse Write/Edit),
 *     auto-fixes .md files in-place. Used as a Claude Code hook.
 *   CLI mode: node dash-cleaner.js "content string"
 *             node dash-cleaner.js --file path/to/content.md
 */

// =============================================================================
// CONFIGURATION
// =============================================================================

// Compound adjectives that should keep hyphens
const COMPOUND_ADJECTIVES = new Set([
  'long-term', 'short-term', 'mid-term',
  'well-known', 'well-established', 'well-documented', 'well-defined',
  'state-of-the-art', 'end-to-end', 'one-on-one', 'face-to-face',
  'user-friendly', 'mobile-friendly', 'seo-friendly', 'eco-friendly',
  'high-quality', 'low-cost', 'high-performance', 'low-level', 'high-level',
  'data-driven', 'results-driven', 'user-driven', 'goal-driven',
  'real-time', 'full-time', 'part-time', 'run-time', 'one-time',
  'client-focused', 'customer-centric', 'business-critical',
  'conversion-focused', 'performance-focused', 'detail-oriented',
  'in-house', 'out-of-the-box', 'hands-on', 'best-in-class',
  'mobile-first', 'cloud-based', 'web-based', 'api-driven',
  'mobile-responsive', 'pixel-perfect', 'seo-optimized',
  'cross-platform', 'cross-functional', 'cross-team',
  'self-service', 'self-hosted', 'self-taught', 'self-paced',
  'open-source', 'closed-source', 'full-stack', 'front-end', 'back-end',
  'locked-in', 'built-in', 'opt-in', 'opt-out',
  'custom-built', 'hand-crafted', 'tailor-made',
  'cost-effective', 'time-sensitive', 'budget-friendly',
  'industry-leading', 'award-winning', 'future-proof'
]);

// Compound nouns that should keep hyphens
const COMPOUND_NOUNS = new Set([
  'decision-maker', 'stakeholder', 'game-changer', 'deal-breaker',
  'follow-up', 'check-in', 'sign-up', 'log-in', 'sign-in',
  'trade-off', 'break-down', 'set-up', 'run-through',
  'walk-through', 'work-around', 'hand-off', 'kick-off',
  'check-out', 'buy-in', 'write-up', 'wrap-up'
]);

// Valid prefixes
const VALID_PREFIXES = [
  'non-', 're-', 'co-', 'pre-', 'post-',
  'self-', 'multi-', 'cross-', 'mid-',
  'over-', 'under-', 'super-', 'sub-',
  'anti-', 'pro-', 'semi-', 'quasi-',
  'ex-', 'vice-', 'de-', 'un-'
];

// =============================================================================
// MARKDOWN STRUCTURE DETECTION
// =============================================================================

/**
 * Detect YAML frontmatter boundaries (--- at start/end of frontmatter block).
 * Returns an array of [start, end] index ranges that should be left untouched.
 */
function getFrontmatterRange(content) {
  if (!content.startsWith('---')) return null;
  const closingIndex = content.indexOf('\n---', 3);
  if (closingIndex === -1) return null;
  // Include the closing --- line
  const endOfClosing = content.indexOf('\n', closingIndex + 1);
  return [0, endOfClosing === -1 ? closingIndex + 4 : endOfClosing];
}

/**
 * Check if a dash at the given index is part of markdown structure:
 * - YAML frontmatter delimiter (--- at file start and end of frontmatter)
 * - Markdown horizontal rule (--- on its own line)
 * - Markdown list marker (- at line start, optionally indented)
 */
function isMarkdownStructure(content, index) {
  const lineStart = content.lastIndexOf('\n', index - 1) + 1;
  const lineEnd = content.indexOf('\n', index);
  const line = content.substring(lineStart, lineEnd === -1 ? content.length : lineEnd);
  const trimmedLine = line.trim();

  // YAML frontmatter delimiter or horizontal rule: line is only dashes (3+)
  if (/^-{3,}\s*$/.test(trimmedLine)) return true;

  // Markdown list marker: line starts with optional whitespace then "- "
  const listMatch = line.match(/^(\s*)-(\s)/);
  if (listMatch) {
    const dashPosInLine = index - lineStart;
    if (dashPosInLine === listMatch[1].length) return true;
  }

  return false;
}

// =============================================================================
// PATTERN DETECTION FUNCTIONS
// =============================================================================

function isInCodeBlock(content, index) {
  const beforeContent = content.substring(0, index);
  const codeBlockMatches = beforeContent.match(/```/g);
  if (codeBlockMatches && codeBlockMatches.length % 2 !== 0) {
    return true;
  }
  const lineStart = beforeContent.lastIndexOf('\n') + 1;
  const lineEnd = content.indexOf('\n', index);
  const line = content.substring(lineStart, lineEnd === -1 ? content.length : lineEnd);
  const backticks = line.match(/`/g);
  if (backticks && backticks.length >= 2) {
    const posInLine = index - lineStart;
    let inCode = false;
    for (const match of line.matchAll(/`/g)) {
      if (match.index < posInLine) {
        inCode = !inCode;
      }
    }
    return inCode;
  }
  return false;
}

function isInURL(context) {
  const urlPattern = /(https?:\/\/|www\.|[a-z0-9-]+\.com|[a-z0-9-]+\.org|[a-z0-9-]+\.net)/i;
  return urlPattern.test(context);
}

function isFilePath(context) {
  const filePattern = /\.(md|pdf|docx?|xlsx?|txt|csv|json|yaml|yml|js|ts|css|html|xml)(\s|$)/i;
  return filePattern.test(context) || context.includes('/') && context.match(/[a-z0-9-_]+\//i);
}

function isDate(context) {
  const datePattern = /\b\d{1,4}-\d{1,2}-\d{1,4}\b/;
  return datePattern.test(context);
}

function isNumericRange(before, after) {
  const beforeNum = before.trim().match(/(\d+)$/);
  const afterNum = after.trim().match(/^(\d+)/);
  return beforeNum && afterNum;
}

function isNumberWord(before, after) {
  const beforeNum = before.trim().match(/(\d+)$/);
  const afterWord = after.trim().match(/^([a-z]+)/i);
  return beforeNum && afterWord;
}

function isBrandName(word) {
  return /^okto-digital$/i.test(word.trim());
}

function isCompoundAdjective(word) {
  return COMPOUND_ADJECTIVES.has(word.toLowerCase().trim());
}

function isCompoundNoun(word) {
  return COMPOUND_NOUNS.has(word.toLowerCase().trim());
}

function hasValidPrefix(word) {
  const lowerWord = word.toLowerCase().trim();
  return VALID_PREFIXES.some(prefix => lowerWord.startsWith(prefix));
}

function extractHyphenatedWord(before, after) {
  // Capture the full multi-hyphen compound (e.g., "best-in-class", "state-of-the-art")
  const beforeMatch = before.match(/([a-z0-9]+(?:-[a-z0-9]+)*)$/i);
  const afterMatch = after.match(/^([a-z0-9]+(?:-[a-z0-9]+)*)/i);
  const beforePart = beforeMatch ? beforeMatch[1] : '';
  const afterPart = afterMatch ? afterMatch[1] : '';
  return `${beforePart}-${afterPart}`;
}

function getContext(content, index, radius = 20) {
  const start = Math.max(0, index - radius);
  const end = Math.min(content.length, index + radius);
  return {
    before: content.substring(start, index),
    after: content.substring(index + 1, end),
    fullContext: content.substring(start, end)
  };
}

// =============================================================================
// VALIDATION FUNCTIONS
// =============================================================================

function isValidHyphen(content, index) {
  if (isMarkdownStructure(content, index)) return true;
  if (isInCodeBlock(content, index)) return true;
  const ctx = getContext(content, index);
  if (isInURL(ctx.fullContext) || isFilePath(ctx.fullContext)) return true;
  if (isDate(ctx.fullContext)) return true;
  if (isNumericRange(ctx.before, ctx.after)) return true;
  if (isNumberWord(ctx.before, ctx.after)) return true;
  const word = extractHyphenatedWord(ctx.before, ctx.after);
  if (isBrandName(word)) return true;
  if (isCompoundAdjective(word)) return true;
  if (isCompoundNoun(word)) return true;
  if (hasValidPrefix(word)) return true;
  return false;
}

function isValidEmdash(content, index) {
  return false;
}

// =============================================================================
// CORRECTION FUNCTIONS
// =============================================================================

function correctEmdash(before, after) {
  const afterTrimmed = after.trimStart();
  if (afterTrimmed && afterTrimmed[0] === afterTrimmed[0].toUpperCase()) {
    return '. ';
  }
  return ', ';
}

function correctHyphen(before, after) {
  return ' ';
}

// =============================================================================
// MAIN CLEANING FUNCTION
// =============================================================================

function cleanContent(content) {
  if (!content || typeof content !== 'string') return content;

  // Detect YAML frontmatter range to skip entirely
  const frontmatterRange = getFrontmatterRange(content);

  let result = content;
  let offset = 0;
  const dashPattern = /[\-\u2014]/g;
  const matches = [];

  let match;
  while ((match = dashPattern.exec(content)) !== null) {
    // Skip dashes inside YAML frontmatter
    if (frontmatterRange && match.index >= frontmatterRange[0] && match.index < frontmatterRange[1]) {
      continue;
    }
    matches.push({ index: match.index, char: match[0] });
  }

  for (const { index, char } of matches) {
    const adjustedIndex = index + offset;
    if (char === '\u2014') {
      if (!isValidEmdash(content, index)) {
        const ctx = getContext(content, index);
        const replacement = correctEmdash(ctx.before, ctx.after);
        result = result.substring(0, adjustedIndex) + replacement + result.substring(adjustedIndex + 1);
        offset += replacement.length - 1;
      }
    } else if (char === '-') {
      if (!isValidHyphen(content, index)) {
        const ctx = getContext(content, index);
        const replacement = correctHyphen(ctx.before, ctx.after);
        result = result.substring(0, adjustedIndex) + replacement + result.substring(adjustedIndex + 1);
        offset += replacement.length - 1;
      }
    }
  }

  return result;
}

// =============================================================================
// EXPORTS & CLI
// =============================================================================

module.exports = {
  cleanContent,
  isValidHyphen,
  isValidEmdash,
  isNumericRange,
  isNumberWord,
  isBrandName,
  isCompoundAdjective,
  isCompoundNoun,
  hasValidPrefix
};

if (require.main === module) {
  const fs = require('fs');
  const path = require('path');
  const args = process.argv.slice(2);

  // CLI mode: explicit arguments provided
  if (args.length > 0) {
    if (args[0] === '--file') {
      const content = fs.readFileSync(args[1], 'utf8');
      const cleaned = cleanContent(content);
      if (args.includes('--fix')) {
        fs.writeFileSync(args[1], cleaned, 'utf8');
      } else {
        console.log('=== ORIGINAL ===');
        console.log(content);
        console.log('\n=== CLEANED ===');
        console.log(cleaned);
      }
    } else {
      const content = args.join(' ');
      console.log(cleanContent(content));
    }
    process.exit(0);
  }

  // Hook mode: read JSON from stdin (PostToolUse Write/Edit)
  let stdin = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (chunk) => { stdin += chunk; });
  process.stdin.on('end', () => {
    try {
      const input = JSON.parse(stdin);
      const filePath = input.tool_input && input.tool_input.file_path;

      // Only process .md files
      if (!filePath || path.extname(filePath).toLowerCase() !== '.md') {
        process.exit(0);
      }

      // Skip non-existent files
      if (!fs.existsSync(filePath)) {
        process.exit(0);
      }

      const content = fs.readFileSync(filePath, 'utf8');
      const cleaned = cleanContent(content);

      // Only write if content changed
      if (cleaned !== content) {
        fs.writeFileSync(filePath, cleaned, 'utf8');
        const diff = content.length - cleaned.length;
        console.log(JSON.stringify({
          systemMessage: `Dash cleaner: auto-corrected dashes in ${path.basename(filePath)}`
        }));
      }
    } catch (e) {
      // Non-blocking: exit 0 even on parse errors
    }
    process.exit(0);
  });
}
