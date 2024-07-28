FROM node:20

# 设置工作目录

# 复制 package.json 和 package-lock.json

WORKDIR /app

COPY . /app

# 安装项目依赖
RUN npm config set registry https://registry.npmmirror.com
RUN npm install

# 复制项目文件

# 暴露端口 5173
EXPOSE 5173

# 启动应用
CMD ["npm", "start"]

