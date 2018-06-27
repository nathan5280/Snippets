import subprocess

args = ["python", "setup_users.py",
        "--db-path", "tests/db/test-users.db",
        "--cfg-path", "cfg_data/users.json"]

subprocess.run(args=args)