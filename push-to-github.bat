@echo off
chcp 65001 >nul
setlocal

echo ================================================
echo  一键推送到 GitHub
echo ================================================
echo.

REM ===== 请修改下面两行为你自己的信息 =====
set GIT_NAME=你的GitHub用户名
set GIT_EMAIL=你的邮箱@example.com
set REPO_URL=https://github.com/你的GitHub用户名/njust-2026fall-bigdata-ch2-homework-4ex.git
REM =========================================

echo [1/5] 配置 Git 用户信息...
git config user.name "%GIT_NAME%"
git config user.email "%GIT_EMAIL%"

echo [2/5] 添加所有文件...
git add -A

echo [3/5] 提交...
git commit -m "第2章 数据科学的编程工具：六道习题解答与逐步解析"

echo [4/5] 设置远程仓库...
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%

echo [5/5] 推送到 GitHub（首次会要求登录）...
git push -u origin main

echo.
if %errorlevel%==0 (
    echo 推送成功！仓库地址：%REPO_URL%
) else (
    echo 推送失败，请检查：
    echo   1. 是否已在 GitHub 网页上创建了空仓库 njust-2026fall-bigdata-ch2-homework-4ex
    echo   2. REPO_URL 中的用户名是否已改成你自己的
    echo   3. 网络是否可访问 GitHub
)
echo.
pause
