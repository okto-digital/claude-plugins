# DataForSEO — Tool Catalog

Full reference of available MCP tools organized by domain. Each section lists the tool name, parameters, and expected output.

---

## SERP Analysis

### serp_organic_live_advanced
Google/Bing/Yahoo organic SERP results.
- **Params:** keyword, location_code (2840), language_code (en), device (desktop), depth (100), se (google|bing|yahoo)
- **Output:** Rank, URL, title, description, domain, featured snippets, AI overview references, People Also Ask

### serp_youtube_organic_live_advanced
YouTube search results.
- **Params:** keyword, location_code, language_code
- **Output:** Video title, channel, views, upload date, description, URL

### serp_youtube_video_info_live_advanced
YouTube video metadata.
- **Params:** video_id
- **Output:** Title, channel, views, likes, description

### serp_youtube_video_comments_live_advanced
YouTube video comments.
- **Params:** video_id
- **Output:** Top comments with engagement metrics

### serp_youtube_video_subtitles_live_advanced
YouTube video subtitles/transcript.
- **Params:** video_id
- **Output:** Subtitle text

### serp_locations
Location code lookups for SERP queries.

---

## Keyword Research

### dataforseo_labs_google_keyword_ideas
Generate keyword ideas from seed.
- **Params:** keywords (array), location_code (2840), language_code (en), limit (50)
- **Output:** Keyword, search volume, CPC, competition, difficulty, trend

### dataforseo_labs_google_keyword_suggestions
Keyword suggestions from seed.
- **Params:** keyword, location_code, language_code, limit

### dataforseo_labs_google_related_keywords
Semantically related keywords.
- **Params:** keyword, location_code, language_code, limit

### kw_data_google_ads_search_volume
Search volume for keyword list.
- **Params:** keywords (array), location_code, language_code
- **Output:** Monthly search volume, CPC, competition, monthly trend

### dataforseo_labs_bulk_keyword_difficulty
Keyword difficulty scores.
- **Params:** keywords (array), location_code, language_code
- **Output:** Difficulty score 0-100 (Easy/Medium/Hard/Very Hard)

### dataforseo_labs_search_intent
Search intent classification.
- **Params:** keywords (array), location_code, language_code
- **Output:** Intent type (informational/navigational/commercial/transactional), confidence

### kw_data_google_trends_explore
Google Trends data.
- **Params:** keywords (array), location_code, date_from, date_to, language_code
- **Output:** Time series, trend direction, seasonality

### kw_data_dfs_trends_explore
DFS proprietary trends data.

### kw_data_dfs_trends_demography
Demographic data for trend analysis.

### kw_data_dfs_trends_subregion_interests
Subregion interest data for trends.

### dataforseo_labs_google_keyword_overview
Quick keyword metrics overview.

### dataforseo_labs_google_historical_keyword_data
Historical keyword metrics.

### kw_data_google_ads_locations
Location lookups for keyword data.

### kw_data_google_trends_categories
Google Trends category lookups.

---

## Domain & Competitor Analysis

### dataforseo_labs_google_competitors_domain
Identify competing domains.
- **Params:** target (domain), location_code, language_code
- **Output:** Competitor domains, keyword overlap %, estimated traffic, domain rank

### dataforseo_labs_google_domain_rank_overview
Domain rank and metrics.
- **Params:** target (domain), location_code, language_code
- **Output:** Domain rank, organic traffic, keywords count

### dataforseo_labs_google_ranked_keywords
Keywords a domain ranks for.
- **Params:** target (domain), location_code, language_code, limit (100)
- **Output:** Keyword, position, URL, search volume, traffic share, SERP features

### dataforseo_labs_google_relevant_pages
Top-performing pages on a domain.
- **Params:** target (domain), location_code, language_code

### dataforseo_labs_google_domain_intersection
Shared keywords across 2-20 domains.
- **Params:** targets (array of domains)
- **Output:** Shared keywords with positions per domain, unique keywords per domain

### dataforseo_labs_bulk_traffic_estimation
Organic traffic estimation for domains.
- **Params:** targets (array of domains)
- **Output:** Estimated organic traffic, traffic cost, top keywords

### dataforseo_labs_google_subdomains
Subdomains with ranking data.
- **Params:** target (domain), location_code, language_code
- **Output:** Subdomain, ranked keywords count, estimated traffic

### dataforseo_labs_google_top_searches
Top queries mentioning a domain.
- **Params:** target (domain), location_code, language_code
- **Output:** Query, search volume, domain position, traffic share

### dataforseo_labs_google_keywords_for_site
Keywords a site ranks for (alternative to ranked_keywords).

### dataforseo_labs_google_page_intersection
Page-level intersection analysis.

### dataforseo_labs_google_historical_serp
Historical SERP results for a keyword.

### dataforseo_labs_google_serp_competitors
Competitors for a specific SERP.

