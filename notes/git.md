
# GIT CLI Cheat Sheet

## Common Examples

### Clone a Repository

```bash
# Clone without submodule repositories
git clone https://github.com/niliopoulos89/arista_ace_l5.git

# Clone with submodule repositories included
git clone https://github.com/niliopoulos89/arista_ace_l5.git --recurse-submodules
```

### Create New Repository from the CLI

```bash
echo "# arista_ace_l5" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/niliopoulos89/arista_ace_l5.git
git push -u origin main
```

### Push Existing Repository from CLI

```bash
git remote add origin https://github.com/niliopoulos89/arista_ace_l5.git
git branch -M main
git push -u origin main
```

...

## CLI Cheat Sheet

### Initiate New Repository

```bash
git init
```

### Change Branch From Master to Main

```bash
git branch -M main
```

### Add file(s) to the GIT Repo

```bash
# Add one file
git add filename.txt

# Add a directory
# git add notes/

# Add everything
# git add .
```

### Check the GIT Repo Files

```bash
git ls-files
```

### Commit the GIT Repo Files

```bash
# Commit most recent change
git commit -m "Adding Placeholder File"

# Commit all changes
git commit -a -m "added everything"
```

### Check Current GIT Status

```bash
git status
```

### Add Upstream Origin

```bash
git remote add origin https://github.com/niliopoulos89/arista_ace_l5.git
```

### Set Default Branch

```bash
git push -u origin main
```

...
