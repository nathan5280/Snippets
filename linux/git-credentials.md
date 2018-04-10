To cache the credentials for a repository.

```commandline
git config credential.helper store
git push https://github.com/<user>/<repo>

```

Reference page
```commandline
https://askubuntu.com/questions/527551/how-to-access-a-git-repository-using-ssh
```

Create an ssh key and post it on Git. Do this in ~/.ssh
```commandline
ssh-keygen -t rsa -b 4096

cat id_rsa.pub
```

Cut and past that into the rsa key section on git in your profile.

Configure git
```commandline
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```

