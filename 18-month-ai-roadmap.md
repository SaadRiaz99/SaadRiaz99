# 12-Month Agentic AI Roadmap — Top 1% Engineer Track

**Background:** Python, MySQL, basic ML, already built agents (LinkedIn, Gmail via MCP)  
**Budget:** $0 — Free/open-source LLMs only  
**Goal:** Production agentic AI engineer + financial independence

---

## Free LLM Stack (No Paid APIs)

| Need | Free Option |
|------|-------------|
| Local inference | Ollama (Llama 3, Mistral, Qwen 2.5, DeepSeek, Gemma 2) |
| Cloud free tier | Google Gemini API (free tier), Groq (free tier) |
| Embeddings | BGE, GTE, all-MiniLM (via sentence-transformers) |
| Code LLM | DeepSeek Coder, CodeLlama, Qwen2.5-Coder |
| Hosting | Hugging Face Inference Endpoints (free), GitHub Codespaces |
| Agent framework | LangGraph, CrewAI, AutoGen (all free, open-source) |

---

## Earning Timeline

| Month | Focus | Earning Strategy | Expected $/mo |
|-------|-------|------------------|---------------|
| 1-2 | Foundation | **No earning** — build core skills | $0 |
| 3-4 | Freelance prep | **Start freelancing** — simple agent automations on Upwork/Fiverr | $200-500 |
| 5-6 | Productize | **Sell agent templates** — LinkedIn/Gmail bots, automation scripts | $500-1.5k |
| 7-8 | Scale delivery | **Retainer clients** — monthly agent maintenance + custom builds | $1.5k-3k |
| 9-10 | SaaS MVP | **Launch micro-SaaS** — agent-as-a-service subscription | $2k-5k |
| 11-12 | Full-time | **Multiple income streams** — SaaS + freelance + consulting | $5k-10k |

### Month 1-2: Zero Income — Pure Skill Building
- No shortcuts. You're investing in yourself.
- Goal: Be able to build any single-agent system from scratch.

### Month 3-4: Freelance Entry ($200-500/mo)
What to sell:
- LinkedIn automation agents (you already built this — sell it)
- Gmail/email automation agents (you already built this — sell it)
- Web scraping + data extraction agents
- Social media content scheduling agents
- Simple CRM automation (HubSpot/Salesforce via API)

Platforms: Upwork, Fiverr, Freelancer, Reddit r/forhire  
Strategy: 5-10 small gigs at $50-100 each. Over-deliver, ask for referrals.

### Month 5-6: Productize ($500-1.5k/mo)
Package what you built into sellable products:
- LinkedIn Auto-Engage Bot → $49 one-time or $19/mo
- Gmail AI Assistant → $29/mo
- Multi-agent automation template → $149

Sell on: Gumroad, your own website, Reddit, LinkedIn DMs

### Month 7-8: Retainers ($1.5k-3k/mo)
- Convert gig clients to monthly retainers ($500-1k/mo each)
- Offer "agent maintenance + continuous improvement"
- 2-3 retainer clients = full-time income

### Month 9-10: Micro-SaaS ($2k-5k/mo)
- Build a simple agent-as-a-service (e.g., "AI Resume Screener for recruiters")
- Deploy with free tier (Hugging Face Spaces + Gemini API + FastAPI)
- Charge $19-49/mo subscription
- 50-100 subscribers = $2k-5k/mo

### Month 11-12: Scale ($5k-10k/mo)
- Multiple income streams
- Raise freelance rates ($100-200/hr)
- Hire or outsource delivery
- Consulting for businesses ($2-5k/project)

---

## Phase 1: Agent Mastery (Months 1-2)

*You've already built LinkedIn/Gmail agents — skip basic tool-use, focus on depth.*

### Week 1-2: Agent Architecture Deep-Dive
| Topic | Deliverable | Free Tool |
|-------|-------------|-----------|
| State machines for agents | Implement agent with `transitions` library | Python + LangGraph |
| Agent loop from scratch (no framework) | Custom agent with tool registry | Python |
| Parallel tool execution | Agent that searches 5 sources simultaneously | asyncio + aiohttp |
| Structured output parsing | JSON mode, Pydantic validation | Ollama + instructor |
| Error recovery & retry logic | Self-healing agent | Python tenacity |

**Free tools:** Ollama (local), Google Gemini API (free tier), Python

### Week 3-4: Multi-Agent Systems
| Topic | Deliverable | Free Tool |
|-------|-------------|-----------|
| Agent communication protocols | 2 agents passing messages | LangGraph / CrewAI |
| Task decomposition | Orchestrator + 3 workers | CrewAI |
| Shared memory between agents | Agents that remember each other's outputs | Qdrant (free 1GB) |
| Human-in-the-loop patterns | Approval workflow agent | FastAPI + WebSocket |

**Project:** Upgrade your LinkedIn agent to multi-agent (profile analyzer → content writer → poster)

---

## Phase 2: Production-Grade Free Stack (Months 3-4)