### dataforseo_labs_google_historical_rank_overview
Historical domain rank data.

### dataforseo_labs_available_filters
Available filter options for Labs endpoints.

---

## Backlinks

### backlinks_summary
Backlink profile summary.
- **Params:** target (domain)
- **Output:** Total backlinks, referring domains, domain rank, dofollow ratio

### backlinks_backlinks
Detailed backlink list.
- **Params:** target (domain), limit (100)
- **Output:** Source URL, anchor, dofollow, first/last seen

### backlinks_anchors
Anchor text distribution.
- **Params:** target (domain), limit

### backlinks_referring_domains
Top referring domains.
- **Params:** target (domain), limit

### backlinks_bulk_spam_score
Spam score for domains.
- **Params:** targets (array)

### backlinks_timeseries_summary
Backlink trends over time.
- **Params:** target (domain)
- **Output:** New/lost backlinks over time

### backlinks_domain_intersection
Shared backlink sources across domains.
- **Params:** targets (array of domains)

### backlinks_competitors
Domains with similar backlink profiles.

### backlinks_bulk_backlinks
Bulk backlink counts for multiple targets.

### backlinks_bulk_new_lost_referring_domains
Bulk new/lost referring domains.

### backlinks_bulk_new_lost_backlinks
Bulk new/lost backlinks.

### backlinks_bulk_ranks
Bulk rank overview for multiple targets.

### backlinks_bulk_referring_domains
Bulk referring domain counts.

### backlinks_domain_pages_summary
Summary of pages on a domain.

### backlinks_domain_pages
List pages on a domain with backlink data.

### backlinks_page_intersection
Shared backlink sources at page level.

### backlinks_referring_networks
Referring network analysis.

### backlinks_timeseries_new_lost_summary
Track new/lost backlinks over time.

### backlinks_bulk_pages_summary
Bulk page summaries.

### backlinks_available_filters
Available filter options for Backlinks endpoints.

---

## Technical / On-Page

### on_page_instant_pages
Quick page analysis.
- **Params:** url
- **Output:** Status codes, meta tags, content size, page timing, broken links

### on_page_content_parsing
Extract and parse page content.
- **Params:** url
- **Output:** Plain text, word count, structure

### on_page_lighthouse
Full Lighthouse audit.
- **Params:** url
- **Output:** Performance, accessibility, best practices, SEO scores, Core Web Vitals

### domain_analytics_technologies_domain_technologies
Technology stack detection.
- **Params:** target (domain)
- **Output:** Technology name, version, category (CMS, analytics, CDN, framework)

### domain_analytics_whois_overview
WHOIS registration data.
- **Params:** target (domain)
- **Output:** Registrar, creation date, expiration date, nameservers

### domain_analytics_whois_available_filters
WHOIS filter options.

### domain_analytics_technologies_available_filters
Technology detection filter options.

---

## Content & Business Data

### content_analysis_search
Search for content by topic.
- **Params:** keyword
- **Output:** Content matches with quality scores, sentiment

### content_analysis_summary
Analyze content quality of a URL.
- **Params:** url
- **Output:** Readability metrics, quality scores

### content_analysis_phrase_trends
Track phrase trends over time.
- **Params:** keyword
- **Output:** Phrase trend data over time

### business_data_business_listings_search
Business listings search.
- **Params:** keyword, location (optional)
- **Output:** Business name, category, address, phone, domain, rating, review count

---

## AI Visibility / GEO

### ai_optimization_chat_gpt_scraper
Scrape ChatGPT web search responses.
- **Params:** query, location_code (optional), language_code (optional)
- **Output:** ChatGPT response content, cited sources/URLs, referenced domains

### ai_optimization_chat_gpt_scraper_locations
Available locations for ChatGPT scraper.

### ai_opt_llm_ment_search
Search LLM mentions of a brand/keyword.
- **Params:** keyword, location_code (optional), language_code (optional)
- **Output:** Mention count, context, source LLM

### ai_opt_llm_ment_top_domains
Top cited domains for a topic across LLMs.
- **Params:** keyword

### ai_opt_llm_ment_top_pages
Top cited pages for a topic across LLMs.
- **Params:** keyword

### ai_opt_llm_ment_agg_metrics
Aggregate LLM mention metrics.
- **Params:** keyword
- **Output:** Overall mention volume, trends

### ai_opt_llm_ment_cross_agg_metrics
Cross-model comparison of mentions.

### ai_opt_llm_ment_loc_and_lang
Available locations/languages for LLM mentions.

### ai_optimization_llm_models
Supported LLM models for mention tracking.

### ai_optimization_llm_response
Direct LLM response analysis.

### ai_optimization_llm_mentions_filters
Available filters for LLM mentions.

### ai_opt_kw_data_loc_and_lang
AI optimization keyword data locations/languages.

### ai_optimization_keyword_data_search_volume
AI-specific keyword volume data.
