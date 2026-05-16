#!/usr/bin/env python3
"""
dev-skill install.py — 一键安装所有开发类 skill

用法：
  python3 install.py
"""

import os
import platform
import pwd
import subprocess
import sys
from pathlib import Path


def _real_home() -> Path:
    """解决 WSL Hermes profile 下 Path.home() 指向 profile 的问题"""
    return Path(pwd.getpwuid(os.getuid()).pw_dir)


REPOS_DIR = _real_home() / "repos"
SKILLS_DIR = _real_home() / ".hermes" / "skills"

SKILLS = [
    ("base-skill",          "https://github.com/relunctance/base-skill.git"),
    ("plan-review-skill",   "https://github.com/relunctance/plan-review-skill.git"),
    ("dev-std-skill",       "https://github.com/relunctance/dev-std-skill.git"),
    ("task-split-skill",    "https://github.com/relunctance/task-split-skill.git"),
    ("git-standards-skill", "https://github.com/relunctance/git-standards-skill.git"),
]


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"  $ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def install_skill(name: str, url: str) -> None:
    repo_dir = REPOS_DIR / name
    skill_link = SKILLS_DIR / name / "SKILL.md"

    # Clone or pull
    if repo_dir.exists():
        print(f"[UPDATE] {name}")
        run(["git", "-C", str(repo_dir), "pull", "--ff-only"], cwd=repo_dir)
    else:
        print(f"[CLONE] {name}")
        run(["git", "clone", url, str(repo_dir)], cwd=REPOS_DIR)

    # Create symlink
    (SKILLS_DIR / name).mkdir(parents=True, exist_ok=True)
    if skill_link.is_symlink() or skill_link.exists():
        skill_link.unlink()
    skill_link.symlink_to(repo_dir / "SKILL.md")
    print(f"  [LINK] {skill_link}")

    # Run skill's own setup if exists
    setup_sh = repo_dir / "scripts" / "setup.sh"
    if setup_sh.exists():
        print(f"  [SETUP] {name}/scripts/setup.sh")
        run(["bash", str(setup_sh)], cwd=repo_dir)


def main():
    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    print("安装 dev-skill 套件...")
    print(f"  REPOS_DIR = {REPOS_DIR}")
    print(f"  SKILLS_DIR = {SKILLS_DIR}")
    print()

    failed = []
    for name, url in SKILLS:
        try:
            install_skill(name, url)
        except Exception as e:
            print(f"  [ERROR] {name}: {e}")
            failed.append(name)

    print()
    if failed:
        print(f"⚠️  安装失败：{', '.join(failed)}")
        sys.exit(1)
    else:
        print("✅ dev-skill 套件安装完成！")


if __name__ == "__main__":
    main()