### Week 5-6: Free Deployment
| Topic | Deliverable | Free Tool |
|-------|-------------|-----------|
| Deploy agent API | FastAPI + Uvicorn | Render / Fly.io (free tier) |
| Free LLM hosting | API endpoint with Ollama | Runpod (free credits) / HF Spaces |
| Background tasks | Async agent jobs | Celery + Redis (free tier) |
| Webhook callbacks | Agent that reports results | ngrok + FastAPI |

**Project:** Deploy your LinkedIn agent as a public API for free

### Week 7-8: Memory & Persistence
| Topic | Deliverable | Free Tool |
|-------|-------------|-----------|
| Session management | Stateless vs stateful agents | Redis (free 30MB) |
| Long-term memory with SQLite | Agent that remembers users | SQLite (free, no server) |
| Vector memory | Semantic search across sessions | ChromaDB / Qdrant (free) |
| Conversation compression | Budget-aware history management | Custom summarization chain |

**Project:** Agent with persistent memory across 100+ conversations

---

## Phase 3: Monetization Engine (Months 5-8)

### Week 9-12: Build Your First Product
| Week | Task | Output |
|------|------|--------|
| 9 | Package LinkedIn agent as standalone product | CLI tool + simple web UI |
| 10 | Add payment (Stripe free tier) | Customers can pay $19/mo |
| 11 | Deploy + SEO landing page | GitHub Pages + simple marketing |
| 12 | Launch on Product Hunt, Reddit, LinkedIn | First 10 paying users |

**Tech stack:** FastAPI + SQLite + Gemini API (free) + Stripe + GitHub Pages

### Week 13-16: Automation Agency
| Week | Task | Output |
|------|------|--------|
| 13 | Find 5 small businesses needing automation | Outreach on LinkedIn/Upwork |
| 14 | Build custom agent for first client | Delivered automation |
| 15 | Build custom agent for second client | Delivered automation |
| 16 | Create reusable template from both projects | Faster delivery next time |

### Week 17-20: Retainer Model
| Week | Task | Output |
|------|------|--------|
| 17 | Propose monthly maintenance ($500/mo each) | 2 retainer clients |
| 18 | Add monitoring + monthly improvements | Client dashboards |
| 19 | Scale to 3 retainer clients | $1.5k/mo recurring |
| 20 | Systematize delivery (templates + docs) | 4hr/week per client |

---

## Phase 4: Scale & Freedom (Months 9-12)

### Week 21-28: Micro-SaaS Build
- Niche: "AI [X] for [Y]" (e.g., AI Resume Screener for Recruiters)
- FREE stack: FastAPI + Gemini API + Qdrant + Streamlit + GitHub Pages
- Launch fast, iterate on feedback
- Goal: 50 paying subscribers × $29 = $1,450/mo recurring

### Week 29-36: Consulting
- Position yourself as "Agentic AI Automation Expert"
- Charge $2-5k per consulting engagement
- Leverage your open-source agent work as proof
- Speak at free events → get paid speaking gigs

### Week 37-48: Full-Time Freedom
- Target: $5k-10k/mo from 3 streams (SaaS + retainers + consulting)
- Automate your own business (agents that handle support, billing, outreach)
- Keep learning but now you're paid to learn

---

## Weekly Schedule (With Earning)

| Day | Morning (2hr) | Afternoon (2hr) | Evening (1hr) |
|-----|---------------|-----------------|---------------|
| Mon | Deep learning (papers/code) | Project building | Client work |
| Tue | Deep learning (papers/code) | Project building | Client work |
| Wed | Deep learning (papers/code) | Project building | Client work |
| Thu | Client/delivery work | Marketing/outreach | Admin |
| Fri | Client/delivery work | Marketing/outreach | Admin |
| Sat | Catch up / learn new | Side project | Rest |
| Sun | Rest | Rest | Plan next week |

**Total:** ~25hr/week learning + 10hr/week earning by month 6

---

## The Strategy

1. **Learn by building** — every concept becomes a working agent
2. **Ship publicly** — GitHub + LinkedIn = your portfolio + marketing
3. **Sell before you build** — get a client first, build for their need
4. **Template everything** — one automation becomes 10 after templating
5. **Raise prices monthly** — as your skills grow, your rates grow
6. **Free tools only** — no excuses. Ollama + Gemini API + open-source = everything you need

---

## Your Head Start

You already built LinkedIn + Gmail agents using MCP + Gemini. That's **Month 5 skill level already.** You can literally start selling today:

1. Polish your LinkedIn agent into a product
2. Find 3 people who want LinkedIn automation
3. Charge them $99 setup + $29/mo
4. Reinvest into learning harder topics

---

## Key Free Resources

| Resource | URL |
|----------|-----|
| Ollama (local LLMs) | ollama.ai |
| Google Gemini API (free) | makersuite.google.com |
| Groq (free fast inference) | groq.com |
| Hugging Face Spaces | huggingface.co/spaces |
| LangGraph docs | langchain-ai.github.io/langgraph |
| CrewAI | docs.crewai.com |
| Qdrant free tier | qdrant.tech |
| ChromaDB | trychroma.com |
| Render free tier | render.com |

---

**No money is not a disadvantage. Open-source is your superpower.**  
You already have the skills to earn. Start small, ship fast, compound.
