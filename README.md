# dev-skill

开发类 Skill 套件 — 一键安装所有开发流程相关的 skill。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 包含的 Skill

| Skill | 用途 |
|-------|------|
| `base-skill` | Agent 初始化套件（一键安装 12 个核心 skills） |
| `plan-review-skill` | 规划评审流程 — LLM 驱动 + 数值 diff 脚本辅助 |
| `dev-std-skill` | SOP 模板下发 — 自动初始化 + 手动同步 |
| `task-split-skill` | 任务拆解 — 澄清模板 + 验收标准强制 |
| `git-standards-skill` | Git 规范 — commit/push 分支策略 |

## 安装

```bash
git clone https://github.com/relunctance/dev-skill.git ~/repos/dev-skill
python3 ~/repos/dev-skill/scripts/install.py
```

## 工作流

```
制定 PLAN（PLAN.md）
    ↓
提交评审（plan-review-skill）
    ↓
批准后任务拆解（task-split-skill）
    ↓
执行开发（git-standards-skill）
```

## 触发条件

用户说：
- `安装开发套件`
- `初始化开发环境`
- `安装 dev-skill`
- `开发环境准备`

## 联动

- **base-skill**：自动安装
- **plan-review-skill**：规划评审
- **dev-std-skill**：SOP 下发
- **task-split-skill**：任务拆解
- **git-standards-skill**：Git 规范

## 许可证

MIT
