
# GIT CLI Cheat Sheet

## Initiate New Repo

```bash
git init
```

## Change Branch From Master to Main

```bash
git branch -M main
```

## Add file(s) to the GIT Repo

```bash
# Add one file
git add filename.txt

# Add a directory
# git add notes/

# Add everything
# git add .
```

## Check the GIT Repo Files

```bash
git ls-files
```

## Commit  the GIT Repo Files

```bash
# Commit most recent change(s)
git commit -m "Adding Placeholder File"

# Commit everything
# git commit -a -m "added everything"
```

## Check Current GIT Status

```bash
git status
```

## Add Upstream Origin & Set Default Branch

```bash
git remote add origin https://github.com/niliopoulos89/arista_ace_l5.git

git push -u origin main
```

...