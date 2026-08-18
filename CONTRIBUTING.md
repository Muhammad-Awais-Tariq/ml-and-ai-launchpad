# Contributing

Welcome! Cohort members are encouraged to share their work here.

## The one rule

**You may only add files inside a week's `community_contributions/` folder, in a subfolder named after your GitHub handle.**

```
week03-regression/community_contributions/your-github-handle/
├── README.md
├── notebook.ipynb
└── requirements.txt
```

Everything else — course material, other weeks, other people's folders — is off limits. A GitHub Action checks this automatically and will fail your PR if it touches anything else.

## How to contribute

You do **not** get push access to this repository. Nobody does except the maintainer. Contributions come in through a fork and a pull request. That is the standard GitHub flow:

1. **Fork** this repo (top-right "Fork" button).

2. **Clone your fork:**
   ```bash
   git clone https://github.com/<your-handle>/ml-and-ai-launchpad.git
   cd ml-and-ai-launchpad
   ```

3. **Create a branch:**
   ```bash
   git checkout -b week03-my-project
   ```

4. **Add your work** in the right place:
   ```bash
   mkdir -p week03-regression/community_contributions/<your-handle>
   # copy your files in
   ```

5. **Commit and push:**
   ```bash
   git add week03-regression/community_contributions/<your-handle>
   git commit -m "week03: add house price regression project"
   git push origin week03-my-project
   ```

6. **Open a pull request** against `main` of this repo. Fill in the template.

7. Wait for the checks to go green, then for the maintainer to merge.

## Keeping your fork up to date

```bash
git remote add upstream https://github.com/Wahab901278/ml-and-ai-launchpad.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## Rules that will get your PR rejected

- **Secrets.** No `.env`, no API keys, no `credentials.json`, no tokens in notebook cells. The CI check scans filenames, but it cannot read your mind — check your notebook outputs too. If you have already pushed a key anywhere, rotate it.
- **Touching files outside your folder.** One PR, one contributor folder.
- **Huge files.** Keep it under ~10 MB. Link to datasets, don't commit them.
- **No README.** A one-paragraph `README.md` in your folder is required so others know what they are looking at.

## Notebook hygiene

Clear outputs before committing unless the output is the point:

```bash
jupyter nbconvert --clear-output --inplace your_notebook.ipynb
```

## Questions

Open an issue.
