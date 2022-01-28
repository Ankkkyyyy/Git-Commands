
# General Purpose Git Commands 

## $ git add path/to/file
Moves changes from the working directory to the staging area. This gives you the opportunity to prepare a snapshot before committing it to the official history.
Or
We can say we use the Git add command to move those changes from the working directory to the staging area.

## $ git add .
To add all changed files to stagging Area use this command For E.g if their are thousands of files you just can't sit & add one by one? So here this command comes in picture use this  command

## $ git add path/to/directoryOnly
To add a all changed files of a directory, use the following command.

## $ git branch
This command is your general-purpose branch administration tool. It lets you create isolated development environments within a single repository.

## $ git clone
Creates a copy of an existing Git repository. Cloning is the most common way for developers to obtain a working copy of a central repository.

## $ git status 
To track the status of your working way, This is one of the Important command to keep checking yourself that you are in right direction, you are going in right path.

## $ git config
A convenient way to set configuration options for your Git installation. You’ll typically only need to use this immediately after installing Git on a new development machine.

## $ git fetch
Fetching downloads a branch from another repository, along with all of its associated commits and files. But, it doesn't try to integrate anything into your local repository. This gives you a chance to inspect changes before merging them with your project.

## $ git init
Initializes a new Git repository. If you want to place a project under revision control, this is the first command you need to learn.

## $ git log
Lets you explore the previous revisions of a project. It provides several formatting options for displaying committed snapshots.

## $ git merge
A powerful way to integrate changes from divergent branches. After forking the project history with git branch, git merge lets you put it back together again.

## $ git pull
Pulling is the automated version of git fetch. It downloads a branch from a remote repository, then immediately merges it into the current branch.

## $ git remote
A convenient tool for administering remote connections. Instead of passing the full URL to the fetch, pull, and push commands, it lets you use a more meaningful shortcut.

## $ git restore -- stagged 
The "restore" command helps to unstage or even discard uncommitted local changes.

## $ git diff
This command tells you the difference between the working  area & the stagging area.


## $ git commit
Git commit command takes a snapshot representing the staged changes.

## $ git commit -m "<message>"
 This Git commit example shows how you set the description with the commit function:

## $ git commit -a -m – “Skipped Staging Area & fixed.”
This will directly commit, it will not go in the staging area.
