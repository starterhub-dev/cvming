# TinyMind · 微型智能实验室

TinyMind is a mobile-first Chinese AI chat web app, built as a first step toward learning machine learning and AI agents.

## Architecture

- **Frontend:** static HTML/CSS/JavaScript hosted by GitHub Pages.
- **Backend:** Supabase Edge Function `tinymind-chat`.
- **Model provider:** OpenAI-compatible Chat Completions API. The provider key stays in Supabase secrets and must never be committed to this repository.

## Publish with GitHub Pages

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. The included workflow publishes the site after a push to `main`.
4. The site URL should be `https://starterhub-dev.github.io/cvming/`.

## Enable real AI replies

The Supabase Edge Function is deployed to the project used by AI Tools Hub. In Supabase Dashboard, open **Edge Functions → Secrets** and add:

- `OPENAI_API_KEY`: your model provider API key.
- `OPENAI_BASE_URL`: optional; defaults to `https://api.openai.com/v1`.
- `OPENAI_MODEL`: optional; defaults to `gpt-4o-mini`.

Use a provider and model available to your account. API usage may incur charges. Do not put API keys in `index.html` or any public GitHub file. Once the secret is saved, the same chat page can call the function.

The public chat endpoint currently does not require a Supabase user JWT so visitors can chat. Before sharing widely, add rate limiting and abuse controls; never treat this starter version as a production service.

## Current scope

- Mobile-first responsive chat UI
- Suggested prompts, enter-to-send, clear conversation
- Sends recent conversation context to the backend
- Friendly error messages for missing API configuration
- No account system or persistent chat history yet
