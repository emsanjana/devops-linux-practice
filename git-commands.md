# Create project folder and initialize Git
mkdir <directiry-name>
cd <directory-name>
git init

# Create README and commit
echo "# Details" > README.md
git add README.md
git commit -m "Initial commit with README"

# Create and switch to branch
git checkout -b <new-branch-name>

# Create login page file and commit
echo "<h1>Page</h1>" > page.html
git add page.html
git commit -m "Add page"

#Merge to main 
git checkout main
git merge <branch-name> -m "Message"

#Add github remote
git remote add origin git@github.com:YOUR_USERNAME/my-git-project.git

## Push main branch
git push -u origin main

# Push other branches
git push origin <branch-name>
