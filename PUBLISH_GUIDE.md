# 如何把这个仓库发布到 GitHub

本目录已经是一个初始化好的本地 Git 仓库（已完成首次提交），并配好了 README、LICENSE、.gitignore。
你只需要在 GitHub 上建一个空仓库，然后把本地内容推上去，三步即可。

---

## 第一步：在 GitHub 网页上创建空仓库

1. 打开 https://github.com/new
2. Repository name 填：`njust-2026fall-bigdata-ch2-homework-4ex`
3. **不要**勾选 Add a README file / Add .gitignore / Choose a license（本地已有了，勾了会冲突）
4. Public（公开）——加分项要求"分享给需要使用的人"，必须是公开仓库
5. 点 Create repository

---

## 第二步：把本目录复制到你的电脑上

建议放到一个固定位置，例如：

```
C:\Users\王\Desktop\njust-2026fall-bigdata-ch2-homework-4ex
```

或用命令复制（在 Git Bash 里执行）：

```bash
cp -r "C:/Users/王/WorkBuddy/2026-10-05-17-18-48/outputs/njust-2026fall-bigdata-ch2-homework-4ex" "C:/Users/王/Desktop/"
```

注意：复制时**要包含隐藏的 .git 目录**，它是本地仓库的记录，别漏掉。

---

## 第三步：推送上去

### 方式一：双击 `推送脚本.bat`（推荐，最省事）

先右键用记事本打开 `推送脚本.bat`，把开头三项改成你自己的：

```bat
set GIT_NAME=你的GitHub用户名
set GIT_EMAIL=你的邮箱@example.com
set REPO_URL=https://github.com/你的GitHub用户名/njust-2026fall-bigdata-ch2-homework-4ex.git
```

保存后双击运行即可。首次推送会弹出登录窗口，用浏览器授权登录 GitHub 就行。

### 方式二：手动敲命令

在该目录打开 Git Bash，依次执行：

```bash
git config user.name "你的GitHub用户名"
git config user.email "你的邮箱@example.com"

git remote add origin https://github.com/你的GitHub用户名/njust-2026fall-bigdata-ch2-homework-4ex.git
git branch -M main
git push -u origin main
```

如果提示 `remote origin already exists`，先执行 `git remote remove origin` 再重试。

---

## 常见问题

**Q：push 时一直卡住或超时**
网络问题。可换用 SSH 方式：先在 GitHub 设置里配好 SSH Key，然后把仓库地址换成
`git@github.com:你的用户名/njust-2026fall-bigdata-ch2-homework-4ex.git`。

**Q：提示 `failed to push some refs`**
说明远程仓库不是空的（可能创建时勾选了 README）。在 GitHub 网页上把仓库删掉重建，记得什么都不要勾。

**Q：想改 commit 里的邮箱**
执行 `git commit --amend --reset-author --no-edit` 后重新 push（用 `git push -f`）。

**Q：后面的代码改了怎么更新**
在目录里执行：

```bash
git add -A
git commit -m "更新说明"
git push
```

---

## 关于本次首次提交

本地仓库已经完成了一次提交，提交信息为：

```
第2章 数据科学的编程工具：六道习题解答与逐步解析
```

包含 7 个文件：README.md、LICENSE、.gitignore、ex1~ex4 四个源文件。

> 提交时使用的作者是占位的 `student <student@example.com>`。
> 如果你希望改为自己的名字，推送前执行：
> ```bash
> git commit --amend --reset-author --no-edit
> ```
> （前提是先执行过 `git config user.name` 和 `user.email`）

---

## 最后一步：把仓库地址填回报告

推送成功后，把仓库地址写到报告的「附录 加分项的完成」第 3 条：

```
3、GitHub 代码分享
仓库地址：https://github.com/你的用户名/njust-2026fall-bigdata-ch2-homework-4ex
（贴：仓库首页截图）
```

加分项(3) 即完成。
