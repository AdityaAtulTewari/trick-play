import subprocess
import shlex
#gives us the ids of the variables
from video_ids import ids
import random

# Settings to change
firefox_profile_name="BLM"
firefox_profile_dir="~/support_BLM"

#Do not mess with these
ssh="ssh {display} {login} {cmd}"
firefox_create_profile="./hello.bash BLM"
firefox_str="firefox -P " + firefox_profile_name + " "
D_ON="-Y"
D_OF=""
player_str="https://www.youtube.com/watch?v="


def runSSH(ssh_str, targets):
  subprocess.Popen(shlex.split(ssh.format(display=D_OF, login=ssh_str, cmd=firefox_create_profile)))
  for target in targets:
    subprocess.Popen(shlex.split(ssh.format(display=D_ON, login=ssh_str, cmd=(firefox_str + player_str + target))))

def run(targets):
  subprocess.Popen(shlex.split(firefox_create_profile))
  for target in targets:
    p0 = subprocess.Popen(shlex.split(firefox_str + player_str + target))
    p0.wait();


# 5/3/r/a/m
# run a video, then run 3-5 others, then run the original again.
def genRand(ids):
  toRand = ids.copy()
  targets = []
  mother = random.choice(toRand)
  toRand.remove(mother)
  while len(toRand) > 0:
    targets.append(mother)
    num = random.randint(3,5)
    for i in range(num):
      if len(toRand) > 0:
        curr = random.choice(toRand)
        toRand.remove(curr)
        targets.append(curr)
  return targets

while True:
  targets = genRand(ids)
  run(targets)
