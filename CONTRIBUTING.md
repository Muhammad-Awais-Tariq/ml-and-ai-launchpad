# How to Contribute Your Work

Welcome! This guide shows you how to add your project to this repository.

It assumes **you have never used GitHub before**. If you have used it, skip to [Route B: the command line](#route-b-the-command-line-git-on-your-computer).

---

## Table of contents

- [The one rule](#the-one-rule)
- [Why you can't just push](#why-you-cant-just-push)
- [Before you start](#before-you-start)
- [Route A: the browser (no terminal, no installs)](#route-a-the-browser-no-terminal-no-installs)
- [Route B: the command line (git on your computer)](#route-b-the-command-line-git-on-your-computer)
- [Route C: GitHub Desktop (clicking, not typing)](#route-c-github-desktop-clicking-not-typing)
- [What goes in your folder](#what-goes-in-your-folder)
- [The automated checks](#the-automated-checks)
- [Fixing a PR after you opened it](#fixing-a-pr-after-you-opened-it)
- [Keeping your fork up to date](#keeping-your-fork-up-to-date)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)
- [FAQ](#faq)

---

## The one rule

**Everything you add must live inside one folder, and that folder must be:**

```
<week-folder>/community_contributions/<your-github-username>/
```

Real example, for someone whose GitHub username is `janedoe`:

```
week03-regression/community_contributions/janedoe/
├── README.md
├── house_prices.ipynb
└── requirements.txt
```

That is it. You may create as many files as you like **inside your own folder**. You may not touch anything outside it — not the course material, not the week READMEs, not another person's folder.

An automated robot checks this on every pull request. If you break the rule, the check turns red and tells you exactly which files are the problem.

### The week folders

Copy the name exactly — the spelling matters.

| Week | Folder name |
|------|-------------|
| 1 | `week01-see-it-work` |
| 2 | `week02-python-data-toolkit` |
| 3 | `week03-regression` |
| 4 | `week04-classification-and-deployment` |
| 5 | `week05-deep-learning-and-llms` |
| 6 | `week06-multi-model-uis-and-rag-concepts` |
| 7 | `week07-build-and-evaluate-rag` |
| 8 | `week08-fine-tuning` |
| 9 | `week09-agent-foundations` |
| 10 | `week10-deep-research-agent` |
| 11 | `week11-crewai` |
| 12 | `week12-mcp-and-mvp` |
| 13 | `week13-ship-it` |
| Demo Day | `demo-day` |

---

## Why you can't just push

You might expect to be given write access to the `community_contributions` folder. **GitHub does not work that way.** Permissions on GitHub are per-repository, never per-folder. There is no setting anywhere that says "this person may write to this directory only."

So the standard, universal solution — the one used by every large open-source project on GitHub — is:

1. You make your **own copy** of this repository. That copy is called a **fork**, and you have full write access to it because you own it.
2. You make your changes in your fork.
3. You send a **pull request** ("PR"): a reviewable request that says *"please pull these changes from my copy into yours."*
4. The maintainer reviews it and clicks Merge.

Nothing lands in this repository until the maintainer approves it. That is the safety mechanism, and it is why the folder rule can be enforced by a robot instead of by trust.

```
   THIS REPO                      YOUR FORK
   Wahab901278/                   janedoe/
   ml-and-ai-launchpad            ml-and-ai-launchpad
   (you can read)                 (you can write)

        |                                |
        |  --- 1. click "Fork" --------->|
        |                                |
        |                                |  2. add your files
        |                                |     on a new branch
        |                                |
        |<------ 3. pull request --------|
        |                                |
        |  4. robot checks the paths     |
        |  5. maintainer clicks Merge    |
        |                                |
      merged!
```

---

## Before you start

You need:

- **A GitHub account.** Free. Sign up at [github.com/signup](https://github.com/signup). Your **username** is the name in your profile URL — if your profile is `github.com/janedoe`, your username is `janedoe`. You will use it as your folder name.
- **Your finished work**, in files on your computer.

For Route B only, you additionally need git installed. Check by opening a terminal and running:

```bash
git --version
```

If that prints something like `git version 2.43.0`, you have it. If not, install it from [git-scm.com/downloads](https://git-scm.com/downloads).

---

## Route A: the browser (no terminal, no installs)

**Best if:** you have a handful of files, you are not comfortable with the command line, or you just want this done in five minutes.

### A1. Fork the repository

Go to **https://github.com/Wahab901278/ml-and-ai-launchpad**

Click the **Fork** button (top right, next to Star). On the next screen leave everything as-is and click **Create fork**.

Wait a few seconds. You are now looking at **your own copy**. Check the URL — it should have your username in it, e.g. `github.com/janedoe/ml-and-ai-launchpad`. Under the repo title it will say *"forked from Wahab901278/ml-and-ai-launchpad."*

> **Everything from here happens in YOUR fork.** If at any point the URL says `Wahab901278`, you are in the wrong place — go back to your fork.

### A2. Create a branch

A **branch** is a separate line of work, so your project does not get tangled up with anything else.

1. Near the top left of the file list, click the button labelled **`main`** (it has a branch icon).
2. In the text box, type a branch name, e.g. `week03-house-prices`. Letters, numbers and hyphens only — no spaces.
3. Click **Create branch: week03-house-prices from main**.

The button should now read `week03-house-prices` instead of `main`.

### A3. Create your folder and files

The upload box does not let you choose a destination folder, so create the first file manually — this is the reliable way to make the folders exist:

1. Click **Add file** (top right of the file list) → **Create new file**.
2. In the filename box at the top, type the full path **including your username folder**, using `/` between parts:

   ```
   week03-regression/community_contributions/janedoe/README.md
   ```

   As soon as you type each `/`, GitHub turns the part before it into a folder. Watch the breadcrumb above the box build up — that is how you know it worked.
3. Write your README content in the editor below (see [What goes in your folder](#what-goes-in-your-folder)).
4. Scroll down. Under **Commit new file**, write a short message like `week03: add house prices project`.
5. Make sure the radio button says **Commit directly to the `week03-house-prices` branch**.
6. Click **Commit new file**.

Now that the folder exists, uploading the rest is easy:

7. Navigate into your new folder (click through `week03-regression` → `community_contributions` → `janedoe`).
8. Click **Add file** → **Upload files**, drag in your notebook and other files, and commit them the same way. Files land in whichever folder you are currently viewing — so make sure the breadcrumb at the top shows your folder before you upload.

### A4. Open the pull request

1. Go to the **Pull requests** tab of your fork.
2. Click **New pull request**.
3. You will see four dropdowns. Set them like this:
   - **base repository:** `Wahab901278/ml-and-ai-launchpad`
   - **base:** `main`
   - **head repository:** `janedoe/ml-and-ai-launchpad` (yours)
   - **compare:** `week03-house-prices` (your branch)

   The arrow between them means "merge the right side into the left side."
4. Scroll down and confirm the **Files changed** list only contains files inside your folder. If anything else is listed, stop and fix it before continuing.
5. Click **Create pull request**.
6. A template appears. Fill in the description and tick the checklist boxes by putting an `x` between the brackets: `- [x]`.
7. Click **Create pull request** again.

Done. Skip to [The automated checks](#the-automated-checks).

---

## Route B: the command line (git on your computer)

**Best if:** you are comfortable in a terminal, or your project has many files and folders.

### B1. Fork

Same as [step A1](#a1-fork-the-repository) — click **Fork** on https://github.com/Wahab901278/ml-and-ai-launchpad.

### B2. Clone your fork

**Clone** means "download a working copy onto my computer."

```bash
git clone https://github.com/YOUR-USERNAME/ml-and-ai-launchpad.git
cd ml-and-ai-launchpad
```

Replace `YOUR-USERNAME` with your actual GitHub username. Clone **your fork**, not the original — cloning the original means you will not be able to push.

Verify you got the right one:

```bash
git remote -v
```

Both lines must contain **your** username.

### B3. Add the original repo as "upstream"

This lets you pull in new course material later.

```bash
git remote add upstream https://github.com/Wahab901278/ml-and-ai-launchpad.git
git remote -v
```

You should now see four lines: `origin` (yours, fetch + push) and `upstream` (the original, fetch + push).

### B4. Start from the latest main

```bash
git checkout main
git fetch upstream
git merge upstream/main
```

### B5. Create a branch

```bash
git checkout -b week03-house-prices
```

`checkout -b` means "create a new branch and switch to it." Confirm with:

```bash
git branch --show-current
```

### B6. Add your files

```bash
mkdir -p week03-regression/community_contributions/YOUR-USERNAME
```

Then copy your work into that directory — with your file manager, or:

```bash
cp -r ~/Desktop/my-project/* week03-regression/community_contributions/YOUR-USERNAME/
```

**Now check what git sees, before you commit anything:**

```bash
git status
```

Every path listed must start with `week03-regression/community_contributions/YOUR-USERNAME/`. If something else appears, remove it or the check will reject your PR.

### B7. Commit

```bash
git add week03-regression/community_contributions/YOUR-USERNAME
git commit -m "week03: add house prices regression project"
```

Use the explicit path in `git add` rather than `git add .` — it makes it much harder to sweep in a stray file by accident.

Confirm exactly what you committed:

```bash
git show --stat HEAD
```

### B8. Push to your fork

```bash
git push origin week03-house-prices
```

If this is your first push, git will ask you to authenticate. Use a **Personal Access Token**, not your account password — GitHub stopped accepting passwords for git in 2021. See [Troubleshooting](#authentication-failed-or-password-authentication-is-not-supported).

### B9. Open the pull request

The push output contains a link like:

```
remote: Create a pull request for 'week03-house-prices' on GitHub by visiting:
remote:      https://github.com/janedoe/ml-and-ai-launchpad/pull/new/week03-house-prices
```

Open it, fill in the template, and click **Create pull request**. Confirm the base repository is `Wahab901278/ml-and-ai-launchpad` and the base branch is `main`.

---

## Route C: GitHub Desktop (clicking, not typing)

**Best if:** you want the power of Route B without the terminal.

1. Install [GitHub Desktop](https://desktop.github.com/) and sign in with your GitHub account.
2. Fork the repository in your browser ([step A1](#a1-fork-the-repository)).
3. In GitHub Desktop: **File → Clone repository**, pick your fork from the list, choose a local folder, click **Clone**.
4. When it asks *"How are you planning to use this fork?"*, choose **To contribute to the parent project**.
5. **Current Branch** (top bar) → **New Branch** → name it `week03-house-prices` → **Create Branch**.
6. In Finder/Explorer, create the folders `week03-regression/community_contributions/YOUR-USERNAME/` inside the cloned repo, and copy your files in.
7. Back in GitHub Desktop, the left panel now lists your changed files. **Read that list.** Every path must be inside your folder. Untick anything that is not.
8. Bottom left: write a summary like `week03: add house prices project`, then click **Commit to week03-house-prices**.
9. Click **Push origin** (top bar).
10. Click **Preview Pull Request**, check the base is `Wahab901278/ml-and-ai-launchpad` `main`, then **Create Pull Request** — it opens your browser to finish.

---

## What goes in your folder

### Required: a `README.md`

One short file so people know what they are looking at. Copy this template:

````markdown
# House Price Prediction

**Week:** 3 — Regression
**Author:** [janedoe](https://github.com/janedoe)

## What this does

Predicts house sale prices from the Ames Housing dataset using linear
regression and gradient boosting, and compares the two.

## Results

| Model | RMSE | R² |
|-------|------|-----|
| Linear Regression | 34,200 | 0.81 |
| Gradient Boosting | 25,900 | 0.89 |

## How to run it

```bash
pip install -r requirements.txt
jupyter notebook house_prices.ipynb
```

## Notes

The dataset is downloaded by the first cell. Training takes about two
minutes on a laptop.
````

### Recommended

- **`requirements.txt`** — the packages you used, so others can reproduce your setup:
  ```
  pandas==2.2.0
  scikit-learn==1.4.0
  matplotlib==3.8.0
  ```
- **`.env.example`** — if your project needs API keys, list the *names* with blank values. Never the actual values.

### Never commit

| Don't commit | Why | Do this instead |
|---|---|---|
| `.env`, `credentials.json`, `*.key`, `*.pem` | Anyone can read a public repo. Bots scrape GitHub for keys within minutes of a push. | Commit `.env.example` with empty values. |
| An API key pasted into a notebook cell | Same problem. Clearing the cell later does **not** remove it — it stays in git history forever. | `os.environ["OPENAI_API_KEY"]` |
| An API key visible in notebook **output** | Easy to miss. Print statements and error tracebacks leak keys. | Clear outputs before committing. |
| Datasets over ~10 MB | Bloats the repo permanently for everyone who clones it. | Link to the source, or add a download script. |
| Model weights (`.pt`, `.h5`, `.pkl` over a few MB) | Same. | Link to Hugging Face or Google Drive. |
| `__pycache__/`, `.venv/`, `.ipynb_checkpoints/` | Machine-specific clutter. | Already covered by the repo's `.gitignore`. |

> **If you have already pushed a key anywhere — even to your own fork, even if a later commit deleted it — treat it as compromised. Rotate it immediately** in the provider's dashboard. Deleting a file does not delete it from git history.

### Notebook hygiene

Clear outputs before committing, unless the output *is* the point (a plot you want people to see without running the code):

```bash
pip install nbconvert
jupyter nbconvert --clear-output --inplace your_notebook.ipynb
```

This shrinks the file, removes accidentally-leaked keys from output cells, and makes the diff readable.

---

## The automated checks

When you open a PR, a workflow called **Restrict contributions** runs a job named **`check-paths`**. It takes under a minute. You will see one of:

- 🟡 **Yellow dot** — still running. Wait.
- ✅ **Green tick** — passed. Now it just needs the maintainer to merge.
- ❌ **Red X** — failed. Click **Details** to read why. Nothing is broken; you just need to push a fix.

### What it checks, and how to fix each failure

| Error message | What it means | Fix |
|---|---|---|
| `PR touches files outside a community_contributions/<your-handle>/ folder` | You changed or added something outside your folder. The listed files are the culprits. | Undo those changes — see [Fixing a PR](#fixing-a-pr-after-you-opened-it). Common causes: an accidental edit to a week `README.md`, or `git add .` sweeping in a stray file. |
| `PR touches more than one contributor folder` | Your PR includes files under two different people's folders, or under two different weeks. | One PR per folder. Move the extra files onto a separate branch and open a second PR. |
| `PR appears to contain secrets` | A filename looks like credentials (`.env`, `*.key`, `*.pem`, anything under `api-keys/`). | Delete the file from the branch **and rotate the key** — it is already in your fork's history. |
| `PR is very large` | The diff is over 200,000 lines, usually a committed dataset or model file. | Remove the big file and link to it instead. |

The check is skipped for the maintainer and repository collaborators. That is expected, not a bug.

---

## Fixing a PR after you opened it

**Do not close the PR and open a new one.** A pull request tracks a *branch* — push more commits to that same branch and the PR updates itself automatically, and the checks re-run.

### In the browser

Go to your fork, switch to your branch using the branch dropdown, then edit, add or delete files exactly as before. Each commit appears in the PR within seconds.

To delete a file: open it, click the **⋯** menu (or the trash icon) → **Delete file** → commit to your branch.

### On the command line

```bash
# make sure you are on the right branch
git checkout week03-house-prices

# remove a file that should not be there
git rm path/to/wrong-file.csv

# or undo an accidental edit to a file you should not have touched
git checkout upstream/main -- week03-regression/README.md

# then
git commit -m "Remove files outside my contribution folder"
git push origin week03-house-prices
```

### If a secret got committed

Removing the file in a new commit is **not enough** — it stays in history and remains readable.

1. **Rotate the key first.** Go to the provider (OpenAI, OpenRouter, Google, whoever) and revoke it. This is the only step that actually protects you.
2. Then clean up. Since the fork is your own, the simplest route is: delete the branch, delete the fork, re-fork fresh, and redo the work without the secret.

---

## Keeping your fork up to date

New course material is added over time. Your fork does **not** update itself.

### Browser

Go to your fork's main page. If it says *"This branch is N commits behind"*, click **Sync fork** → **Update branch**. Done.

### Command line

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

Then, if you want your in-progress branch to include the new material:

```bash
git checkout week03-house-prices
git merge main
```

Always branch off an up-to-date `main`. It avoids most merge conflicts.

---

## Troubleshooting

### `remote: Permission to Wahab901278/ml-and-ai-launchpad.git denied`

You are pushing to the original repo instead of your fork. Nobody has push access to the original — this is working as designed.

```bash
git remote -v          # look at the 'origin' lines
git remote set-url origin https://github.com/YOUR-USERNAME/ml-and-ai-launchpad.git
git push origin your-branch-name
```

### `Authentication failed`, or `password authentication is not supported`

GitHub has not accepted account passwords for git since August 2021. Use a **Personal Access Token**:

1. GitHub → your avatar → **Settings** → **Developer settings** (very bottom of the left sidebar) → **Personal access tokens** → **Tokens (classic)**.
2. **Generate new token (classic)**. Give it a name, an expiry, and tick the **`repo`** scope.
3. Copy the token. **You will never see it again** — save it in a password manager.
4. When git asks for a password, paste the token.

Easier long-term option: install the [GitHub CLI](https://cli.github.com/) and run `gh auth login` once, which handles this for you.

### `Permission denied (publickey)`

You cloned over SSH without an SSH key set up. Switch to HTTPS:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/ml-and-ai-launchpad.git
```

### `error: failed to push some refs` / `Updates were rejected`

Your branch on GitHub has commits your local copy does not — usually because you also edited in the browser.

```bash
git pull --rebase origin your-branch-name
git push origin your-branch-name
```

### `CONFLICT (content): Merge conflict in ...`

Two changes to the same lines. If it is a file inside your own folder, open it — git marks the clash like this:

```
<<<<<<< HEAD
your version
=======
their version
>>>>>>> upstream/main
```

Delete the marker lines and keep whatever the file should say. Then:

```bash
git add the-file
git commit
```

If the conflict is in a file **outside** your folder, you should not have edited it:

```bash
git checkout upstream/main -- path/to/that/file
git add path/to/that/file
git commit
```

### The check is stuck on yellow

Workflows queue occasionally. Give it five minutes. If it never starts, push an empty commit to retrigger:

```bash
git commit --allow-empty -m "Retrigger checks"
git push origin your-branch-name
```

### My PR shows hundreds of changed files

Your branch is based on an outdated `main`, so git thinks you reverted everything that changed since. Fix:

```bash
git checkout main
git fetch upstream
git merge upstream/main
git checkout your-branch-name
git merge main
git push origin your-branch-name
```

### I forgot to switch branches and committed to `main`

```bash
git branch week03-house-prices   # bookmark the current state
git reset --hard upstream/main   # put main back how it was (discards uncommitted work)
git checkout week03-house-prices # your commits are safely here
```

### I am completely stuck

[Open an issue](https://github.com/Wahab901278/ml-and-ai-launchpad/issues/new) describing what you tried and pasting the exact error text. Screenshots are fine. Nobody will judge you for asking — everyone has fought git at some point.

---

## Glossary

| Term | Meaning |
|---|---|
| **Repository** ("repo") | A project folder whose history git tracks. |
| **Fork** | Your personal copy of someone else's repo, living on your GitHub account. You have full write access to it. |
| **Clone** | A copy of a repo downloaded onto your own computer. |
| **Branch** | A parallel line of work inside a repo, so unfinished changes do not disturb `main`. |
| **`main`** | The default, official branch. |
| **Commit** | One saved snapshot of your changes, with a message describing them. |
| **Push** | Upload your commits from your computer to GitHub. |
| **Pull** | Download commits from GitHub to your computer. |
| **Pull request** ("PR") | A request to merge your branch into someone else's repo, with room for review and discussion. |
| **Merge** | Combining one branch's changes into another. |
| **`origin`** | Git's default nickname for the repo you cloned from — for you, your fork. |
| **`upstream`** | The conventional nickname for the original repo you forked from. |
| **CI / checks / Actions** | Automated scripts GitHub runs on your PR. Here: the folder rule. |
| **Conflict** | Two people changed the same lines; git needs a human to decide. |

---

## FAQ

**Do I need permission before I start?**
No. Fork and open a PR whenever you like.

**Can I contribute to a week that has already passed?**
Yes. Every week's folder stays open.

**Can I submit more than one project?**
Yes — one PR per project, each in its own subfolder inside your username folder:
`week03-regression/community_contributions/janedoe/house-prices/` and `.../janedoe/car-prices/`.

**Two people have the same first name — how do we avoid collisions?**
Folders are named after your **GitHub username**, which is globally unique. No collisions.

**What if my code is messy or the model performs badly?**
Submit it. This is a learning cohort, not a portfolio review. A documented failed experiment teaches more than a polished result.

**Can I edit someone else's contribution?**
No — the check blocks it. Open an issue, or comment on their original PR.

**Can I use a language other than Python?**
Yes, if it fits the week. Include setup instructions in your README.

**How long until my PR is merged?**
The automated check runs in about a minute. A human merge depends on the maintainer's availability. Comment on your PR if a week goes by with no response.

**My PR was closed without merging. Why?**
Check the closing comment. Usually an unfixed check failure, or a duplicate PR. You can always open a new one.

**Do I need to delete my fork afterwards?**
No. Keep it — you will want it for the next week.

**Something in the course material is wrong. Can I fix it?**
Not via a PR (the check blocks it, correctly). [Open an issue](https://github.com/Wahab901278/ml-and-ai-launchpad/issues/new) instead.

---

## Final checklist

Before you click **Create pull request**:

- [ ] Everything is inside `<week-folder>/community_contributions/<my-github-username>/`
- [ ] The week folder name is spelled exactly as in [the table](#the-week-folders)
- [ ] Only **one** contributor folder is touched
- [ ] My folder has a `README.md` explaining what it does and how to run it
- [ ] No `.env`, no API keys, no credentials — in files **or** in notebook outputs
- [ ] Notebook outputs cleared (or deliberately kept and small)
- [ ] No large datasets or model weights
- [ ] I read the **Files changed** tab and recognise every single file listed

Thanks for contributing. 🚀
