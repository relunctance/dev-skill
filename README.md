# dev-skill
[![version](https://img.shields.io/badge/version-1.0.0-green.svg)]()
[![category](https://img.shields.io/badge/category-development-blue.svg)]()
[![platforms](https://img.shields.io/badge/platforms-claude code%20%7C%20openclaw%20%7C%20hermes%20%7C%20cursor%20%7C%20vscode-blue.svg)]()

开发类 Skill 套件 — 一键安装所有开发流程相关的 skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/relunctance/dev-skill)](https://github.com/relunctance/dev-skill/stargazers)

## 包含的 Skill

| Skill | 用途 |
|-------|------|
| [`base-skill`](https://github.com/relunctance/base-skill) | Agent 初始化套件（14 个核心 skills，含 task-split / git-standards） |
| [`plan-review-skill`](https://github.com/relunctance/plan-review-skill) | 规划评审流程 — LLM 驱动 + 数值 diff 脚本辅助 |
| [`dev-std-skill`](https://github.com/relunctance/dev-std-skill) | SOP 模板下发 — 自动初始化 + 手动同步 |

## 安装

```bash
git clone https://github.com/relunctance/dev-skill.git ~/repos/dev-skill
cd ~/repos/dev-skill
bash scripts/setup.sh
```

安装脚本会自动：
- 检查 python3 / git / pip 环境，缺失时引导安装
- 克隆/更新所有 skill 到 `~/repos/`
- 创建 symlink 到 `~/.hermes/skills/`
- 运行各 skill 的 setup.sh

## 触发条件

用户说：
- `安装开发套件`
- `初始化开发环境`
- `安装 dev-skill`
- `开发环境准备`

## 环境要求

- Python 3.8+
- Git
- pip

## 许可证

MIT
