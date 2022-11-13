# Creating PR

## 1. Branch out from the main branch 
```
% git branch dir_restructure
% git checkout dir_restructure
```
## 2. Make necessary changes, commit, push
```
git commit -a -m "directory restructuring"
git push origin dir_restructure
```
```
spartan@IMS-073MBA stock-prediction % git status
On branch dir_restructure
    Untracked files:
    (use "git add <file>..." to include in what will be committed)
            Devansh Bansal/
            Nimish Lingesh/
            Rohan Upadhyay/
            Shwetha Shyam Bhandary/
            developing.md

nothing added to commit but untracked files present (use "git add" to track)

spartan@IMS-073MBA stock-prediction % git add . 
spartan@IMS-073MBA stock-prediction % git commit -a -m "directory restructuring"
[dir_restructure b0fbeb5] directory restructuring
 5 files changed, 563 insertions(+)
 create mode 100644 Devansh Bansal/data_exploration.ipynb
 create mode 100644 Nimish Lingesh/data_exploration.ipynb
 create mode 100644 Rohan Upadhyay/data_exploration.ipynb
 create mode 100644 Shwetha Shyam Bhandary/data_exploration.ipynb
 create mode 100644 developing.md
> spartan@IMS-073MBA stock-prediction % git push origin dir_restructure
Enumerating objects: 23, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 8 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (17/17), 18.28 KiB | 9.14 MiB/s, done.
Total 17 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), done.
remote: 
remote: Create a pull request for 'dir_restructure' on GitHub by visiting:
remote:      https://github.com/NimishLingesh/stock-prediction/pull/new/dir_restructure
remote: 
To https://github.com/NimishLingesh/stock-prediction.git
 * [new branch]      dir_restructure -> dir_restructure
```

## 3. Create a PR in the github UI. Add other Reviewers

## 4. Once the PR is merged, please update your main branch locally to be in sync with the updates made by the other team members
```
git checkout main
git pull origin main
```
Eg:
```
spartan@IMS-073MBA stock-prediction % git branch
  del_ds
  dir_restructure
* main
  nimish_pr
spartan@IMS-073MBA stock-prediction % git pull origin main
From https://github.com/NimishLingesh/stock-prediction
 * branch            main       -> FETCH_HEAD
Updating 19f5809..04a4800
Fast-forward
 .DS_Store                                     | Bin 6148 -> 0 bytes
 .gitignore                                    |   1 +
 Devansh Bansal/data_exploration.ipynb         |  68 ++++++++++++
 Nimish Lingesh/data_exploration.ipynb         | 497 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 README.md                                     |  23 ++--
 Rohan Upadhyay/data_exploration.ipynb         |  22 ++++
 Shwetha Shyam Bhandary/data_exploration.ipynb |  22 ++++
 developing.md                                 |   0
 8 files changed, 623 insertions(+), 10 deletions(-)
 delete mode 100644 .DS_Store
 create mode 100644 .gitignore
 create mode 100644 Devansh Bansal/data_exploration.ipynb
 create mode 100644 Nimish Lingesh/data_exploration.ipynb
 create mode 100644 Rohan Upadhyay/data_exploration.ipynb
 create mode 100644 Shwetha Shyam Bhandary/data_exploration.ipynb
 create mode 100644 developing.md
```
