# Week 1: See It Work, Then Hit the Wall — Community Contributions

Cohort projects for this week live here. **New here? Read the full step-by-step
guide: [CONTRIBUTING.md](../../CONTRIBUTING.md)** — it covers everything from
creating a GitHub account to fixing a failed check, and has a browser-only route
that needs no terminal.

## The short version

1. **Fork** [this repository](https://github.com/Wahab901278/ml-and-ai-launchpad) to your own GitHub account.
2. Create a **branch** in your fork.
3. Put your work in **exactly this folder**, and nowhere else:

   ```
   week01-see-it-work/community_contributions/<your-github-username>/
   ```

4. Open a **pull request** back to `main` of this repository.
5. Wait for the `check-paths` check to go green, then for the maintainer to merge.

## Rules

- One folder per person, named after your GitHub username.
- Include a short `README.md` in your folder: what you built, how to run it.
- **No API keys, no `.env` files, no credentials** — not in files, not in
  notebook outputs. Public repo; bots scrape it.
- Clear notebook outputs unless the output is the point.
- No datasets or model weights over ~10 MB. Link to them instead.

Touching anything outside your own folder makes the automated check fail. It
will tell you exactly which files are the problem.
