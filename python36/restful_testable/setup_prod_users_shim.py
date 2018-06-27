import subprocess

args = ["python", "setup_users.py",
        "--db-path", "db/prod-users.db",
        "--cfg-path", "cfg_data/users.json"]

subprocess.run(args=args)