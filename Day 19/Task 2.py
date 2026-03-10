import os
import subprocess

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

project = "git_merge_conflict_demo"

if not os.path.exists(project):
    os.mkdir(project)

os.chdir(project)

run("git init")
run("git checkout -b main")

with open("code.py", "w") as f:
    f.write('print("Hello from Main branch")\n')

run("git add code.py")
run('git commit -m "Initial commit on main"')

run("git checkout -b feature-branch")

with open("code.py", "w") as f:
    f.write('print("Hello from Feature branch")\n')

run("git add code.py")
run('git commit -m "Edited line in feature branch"')

run("git checkout main")

with open("code.py", "w") as f:
    f.write('print("Hello from Main branch - updated")\n')

run("git add code.py")
run('git commit -m "Edited line in main branch"')

print("Now attempting merge (this will create a conflict)...")

run("git merge feature-branch")

print("Open code.py and you will see conflict markers like:")
print("<<<<<<< HEAD")
print("=======")
print(">>>>>>> feature-branch")
print("Edit the file, remove markers, keep the correct line, then run:")
print("git add code.py")
print('git commit -m "Resolved merge conflict"')